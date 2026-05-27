import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "data" / "task_clusters" / "clusters.yaml"
DEFAULT_OUTPUT_DIR = ROOT / ".scratch" / "task-cluster-split"


EXPLICIT_TARGETS = {
    "simple-variational-calculus": "variational.yaml",
    "linear-first-order-ode": "linear.yaml",
    "separable-homogeneous-first-order": "first_order.yaml",
    "linear-equations-variable-coefficients": "linear.yaml",
    "integrating-factor-exact-forms": "first_order.yaml",
    "constant-coefficient-linear-systems": "systems.yaml",
    "matrix-exponential-methods": "systems.yaml",
    "boundary-spectral-problems": "bvp.yaml",
    "phase-line-stability": "qualitative.yaml",
    "variation-of-constants": "linear.yaml",
    "sturm-oscillation-comparison": "bvp.yaml",
    "green-functions-bvp": "bvp.yaml",
    "first-integrals-plane-systems": "systems.yaml",
    "energy-estimates-second-order-ode": "qualitative.yaml",
    "pde-characteristics-first-order": "first_order.yaml",
    "riccati-bernoulli-reductions": "first_order.yaml",
    "nonlinear-second-order-order-reductions": "misc.yaml",
    "existence-uniqueness-continuation": "qualitative.yaml",
    "floquet-periodic-linear-systems": "linear.yaml",
    "parameter-dependence-variational-equation": "variational.yaml",
    "recover-ode-from-family": "first_order.yaml",
    "implicit-ode-discriminant": "first_order.yaml",
    "olympiad-transformed-linear-mvt": "olympiad.yaml",
    "olympiad-differential-inequalities-barriers": "olympiad.yaml",
    "olympiad-functional-differential-equations": "olympiad.yaml",
    "orthogonal-trajectories": "first_order.yaml",
    "guess-cauchy-solution-uniqueness": "first_order.yaml",
    "scalar-constant-coefficient-linear-ode": "linear.yaml",
    "linear-bvp-solvability-resonance": "bvp.yaml",
    "fundamental-matrix-linear-systems": "systems.yaml",
    "power-series-linear-ode": "linear.yaml",
    "integral-equation-to-ode": "misc.yaml",
    "wronskian-nonlinear-transforms": "linear.yaml",
    "limit-cycles-qualitative-criteria": "qualitative.yaml",
}


TOPIC_ORDER = [
    "linear.yaml",
    "systems.yaml",
    "first_order.yaml",
    "qualitative.yaml",
    "bvp.yaml",
    "variational.yaml",
    "olympiad.yaml",
    "misc.yaml",
]


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Plan a thematic split of data/task_clusters/clusters.yaml. "
            "By default this is a dry run and does not write files."
        )
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help="Source JSON-compatible YAML file to read.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory used only when --write is passed.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write planned split files to --output-dir.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing output files when used with --write.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the plan as JSON instead of a grouped text report.",
    )
    return parser.parse_args()


def load_cluster_file(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: {path} is not valid JSON-compatible YAML: {exc}") from exc


def load_sibling_cluster_files(source):
    clusters = []
    source_files = []
    for path in sorted(source.parent.glob("*.yaml")):
        if path == source:
            continue
        data = load_cluster_file(path)
        items = data.get("clusters", [])
        if not items:
            continue
        clusters.extend(items)
        source_files.append(path)
    return {"task_clusters_version": 1, "clusters": clusters}, source_files


def infer_target(cluster_id):
    if cluster_id in EXPLICIT_TARGETS:
        return EXPLICIT_TARGETS[cluster_id], False
    if cluster_id.startswith("olympiad-"):
        return "olympiad.yaml", True
    if "variational" in cluster_id or "calculus" in cluster_id:
        return "variational.yaml", True
    if any(token in cluster_id for token in ("bvp", "boundary", "spectral", "sturm", "green")):
        return "bvp.yaml", True
    if any(
        token in cluster_id
        for token in (
            "phase",
            "stability",
            "limit-cycle",
            "first-integral",
            "energy-estimate",
            "existence",
            "uniqueness",
            "parameter-dependence",
        )
    ):
        return "qualitative.yaml", True
    if any(
        token in cluster_id
        for token in (
            "linear",
            "matrix",
            "fundamental-matrix",
            "floquet",
            "power-series",
            "wronskian",
            "variation-of-constants",
        )
    ):
        return "linear.yaml", True
    if any(
        token in cluster_id
        for token in (
            "first-order",
            "riccati",
            "bernoulli",
            "implicit",
            "orthogonal",
            "recover-ode",
            "pde-characteristics",
            "integral-equation",
            "order-reductions",
        )
    ):
        return "first_order.yaml", True
    return "misc.yaml", True


def build_plan(data):
    clusters = data.get("clusters")
    if not isinstance(clusters, list):
        raise SystemExit("ERROR: source root must contain a clusters list")

    grouped = defaultdict(list)
    inferred = []
    for cluster in clusters:
        if not isinstance(cluster, dict):
            raise SystemExit("ERROR: every cluster item must be an object")
        cluster_id = cluster.get("id")
        if not isinstance(cluster_id, str) or not cluster_id:
            raise SystemExit("ERROR: every cluster must have a non-empty string id")
        target, was_inferred = infer_target(cluster_id)
        grouped[target].append(cluster)
        if was_inferred:
            inferred.append(cluster_id)
    return grouped, inferred


def ordered_targets(grouped):
    known = [target for target in TOPIC_ORDER if target in grouped]
    extra = sorted(target for target in grouped if target not in TOPIC_ORDER)
    return known + extra


def print_text_plan(grouped, inferred):
    total = sum(len(items) for items in grouped.values())
    print(f"Planned split: {total} cluster(s) into {len(grouped)} file(s)")
    for target in ordered_targets(grouped):
        print()
        print(f"{target} ({len(grouped[target])})")
        for cluster in grouped[target]:
            print(f"  - {cluster['id']}")
    if inferred:
        print()
        print("WARNING: target file inferred by heuristic for:")
        for cluster_id in inferred:
            print(f"  - {cluster_id}")


def print_json_plan(grouped, inferred):
    rows = []
    for target in ordered_targets(grouped):
        for cluster in grouped[target]:
            rows.append({"id": cluster["id"], "target": target})
    print(json.dumps({"clusters": rows, "inferred": inferred}, ensure_ascii=False, indent=2))


def write_files(grouped, version, output_dir, force):
    output_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for target in ordered_targets(grouped):
        output_path = output_dir / target
        if output_path.exists() and not force:
            raise SystemExit(f"ERROR: {output_path} already exists; pass --force to overwrite")
        payload = {
            "task_clusters_version": version,
            "clusters": grouped[target],
        }
        output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        written.append(output_path)
    print()
    print(f"Wrote {len(written)} file(s) to {output_dir}")
    for path in written:
        print(f"  - {path}")


def main():
    args = parse_args()
    source = args.source if args.source.is_absolute() else ROOT / args.source
    output_dir = args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir

    data = load_cluster_file(source)
    source_files = [source]
    if not data.get("clusters"):
        fallback_data, fallback_files = load_sibling_cluster_files(source)
        if fallback_files:
            data = fallback_data
            source_files = fallback_files
    grouped, inferred = build_plan(data)

    if args.json:
        print_json_plan(grouped, inferred)
    else:
        if source_files != [source]:
            print("Source clusters list is empty; using sibling split files:")
            for path in source_files:
                print(f"  - {path}")
            print()
        print_text_plan(grouped, inferred)

    if args.write:
        version = data.get("task_clusters_version")
        if not isinstance(version, int):
            raise SystemExit("ERROR: task_clusters_version must be an integer before writing")
        write_files(grouped, version, output_dir, args.force)
    else:
        print()
        print("Dry run only. Pass --write to emit files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
