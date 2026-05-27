import sys
from pathlib import Path
from lib import ROOT

BAD = [
    "\ufffd",
    "\u00d0",
    "\u00d1",
    "\u0420\u045f",
    "\u0420\u0459",
    "\u0420\u040e",
    "\u0420\u045c",
    "\u0420\u045a",
    "\u0420\u201d",
    "\u0420\u2019",
    "\u0420\u2022",
    "\u0420\u0098",
    "\u0421\u0453",
    "\u0421\u201a",
    "\u0421\u040a",
    "\u0421\u2039",
    "\u0421\u2021",
    "\u0421\u20ac",
]


def main():
    errors = []
    for path in sorted(ROOT.rglob("*")):
        if path.suffix.lower() not in {".md", ".yaml", ".json", ".py", ".html"}:
            continue
        text = path.read_text(encoding="utf-8")
        for marker in BAD:
            if marker in text:
                errors.append(f"{path}: suspicious encoding marker {ascii(marker)}")
                break
    if errors:
        for e in errors:
            print("ERROR:", e)
        return 1
    print("OK: UTF-8 text has no obvious mojibake markers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
