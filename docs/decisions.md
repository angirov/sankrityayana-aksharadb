# Decisions

Decisions taken while transcribing, with the reason. The owner's decisions are marked (owner).
Open questions are in `progress.md`.

## Model

- (owner) Collections: `_publications` (pages as attachments, not a collection of their own),
  `_locations` (monasteries, libraries), `_lists` (lists drawn up by someone: the photographed
  list of 1937, the Göttingen collection), `_manuscripts` (one volume = "Vol. No."), `_works`
  ("Name"), `_authors`.
- What a list says about one title in one volume is an attribute of the `_contains` link.
- A title's number inside its volume is `no_in_volume`; the running number of the list is `item_no`.
- A second copy of a work in one volume goes to `_contains-also`, because AksharaDB allows a work
  once per link list. To be replaced by a link discriminator (AksharaDB issue #11).
- Titles that are only descriptions (“(darśanagrantha)”, “Vyākaraṇa (?)”) are works with keys
  `unidentified-<year>-<no>`; untitled or fragmentary titles likewise get a work of their own.
- Works of the same title by different authors are separate works (`hevajrasadhana-<author>`); a
  second work of the same title by the same author gets a `-2` key.
- “Miscellaneous leaves”, “Loose leaves” link to the work `miscellaneous-leaves` (not a real work).
- A work named only in a footnote, not numbered in the list (1938, Pratyekabuddhabhūmi with
  no. 350), is a `_contains` link without `item_no`.
- Quotations of a text's beginning and end ("Begins—", "In the end—") go into `incipit` and
  `explicit` (added for 1938); a colophon into `colophon`.

## Reading

- Sanskrit in records in IAST; editorial marks and doubts of the source kept as printed.
- Ditto marks are expanded; the note says which fields were dittos. An unclear ditto is flagged.
- A printed misprint is kept in the `*_as_printed` field; the work or author has the normal form
  and a note (“printed so”). No identification beyond the obvious is made in a record; a likely
  identification goes into a note.
- Brackets the source puts round an author (“(Haribhadra)”, “(”)”) are kept in
  `author_as_printed`; the author is still linked.
- `uncertain_fields` marks our doubts only (blurred figures, unclear dittos, hard colophons);
  `scripts/doubts.py` lists them.
- A column that holds something other than a status (“page 13 missing”, “(Pāṇini 1.1)”, “II,III
  Chapters”) is kept in `status` or explained in `notes`, as printed.

## Pages and texts

- Page images: one per printed page, spreads cut at the gutter, sideways pages turned upright,
  lossless 1-bit PNG. Unnumbered plates and front matter get tags `plateN`, `frontN`.
- Page texts (`.md`): as printed, without running heads; Devanagari stays Devanagari; paragraphs
  joined; a word cut at the page break stays cut.
