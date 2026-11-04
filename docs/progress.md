# Progress

**State (2026-11-04):** all three articles are done: inventory, scans of every page, the text of
every prose page, and every list (1935 nos. 1–184; 1938 nos. 4–9 and 337–363; 1937 nos. 180–336
and the photographed list nos. 1–55). 139 manuscripts, 322 works, 97 authors, 8 locations,
1 list. `scripts/doubts.py` lists the readings to check against the scans (41).
What is left is listed under “Open questions” and “Not yet transcribed”.

## Not yet transcribed

- Long quotations in footnotes (see Next steps), given in the records as “not transcribed here” (1938 pp. 148–162;
  1937 nos. 195, 200, 201, 251, 307, 310, 325 and others): their text belongs in the page texts
  (`.md`) of the table pages, which do not exist yet.
- The chart of figures (1937, `chart1`, `chart2`) and the plates are kept as images only.

Inventory and scans: the `pages` list of each `_publications/<key>.yaml` is the inventory;
`scripts/cut_pages.py` cuts the scans from it.

| Publication | Inventory | Scans | Texts (.md) | Tables |
|---|---|---|---|---|
| sankrtyayana1935 | done (PDF pp. 1–15: 2 front, 6 text, 2 plates, 17 tables, 3 blanks) | done | done (pp. 21–26, front matter) | pp. 27–43 done |
| sankrtyayana1937 | done (PDF pp. 1–36: contents, pp. 1–57, 6 plates, a chart in 2 parts) | done | done (pp. 1–20, contents) | pp. 21–57 done |
| sankrtyayana1938 | done (PDF pp. 1–14: contents p. vi, pp. 137–163) | done | done (pp. 137–142, contents) | pp. 143–163 done (long quotations pending) |

## Tables of 1935

| Page | Contents | Status | Notes |
|---|---|---|---|
| 27 | I. Kun-de-ling, nos. 1–3 | done | Colophons of nos. 1 and 3 to be checked against the scan. |
| 28 | II. Spos-khang, nos. 4–9; III. Ṣa-lu, nos. 10–12 | done | Size of no. 12 (21⅓×2⅛): the last denominator is blurred. Ṣa-lu II and III print a number in the volume (2, 3) though each holds one title. |
| 29 | Ṣa-lu, nos. 13–26 | done | Status column printed below the titles, read in order. Size of no. 13's script is a ditto from p. 28. |
| 30 | Ṣa-lu, nos. 27–37 | done | Vol. VIII (Ratnakīrti) runs over pp. 29–30. No. 27 printed Cittādvaitaprakaraṇavāda; no. 34's author printed Āryakuddāliyāda. |
| 31 | Ṣa-lu, nos. 38–46; IV. Ngor, nos. 47–49 | done | No. 41 has no title. Statuses of vol. XI are dittos of no. 38 (Incomplete). |
| 32 | Ngor, nos. 50–59 | done | Vol. I runs over pp. 31–32. Colophons of nos. 58 (“hca (?)”) and 59 to be checked. |
| 33 | Ngor, nos. 60–71 | done | Size of no. 61 printed 22×2 2/9. |
| 34 | Ngor, nos. 72–80 | done | |
| 35 | Ngor, nos. 81–90 | done | Colophon of no. 84 to be checked. |
| 36 | Ngor, nos. 91–104 | done | No. 91's author printed Saroruvavajra. Vol. XX goes on on p. 37. |
| 37 | Ngor, nos. 105–113 | done | Colophons of nos. 107 and 109 to be checked. |
| 38 | Ngor, nos. 114–124 | done | Size of no. 118 blurred. |
| 39 | Ngor, nos. 125–141 | done | Vol. XXVI (Hevajra texts) runs over pp. 38–40. Works of the same title by different authors are separate works. |
| 40 | Ngor, nos. 142–155 | done | |
| 41 | Ngor, nos. 156–167 | done | No. 167: “Tamil” in the author column; size printed 51⅓×1⅓. |
| 42 | Ngor, nos. 168–178; V. Gu-rim-lha-khang, no. 179 | done | No. 169: “Rañjana” printed in the author column. |
| 43 | Gu-rim-lha-khang, nos. 180–184 | done | The colophon of no. 184 breaks off at the end of the page; its footnotes 3–6 are not in the scan. |

## Open questions

To decide (owner):

- The photographed list of 1937: accept or reject the probable and possible identifications
  (nos. 24, 28, 50, 55; 51); on acceptance, merge the list's work into the volume's work
  (e.g. vinayaksudraka → bhiksuprakirnakavinaya). Nos. 10, 19, 22 are list-only volumes at Ṣha-lu
  whose candidate is at Ngor. Details: `photographed-1937-matches.md`.
- Works kept apart for now (decisions.md): the two Hevajrasādhanas of Anaṅgavajra (Ngor XXVI),
  the two Cakrasaṃvaravivṛtis, the Cāndravyākaraṇa commentaries (1935 no. 82, 1937 no. 295),
  Madhyāntavibhaṅgasūtra and -kārikā (1935 nos. 7, 8).
- 1938 p. 139: the Parikathā (Spos-khang, 1935 no. 6, 1938 no. 7) is “by a later author”, not
  Aśvaghoṣa; the work is still linked to Aśvaghoṣa as in 1935.
- 1938 Spos-khang corrects 1935 (no. 4 is a Sūtra-dhāraṇīsaṃgraha, not an Aṣṭasāhasrikā; no. 5 a
  grammatical commentary in vol. I; no. 8 a Dharmadharmatāvibhāga). Both are kept as printed.
- 1937 Chhag-pe-lha-khang vol. IV: taken (owner) as the volume of nos. 186–192. The layout of
  p. 21 speaks rather for no. 185: the roman numbers and the data columns stand about half a line
  above the titles (II by no. 183, III by 184, IV by 185). To confirm.
- Ngor VIII holds two copies of the Aṣṭasāhasrikā (nos. 63, 64): kept in `_contains-also` until
  AksharaDB issue #11; alternatively no. 64 as a separate manuscript.

To check or find:

- The 42 readings listed by `scripts/doubts.py` against the scans.
- 1935: the scan ends with p. 43, but the article goes on (the footnote of no. 184 breaks off and
  refers to footnotes 3–6). We need pp. 44 ff. of JBORS XXI, Pt. I.
- 1938: the headings refer to “Vol. XXI, Part I, pp 8–10” (Ṣhalu) and “Page 8” (Spos-khang) for
  the list of 1935, which in our scan is on pp. 28–31: an offprint pagination? Check the issue.

Noted, no action:

- “Miscellaneous leaves” is kept as a work (`_works/miscellaneous-leaves`) so that a volume can
  link to it.

## Next steps (not started)

- Page texts (`.md`) for the table pages, to hold the long footnote quotations that the records
  mark “not transcribed here” (1938 pp. 148–162; 1937 nos. 195, 200, 201, 251, 307, 310, 325 …).
- When AksharaDB has issue #11 (link discriminator) and #12 (reference attributes): replace
  `_contains-also` and `_includes-also` by discriminated links (`item_no`, `source`, `location`),
  make `location` and `manuscript` of list entries reference attributes, and drop the matching
  checks from `scripts/check_pages.py`.
- GitHub Actions: no workflow yet. AksharaDB is private and this repository public, so
  `uses: angirov/AksharaDB@…` does not work yet. Planned: check AksharaDB out with a read-only
  token (secret `AKSHARADB_TOKEN`) into `.aksharadb/` (add it to `.gitignore`), run it as a local
  action, then `python scripts/check_pages.py`. Alternatives: make AksharaDB public, or this
  repository private and allow access in AksharaDB's Actions settings.
- The viewer: `aksharadb build --out output` (output/ is ignored), served with
  `python3 -m http.server 8000 --bind 127.0.0.1` in `output/viewer`. The schema page
  (`schema.html`) needs the AksharaDB branch `schema-diagram`.

## Tables of 1938

| Page | Contents | Status | Notes |
|---|---|---|---|
| 143–144 | IX. Ṣhalu (continued), vol. XXXIX (Jñānaśrīmitra, nos. 337–349), vol. XL (no. 350) | done | Heading refers to “Vol. XXI, Part I, pp 8–10” for the Ṣhalu list of 1935, which is on pp. 28–31 of our scan: an offprint pagination? |
| 145 | Ṣhalu vols. XL (end)–XLV, nos. 351–360 and unnumbered leaves | done | From here the author stands in the name column. |
| 146 | Ṣhalu vol. XLVI, no. 361 (astrology) | done | |
| 147–163 | Spos-khang (correction and addition to 1935): vol. I nos. 4, 5, 362; vol. II nos. 6, 7; vol. III nos. 8, 363, 9 | done | Merged into the volumes of 1935 (see decisions.md). Vol. II not printed for nos. 6–7. Long quotations (pp. 148–162) not transcribed yet. |

## Tables of 1937

| Page | Contents | Status | Notes |
|---|---|---|---|
| 21–22 | VI. Chhag-pe-lha-khang (Sa-skya), vols. I–V, nos. 180–194 | done | (owner) Nos. 186–192 are vol. IV, no. 185 is unnumbered (see Open questions). No. 185 continues 1935 no. 150 (Ngor). |
| 23 | Chhag-pe-lha-khang vol. V (end), no. 195 | done | Long quotation of leaf 62 not transcribed. |
| 24–26 | Chhag-pe-lha-khang vols. VI–IX, nos. 196–202 | done | Footnote 3 of no. 200 gives 103 leaves, which is the count of no. 201; recorded as printed. Long verse quotations not transcribed. |
| 27–29 | Chhag-pe-lha-khang vols. IX (end)–XIX, nos. 203–215 | done | Footnotes 1–2 of p. 28 seem shifted by one; assigned by content (decisions.md). |
| 30 | Chhag-pe-lha-khang vols. XX–XXIII, no. 216 (Śatasāhasrikā, 4 vols.) | done | One record for the 4 volumes. |
| 31 | Chhag-pe-lha-khang vols. XXIV–XXXIII, nos. 217–225 | done | Nos. 217–222: copies of the Śatasāhasrikā (ditto marks). |
| 32 | Chhag-pe-lha-khang vols. XXXIV–XXXVIII, nos. 226–236 | done | Tamil Grantha and Sinhalese MSS.; dittos of no. 236 doubtful. |
| 33–34 | VII. Ṣhalu vols. XII–XIV, nos. 237–244 | done | No. 240 (kroḍapatra) linked to the Pramāṇavārttika, flagged. |
| 35–37 | Ṣhalu vol. XIV (end)–XVI, nos. 245–254 | done | Nos. 245, 251: footnote content does not match the title; flagged. |
| 38–39 | Ṣhalu vols. XVII–XXII, nos. 255–268 | done | Size of no. 265 printed “½×2”. |
| 40 | Ṣhalu vols. XXII (end)–XXIV, nos. 269–276 | done | “N.” after Bhāskarācārya (no. 271) unexplained. |
| 41 | Ṣhalu vols. XXIV (end)–XXVII, nos. 277–287 | done | No. 283 numbered 10 in vol. XXV; footnote of no. 280 does not fit the title. |
| 42 | Ṣhalu vols. XXVIII–XXXIII, nos. 288–293 | done | |
| 43 | Ṣhalu vols. XXXIII (end)–XXXIV, nos. 294–296 | done | |
| 44 | Ṣhalu vol. XXXV, nos. 297–300 | done | Cross-reference “XXIV. 4” for no. 300 points to no. 277; the copy is no. 276. |
| 45 | Ṣhalu vol. XXXV (end), nos. 301–303 | done | |
| 46 | Ṣhalu vols. XXXV (end)–XXXVI, nos. 304–307 | done | Eclipse table on no. 307 not transcribed. |
| 47 | Ṣhalu vol. XXXVI (end), nos. 308–310 | done | Notes of Vibhūticandra (no. 310) not transcribed. |
| 48 | Ṣhalu vol. XXXVII, nos. 311–313 | done | |
| 49 | Ṣhalu vol. XXXVII (end), nos. 314–318 | done | |
| 50 | Ṣhalu vols. XXXVII (end)–XXXVIII, nos. 319–324 | done | |
| 51–53 | Ṣhalu vol. XXXVIII (end), nos. 325–330; VIII. Rta-nag Thub-stan, nos. 331–334; IX. Ngor vol. XL, nos. 335–336 | done | Ngor “XL” printed for both 335 and 336. |
| 54–57 | MSS. Photographed or copied, nos. 1–55 | done | Complete list (p. 57 lower half blank). Links to works in `_lists/photographed-1937.yaml`; comparison in photographed-1937-matches.md. |
