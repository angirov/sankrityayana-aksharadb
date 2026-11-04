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
  addition” in 1938) stays one manuscript with two `_described-in` links, and its `_contains`
  links follow 1938 (owner, 2026-11-04; replaces “both lists kept as printed”). One link per
  entry of 1938, with `source: sankrtyayana1938`; the reading of 1935 (title, number, marks) goes
  into the notes of the link it corresponds to. Correspondences: III by position (1935 nos. 7, 8,
  9 → 1938 nos. 8, 363, 9; confirmed by the title page quoted in 1938); I no. 4 → no. 4 (the
  footnote cites 1935); II no. 6 → no. 7 (Parikathā) and no. 5 → no. 6: the “Commentary on some
  Sarvāstivāda Sūtras” of 1935 is most likely the Tridaṇḍamālā (owner), so that work was removed.
- In 1938 Spos-khang nos. 6–7 the Vol. column is empty (p. 157: only the number in the volume, 1,
  begins anew); most likely vol. II, its number left out by mistake (owner), where 1935 has nos.
  5–6.
- Madhyāntavibhaṅgakārikā and Madhyāntavibhaṅgasūtra (1935, Spos-khang III nos. 7, 8) are not told
  apart: one work `madhyantavibhaga` (owner, 2026-11-04). 1938 has the title once; in the place of
  the second it has the Dharmadharmatāvibhāga.
- 1937: item numbers 180–184 of section VI (Chhag-pe-lha-khang, Sa-skya) repeat the numbers of
  1935 (Gu-rim-lha-khang, nos. 180–184): the list of 1937 restarts its count at 180. Numbers are
  only unique within a publication; `item_no` is read together with the publication.
- A volume without a printed vol. no. is keyed by location + its first item number.
  (owner) 1937 Chhag-pe-lha-khang: the IV printed between nos. 184 and 185 is the number of the
  volume of nos. 186–192 (counted 1–7), `chhag-pe-lha-khang-iv`; no. 185 is the unnumbered
  volume `chhag-pe-lha-khang-185`.
- A footnote whose number points to one row but whose content clearly describes another (1937, p. 28) is assigned by its content, said so in the notes, and the notes are flagged.
- A work in several physical volumes given one entry and a range of vol. nos. (1937 no. 216, vols. XX–XXIII) is one manuscript record, `vol_no: XX-XXIII`.
- Unidentified titles printed as ditto marks of each other in one volume (1937 nos. 231–233, “saṃskṛtapustaka”) are separate works, since nothing shows they are one text (and a third copy could not go into `_contains-also`, issue #11).
- (owner) The list “MSS. Photographed or copied” (1937) lists works, not volumes. It is one
  `_lists` document whose `_works._includes` links name the works; each link carries the entry
  as printed (number, page, subject, name, author, size in ślokas, status), the place
  (`location`, the key of a `_locations` document; S = Sa-skya as a monastery, since the library
  is not named) and `reproduction` (x = copied). The 55 manuscript records made for it at first
  were removed. A work listed twice (Vinayasūtravṛtti, nos. 53 Sh and 54 S) has its second entry
  in `_includes-also` (issue #11). `scripts/check_pages.py` checks that each `location` exists;
  AksharaDB issue #12 (reference attributes) would let AksharaDB check it, and with #11 make
  `location` the discriminator, so that `_includes-also` goes.
  `docs/photographed-1937-matches.md` compares the list with the catalogue volumes.
- (owner) Each entry of the photographed list names the volume it is identified with
  (`manuscript`) and how sure that is (`match`: certain, probable, possible, list-only; reasons in
  `match_note`). An entry with no catalogued volume got a new volume record
  `<location>-photographed-<no>` (9: nos. 5, 10, 12, 19, 22, 31, 37, 41, 48), described in the list
  (1937, its page). For a certain match the volume must contain the entry's work (checked by
  `scripts/check_pages.py`); a probable or possible match may name the work differently, and the
  note says which catalogue work it would be. No work records are merged until the owner accepts.
- (owner) No `_listed-in` relation from volumes to lists: lists link to works.
- (owner) Works merged (2026-11-04): abhisamayalankara-prajnopadesasastra → abhisamayalankara,
  katantravrttipanjika → katantrapanjika, kasika-pancika → kasikavivaranapanjika,
  vadanyayatika-1935-171 → vadanyayatika (probable, the link is flagged); pramanavarttikavrtti
  renamed pramanavarttikasvavrtti. The printed titles stay in `name_as_printed` and
  `other_titles`. Kept apart for now: the two Hevajrasādhanas of Anaṅgavajra, the two
  Cakrasaṃvaravivṛtis, the Cāndravyākaraṇa commentaries (Madhyāntavibhaṅgasūtra/-kārikā: merged,
  see above).
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
