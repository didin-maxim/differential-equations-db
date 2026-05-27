import argparse
import html
import json
import re
import sys
from pathlib import Path

from lib import ROOT


VISIBLE_KEYS = {
    "allowed_variants",
    "canonical_solution_plan",
    "title",
    "text",
    "comment",
    "common_errors",
    "criteria",
    "deficit_policy",
    "note",
    "notes",
    "description",
    "distractor_notes",
    "do_not_add_when",
    "duplicate_signals",
    "explanation",
    "feedback",
    "gap_policy",
    "goal",
    "hint",
    "hints",
    "label",
    "need",
    "options",
    "prefer_new_cards",
    "prompt",
    "prompt_override",
    "question",
    "rubric",
    "saturation_policy",
    "solution",
    "solutions",
    "statement",
    "success_criteria",
    "task",
    "use_when",
    "forward_text",
    "backward_text",
    "caption",
    "alt",
}

SKIP_KEYS = {
    "id",
    "ids",
    "source_id",
    "source_ids",
    "definition_id",
    "definition_ids",
    "standard_idea_id",
    "standard_idea_ids",
    "cluster_id",
    "cluster_ids",
    "task_block_ids",
    "tags",
    "keywords",
    "status",
    "priority",
    "path",
    "href",
    "url",
    "created_at",
    "value",
    "tolerance",
    "accepted_text",
    "accepted_latex",
    "accepted_math",
    "correct_options",
}

MATH_DELIMS = [
    re.compile(r"\$\$.*?\$\$", re.DOTALL),
    re.compile(r"\\\[.*?\\\]", re.DOTALL),
    re.compile(r"\\\(.*?\\\)", re.DOTALL),
    re.compile(r"(?<!\\)\$.*?(?<!\\)\$", re.DOTALL),
]

RAW_PATTERNS = [
    ("subscript-without-underscore", re.compile(r"\b[xtypuvwsz][0-9]\b")),
    ("raw-real-product", re.compile(r"\bR\s*x\s*R(?:\^n)?\b")),
    ("raw-exp", re.compile(r"(?<![\\A-Za-z])exp\(")),
    ("raw-e-power-paren", re.compile(r"(?<!\\)e\^\(")),
    ("raw-e-power", re.compile(r"(?<!\\)e\^(?:\{[^}\n]{1,120}\}|[A-Za-z0-9_+\-*/()]{1,120})")),
    ("raw-unicode-integral-limit", re.compile(r"∫_[A-Za-z0-9{}()'\\^+\-/]+")),
    ("raw-integral", re.compile(r"(?<!\\)\b(?:int|sum|prod|product|lim)_[A-Za-z0-9{}()'\\^+\-/]+")),
    ("raw-pi", re.compile(r"(?<![\\A-Za-z])\bpi\b")),
    ("raw-infty", re.compile(r"(?<![\\A-Za-z])\binfty\b")),
    ("raw-arrow", re.compile(r"->")),
    ("raw-comparison", re.compile(r"(?<![<>=!])(?:<=|>=|!=)(?![<>=])")),
    ("bare-tex-command", re.compile(r"\\(?:int|sum|prod|lim|pi|infty|le|ge|ne|to)\b")),
]

RAW_ANYWHERE_PATTERNS = [
    ("double-escaped-tex-command", re.compile(r"\\\\(?:int|sum|prod|lim|frac|left|right|ln|sin|cos|exp|operatorname|mathbb|Phi|Delta|lambda|mu|alpha|beta|gamma|le|ge|ne|to|infty|pi|cdot|times)\b")),
]


def strip_math(text):
    result = str(text or "")
    for pattern in MATH_DELIMS:
        result = pattern.sub(" ", result)
    return result


def iter_data_files():
    for path in sorted((ROOT / "data").rglob("*.yaml")):
        yield path


def iter_svg_text_nodes():
    pattern = re.compile(r"<(?:title|desc|text)\b[^>]*>(.*?)</(?:title|desc|text)>", re.DOTALL)
    for path in sorted((ROOT / "data" / "assets").rglob("*.svg")):
        value = path.read_text(encoding="utf-8")
        for index, match in enumerate(pattern.finditer(value)):
            text = re.sub(r"<[^>]+>", "", match.group(1))
            yield path, f"svg_text.{index}", html.unescape(text)


def is_visible_key(key):
    return key in VISIBLE_KEYS


def iter_visible_strings(obj, path=(), force_visible=False):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in SKIP_KEYS:
                continue
            next_visible = force_visible or is_visible_key(key)
            yield from iter_visible_strings(value, path + (str(key),), next_visible)
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            yield from iter_visible_strings(value, path + (str(index),), force_visible)
    elif isinstance(obj, str) and force_visible:
        yield path, obj


def find_hits(text):
    original = str(text or "")
    hits = []
    for name, pattern in RAW_ANYWHERE_PATTERNS:
        for match in pattern.finditer(original):
            hits.append((name, match.group(0)))
            if len(hits) >= 5:
                return hits
    visible = strip_math(text)
    for name, pattern in RAW_PATTERNS:
        for match in pattern.finditer(visible):
            hits.append((name, match.group(0)))
            if len(hits) >= 5:
                return hits
    return hits


def replace_balanced_function(text, name, renderer):
    out = []
    index = 0
    needle = f"{name}("
    while index < len(text):
        start = text.find(needle, index)
        if start < 0:
            out.append(text[index:])
            break
        if start > 0 and (text[start - 1].isalpha() or text[start - 1] == "\\"):
            out.append(text[index : start + len(needle)])
            index = start + len(needle)
            continue
        pos = start + len(needle)
        depth = 1
        while pos < len(text) and depth:
            if text[pos] == "(":
                depth += 1
            elif text[pos] == ")":
                depth -= 1
            pos += 1
        if depth:
            out.append(text[index:])
            break
        inner = text[start + len(needle) : pos - 1]
        out.append(text[index:start])
        out.append(renderer(inner))
        index = pos
    return "".join(out)


def transform_outside_math(text, transform):
    value = str(text)
    spans = []
    for pattern in MATH_DELIMS:
        spans.extend(match.span() for match in pattern.finditer(value))
    if not spans:
        return transform(value)
    spans.sort()
    merged = []
    for start, end in spans:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    out = []
    pos = 0
    for start, end in merged:
        out.append(transform(value[pos:start]))
        out.append(value[start:end])
        pos = end
    out.append(transform(value[pos:]))
    return "".join(out)


def fix_text(text):
    double_escaped_commands = (
        "int",
        "sum",
        "prod",
        "lim",
        "frac",
        "left",
        "right",
        "ln",
        "sin",
        "cos",
        "exp",
        "operatorname",
        "mathbb",
        "Phi",
        "Delta",
        "lambda",
        "mu",
        "alpha",
        "beta",
        "gamma",
        "le",
        "ge",
        "ne",
        "to",
        "infty",
        "pi",
        "cdot",
        "times",
    )
    text = str(text)
    for command in double_escaped_commands:
        text = text.replace("\\\\" + command, "\\" + command)

    def transform(value):
        value = re.sub(r"\bR\s*x\s*R\^n\b", r"\\(\\mathbb R\\times \\mathbb R^n\\)", value)
        value = re.sub(r"\bR\s*x\s*R\b", r"\\(\\mathbb R\\times \\mathbb R\\)", value)
        value = re.sub(r"\bR\^n\b", r"\\(\\mathbb R^n\\)", value)

        def math_exp(inner):
            return r"\(e^{" + inner.strip() + r"}\)"

        value = replace_balanced_function(value, "exp", math_exp)
        value = re.sub(r"(?<!\\)e\^\{([^{}\n]{1,120})\}", lambda m: r"\(e^{" + m.group(1).strip() + r"}\)", value)
        value = re.sub(r"(?<!\\)e\^\(([^()\n]{1,120})\)", lambda m: r"\(e^{" + m.group(1).strip() + r"}\)", value)
        value = re.sub(r"(?<!\\)e\^\(\(([^()\n]{1,80})\)([^()\n]{0,30})\)", lambda m: r"\(e^{(" + m.group(1).strip() + ")" + m.group(2).strip() + r"}\)", value)
        value = re.sub(r"(?<!\\)e\^([A-Za-z0-9_+\-*/]{1,80})", lambda m: r"\(e^{" + m.group(1).strip() + r"}\)", value)

        for var in ("x", "t", "y", "p", "v", "u", "z", "w", "s"):
            value = re.sub(rf"\b{var}([0-9])\b", rf"{var}_\1", value)

        def wrap_operator(match):
            token = match.group(0)
            if token.startswith("\\("):
                return token
            return r"\(" + token + r"\)"

        value = re.sub(
            r"∫_[^\s,.;:!?]+",
            lambda m: r"\(\int" + m.group(0)[1:] + r"\)",
            value,
        )
        value = re.sub(r"(?<!\\)\b(?:int|sum|prod|product|lim)_[^\s,.;:!?]+", lambda m: r"\(\\" + m.group(0) + r"\)", value)
        value = re.sub(r"\\(?:int|sum|prod|product|lim)_[^\s,.;:!?]+", wrap_operator, value)
        value = value.replace(r"\le", "≤").replace(r"\ge", "≥").replace(r"\ne", "≠").replace(r"\to", "→")
        value = value.replace(r"\pi", "π").replace(r"\infty", "∞")
        value = re.sub(r"(?<![\\A-Za-z])\bpi\b", "π", value)
        value = re.sub(r"(?<![\\A-Za-z])\binfty\b", "∞", value)
        value = value.replace("->", "→")
        value = value.replace("<=", "≤")
        value = value.replace(">=", "≥")
        value = value.replace("!=", "≠")
        return value

    return transform_outside_math(text, transform)


def walk_fix(obj, force_visible=False):
    changed = False
    if isinstance(obj, dict):
        out = {}
        for key, value in obj.items():
            if key in SKIP_KEYS:
                out[key] = value
                continue
            next_visible = force_visible or is_visible_key(key)
            out[key], child_changed = walk_fix(value, next_visible)
            changed = changed or child_changed
        return out, changed
    if isinstance(obj, list):
        out = []
        for value in obj:
            fixed, child_changed = walk_fix(value, force_visible)
            out.append(fixed)
            changed = changed or child_changed
        return out, changed
    if isinstance(obj, str) and force_visible:
        fixed = fix_text(obj)
        return fixed, fixed != obj
    return obj, False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fix", action="store_true", help="Rewrite visible data strings mechanically.")
    parser.add_argument("--max-items", type=int, default=80)
    args = parser.parse_args()

    reports = []
    changed_files = []
    for path in iter_data_files():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            reports.append((path, "<json>", "invalid-json", str(exc)))
            continue
        if args.fix:
            fixed, changed = walk_fix(data)
            if changed:
                path.write_text(json.dumps(fixed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                changed_files.append(path)
                data = fixed
        for place, text in iter_visible_strings(data):
            for kind, hit in find_hits(text):
                reports.append((path, ".".join(place), kind, hit))
    for path, place, text in iter_svg_text_nodes():
        for kind, hit in find_hits(text):
            reports.append((path, place, kind, hit))

    for path, place, kind, hit in reports[: args.max_items]:
        rel = path.relative_to(ROOT)
        print(f"WARN {rel}#{place}: {kind}: {hit}")
    if len(reports) > args.max_items:
        print(f"... {len(reports) - args.max_items} more warnings")
    if args.fix:
        print(f"Changed files: {len(changed_files)}")
    if reports:
        print(f"ERROR: TeX quality check found {len(reports)} issue(s).")
        return 1
    print("OK: TeX quality check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
