# scripts

- `check_pages.py`: checks that every page an entry cites is in its publication's `pages` list,
  and counts listed pages that have no scan yet.
- `cut_pages.py`: cuts a publication's scan into one PNG per page (the attachments), from the
  `pages` list of `_publications/<key>.yaml`.
