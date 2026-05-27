import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def data_files(*parts):
    base = ROOT.joinpath("data", *parts)
    if not base.exists():
        return []
    return sorted(base.rglob("*.yaml"))


def load_problem_files():
    return [(p, load_json(p)) for p in data_files("problems")]


def load_relations():
    out = []
    for p in data_files("relations"):
        data = load_json(p)
        out.extend(data.get("relations", []))
    return out


def load_sources():
    path = ROOT / "data" / "sources" / "sources.yaml"
    return load_json(path).get("sources", [])


def load_definitions():
    path = ROOT / "data" / "definitions" / "definitions.yaml"
    return load_json(path).get("definitions", [])


def load_standard_ideas():
    path = ROOT / "data" / "standard_ideas" / "standard_ideas.yaml"
    return load_json(path).get("standard_ideas", [])


def load_taxonomy(filename, key):
    path = ROOT / "data" / "taxonomy" / filename
    return load_json(path).get(key, [])
