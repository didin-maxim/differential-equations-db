import argparse
import json
import sys

from build_index import definition_ids, source_ids
from lib import ROOT, data_files, load_problem_files


WARN_REPRESENTATIVE_THRESHOLD = 8
STRICT_ERROR_REPRESENTATIVE_THRESHOLD = 15
LOW_TECHNICAL_SCORE_MAX = 3
EXCEPTION_MARKERS = {
    "method_guide_exception",
    "no_method_guide",
    "intentional_method_guide_gap",
}


def as_list(value):
    return value if isinstance(value, list) else []


def load_cluster_files():
    out = []
    for path in data_files("task_clusters"):
        data = json.loads(path.read_text(encoding="utf-8"))
        out.append((path, data.get("clusters", []) or []))
    return out


def markers(card):
    kind = card.get("kind") or {}
    return set(as_list(kind.get("secondary"))) | set(as_list(card.get("tags")))


def is_method_guide(card):
    return "method_guide" in markers(card)


def has_sources_or_references(card):
    return bool(card.get("references")) or bool(card.get("sources")) or bool(source_ids(card))


def has_intentional_exception(cluster):
    values = []
    for key in ("notes", "goal"):
        values.append(cluster.get(key))
    for key in ("saturation_policy", "deficit_policy"):
        value = cluster.get(key)
        if isinstance(value, dict):
            values.extend(value.values())
    text = json.dumps(values, ensure_ascii=False).lower()
    return any(marker in text for marker in EXCEPTION_MARKERS)


def is_olympiad_cluster(cluster):
    cluster_id = str(cluster.get("id") or "").lower()
    haystack = json.dumps(
        [
            cluster.get("id"),
            cluster.get("title"),
            cluster.get("goal"),
            cluster.get("notes"),
        ],
        ensure_ascii=False,
    ).lower()
    return cluster_id.startswith("olympiad-") or "olympiad" in haystack or "олимпиад" in haystack


def guide_issues(card):
    found_markers = markers(card)
    issues = []
    if "task_cluster" not in found_markers:
        issues.append("missing task_cluster")
    if "cluster_representative" not in found_markers:
        issues.append("missing cluster_representative")
    if not has_sources_or_references(card):
        issues.append("missing references/sources")
    if not definition_ids(card):
        issues.append("missing definition_ids")

    technical_score = (card.get("difficulty") or {}).get("technical_score")
    if not isinstance(technical_score, int):
        issues.append("missing technical_score")
    elif technical_score > LOW_TECHNICAL_SCORE_MAX:
        issues.append(f"technical_score {technical_score} > {LOW_TECHNICAL_SCORE_MAX}")
    return issues


def cluster_status(cluster, representative_count, guide_cards, strict):
    if not guide_cards:
        if representative_count >= STRICT_ERROR_REPRESENTATIVE_THRESHOLD:
            if strict and not is_olympiad_cluster(cluster) and not has_intentional_exception(cluster):
                return "ERROR", ["large cluster has no method guide"]
            return "WARN", ["large cluster has no method guide"]
        if representative_count >= WARN_REPRESENTATIVE_THRESHOLD:
            return "WARN", ["cluster has no method guide"]
        return "INFO", ["small cluster has no method guide"]

    issues = []
    for card in guide_cards:
        issues.extend(f"{card.get('id')}: {issue}" for issue in guide_issues(card))
    if issues:
        return "WARN", issues
    return "OK", []


def format_table(rows):
    headers = ("cluster id", "reps", "guide", "status")
    widths = [len(item) for item in headers]
    for row in rows:
        values = (row["cluster_id"], str(row["representative_count"]), row["guide_ids"], row["status"])
        widths = [max(width, len(value)) for width, value in zip(widths, values)]

    def fmt(values):
        return "  ".join(value.ljust(width) for value, width in zip(values, widths))

    lines = [fmt(headers), fmt(tuple("-" * width for width in widths))]
    for row in rows:
        lines.append(
            fmt(
                (
                    row["cluster_id"],
                    str(row["representative_count"]),
                    row["guide_ids"],
                    row["status"],
                )
            )
        )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat non-olympiad clusters with at least 15 representatives and no guide as errors.",
    )
    args = parser.parse_args()

    problems = {problem.get("id"): problem for _, problem in load_problem_files()}
    rows = []
    details = []
    cluster_count = 0

    for path, clusters in load_cluster_files():
        for cluster in clusters:
            cluster_count += 1
            cluster_id = cluster.get("id") or "<missing cluster id>"
            representative_ids = as_list(cluster.get("representative_card_ids"))
            guide_cards = [
                problems[card_id]
                for card_id in representative_ids
                if card_id in problems and is_method_guide(problems[card_id])
            ]
            status, issues = cluster_status(cluster, len(representative_ids), guide_cards, args.strict)
            guide_ids = ", ".join(card.get("id") or "<missing id>" for card in guide_cards) or "none"
            rows.append(
                {
                    "cluster_id": str(cluster_id),
                    "representative_count": len(representative_ids),
                    "guide_ids": guide_ids,
                    "status": status,
                }
            )
            for issue in issues:
                if status != "OK":
                    details.append(f"{status}: {cluster_id}: {issue}")

    print(format_table(rows))
    if details:
        print()
        for detail in details:
            print(detail)

    error_count = sum(1 for row in rows if row["status"] == "ERROR")
    warn_count = sum(1 for row in rows if row["status"] == "WARN")
    info_count = sum(1 for row in rows if row["status"] == "INFO")
    print()
    print(
        f"OK: checked {cluster_count} clusters; "
        f"{error_count} errors, {warn_count} warnings, {info_count} info."
    )
    return 1 if error_count else 0


if __name__ == "__main__":
    sys.exit(main())
