import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEWS = ROOT / "docs" / "reviews"


def parse_table(path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 7 or cells[0] in {"---", "year/problem", "competition/archive"}:
            continue
        if re.fullmatch(r"-+", cells[0] or ""):
            continue
        if len(cells) >= 8 and cells[2] in {"include", "borderline", "exclude-near-miss"}:
            item = f"{cells[0]} / {cells[1]}"
            verdict = cells[2]
            summary = cells[3]
            why = cells[4]
            mechanism = cells[5]
            url = cells[6]
            tags = cells[7]
        else:
            item = cells[0]
            verdict = cells[1]
            summary = cells[2]
            why = cells[3]
            mechanism = cells[4]
            url = cells[5]
            tags = cells[6]
        if verdict not in {"include", "borderline", "exclude-near-miss"}:
            continue
        rows.append({
            "source_file": path.name,
            "item": item,
            "verdict": verdict,
            "summary": summary,
            "why": why,
            "mechanism": mechanism,
            "url": url,
            "tags": tags,
        })
    return rows


def main():
    all_rows = []
    for path in sorted(REVIEWS.glob("olympiad-scan-*.md")):
        all_rows.extend(parse_table(path))

    include = [row for row in all_rows if row["verdict"] == "include"]
    borderline = [row for row in all_rows if row["verdict"] == "borderline"]
    near = [row for row in all_rows if row["verdict"] == "exclude-near-miss"]

    lines = [
        "# Очередь импорта из студенческих олимпиад",
        "",
        "Файл сгенерирован из `docs/reviews/olympiad-scan-*.md`.",
        "",
        f"- `include`: {len(include)}",
        f"- `borderline`: {len(borderline)}",
        f"- `exclude-near-miss`: {len(near)}",
        "",
        "## Include",
        "",
        "| source | item | summary | mechanism | proposed tags | url |",
        "|---|---|---|---|---|---|",
    ]
    for row in include:
        lines.append(f"| {row['source_file']} | {row['item']} | {row['summary']} | {row['mechanism']} | {row['tags']} | {row['url']} |")
    lines.extend(["", "## Borderline", "", "| source | item | summary | why | mechanism | url |", "|---|---|---|---|---|---|"])
    for row in borderline:
        lines.append(f"| {row['source_file']} | {row['item']} | {row['summary']} | {row['why']} | {row['mechanism']} | {row['url']} |")

    out = REVIEWS / "olympiad-import-queue.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"OK: wrote {out} from {len(all_rows)} scanned rows.")


if __name__ == "__main__":
    main()
