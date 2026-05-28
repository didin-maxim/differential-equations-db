from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_RE = re.compile(r"<script(?P<attrs>[^>]*)>(?P<body>.*?)</script>", re.S | re.I)


def iter_inline_javascript(html: str) -> list[str]:
    blocks: list[str] = []
    for match in SCRIPT_RE.finditer(html):
        attrs = match.group("attrs").lower()
        if "src=" in attrs or "application/json" in attrs:
            continue
        body = match.group("body").strip()
        if body:
            blocks.append(body)
    return blocks


def check_html(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    blocks = iter_inline_javascript(html)
    if not blocks:
        return True

    node = shutil.which("node")
    if node is None:
        print("ERROR: node is required for viewer JavaScript syntax checks.", file=sys.stderr)
        return False

    with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as tmp:
        tmp.write("\n;\n".join(blocks))
        tmp_path = Path(tmp.name)
    try:
        result = subprocess.run(
            [node, "--check", str(tmp_path)],
            text=True,
            capture_output=True,
            check=False,
        )
    finally:
        tmp_path.unlink(missing_ok=True)

    if result.returncode != 0:
        print(f"ERROR: inline JavaScript in {path.relative_to(ROOT)} does not parse.")
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        return False
    return True


def main() -> int:
    ok = True
    for relative in ("index.html", "viewer/index.html"):
        ok = check_html(ROOT / relative) and ok
    if ok:
        print("OK: inline JavaScript parses.")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
