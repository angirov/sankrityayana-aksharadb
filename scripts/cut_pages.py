"""Cut a publication's scan into one image per page, as the publication's attachments.

Takes a publication key and the path of its source PDF; reads the `pages` list of
_publications/<key>.yaml (pdf_page, side, rotated, tag) and writes
_publications/<key>/<key>_<tag>.png, lossless and 1-bit like the scan.
A two-page spread is split at its gutter, the dark band of the binding near the
middle; a page printed sideways is turned 90° clockwise.
Run: python3 scripts/cut_pages.py sankrtyayana1935 path/to/scan.pdf [--only TAG ...]
Needs poppler-utils (pdfimages, pdfinfo), Pillow and PyYAML.
"""
import argparse
import re
import subprocess
import tempfile
from pathlib import Path

import yaml
from PIL import Image

# The gutter is looked for in the middle part of the spread only, so that a dark
# edge of the scan is never taken for it.
GUTTER_SEARCH = (0.35, 0.65)
GUTTER_SMOOTHING = 15


def page_rotation(pdf, pdf_page):
    """The /Rotate of one PDF page, in degrees clockwise."""
    info = subprocess.run(["pdfinfo", "-f", str(pdf_page), "-l", str(pdf_page), str(pdf)],
                          capture_output=True, text=True, check=True).stdout
    return int(re.search(rf"Page\s+{pdf_page} rot:\s+(\d+)", info).group(1))


def spread_image(pdf, pdf_page, workdir):
    """The scan of one PDF page as it is displayed: the stored image, turned by /Rotate."""
    prefix = Path(workdir) / f"pdf{pdf_page:03d}"
    subprocess.run(["pdfimages", "-f", str(pdf_page), "-l", str(pdf_page), "-png", str(pdf), str(prefix)],
                   check=True)
    images = sorted(Path(workdir).glob(f"{prefix.name}-*.png"))
    if len(images) != 1:
        raise SystemExit(f"PDF page {pdf_page}: expected one image, found {len(images)}")
    return Image.open(images[0]).rotate(-page_rotation(pdf, pdf_page), expand=True)


def gutter(spread):
    """The column of the binding: the darkest column in the middle of the spread."""
    gray = spread.convert("L")
    width, height = gray.size
    start, end = (int(width * f) for f in GUTTER_SEARCH)
    band = gray.crop((start, 0, end, height)).resize((end - start, 1), Image.Resampling.BOX)
    darkness = [255 - v for v in band.getdata()]
    smoothed = [sum(darkness[max(0, i - GUTTER_SMOOTHING):i + GUTTER_SMOOTHING + 1]) for i in range(len(darkness))]
    return start + smoothed.index(max(smoothed))


def cut(spread, side):
    if side == "single":
        return spread
    middle = gutter(spread)
    box = (0, 0, middle, spread.height) if side == "left" else (middle, 0, spread.width, spread.height)
    return spread.crop(box)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("key")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--only", nargs="*", help="cut only these tags")
    args = parser.parse_args()

    publication = yaml.safe_load(Path(f"_publications/{args.key}.yaml").read_text(encoding="utf-8"))
    out = Path(f"_publications/{args.key}")
    out.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as workdir:
        spreads = {}
        for page in publication["pages"]:
            if "tag" not in page or (args.only and page["tag"] not in args.only):
                continue
            n = page["pdf_page"]
            if n not in spreads:
                spreads[n] = spread_image(args.pdf, n, workdir)
            image = cut(spreads[n], page["side"])
            if page.get("rotated"):
                image = image.rotate(-90, expand=True)
            target = out / f"{args.key}_{page['tag']}.png"
            image.convert("1").save(target, optimize=True)
            print(f"{target}  {image.width}x{image.height}  {target.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
