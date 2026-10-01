#!/usr/bin/env python3
"""
Scraper for Artificial Analysis LLM Leaderboard.

Extracts the full model dataset from the Next.js RSC payload embedded in the page.

V19 (2026-10-01): AA changed the payload again. The benchmark array no longer
carries releaseDate at all. Dates now live in a separate `releases` array
inside `modelsAndReleases`:
  * benchmark array (~50 fields: scores, pricing, speed, creator, ... + slug,
    releaseSlug? no date)
  * modelsAndReleases.models: [{slug, name, releaseSlug}] (688 entries, 3 fields)
  * modelsAndReleases.releases: [{slug, name, deprecated, releaseDate,
    creator{slug,name,logo}}] (499 entries, one per release; multiple model
    variants share one releaseSlug, e.g. gpt-6-sol-low -> gpt-6-sol)
The scraper joins releaseSlug -> releases[slug].releaseDate and writes
`releaseDate` back onto each benchmark model, restoring the field analyze.py
expects. Verified 688/688 join coverage on 2026-10-01 snapshot.

The RSC payload contains EVERY model regardless of the page Status filter,
including deprecated ones, which analyze.py keeps (Status: All).
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
function _findAllModels(obj, maxDepth) {
  const out = [];
  function search(o, d) {
    if (d > maxDepth || !o || typeof o !== "object") return;
    if (!Array.isArray(o) && o.models && Array.isArray(o.models) && o.models.length > 0) {
      out.push(o.models);
    }
    if (Array.isArray(o)) for (const v of o) search(v, d + 1);
    else for (const v of Object.values(o)) search(v, d + 1);
  }
  search(obj, 0);
  return out;
}
function _findAllReleases(obj, maxDepth) {
  const out = [];
  function search(o, d) {
    if (d > maxDepth || !o || typeof o !== "object") return;
    if (!Array.isArray(o) && o.releases && Array.isArray(o.releases) && o.releases.length > 0) {
      const r0 = o.releases[0];
      if (r0 && typeof r0 === "object" && r0.slug && r0.releaseDate) {
        out.push(o.releases);
      }
    }
    if (Array.isArray(o)) for (const v of o) search(v, d + 1);
    else for (const v of Object.values(o)) search(v, d + 1);
  }
  search(obj, 0);
  return out;
}
"""

EXTRACT_JS = """
(() => {
  SEARCH
  const scripts = document.querySelectorAll("script");
  const modelsFound = [];
  const releasesFound = [];
  for (let i = 0; i < scripts.length; i++) {
    const text = scripts[i].textContent || "";
    if (!text.includes("__next_f")) continue;
    if (!text.includes("models") && !text.includes("releases")) continue;
    const match = text.match(/^self\\.__next_f\\.push\\((.+)\\)$/s);
    if (!match) continue;
    try {
      const arr = eval(match[1]);
      const content = arr[1];
      const colonIdx = content.indexOf(":");
      const data = JSON.parse(content.substring(colonIdx + 1));
      for (const m of _findAllModels(data, 25)) modelsFound.push(m);
      for (const r of _findAllReleases(data, 25)) releasesFound.push(r);
    } catch(e) { /* skip chunk */ }
  }
  return JSON.stringify({models: modelsFound, releases: releasesFound});
})()
""".replace("SEARCH", _SEARCH_ALL_JS)


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
        payload = json.loads(raw_json)
        # Backward compat: very old payloads returned a bare list of models arrays
        if isinstance(payload, list):
            models_arrays = payload
            releases_arrays = []
        else:
            models_arrays = payload.get("models", [])
            releases_arrays = payload.get("releases", [])
        print(f"  models arrays found: {len(models_arrays)} "
              f"({[len(a) for a in models_arrays]} models, "
              f"{[len(a[0].keys()) if a else 0 for a in models_arrays]} fields each)")
        print(f"  releases arrays found: {len(releases_arrays)} "
              f"({[len(a) for a in releases_arrays]} releases, "
              f"{[len(a[0].keys()) if a else 0 for a in releases_arrays]} fields each)")

        models = max(models_arrays, key=lambda a: len(a[0].keys())) if models_arrays else []
        if len(models_arrays) > 1:
            main_slugs = {m.get("slug") for m in models}
            meta_by_slug = {}
            for arr in models_arrays:
                if arr is models:
                    continue
                for m in arr:
                    sl = m.get("slug")
                    if sl and sl in main_slugs and sl not in meta_by_slug:
                        meta_by_slug[sl] = m
            n_merged = 0
            for m in models:
                meta = meta_by_slug.get(m.get("slug"))
                if not meta:
                    continue
                for k, v in meta.items():
                    if k not in m and v is not None:
                        m[k] = v
                        n_merged += 1
            print(f"  Merged metadata fields into {len(meta_by_slug)} models "
                  f"({n_merged} field values, e.g. releaseSlug)")

        # V19: join releaseSlug -> releases[slug].releaseDate
        release_map = {}
        for arr in releases_arrays:
            for r in arr:
                sl = r.get("slug")
                rd = r.get("releaseDate")
                if sl and rd and sl not in release_map:
                    release_map[sl] = rd
        print(f"  Release-date map: {len(release_map)} releases")
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
        print(f"  Models with releaseDate after join: {n_dated}/{len(models)} "
              f"(no releaseSlug: {n_no_slug})")
        if models and n_dated == 0:
            sample_slugs = [m.get("releaseSlug") for m in models[:5]]
            raise RuntimeError(
                "No releaseDate resolved after releases join "
                f"(models={len(models)}, releases={len(release_map)}, "
                f"sample releaseSlugs={sample_slugs}). AA payload likely changed again."
            )

        print(f"  Extracted {len(models)} models")
        if models:
            print(f"  Fields per model: {len(models[0].keys())}")
            m = models[0]
            raw_cost = m.get("intelligenceIndexCostTotal")
            try:
                if raw_cost in (None, "", "--", "?"):
                    cost_str = "$?"
                else:
                    cost_str = f"${float(raw_cost):.2f}"
            except (ValueError, TypeError):
                cost_str = "$?"
            print("  Sample: " + str(m.get("name")) + ", releaseDate=" + str(m.get("releaseDate")) + ", releaseSlug=" + str(m.get("releaseSlug")) + ", intelIndex=" + str(m.get("intelligenceIndex")))

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
            print(f"WARNING: Only {len(data) if data else 0} models scraped (expected {MIN_MODELS_EXPECTED})")
    except Exception as e:
        print(f"Scraping failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
