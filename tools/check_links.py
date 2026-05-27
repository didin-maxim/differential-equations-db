import sys
from lib import load_definitions, load_problem_files, load_relations, load_sources, load_standard_ideas


def main():
    errors = []
    problem_ids = {p.get("id") for _, p in load_problem_files()}
    source_ids = {s.get("id") for s in load_sources()}
    definition_ids = {d.get("id") for d in load_definitions()}
    idea_ids = {i.get("id") for i in load_standard_ideas()}
    for path, p in load_problem_files():
        for src in p.get("sources", []):
            if src.get("source_id") not in source_ids:
                errors.append(f"{path}: unknown source {src.get('source_id')}")
        for group in p.get("statements", {}).values():
            for stmt in group:
                for did in stmt.get("definition_ids", []):
                    if did not in definition_ids:
                        errors.append(f"{path}: unknown definition {did}")
        for group_name in ["ideas", "solutions"]:
            for item in p.get(group_name, []):
                for sid in item.get("standard_idea_ids", []):
                    if sid not in idea_ids:
                        errors.append(f"{path}: unknown standard idea {sid}")
    for rel in load_relations():
        if rel.get("from") not in problem_ids or rel.get("to") not in problem_ids:
            errors.append(f"{rel.get('id')}: broken relation endpoint")
    if errors:
        for e in errors:
            print("ERROR:", e)
        return 1
    print("OK: links are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
