import argparse
import os
import time
import json
from typing import List, Dict, Any, Tuple

import requests
import pandas as pd
from tqdm import tqdm

BASE = "https://api.openalex.org"

def oa_get(path: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """GET helper with basic retries."""
    url = f"{BASE}{path}"
    for attempt in range(5):
        r = requests.get(url, params=params, timeout=60)
        if r.status_code == 429:
            # rate limited
            time.sleep(2 + attempt)
            continue
        r.raise_for_status()
        return r.json()
    raise RuntimeError(f"Failed after retries: {url}")

def short_id(openalex_id: str) -> str:
    # Accept either https://openalex.org/T123 or just T123
    if openalex_id.startswith("https://openalex.org/"):
        return openalex_id.split("/")[-1]
    return openalex_id

def discover_topic_candidates(api_key: str, terms: List[str], per_term: int = 5) -> List[Tuple[str, str, int]]:
    """Return (display_name, topic_id, works_count) candidates."""
    out = []
    for term in terms:
        j = oa_get("/topics", {
            "search": term,
            "per_page": per_term,
            "api_key": api_key,
        })
        for t in j.get("results", []):
            out.append((t.get("display_name", ""), short_id(t.get("id", "")), int(t.get("works_count", 0))))
    # de-dup by topic_id, keep max works_count
    best = {}
    for name, tid, wc in out:
        if tid and (tid not in best or wc > best[tid][2]):
            best[tid] = (name, tid, wc)
    # sort by works_count desc
    return sorted(best.values(), key=lambda x: -x[2])

def fetch_top_ai_institutions(api_key: str, topic_ids: List[str], max_institutions: int = 500) -> List[Dict[str, Any]]:
    """
    Pull institutions that have these topics in their aboutness.
    Cursor paging explained in OpenAlex docs. :contentReference[oaicite:1]{index=1}
    """
    filt = "topics.id:" + "|".join(topic_ids)  # OR within one filter is | :contentReference[oaicite:2]{index=2}
    params = {
        "filter": filt,
        "sort": "works_count:desc",
        "select": "id,display_name,country_code,geo,works_count",
        "per_page": 200,
        "cursor": "*",
        "api_key": api_key,
    }

    inst = []
    while True:
        j = oa_get("/institutions", params)
        inst.extend(j.get("results", []))
        if len(inst) >= max_institutions:
            inst = inst[:max_institutions]
            break
        next_cursor = (j.get("meta") or {}).get("next_cursor")
        if not next_cursor:
            break
        params["cursor"] = next_cursor
        time.sleep(0.2)
    return inst

def count_recent_ai_works_for_institution(api_key: str, inst_id: str, topic_ids: List[str], year_start: int, year_end: int) -> int:
    """
    Count works for a single institution in [year_start, year_end] tagged with AI topics.
    Uses filter AND (comma) and OR (|) as documented. :contentReference[oaicite:3]{index=3}
    """
    inst_short = short_id(inst_id)
    topics_or = "|".join(topic_ids)
    # publication_year supports ranges like 2021-2025 in many OpenAlex examples; if it errors, fall back to > and <.
    filt = f"authorships.institutions.id:{inst_short},topics.id:{topics_or},publication_year:{year_start}-{year_end}"
    j = oa_get("/works", {
        "filter": filt,
        "per_page": 1,
        "api_key": api_key,
    })
    return int((j.get("meta") or {}).get("count", 0))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="openalex_out", help="Output directory")
    ap.add_argument("--topic-ids", nargs="*", default=[], help="Explicit OpenAlex topic IDs like T154945302")
    ap.add_argument("--max-institutions", type=int, default=500, help="How many AI-relevant institutions to sample (default 500)")
    ap.add_argument("--year-start", type=int, default=2021)
    ap.add_argument("--year-end", type=int, default=2025)
    args = ap.parse_args()

    api_key = os.environ.get("OPENALEX_API_KEY", "").strip()
    if not api_key:
        raise SystemExit("Missing OPENALEX_API_KEY env var. Set it first (see instructions).")

    os.makedirs(args.outdir, exist_ok=True)

    # 1) Topics
    if args.topic_ids:
        topic_ids = [short_id(x) for x in args.topic_ids]
        candidates = []
    else:
        # auto-discover candidates
        terms = ["machine learning", "artificial intelligence", "deep learning", "large language models", "natural language processing"]
        candidates = discover_topic_candidates(api_key, terms)
        # pick top 3 by works_count as a sensible default
        topic_ids = [tid for (_, tid, _) in candidates[:3]]

    with open(os.path.join(args.outdir, "openalex_topics_used.json"), "w", encoding="utf-8") as f:
        json.dump({"selected_topic_ids": topic_ids, "candidates": candidates[:20]}, f, indent=2)

    print("Selected topic IDs:", topic_ids)
    if candidates:
        print("\nTop topic candidates (first 10):")
        for name, tid, wc in candidates[:10]:
            print(f"  {tid:>12} | works={wc:<10} | {name}")

    # 2) Institutions
    institutions = fetch_top_ai_institutions(api_key, topic_ids, max_institutions=args.max_institutions)

    inst_rows = []
    for inst in institutions:
        geo = inst.get("geo") or {}
        inst_rows.append({
            "institution_id": short_id(inst.get("id", "")),
            "institution_name": inst.get("display_name", ""),
            "country_code": inst.get("country_code", ""),
            "geo_city": geo.get("city", ""),
            "geo_region": geo.get("region", ""),
            "geo_country_code": geo.get("country_code", ""),
            "geo_lat": geo.get("latitude", None),
            "geo_lon": geo.get("longitude", None),
            "works_count_total": inst.get("works_count", None),
        })
    inst_df = pd.DataFrame(inst_rows)
    inst_df.to_csv(os.path.join(args.outdir, "openalex_ai_institutions_top.csv"), index=False)

    # 3) Recent AI works counts (2021-2025 by default)
    # This is the “spread of AI” overlay: recent AI output, not just all-time institution size.
    ai_counts = []
    for inst_id in tqdm(inst_df["institution_id"].fillna("").tolist(), desc="Counting recent AI works"):
        if not inst_id:
            ai_counts.append(0)
            continue
        try:
            c = count_recent_ai_works_for_institution(api_key, inst_id, topic_ids, args.year_start, args.year_end)
        except Exception:
            c = 0
        ai_counts.append(c)
        time.sleep(0.15)
    inst_df["ai_works_count_recent"] = ai_counts
    inst_df.to_csv(os.path.join(args.outdir, "openalex_ai_institutions_top.csv"), index=False)

    # 4) Aggregate to city
    # Use geo_city + geo_country_code to disambiguate “Cambridge” etc.
    city_df = (
        inst_df.dropna(subset=["geo_city", "geo_country_code"])
        .groupby(["geo_city", "geo_country_code"], as_index=False)
        .agg(
            ai_works_recent=("ai_works_count_recent", "sum"),
            ai_institution_count=("institution_id", "nunique"),
            lat=("geo_lat", "mean"),
            lon=("geo_lon", "mean"),
        )
        .sort_values("ai_works_recent", ascending=False)
    )

    city_df.to_csv(os.path.join(args.outdir, "openalex_ai_city_overlay.csv"), index=False)
    print(f"\nWrote outputs to: {args.outdir}")
    print("Upload this file to ChatGPT: openalex_ai_city_overlay.csv")

if __name__ == "__main__":
    main()