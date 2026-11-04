# Wishes for AksharaDB

What this DB root needs from AksharaDB. Filed: angirov/AksharaDB #11 (link discriminator, keyword
`linkDiscriminator`), #12 (reference attributes, keyword `refersTo`), #13 (strict schemas, to land
first) and, on 2026-11-04, the issue below as #15. Kept here as the record of what was asked.

## Viewer: images, tables of fields and links, collection tables

Found while building the viewer for this DB root (139 volumes, 322 works, page scans as
attachments of publications). The viewer works, but for such data it is hard to read:

1. **Image attachments are only links.** A publication has one PNG per printed page
   (`<key>_p027.png`); the viewer lists them as links. Show images inline (thumbnails with a link
   to the full image), in the order of the files or of a list in the document.
2. **Documents are shown as raw YAML.** A table of fields (name, value) would read better; nested
   lists of objects (e.g. `pages`) as tables.
3. **Links are shown inside the YAML.** A relation with many attributes (here `_contains` with 21:
   number, title as printed, script, size, colophon …) should be a table, one row per link, the
   target as a link, the attributes as columns (empty columns left out).
4. **Collection pages list keys only.** A table with a few chosen fields per document
   (configurable, e.g. in `config.yaml`: `viewer: {columns: [vol_no, _locations._kept-in]}`) would
   make a catalogue browsable; a default title field (AksharaDB TODO.md “default title field”).
5. **Linking a page from a link attribute.** A link `_described-in: [{id: P, pages: [27]}]` could
   link “p. 27” to the page image of P (attachment tag `p027`), so a record leads straight to its
   scan. This may need a small declaration in the schema or config.
6. **Schema diagram.** The label of a relation lists all its attributes; with 21 attributes it
   becomes unreadable. Show the attribute count, or the attributes in a box of their own.

The branch `schema-diagram` (phase 5) should land first; items 1–3 are the most useful.
