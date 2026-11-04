"""Check what AksharaDB cannot: that cited pages and the locations of list entries exist.

Reads the DB root (default: the current directory). Every page number in a
_described-in or _published-in link must be in that publication's `pages` list,
and every page with a tag should have its scan attachment <key>_<tag>.png.
Prints one line per problem; exits 1 if a cited page is not listed.
Run: python scripts/check_pages.py [DB_ROOT]
"""
import sys
from pathlib import Path

import yaml


def load_collection(root, name):
    return {p.stem: yaml.safe_load(p.read_text(encoding="utf-8"))
            for p in sorted((root / f"_{name}").rglob("*.yaml"))}


def cited_pages(documents, relation):
    """Yield (document key, publication key, page) for every cited page."""
    for key, doc in documents.items():
        links = (doc.get("_publications") or {}).get(relation) or []
        for link in links:
            for page in link.get("pages", []):
                yield key, link["id"], page


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    publications = load_collection(root, "publications")
    listed = {key: {p["page"] for p in doc["pages"] if "page" in p} for key, doc in publications.items()}

    errors = 0
    citations = [("_manuscripts", c) for c in cited_pages(load_collection(root, "manuscripts"), "_described-in")]
    citations += [("_lists", c) for c in cited_pages(load_collection(root, "lists"), "_published-in")]
    for collection, (key, publication, page) in citations:
        if page not in listed.get(publication, set()):
            print(f"{collection}/{key}: cites page {page} of {publication}, which is not in its pages list")
            errors += 1

    # A list entry names its place by key in an attribute, which AksharaDB does not check.
    locations = set(load_collection(root, "locations"))
    for key, doc in load_collection(root, "lists").items():
        for relation in ("_includes", "_includes-also"):
            for link in (doc.get("_works") or {}).get(relation, []):
                if "location" in link and link["location"] not in locations:
                    print(f"_lists/{key}: entry {link.get('item_no')} names location {link['location']!r}, which does not exist")
                    errors += 1

    scans = {p.stem for p in (root / "_publications").rglob("*.png")}
    missing = sorted(f"{key}_{p['tag']}" for key, doc in publications.items() for p in doc["pages"]
                     if "tag" in p and f"{key}_{p['tag']}" not in scans)
    if missing:
        print(f"{len(missing)} listed page(s) have no scan yet, e.g. {missing[0]}.png")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
