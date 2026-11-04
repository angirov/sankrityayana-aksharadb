# sankrityayana-mss

The lists of Sanskrit manuscripts that Rāhula Sāṅkṛtyāyana found in Tibetan monasteries,
transcribed from his three reports in the *Journal of the Bihar and Orissa Research Society*
(1935, 1937, 1938) into structured data, with a scan of every printed page.

This directory is an [AksharaDB](https://github.com/angirov/AksharaDB) DB root: one YAML file per
record, JSON Schemas in `schemas/`, rules in `config.yaml`. Check it with:

```bash
aksharadb validate
python scripts/check_pages.py
```

## Collections

| Collection | One document is | Links to |
|---|---|---|
| `_publications` | an article; its printed pages are attachments (`<key>_p027.png` scan, `<key>_p027.md` text) | — |
| `_locations` | a place where manuscripts are kept (a monastery) | — |
| `_lists` | a list drawn up by someone: the photographed list of 1937 (of works), the Göttingen collection | `_publications` (`_published-in`), `_works` (`_includes`, with number, place and kind of reproduction) |
| `_manuscripts` | one physical volume ("Vol. No.") | `_locations` (`_kept-in`), `_publications` (`_described-in`, with pages), `_lists` (`_listed-in`, with number and catalogue number), `_works` (`_contains`) |
| `_works` | a text ("Name" in the tables) | `_authors` (`_composed-by`) |
| `_authors` | an author | — |

What a table says about one title in one volume (its number, script, size, leaves, colophon) is an
attribute of the `_contains` link, because a volume can hold several titles. The title and the author
are kept as printed there; the linked work and author carry the normalised forms.

`_lists` are lists drawn up by someone, not AksharaDB's "collections" (the `_` directories).

## Conventions

- Sanskrit in IAST, not Devanagari; editorial marks of the source (`[...]`, `(?)`) kept as printed.
- Ditto marks are expanded to the value they repeat; a doubtful reading goes into `uncertain_fields`.
- A field the source leaves blank or prints as `..` is left out.
- Page numbers are printed pages; a two-page spread of the scan is cut into its two pages.
- A page's text (`<key>_p021.md`) is the text as printed, without the running head: diacritics,
  spelling and misprints kept, Devanagari kept as Devanagari, paragraphs joined into lines, words
  broken at a line end joined. A word or paragraph cut by the page break stays cut.

The source scans are not in the repository. Details of the work: `docs/CLAUDE.md` (the method), `docs/progress.md`.
