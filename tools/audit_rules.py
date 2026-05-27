import argparse
import sys
from lib import load_problem_files


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-items", type=int, default=20)
    args = parser.parse_args()
    warnings = []
    for path, p in load_problem_files():
        if p.get("editorial", {}).get("public_ready") and p.get("editorial", {}).get("review_status") != "ai_checked":
            warnings.append(f"{p.get('id')}: public_ready with non-ai_checked review_status")
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
