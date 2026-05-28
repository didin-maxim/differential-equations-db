import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def repair_mojibake_text(value):
    text = value
    for _ in range(2):
        repaired = text
        for encoding in ("cp1251", "latin1"):
            try:
                candidate = text.encode(encoding).decode("utf-8")
            except UnicodeError:
                continue
            if _mojibake_score(candidate) < _mojibake_score(repaired):
                repaired = candidate
        if repaired == text:
            break
        text = repaired
    return text


def repair_mojibake(value):
    if isinstance(value, str):
        return repair_mojibake_text(value)
    if isinstance(value, list):
        return [repair_mojibake(item) for item in value]
    if isinstance(value, dict):
        return {key: repair_mojibake(item) for key, item in value.items()}
    return value


def _mojibake_score(text):
    markers = (
        "Рђ", "Р‘", "Р’", "Р“", "Р”", "Р•", "Р–", "Р—", "Р˜", "Р™", "Рљ", "Р›", "Рњ",
        "Рќ", "Рћ", "Рџ", "Р ", "РЎ", "Рў", "РЈ", "Р¤", "РҐ", "Р¦", "Р§", "РЁ", "Р©",
        "РЄ", "Р«", "Р¬", "Р­", "Р®", "РЇ", "Р°", "Р±", "РІ", "Рі", "Рґ", "Рµ", "Р¶",
        "Р·", "Рё", "Р№", "Рє", "Р»", "Рј", "РЅ", "Рѕ", "Рї", "СЂ", "СЃ", "С‚", "Сѓ",
        "С„", "С…", "С†", "С‡", "С€", "С‰", "СЉ", "С‹", "СЊ", "СЌ", "СЋ", "СЏ",
        "Ð", "Ñ", "Ï", "â€", "â€™", "â€œ", "â€�", "â€“", "â€”", "â†", "â‰", "âˆ",
        "Рџ", "РЎ", "Рќ", "РµР", "СЊ", "СЏ",
    )
    return sum(text.count(marker) for marker in markers)


def load_json(path):
    return repair_mojibake(json.loads(Path(path).read_text(encoding="utf-8")))


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
