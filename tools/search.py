import argparse
from lib import load_problem_files, load_relations


def haystack(p):
    parts = [p.get("id", ""), p.get("title", ""), p.get("fragment", ""), " ".join(p.get("tags", []))]
    for group in p.get("statements", {}).values():
        for s in group:
            parts.extend([s.get("title", ""), s.get("text", "")])
    for key in ["ideas", "solutions"]:
        for item in p.get(key, []):
            parts.extend([item.get("title", ""), item.get("text", "")])
    return "\n".join(parts).lower()


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    q = sub.add_parser("query")
    q.add_argument("text")
    c = sub.add_parser("card")
    c.add_argument("id")
    n = sub.add_parser("neighbors")
    n.add_argument("id")
    args = parser.parse_args()
    problems = [p for _, p in load_problem_files()]
    by_id = {p.get("id"): p for p in problems}
    if args.cmd == "query":
        needle = args.text.lower()
        found = [p for p in problems if needle in haystack(p)]
        for p in found[:30]:
            print(f"{p['id']}: {p['title']} [{p['fragment']}]")
        print(f"FOUND: {len(found)}")
    elif args.cmd == "card":
        p = by_id.get(args.id)
        if not p:
            raise SystemExit(f"unknown card {args.id}")
        print(f"{p['id']}: {p['title']}")
        print(f"fragment: {p['fragment']}")
        print(f"tags: {', '.join(p.get('tags', []))}")
        print(p["statements"]["original"][0]["text"])
    else:
        rels = [r for r in load_relations() if r.get("from") == args.id or r.get("to") == args.id]
        for r in rels:
            other = r["to"] if r["from"] == args.id else r["from"]
            direction = r["forward_text"] if r["from"] == args.id else r["backward_text"]
            print(f"{other}: {r['type']} - {direction}")
        print(f"FOUND: {len(rels)}")


if __name__ == "__main__":
    main()
