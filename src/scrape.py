#!/usr/bin/env python3
"""
Scraper for Artificial Analysis LLM Leaderboard (Evolution variant).

Extracts the full model dataset from the Next.js RSC payload embedded in the page,
and joins release dates from releases metadata.

V20 (2026-10-20): AA updated the RSC payload key from `models` to `initialModels`
for the main evaluation dataset. The scraper dynamically discovers all model arrays
(initialModels, models, releases), selects the primary benchmark array by evaluation
coverage, merges missing fields across arrays by slug, and resolves releaseDate
via direct slug match and releaseSlug -> releases[slug].releaseDate mapping.
"""

import json
import os
import sys

from playwright.sync_api import sync_playwright

URL = "https://artificialanalysis.ai/leaderboards/models"
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "raw_data.json")
MIN_MODELS_EXPECTED = 100

_SEARCH_ALL_JS = """
function _findAllModelArrays(obj, maxDepth) {
  const found = [];
  const seen = new Set();
  function search(o, d) {
    if (d > maxDepth || !o || typeof o !== 'object') return;
    if (Array.isArray(o)) {
      if (o.length > 0 && typeof o[0] === 'object' && o[0] !== null && 'slug' in o[0]) {
        if (!seen.has(o)) {
          seen.add(o);
          found.push(o);
        }
      }
      for (const v of o) search(v, d + 1);
    } else {
      for (const v of Object.values(o)) {
        search(v, d + 1);
      }
    }
  }
  search(obj, 0);
  return found;
}
"""

EXTRACT_JS = """
(() => {
  ${SEARCH}
  const scripts = document.querySelectorAll('script');
  const found = [];
  const seenSigs = new Set();

  function processData(data) {
    const modelArrays = _findAllModelArrays(data, 25);
    for (const arr of modelArrays) {
      const sig = arr.length + ':' + (arr[0] ? arr[0].slug : '');
      if (!seenSigs.has(sig)) {
        seenSigs.add(sig);
        found.push(arr);
      }
    }
  }

  for (let i = 0; i < scripts.length; i++) {
    const text = scripts[i].textContent || '';
    if (!text.includes('__next_f')) continue;
    if (!text.toLowerCase().includes('model') && !text.includes('slug') && !text.includes('release')) continue;

    const pushPattern = /self\\.__next_f\\.push\\(\\s*(\\[.*?\\])\\s*\\)\\s*;?/gs;
    let m;
    let matchedAny = false;
    while ((m = pushPattern.exec(text)) !== null) {
      matchedAny = true;
      try {
        const arr = eval(m[1]);
        if (!arr || arr.length < 2 || typeof arr[1] !== 'string') continue;
        const content = arr[1];
        const colonIdx = content.indexOf(':');
        if (colonIdx === -1) continue;
        const data = JSON.parse(content.substring(colonIdx + 1));
        processData(data);
      } catch(e) { /* skip */ }
    }

    if (!matchedAny) {
      const match = text.match(/^self\\.__next_f\\.push\\((.+)\\)$/s);
      if (match) {
        try {
          const arr = eval(match[1]);
          if (arr && arr.length >= 2 && typeof arr[1] === 'string') {
            const content = arr[1];
            const colonIdx = content.indexOf(':');
            if (colonIdx !== -1) {
              const data = JSON.parse(content.substring(colonIdx + 1));
              processData(data);
            }
          }
        } catch(e) { /* skip */ }
      }
    }
  }
  return JSON.stringify(found);
})()
""".replace("${SEARCH}", _SEARCH_ALL_JS)


def scrape_leaderboard():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print(f"[1/3] Navigating to {URL} ...")
        page.goto(URL, wait_until="networkidle", timeout=90000)
        page.wait_for_timeout(8000)

        print("[2/3] Extracting model data from RSC payload ...")
        raw_json = page.evaluate(EXTRACT_JS)
        arrays = json.loads(raw_json)
        print(f"  models arrays found: {len(arrays)} "
              f"({[len(a) for a in arrays]} models, "
              f"{[len(a[0].keys()) if a else 0 for a in arrays]} fields each)")

        def array_score(a):
            if not a:
                return (0, 0, 0)
            intel_count = sum(1 for m in a if m.get("intelligenceIndex") is not None)
            total_fields = sum(len(m.keys()) for m in a)
            return (intel_count, len(a), total_fields)

        models = max(arrays, key=array_score) if arrays else []

        # Build release_map from any array with releaseDate
        release_map = {}
        for arr in arrays:
            for r in arr:
                sl = r.get("slug")
                rd = r.get("releaseDate")
                if sl and rd and sl not in release_map:
                    release_map[sl] = rd
        print(f"  Release-date map: {len(release_map)} releases")

        if len(arrays) > 1 and models:
            models_by_slug = {m["slug"]: m for m in models if m.get("slug")}
            n_merged = 0
            for arr in arrays:
                if arr is models:
                    continue
                for item in arr:
                    slug = item.get("slug")
                    if slug and slug in models_by_slug:
                        target = models_by_slug[slug]
                        for k, v in item.items():
                            if k not in target and v is not None:
                                target[k] = v
                                n_merged += 1
            print(f"  Merged {n_merged} missing field values across {len(models_by_slug)} models "
                  f"(e.g. name/releaseDate/releaseSlug)")

        # Join releaseSlug -> releases[slug].releaseDate for any models still missing releaseDate
        n_dated = 0
        n_no_slug = 0
        for m in models:
            if m.get("releaseDate"):
                n_dated += 1
                continue
            rs = m.get("releaseSlug")
            if not rs:
                n_no_slug += 1
                continue
            rd = release_map.get(rs)
            if rd:
                m["releaseDate"] = rd
                n_dated += 1

        print(f"  Models with releaseDate after join: {n_dated}/{len(models)} (no releaseSlug: {n_no_slug})")

        models_with_intel = sum(1 for m in models if m.get("intelligenceIndex") is not None)
        if len(models) < MIN_MODELS_EXPECTED or models_with_intel < 50:
            raise RuntimeError(
                f"Extraction validation failed: {len(models)} models extracted "
                f"(expected >= {MIN_MODELS_EXPECTED}), {models_with_intel} models with "
                f"intelligenceIndex (expected >= 50). Available fields: "
                f"{list(models[0].keys()) if models else []}"
            )
        if models and n_dated == 0:
            raise RuntimeError(
                f"No releaseDate resolved after releases join "
                f"(models={len(models)}, releases={len(release_map)})."
            )

        print(f"  Extracted {len(models)} models ({models_with_intel} with intelligenceIndex, {n_dated} with releaseDate)")
        if models:
            sample_model = next((x for x in models if x.get("intelligenceIndex") is not None and x.get("price1mInputTokens") is not None), models[0])
            print(f"  Fields per model: {len(sample_model.keys())}")
            raw_cost = sample_model.get("intelligenceIndexCostTotal")
            try:
                if raw_cost in (None, "", "--", "?"):
                    cost_str = "$?"
                else:
                    cost_str = f"${float(raw_cost):.2f}"
            except (ValueError, TypeError):
                cost_str = "$?"
            print("  Sample: " + str(sample_model.get("name")) + ", releaseDate=" + str(sample_model.get("releaseDate")) + ", releaseSlug=" + str(sample_model.get("releaseSlug")) + ", intelIndex=" + str(sample_model.get("intelligenceIndex")))

        print(f"[3/3] Saving to {OUTPUT_FILE} ...")
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(models, f, ensure_ascii=False, indent=2)

        browser.close()

    print(f"Done! {len(models)} models saved.")
    return models


if __name__ == "__main__":
    try:
        data = scrape_leaderboard()
        if not data or len(data) < MIN_MODELS_EXPECTED:
            raise RuntimeError(f"Scraping returned insufficient models: {len(data) if data else 0} (expected >= {MIN_MODELS_EXPECTED})")
    except Exception as e:
        print(f"Scraping failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
