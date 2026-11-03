"""List every reading marked for a check against the scan.

Reads _manuscripts/*.yaml (default DB root: the current directory) and prints one
line per title whose `uncertain_fields` is not empty: publication, page, item
number, volume and the doubtful fields, sorted by publication and item number.
Run: python scripts/doubts.py [DB_ROOT]
"""
import sys
from pathlib import Path

import yaml


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    rows = []
    for path in sorted((root / "_manuscripts").rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        descriptions = {d["id"]: d for d in doc["_publications"]["_described-in"]}
        first = doc["_publications"]["_described-in"][0]
        for relation in ("_contains", "_contains-also"):
            for link in doc["_works"].get(relation, []):
                if link.get("uncertain_fields"):
                    # a link names its list (source) when the volume is described twice
                    described = descriptions.get(link.get("source"), first)
                    rows.append((described["id"], link.get("item_no", 0), described["pages"], path.stem,
                                 ", ".join(link["uncertain_fields"])))
    for publication, item, pages, volume, fields in sorted(rows):
        print(f"{publication}  no. {item:<4} pp. {','.join(map(str, pages)):<9} {volume:<22} {fields}")
    print(f"{len(rows)} title(s) to check")


if __name__ == "__main__":
    main()
