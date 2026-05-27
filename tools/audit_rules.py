import argparse
import re
import sys
from lib import load_problem_files


EXAM_SCORE_TAGS = {f"exam_score_{score}" for score in range(3, 11)}
TITLE_MARKERS = ["TODO", "???", "FIXME"]
RAW_TEX_PATTERNS = [
    re.compile(r"\b(?:int|sum|prod|lim|sup|inf)_[A-Za-z0-9{}()'\\^+-]+"),
    re.compile(r"\b[A-Za-z][A-Za-z0-9]*_\{[^{}]{1,40}\}"),
    re.compile(r"\b[A-Za-z][A-Za-z0-9]*\^[A-Za-z0-9{}()+-]+"),
    re.compile(r"\bd\^?\d*/d[A-Za-z]\^?\d*"),
    re.compile(r"\by\^\([^)]+\)"),
]


def as_list(value):
    return value if isinstance(value, list) else []


def strip_delimited_math(text):
    text = str(text or "")
    patterns = [
        r"\$\$.*?\$\$",
        r"\\\[.*?\\\]",
        r"\\\(.*?\\\)",
        r"(?<!\\)\$.*?(?<!\\)\$",
    ]
    for pattern in patterns:
        text = re.sub(pattern, " ", text, flags=re.DOTALL)
    return text


def raw_tex_hits(text):
    visible = strip_delimited_math(text)
    hits = []
    for pattern in RAW_TEX_PATTERNS:
        hits.extend(match.group(0) for match in pattern.finditer(visible))
    return hits[:3]


def iter_visible_texts(problem):
    yield "title", problem.get("title", "")
    for stmt_group in problem.get("statements", {}).values():
        for stmt in as_list(stmt_group):
            yield f"statement#{stmt.get('id', '?')}", stmt.get("text", "")
            yield f"statement-title#{stmt.get('id', '?')}", stmt.get("title", "")
    for group_name in ["ideas", "solutions"]:
        for item in as_list(problem.get(group_name)):
            yield f"{group_name}#{item.get('id', '?')}", item.get("text", "")
            yield f"{group_name}-title#{item.get('id', '?')}", item.get("title", "")


def has_method_guide_marker(problem):
    kind = problem.get("kind", {})
    secondary = set(as_list(kind.get("secondary")))
    tags = set(problem.get("tags", []))
    return "method_guide" in secondary or "method_guide" in tags


def iter_definition_ids(problem):
    for stmt_group in problem.get("statements", {}).values():
        for stmt in as_list(stmt_group):
            yield from as_list(stmt.get("definition_ids"))
    for group_name in ["ideas", "solutions"]:
        for item in as_list(problem.get(group_name)):
            yield from as_list(item.get("definition_ids"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-items", type=int, default=20)
    parser.add_argument(
        "--check-raw-tex",
        action="store_true",
        help="Report possible TeX/ASCII math fragments in visible fields. Noisy until the legacy corpus is cleaned.",
    )
    args = parser.parse_args()
    warnings = []
    for path, p in load_problem_files():
        tags = set(p.get("tags", []))
        kind = p.get("kind", {})
        secondary = set(as_list(kind.get("secondary")))
        difficulty = p.get("difficulty", {})
        editorial = p.get("editorial", {})
        title = p.get("title", "")

        if editorial.get("public_ready") and editorial.get("review_status") != "ai_checked":
            warnings.append(f"{p.get('id')}: public_ready with non-ai_checked review_status")
        if editorial.get("public_ready") and (
            editorial.get("review_status") == "needs_human_review"
            or "needs_solution_completion" in tags
        ):
            warnings.append(f"{p.get('id')}: public_ready while marked as needing human/solution review")
        if len(title) > 110:
            warnings.append(f"{p.get('id')}: title is very long")
        for marker in TITLE_MARKERS:
            if marker.lower() in title.lower():
                warnings.append(f"{p.get('id')}: title contains marker {marker}")
        if "standard_course_methods" in tags and "beyond_standard_course" in tags:
            warnings.append(f"{p.get('id')}: both standard_course_methods and beyond_standard_course tags")
        if EXAM_SCORE_TAGS.intersection(tags) and difficulty.get("technical_score", 0) > 5:
            warnings.append(f"{p.get('id')}: exam_score tag with technical_score > 5")
        if "olympiad_above_exam" in tags and EXAM_SCORE_TAGS.intersection(tags):
            warnings.append(f"{p.get('id')}: olympiad_above_exam with exam_score tag")
        if args.check_raw_tex:
            for place, text in iter_visible_texts(p):
                hits = raw_tex_hits(text)
                if hits:
                    warnings.append(
                        f"{p.get('id')}#{place}: possible raw TeX outside delimiters: {', '.join(hits)}"
                    )

        if has_method_guide_marker(p):
            if kind.get("primary") not in {"theorem", "standard_fact"}:
                warnings.append(f"{p.get('id')}: method guide should be theorem/standard_fact")
            if not {"method_guide", "task_cluster"}.issubset(secondary):
                warnings.append(f"{p.get('id')}: method guide should have secondary method_guide and task_cluster")
            if "cluster_representative" not in tags:
                warnings.append(f"{p.get('id')}: method guide should be a cluster representative")
            if difficulty.get("technical_score", 0) > 3:
                warnings.append(f"{p.get('id')}: method guide has high technical_score")
            if not p.get("references"):
                warnings.append(f"{p.get('id')}: method guide has no references")
            if not list(iter_definition_ids(p)):
                warnings.append(f"{p.get('id')}: method guide has no definition_ids")
        for sol in p.get("solutions", []):
            text = sol.get("text", "")
            if len(text) < 120:
                warnings.append(f"{p.get('id')}#{sol.get('id')}: solution is very short")
            for weak in ["очевидно", "легко видеть", "аналогично"]:
                if weak in text.lower():
                    warnings.append(f"{p.get('id')}#{sol.get('id')}: contains weak proof word {weak}")
        if p.get("kind", {}).get("primary") in {"theorem", "lemma"} and not p.get("solutions"):
            warnings.append(f"{p.get('id')}: theorem/lemma has no proof")
    for w in warnings[:args.max_items]:
        print("WARN:", w)
    if len(warnings) > args.max_items:
        print(f"... {len(warnings) - args.max_items} more warnings")
    print(f"OK: audit finished with {len(warnings)} warnings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
