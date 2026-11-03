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
- A volume described in two publications (Spos-khang I–III: 1935, and “some correction and
  addition” in 1938) stays one manuscript with two `_described-in` links. Each `_contains` link
  of such a volume names its list in `source`. Both lists are kept as printed, even where 1938
  corrects 1935 (titles, numbers, the volume a title is in); notes point out the differences.
  Where both lists name the same work, the entry of 1938 goes to `_contains-also` (see issue #11:
  `source` plus `item_no` would be the discriminator).
- In 1938 Spos-khang nos. 6–7 have no vol. no.; a new count (1) begins after vol. I, so they are
  taken as vol. II (where 1935 has nos. 5–6).
- 1937: item numbers 180–184 of section VI (Chhag-pe-lha-khang, Sa-skya) repeat the numbers of
  1935 (Gu-rim-lha-khang, nos. 180–184): the list of 1937 restarts its count at 180. Numbers are
  only unique within a publication; `item_no` is read together with the publication.
- A run of numbered titles that starts a new count (1, 2, ...) without a printed vol. no. is an
  unnumbered volume, keyed by location + first item number (`chhag-pe-lha-khang-186`).
- A footnote whose number points to one row but whose content clearly describes another (1937, p. 28) is assigned by its content, said so in the notes, and the notes are flagged.
- Long quotations in footnotes (1938 Spos-khang, pp. 148–162: several pages of verse and prose)
  are not transcribed into the records; the records say where they are. Their text is to come
  with the page texts (`.md`) of those pages, a later step.
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
