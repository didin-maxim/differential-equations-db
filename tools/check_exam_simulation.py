import sys
from collections import Counter, defaultdict

from lib import ROOT, data_files, load_json, load_problem_files, load_taxonomy


ACTIVE_OVERLAY_PATH = ROOT / "data" / "exam_simulation" / "questions.yaml"
CONFIG_PATH = ROOT / "data" / "exam_simulation" / "config.yaml"
GENERATED_INDEX_PATH = ROOT / "index" / "generated.json"

AUTO_CHECK_MODES = {"numeric", "formula", "formula_slots", "multiple_choice"}
EXAM_SCORE_TAG_PREFIX = "exam_score_"
MANUAL_ALLOW_KEYS = {
    "allow_in_exam_simulation",
    "exam_simulation_allow",
    "manual_exam_allow",
    "manual_overlay_allow",
    "manual_overlay_admission",
}
HIGH_TECH_ALLOW_KEYS = MANUAL_ALLOW_KEYS | {
    "allow_high_technical",
    "high_technical_exam_allow",
    "technical_score_override",
}
OLYMPIAD_ALLOW_KEYS = MANUAL_ALLOW_KEYS | {
    "allow_olympiad_above_exam",
    "olympiad_exam_suitable",
    "strong_exam_question",
    "strong_exam_fit",
    "explicit_strong_exam_question",
}


def rel(path):
    return str(path.relative_to(ROOT)).replace("\\", "/")


def add(errors, warnings, severity, label, message):
    if severity == "ERROR":
        errors.append(f"{label}: {message}")
    else:
        warnings.append(f"{label}: {message}")


def is_truthy_marker(value):
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "allow", "allowed", "manual", "strong_exam"}
    return False


def has_allow(obj, keys):
    if not isinstance(obj, dict):
        return False
    if any(is_truthy_marker(obj.get(key)) for key in keys):
        return True
    flags = obj.get("exam_simulation_flags") or obj.get("manual_flags") or []
    if isinstance(flags, list) and any(flag in keys for flag in flags):
        return True
    return False


def has_exam_score_tag(tags):
    return any(isinstance(tag, str) and tag.startswith(EXAM_SCORE_TAG_PREFIX) for tag in tags or [])


def load_index_or_sources():
    if GENERATED_INDEX_PATH.exists():
        data = load_json(GENERATED_INDEX_PATH)
        return data, f"index:{rel(GENERATED_INDEX_PATH)}"

    # Fallback keeps the checker usable before the first build_index run.
    problems = [problem for _, problem in load_problem_files()]
    return {"problems": problems, "cards": [], "task_clusters": [], "exam_simulation": {}}, "source:data/**"


def load_exam_sources():
    groups = []
    for path in data_files("exam_simulation"):
        data = load_json(path)
        questions = data.get("questions")
        if isinstance(questions, list):
            groups.append(
                {
                    "path": path,
                    "id": data.get("id") or path.stem,
                    "status": data.get("status") or ("active" if path == ACTIVE_OVERLAY_PATH else "proposal"),
                    "questions": questions,
                }
            )
    return groups


def problem_cards(index_data):
    problems = {problem.get("id"): problem for problem in index_data.get("problems", []) if problem.get("id")}
    cards = {card.get("id"): card for card in index_data.get("cards", []) if card.get("id")}

    for problem_id, problem in problems.items():
        if problem_id in cards:
            continue
        difficulty = problem.get("difficulty") or {}
        editorial = problem.get("editorial") or {}
        kind = problem.get("kind") or {}
        cards[problem_id] = {
            "id": problem_id,
            "kind": kind.get("primary"),
            "fragment": problem.get("fragment"),
            "tags": problem.get("tags") or [],
            "technical_score": difficulty.get("technical_score"),
            "idea_score": difficulty.get("idea_score"),
            "public_ready": editorial.get("public_ready"),
            "review_status": editorial.get("review_status"),
        }
    return problems, cards


def overlay_severity(group):
    return "ERROR" if group["path"] == ACTIVE_OVERLAY_PATH else "WARN"


def normalized_auto_check(question):
    auto_check = question.get("auto_check")
    if isinstance(auto_check, dict):
        return auto_check
    return {}


def list_has_values(value):
    return isinstance(value, list) and any(item not in (None, "") for item in value)


def has_any_answer_value(obj, keys):
    return any(obj.get(key) not in (None, "", []) for key in keys)


def check_numeric(errors, warnings, severity, label, question, auto_check):
    if auto_check.get("type") not in (None, "numeric"):
        add(errors, warnings, severity, label, f"answer_mode numeric has auto_check.type={auto_check.get('type')}")
    if not has_any_answer_value(auto_check, ["value", "accepted_text", "accepted_latex", "accepted_answers", "answers"]):
        add(errors, warnings, severity, label, "numeric question has no checkable value/accepted answers")
    if "tolerance" not in auto_check:
        add(errors, warnings, "WARN", label, "numeric question has no explicit tolerance")


def check_formula(errors, warnings, severity, label, question, auto_check):
    if auto_check.get("type") not in (None, "formula", "formula_slots"):
        add(errors, warnings, severity, label, f"answer_mode formula has auto_check.type={auto_check.get('type')}")
    if not has_any_answer_value(
        auto_check,
        ["accepted_latex", "accepted_text", "accepted_answers", "answers", "value", "slots"],
    ):
        add(errors, warnings, severity, label, "formula question has no accepted_latex/accepted_text/slots")


def check_multiple_choice(errors, warnings, severity, label, question, auto_check):
    options = auto_check.get("options") or question.get("options") or question.get("choices") or []
    correct_options = auto_check.get("correct_options") or question.get("correct_options") or []
    if not correct_options and isinstance(options, list):
        correct_options = [option.get("id") for option in options if isinstance(option, dict) and option.get("is_correct")]

    if not isinstance(options, list) or len(options) < 2:
        add(errors, warnings, severity, label, "multiple_choice question must have at least two options")
        return
    option_ids = [option.get("id") for option in options if isinstance(option, dict)]
    if len(option_ids) != len(options) or any(not option_id for option_id in option_ids):
        add(errors, warnings, severity, label, "multiple_choice options must all have ids")
    for option_id, count in Counter(option_ids).items():
        if option_id and count > 1:
            add(errors, warnings, severity, label, f"duplicate multiple_choice option id {option_id}")
    if not list_has_values(correct_options):
        add(errors, warnings, severity, label, "multiple_choice question has no correct option")
        return
    missing = [option_id for option_id in correct_options if option_id not in option_ids]
    for option_id in missing:
        add(errors, warnings, severity, label, f"correct option {option_id} is not present in options")


def check_self_check(errors, warnings, severity, label, question):
    self_check = question.get("self_check") or {}
    criteria = (
        self_check.get("criteria")
        or self_check.get("rubric")
        or question.get("criteria")
        or question.get("rubric")
    )
    if not list_has_values(criteria):
        add(errors, warnings, severity, label, "self_check question has no criteria/rubric")


def check_question_answer(errors, warnings, group, question):
    label = f"{rel(group['path'])}:{question.get('id', '<missing question id>')}"
    severity = overlay_severity(group)
    answer_mode = question.get("answer_mode")
    auto_check = normalized_auto_check(question)

    if not answer_mode:
        add(errors, warnings, severity, label, "missing answer_mode")
        return
    if answer_mode == "numeric":
        check_numeric(errors, warnings, severity, label, question, auto_check)
    elif answer_mode in {"formula", "formula_slots"}:
        check_formula(errors, warnings, severity, label, question, auto_check)
    elif answer_mode == "multiple_choice":
        check_multiple_choice(errors, warnings, severity, label, question, auto_check)
    elif answer_mode == "self_check":
        check_self_check(errors, warnings, severity, label, question)
    else:
        add(errors, warnings, "WARN", label, f"unknown answer_mode {answer_mode}")


def check_overlay_quality(errors, warnings, group, question, card):
    label = f"{rel(group['path'])}:{question.get('id', '<missing question id>')}"
    severity = overlay_severity(group)
    tags = set(card.get("tags") or [])
    review_status = card.get("review_status")
    technical_score = card.get("technical_score")
    overlay_needs_review = question.get("needs_human_review") or question.get("review_status") == "needs_human_review"

    if review_status == "needs_human_review" or "needs_human_review" in tags or overlay_needs_review:
        add(errors, warnings, severity, label, f"references review-only content ({question.get('card_id')})")
    if card.get("public_ready") is not True or question.get("public_ready") is False:
        add(errors, warnings, severity, label, f"references non-public-ready content ({question.get('card_id')})")

    if isinstance(technical_score, (int, float)) and technical_score > 5 and not has_allow(question, HIGH_TECH_ALLOW_KEYS):
        add(
            errors,
            warnings,
            severity,
            label,
            f"technical_score={technical_score} requires explicit manual overlay allow",
        )

    if "olympiad_above_exam" in tags and not (
        has_allow(question, OLYMPIAD_ALLOW_KEYS) or has_exam_score_tag(tags)
    ):
        add(
            errors,
            warnings,
            severity,
            label,
            "olympiad_above_exam card needs explicit strong exam question marker",
        )


def check_overlays(errors, warnings, groups, cards):
    ids = []
    by_card = defaultdict(list)
    for group in groups:
        severity = overlay_severity(group)
        if not isinstance(group["questions"], list):
            add(errors, warnings, severity, rel(group["path"]), "questions must be a list")
            continue
        for question in group["questions"]:
            label = f"{rel(group['path'])}:{question.get('id', '<missing question id>') if isinstance(question, dict) else '<invalid question>'}"
            if not isinstance(question, dict):
                add(errors, warnings, severity, label, "question item must be an object")
                continue
            question_id = question.get("id")
            card_id = question.get("card_id")
            if not question_id:
                add(errors, warnings, severity, label, "missing question id")
            else:
                ids.append((question_id, group["path"]))
            if not card_id:
                add(errors, warnings, severity, label, "missing card_id")
                continue
            by_card[card_id].append((question_id, group["path"]))
            card = cards.get(card_id)
            if not card:
                add(errors, warnings, "ERROR", label, f"unknown card_id {card_id}")
                continue
            check_overlay_quality(errors, warnings, group, question, card)
            check_question_answer(errors, warnings, group, question)

    for question_id, count in Counter(question_id for question_id, _ in ids).items():
        if count > 1:
            paths = ", ".join(sorted(rel(path) for qid, path in ids if qid == question_id))
            add(errors, warnings, "ERROR", "exam_simulation", f"duplicate overlay question id {question_id} in {paths}")

    for card_id, uses in sorted(by_card.items()):
        active_uses = [use for use in uses if use[1] == ACTIVE_OVERLAY_PATH]
        if len(active_uses) > 1:
            add(
                errors,
                warnings,
                "WARN",
                "exam_simulation",
                f"card {card_id} has {len(active_uses)} active overlay questions",
            )


def check_major_topics(errors, warnings, index_data):
    config = load_json(CONFIG_PATH) if CONFIG_PATH.exists() else {}
    topics = config.get("major_topics")
    if not isinstance(topics, list):
        add(errors, warnings, "ERROR", rel(CONFIG_PATH), "major_topics must be a list")
        return

    cluster_ids = {cluster.get("id") for cluster in index_data.get("task_clusters", []) if cluster.get("id")}
    if not cluster_ids:
        cluster_path = ROOT / "data" / "task_clusters" / "clusters.yaml"
        if cluster_path.exists():
            cluster_ids = {cluster.get("id") for cluster in load_json(cluster_path).get("clusters", []) if cluster.get("id")}
    fragments = {fragment.get("id") for fragment in load_taxonomy("fragments.yaml", "fragments")}
    tags = set(load_taxonomy("tags.yaml", "tags"))

    topic_ids = []
    for topic in topics:
        label = f"{rel(CONFIG_PATH)}:{topic.get('id', '<missing topic id>') if isinstance(topic, dict) else '<invalid topic>'}"
        if not isinstance(topic, dict):
            add(errors, warnings, "ERROR", label, "major topic item must be an object")
            continue
        topic_id = topic.get("id")
        if not topic_id:
            add(errors, warnings, "ERROR", label, "missing topic id")
        else:
            topic_ids.append(topic_id)
        for cluster_id in topic.get("cluster_ids", []) or []:
            if cluster_id not in cluster_ids:
                add(errors, warnings, "ERROR", label, f"unknown cluster_id {cluster_id}")
        for fragment_id in topic.get("fragments", []) or []:
            if fragment_id not in fragments:
                add(errors, warnings, "ERROR", label, f"unknown fragment {fragment_id}")
        for tag in topic.get("tags", []) or topic.get("tag_ids", []) or []:
            if tag not in tags:
                add(errors, warnings, "ERROR", label, f"unknown tag {tag}")

    for topic_id, count in Counter(topic_ids).items():
        if count > 1:
            add(errors, warnings, "ERROR", rel(CONFIG_PATH), f"duplicate major topic id {topic_id}")

    valid_topic_ids = set(topic_ids)
    for group in load_exam_sources():
        for question in group["questions"]:
            if isinstance(question, dict) and question.get("topic") not in valid_topic_ids:
                severity = overlay_severity(group)
                add(
                    errors,
                    warnings,
                    severity,
                    f"{rel(group['path'])}:{question.get('id', '<missing question id>')}",
                    f"unknown exam topic {question.get('topic')}",
                )


def main():
    errors = []
    warnings = []
    index_data, source_label = load_index_or_sources()
    _, cards = problem_cards(index_data)
    groups = load_exam_sources()

    if not groups:
        add(errors, warnings, "ERROR", "data/exam_simulation", "no question overlay files found")
    if not cards:
        add(errors, warnings, "ERROR", source_label, "no cards/problems loaded")

    check_major_topics(errors, warnings, index_data)
    check_overlays(errors, warnings, groups, cards)

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    overlay_count = sum(len(group["questions"]) for group in groups)
    active_count = sum(len(group["questions"]) for group in groups if group["path"] == ACTIVE_OVERLAY_PATH)
    print(
        f"Checked exam simulation: {overlay_count} overlay questions "
        f"({active_count} active), {len(cards)} cards from {source_label}."
    )
    if errors:
        print(f"FAILED: {len(errors)} errors, {len(warnings)} warnings")
        return 1
    print(f"OK: {len(warnings)} warnings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
