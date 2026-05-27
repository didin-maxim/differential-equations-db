import json
import re
import sys
from collections import Counter
from pathlib import Path

from lib import ROOT, load_problem_files

CLUSTER_REQUIRED = [
    "id",
    "title",
    "status",
    "goal",
    "duplicate_signals",
    "canonical_solution_plan",
    "allowed_variants",
    "saturation_policy",
    "deficit_policy",
    "representative_card_ids",
    "notes",
]
CLUSTER_STATUSES = {"deficit", "active", "watch", "saturated"}
SATURATION_STATUSES = {"deficit", "watch", "saturated"}
PRIORITIES = {"low", "medium", "high"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
VARIANT_ID_RE = re.compile(r"^[a-z0-9][a-z0-9_]*$")


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def fail(errors, label, message):
    errors.append(f"{label}: {message}")


def require_nonempty_string(errors, label, obj, field):
    value = obj.get(field)
    if not isinstance(value, str) or not value.strip():
        fail(errors, label, f"{field} must be a non-empty string")


def require_string_list(errors, label, obj, field, min_items=1):
    value = obj.get(field)
    if not isinstance(value, list):
        fail(errors, label, f"{field} must be a list")
        return
    if len(value) < min_items:
        fail(errors, label, f"{field} must contain at least {min_items} item(s)")
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            fail(errors, label, f"{field}[{index}] must be a non-empty string")


def check_variant(errors, label, variant):
    if not isinstance(variant, dict):
        fail(errors, label, "allowed_variants item must be an object")
        return
    for field in ["id", "description", "use_when"]:
        require_nonempty_string(errors, label, variant, field)
    variant_id = variant.get("id")
    if isinstance(variant_id, str) and not VARIANT_ID_RE.match(variant_id):
        fail(errors, label, f"allowed variant id has invalid format: {variant_id}")


def check_cluster(errors, path, cluster, problem_ids):
    label = f"{path}:{cluster.get('id', '<missing cluster id>') if isinstance(cluster, dict) else '<invalid cluster>'}"
    if not isinstance(cluster, dict):
        fail(errors, str(path), "cluster item must be an object")
        return

    for field in CLUSTER_REQUIRED:
        if field not in cluster:
            fail(errors, label, f"missing required field {field}")

    cluster_id = cluster.get("id")
    if not isinstance(cluster_id, str) or not ID_RE.match(cluster_id):
        fail(errors, label, f"invalid id {cluster_id}")
    require_nonempty_string(errors, label, cluster, "title")
    require_nonempty_string(errors, label, cluster, "goal")
    if cluster.get("status") not in CLUSTER_STATUSES:
        fail(errors, label, f"unknown status {cluster.get('status')}")

    require_string_list(errors, label, cluster, "duplicate_signals")
    require_string_list(errors, label, cluster, "canonical_solution_plan")

    variants = cluster.get("allowed_variants")
    if not isinstance(variants, list) or not variants:
        fail(errors, label, "allowed_variants must be a non-empty list")
    else:
        variant_ids = []
        for variant in variants:
            check_variant(errors, label, variant)
            if isinstance(variant, dict):
                variant_ids.append(variant.get("id"))
        for variant_id, count in Counter(variant_ids).items():
            if variant_id and count > 1:
                fail(errors, label, f"duplicate allowed variant id {variant_id}")

    saturation = cluster.get("saturation_policy")
    if not isinstance(saturation, dict):
        fail(errors, label, "saturation_policy must be an object")
    else:
        if saturation.get("status") not in SATURATION_STATUSES:
            fail(errors, label, f"unknown saturation status {saturation.get('status')}")
        count = saturation.get("target_representative_count")
        if not isinstance(count, int) or count < 0:
            fail(errors, label, "target_representative_count must be a non-negative integer")
        require_string_list(errors, label, saturation, "do_not_add_when")

    deficit = cluster.get("deficit_policy")
    if not isinstance(deficit, dict):
        fail(errors, label, "deficit_policy must be an object")
    else:
        if deficit.get("priority") not in PRIORITIES:
            fail(errors, label, f"unknown deficit priority {deficit.get('priority')}")
        require_nonempty_string(errors, label, deficit, "need")
        require_string_list(errors, label, deficit, "prefer_new_cards", min_items=0)

    representative_ids = cluster.get("representative_card_ids")
    if not isinstance(representative_ids, list):
        fail(errors, label, "representative_card_ids must be a list")
    else:
        for rid in representative_ids:
            if not isinstance(rid, str) or not rid.strip():
                fail(errors, label, "representative_card_ids items must be non-empty strings")
            elif rid not in problem_ids:
                fail(errors, label, f"unknown representative card id {rid}")
        for rid, count in Counter(representative_ids).items():
            if count > 1:
                fail(errors, label, f"duplicate representative card id {rid}")

    if not isinstance(cluster.get("notes"), str):
        fail(errors, label, "notes must be a string")


def main():
    errors = []
    cluster_dir = ROOT / "data" / "task_clusters"
    paths = sorted(cluster_dir.rglob("*.yaml")) if cluster_dir.exists() else []
    problem_ids = {p.get("id") for _, p in load_problem_files()}

    all_cluster_ids = []
    cluster_count = 0
    for path in paths:
        try:
            data = load_json(path)
        except json.JSONDecodeError as exc:
            fail(errors, str(path), f"invalid JSON-compatible YAML: {exc}")
            continue
        if not isinstance(data, dict):
            fail(errors, str(path), "root must be an object")
            continue
        if not isinstance(data.get("task_clusters_version"), int):
            fail(errors, str(path), "task_clusters_version must be an integer")
        clusters = data.get("clusters")
        if not isinstance(clusters, list):
            fail(errors, str(path), "clusters must be a list")
            continue
        for cluster in clusters:
            if isinstance(cluster, dict):
                all_cluster_ids.append(cluster.get("id"))
            check_cluster(errors, path, cluster, problem_ids)
            cluster_count += 1

    for cluster_id, count in Counter(all_cluster_ids).items():
        if cluster_id and count > 1:
            fail(errors, "task_clusters", f"duplicate cluster id {cluster_id}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"FAILED: {len(errors)} errors")
        return 1
    print(f"OK: {cluster_count} task clusters in {len(paths)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
