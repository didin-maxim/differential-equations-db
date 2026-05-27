import sys
from collections import Counter

from lib import load_definitions, load_problem_files, load_relations, load_sources, load_standard_ideas, load_taxonomy

REQUIRED = ["id", "title", "fragment", "kind", "language", "statements", "ideas", "solutions", "differential_equations_profile", "difficulty", "tags", "sources", "editorial"]
REL_REQUIRED = ["id", "from", "to", "type", "distance", "forward_text", "backward_text", "status", "confidence"]


def fail(errors, msg):
    errors.append(msg)


def main():
    errors = []
    problem_files = load_problem_files()
    problems = [p for _, p in problem_files]
    problem_ids = [p.get("id") for p in problems]
    source_ids = {s.get("id") for s in load_sources()}
    definition_ids = {d.get("id") for d in load_definitions()}
    idea_ids = {i.get("id") for i in load_standard_ideas()}
    fragments = {f.get("id") for f in load_taxonomy("fragments.yaml", "fragments")}
    tags = set(load_taxonomy("tags.yaml", "tags"))
    difficulty = {d.get("id") for d in load_taxonomy("difficulty.yaml", "difficulty")}
    relation_types = {r.get("id") for r in load_taxonomy("relation-types.yaml", "relation_types")}

    for pid, count in Counter(problem_ids).items():
        if count > 1:
            fail(errors, f"duplicate problem id: {pid}")

    for path, problem in problem_files:
        label = str(path)
        for field in REQUIRED:
            if field not in problem:
                fail(errors, f"{label}: missing required field {field}")
        if problem.get("fragment") not in fragments:
            fail(errors, f"{label}: unknown fragment {problem.get('fragment')}")
        if problem.get("language") != "ru":
            fail(errors, f"{label}: language must be ru")
        if problem.get("difficulty", {}).get("main") not in difficulty:
            fail(errors, f"{label}: unknown difficulty {problem.get('difficulty', {}).get('main')}")
        for tag in problem.get("tags", []):
            if tag not in tags:
                fail(errors, f"{label}: unknown tag {tag}")
        for src in problem.get("sources", []):
            if src.get("source_id") not in source_ids:
                fail(errors, f"{label}: unknown source {src.get('source_id')}")
        statements = problem.get("statements", {})
        if not statements.get("original"):
            fail(errors, f"{label}: statements.original is required")
        for group_name, group in statements.items():
            if not isinstance(group, list):
                fail(errors, f"{label}: statements.{group_name} must be a list")
                continue
            for stmt in group:
                for field in ["id", "title", "text", "status", "self_contained", "definition_ids"]:
                    if field not in stmt:
                        fail(errors, f"{label}: statement missing {field}")
                for did in stmt.get("definition_ids", []):
                    if did not in definition_ids:
                        fail(errors, f"{label}: unknown definition {did}")
                for sid in stmt.get("source_ids", []):
                    if sid not in source_ids:
                        fail(errors, f"{label}: statement unknown source {sid}")
        for group_name in ["ideas", "solutions"]:
            group = problem.get(group_name, [])
            if not isinstance(group, list):
                fail(errors, f"{label}: {group_name} must be a list")
                continue
            for item in group:
                for field in ["id", "title", "text", "status"]:
                    if field not in item:
                        fail(errors, f"{label}: {group_name} item missing {field}")
                for sid in item.get("standard_idea_ids", []):
                    if sid not in idea_ids:
                        fail(errors, f"{label}: unknown standard idea {sid}")
                for did in item.get("definition_ids", []):
                    if did not in definition_ids:
                        fail(errors, f"{label}: unknown definition {did}")

    id_set = set(problem_ids)
    relations = load_relations()
    for rid, count in Counter(r.get("id") for r in relations).items():
        if count > 1:
            fail(errors, f"duplicate relation id: {rid}")
    for rel in relations:
        label = rel.get("id", "<missing relation id>")
        for field in REL_REQUIRED:
            if field not in rel:
                fail(errors, f"{label}: missing {field}")
        if rel.get("from") not in id_set:
            fail(errors, f"{label}: unknown from {rel.get('from')}")
        if rel.get("to") not in id_set:
            fail(errors, f"{label}: unknown to {rel.get('to')}")
        if rel.get("type") not in relation_types:
            fail(errors, f"{label}: unknown type {rel.get('type')}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        print(f"FAILED: {len(errors)} errors")
        return 1
    print(f"OK: {len(problems)} cards, {len(relations)} relations, {len(source_ids)} sources.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
