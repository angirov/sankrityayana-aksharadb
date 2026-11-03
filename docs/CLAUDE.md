# CLAUDE.md

An AksharaDB DB root (see `README.md`) built from Sāṅkṛtyāyana's lists of manuscripts in JBORS
1935, 1937, 1938. It continues `~/Dropbox/sankrtyayana-catalog` (the first draft, page 27 of 1935).

## Sources

The scans live outside the repository, in `~/Dropbox/sankrtyayana-catalog/pdfs/` (the original
1935 scan is `~/Dropbox/PDFs/sāṅkṛtyāyana_1935_sanskrit_palm-leaf_mss._in_tibet.pdf`). They are
600 dpi bilevel. Most PDF pages are two-page spreads; the tables are printed rotated 90°. Ordinary
OCR fails on the tables: read them from the rendered image directly.

## Checks

```bash
/home/dev/AksharaDB/venv/bin/aksharadb validate
/home/dev/AksharaDB/venv/bin/python scripts/check_pages.py
```

Both must pass before a commit.

## Transcribing a table page

1. Find the next page in `docs/progress.md`. Look at the page's scan, not an OCR layer.
2. One `_manuscripts` document per volume (key: location + roman vol. no., `ngor-xl`; a volume
   from a list without vol. no.: list + number, `photographed-1937-12`). Each title is one
   `_contains` link with the attributes of `schemas/_manuscripts.yaml`; create the work and the
   author if they are new. Footnotes go to the entry they annotate.
3. IAST for all Sanskrit; marks of the source kept; ditto marks expanded; doubts in
   `uncertain_fields`; blanks and `..` left out.
4. Cite the printed page(s) of the row and its footnotes in `_described-in`.
5. Run the checks; update `docs/progress.md` (status, doubts for a manual check).

One page at a time: check each page's result against the scan before the next. Don't
batch-transcribe pages unread.

## Working rules

- English in files and commits. Commit each finished page or step; push only when asked.
- Work out a key, a work's identity or an author's name carefully; when unsure, keep the
  printed form and say so in `notes`, rather than guessing an identification.
