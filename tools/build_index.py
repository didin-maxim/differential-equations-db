import json

from lib import (
    ROOT,
    load_definitions,
    load_problem_files,
    load_relations,
    load_sources,
    load_standard_ideas,
    load_taxonomy,
)


COURSE_TAGS = [
    "standard_course_methods",
    "advanced_standard_course",
    "beyond_standard_course",
]


def load_json_file(path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def load_task_clusters():
    path = ROOT / "data" / "task_clusters" / "clusters.yaml"
    return load_json_file(path, {}).get("clusters", [])


def taxonomy():
    return {
        "tags": load_taxonomy("tags.yaml", "tags"),
        "statuses": load_taxonomy("statuses.yaml", "statuses"),
        "relation_types": load_taxonomy("relation-types.yaml", "relation_types"),
        "fragments": load_taxonomy("fragments.yaml", "fragments"),
        "difficulty": load_taxonomy("difficulty.yaml", "difficulty"),
    }


def as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def compact(values):
    out = []
    seen = set()
    for value in values:
        if value is None:
            continue
        text = str(value).strip()
        if not text or text in seen:
            continue
        seen.add(text)
        out.append(text)
    return out


def flatten_text(value):
    parts = []

    def walk(item):
        if item is None:
            return
        if isinstance(item, str):
            parts.append(item)
            return
        if isinstance(item, (int, float, bool)):
            parts.append(str(item))
            return
        if isinstance(item, list):
            for child in item:
                walk(child)
            return
        if isinstance(item, dict):
            for child in item.values():
                walk(child)

    walk(value)
    return "\n".join(parts)


def first_statement(problem):
    statements = problem.get("statements") or {}
    for group in statements.values():
        for statement in group or []:
            text = statement.get("text")
            if text:
                return text
    return ""


def source_ids(problem):
    ids = []
    for source in problem.get("sources", []) or []:
        ids.append(source.get("source_id"))
    for group in (problem.get("statements") or {}).values():
        for statement in group or []:
            ids.extend(statement.get("source_ids", []) or [])
            ids.append(statement.get("source_id"))
    return compact(ids)


def standard_idea_ids(problem):
    ids = []
    for block_name in ("ideas", "solutions"):
        for block in problem.get(block_name, []) or []:
            ids.extend(block.get("standard_idea_ids", []) or [])
    return compact(ids)


def compact_assets(problem):
    assets = []
    seen = set()

    def add(asset, default_role=None):
        if not isinstance(asset, dict):
            return
        path = asset.get("path") or asset.get("href") or asset.get("url")
        if not path:
            return
        item = {
            "id": asset.get("id"),
            "type": asset.get("type") or ("image" if str(path).lower().split("?")[0].endswith((".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp")) else "asset"),
            "path": path,
            "role": asset.get("role") or default_role,
            "title": asset.get("title"),
            "caption": asset.get("caption"),
            "alt": asset.get("alt"),
            "status": asset.get("status"),
        }
        key = (item["path"], item.get("id"), item.get("role"))
        if key in seen:
            return
        seen.add(key)
        assets.append({key: value for key, value in item.items() if value is not None})

    for asset in problem.get("assets", []) or []:
        add(asset)

    statements = problem.get("statements") or {}
    for group in statements.values():
        for statement in group or []:
            for figure in statement.get("figures", []) or []:
                add(figure, "statement_figure")

    for block_name in ("ideas", "solutions", "proofs", "strategies", "impossibility_proofs"):
        for block in problem.get(block_name, []) or []:
            for figure in block.get("figures", []) or []:
                add(figure, f"{block_name}_figure")
            for example in block.get("examples", []) or []:
                add(example, f"{block_name}_example")

    return assets


def problem_authors(problem):
    authors = []
    for key in ("authors", "attributed_authors", "attribution_authors"):
        for item in as_list(problem.get(key)):
            if isinstance(item, dict):
                authors.append(item.get("name") or item.get("id") or item.get("title"))
            else:
                authors.append(item)
    attribution = problem.get("attribution") or {}
    for key in ("authors", "author", "created_by"):
        for item in as_list(attribution.get(key)):
            if isinstance(item, dict):
                authors.append(item.get("name") or item.get("id") or item.get("title"))
            else:
                authors.append(item)
    created_by = (problem.get("editorial") or {}).get("created_by")
    if created_by:
        authors.append(f"created_by:{created_by}")
    return compact(authors)


def course_bucket(problem):
    tags = set(problem.get("tags", []) or [])
    for tag in COURSE_TAGS:
        if tag in tags:
            return tag
    return "uncategorized"


def cluster_memberships(problem_id, clusters):
    memberships = []
    for cluster in clusters:
        ids = []
        for key in ("representative_card_ids", "problem_ids", "core_problem_ids", "card_ids"):
            ids.extend(cluster.get(key, []) or [])
        if problem_id in set(ids):
            memberships.append(cluster.get("id"))
    return compact(memberships)


def build_cards(problem_files, clusters, sources, standard_ideas):
    source_labels = {
        item.get("id"): item.get("short_name") or item.get("short_title") or item.get("title") or item.get("id")
        for item in sources
    }
    idea_labels = {
        item.get("id"): item.get("title") or item.get("id")
        for item in standard_ideas
    }
    cluster_labels = {
        item.get("id"): item.get("title") or item.get("title_ru") or item.get("id")
        for item in clusters
    }
    cards = []
    for path, problem in problem_files:
        difficulty = problem.get("difficulty") or {}
        editorial = problem.get("editorial") or {}
        kind = problem.get("kind") or {}
        ids = source_ids(problem)
        idea_ids = standard_idea_ids(problem)
        cluster_ids = cluster_memberships(problem.get("id"), clusters)
        authors = problem_authors(problem)
        assets = compact_assets(problem)
        has_image = any((asset.get("type") == "image") for asset in assets)
        search_text = flatten_text(
            [
                problem.get("id"),
                problem.get("title"),
                problem.get("fragment"),
                kind.get("primary"),
                problem.get("tags", []),
                first_statement(problem),
                problem.get("ideas", []),
                problem.get("solutions", []),
                ids,
                [source_labels.get(item, item) for item in ids],
                idea_ids,
                [idea_labels.get(item, item) for item in idea_ids],
                cluster_ids,
                [cluster_labels.get(item, item) for item in cluster_ids],
                authors,
                assets,
                ["image", "asset", "figure", "рисунок", "картинка"] if assets else [],
                difficulty,
                editorial.get("review_status"),
                editorial.get("public_ready"),
            ]
        ).lower()
        cards.append(
            {
                "id": problem.get("id"),
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "title": problem.get("title"),
                "fragment": problem.get("fragment"),
                "kind": kind.get("primary"),
                "secondary_kinds": kind.get("secondary", []),
                "difficulty_main": difficulty.get("main"),
                "idea_score": difficulty.get("idea_score"),
                "technical_score": difficulty.get("technical_score"),
                "local_score": difficulty.get("local_score"),
                "tags": problem.get("tags", []) or [],
                "course_bucket": course_bucket(problem),
                "source_ids": ids,
                "source_labels": [source_labels.get(item, item) for item in ids],
                "authors": authors,
                "cluster_ids": cluster_ids,
                "cluster_labels": [cluster_labels.get(item, item) for item in cluster_ids],
                "standard_idea_ids": idea_ids,
                "standard_idea_labels": [idea_labels.get(item, item) for item in idea_ids],
                "review_status": editorial.get("review_status"),
                "public_ready": editorial.get("public_ready"),
                "created_by": editorial.get("created_by"),
                "created_at": editorial.get("created_at"),
                "statement": first_statement(problem),
                "assets": assets,
                "has_image": has_image,
                "search_text": search_text,
            }
        )
    return sorted(cards, key=lambda card: (card.get("fragment") or "", card.get("title") or "", card.get("id") or ""))


def build_data():
    problem_files = load_problem_files()
    problems = [problem for _, problem in problem_files]
    problem_count = sum(1 for problem in problems if (problem.get("kind") or {}).get("primary") == "problem")
    theory_count = sum(
        1
        for problem in problems
        if (problem.get("kind") or {}).get("primary") in {"theorem", "lemma", "definition", "corollary"}
    )
    sources = load_sources()
    standard_ideas = load_standard_ideas()
    clusters = load_task_clusters()
    return {
        "problems": problems,
        "cards": build_cards(problem_files, clusters, sources, standard_ideas),
        "relations": load_relations(),
        "sources": sources,
        "definitions": load_definitions(),
        "standard_ideas": standard_ideas,
        "task_clusters": clusters,
        "taxonomy": taxonomy(),
        "meta": {
            "card_count": len(problems),
            "problem_count": problem_count,
            "theory_count": theory_count,
            "cluster_count": len(clusters),
        },
    }


def main():
    data = build_data()
    out = ROOT / "index" / "generated.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: wrote {out} with {len(data['problems'])} cards.")


if __name__ == "__main__":
    main()
