import requests
import csv
from typing import List

START_URL = "https://gutendex.com/books/?languages=hu"
OUTPUT_CSV = "talalatok.csv"
MAX_PAGES = 4
TIMEOUT = 200

def join_authors(authors: List[dict]) -> str:
    names = [a.get("name", "").strip() for a in authors if a.get("name")]
    return ", ".join(names)

def join_summaries(summaries) -> str:
    if not summaries:
        return ""
    # summaries lehet lista vagy más típus; kezeljük biztonságosan
    if isinstance(summaries, list):
        parts = [str(s).strip() for s in summaries if s is not None and str(s).strip() != ""]
        return "\n".join(parts)
    return str(summaries).strip()

def process_page(url: str, page_number: int) -> (List[dict], str):
    """
    Lekéri az adott URL-t, visszaadja a feldolgozott könyvlistát és a next URL-t (vagy None).
    """
    try:
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Hiba a {url} lekérésekor: {e}")

    try:
        data = resp.json()
    except ValueError as e:
        raise RuntimeError(f"Nem sikerült JSON-t dekódolni a {url}-ről: {e}")

    results = data.get("results", [])
    processed = []
    for book in results:
        title = book.get("title", "") or ""
        authors = join_authors(book.get("authors", []))
        summaries = join_summaries(book.get("summaries", []))
        processed.append({
            "title": title,
            "authors": authors,
            "summaries": summaries,
            "page": page_number
        })

    next_url = data.get("next")
    return processed, next_url

def main():
    url = START_URL
    all_records = []
    page = 1

    while url and page <= MAX_PAGES:
        print(f"Lekérem: {url}  (oldal {page})")
        try:
            records, next_url = process_page(url, page)
        except RuntimeError as e:
            print("Hiba:", e)
            break

        all_records.extend(records)

        if not next_url:
            break

        url = next_url
        page += 1

    if not all_records:
        print("Nincs mentendő rekord.")
        return

    # CSV írás
    fieldnames = ["title", "authors", "summaries", "page"]
    try:
        with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for r in all_records:
                writer.writerow(r)
        print(f"{len(all_records)} rekord mentve a {OUTPUT_CSV} fájlba.")
    except IOError as e:
        print("Hiba a fájl írása közben:", e)

if __name__ == "__main__":
    main()
