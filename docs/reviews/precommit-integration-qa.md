# Precommit Integration QA

Date: 2026-05-27

Scope: integration QA before commit/push while Boole, Beauvoir, Mendel, Ampere, and Dewey are still active. No commit/push performed. No edits were made to card data or other active agents' zones; only this report was added.

## Verdict

Status: not ready for commit/push yet.

Main reasons:

- Active agents are still open, including Dewey on warning resolution.
- `check_exam_simulation` exits 0 but still reports 11 warnings.
- `audit_rules` exits 0 but still reports 4 warnings.
- There are large untracked working directories that need explicit keep/drop/stage decisions: `.scratch/` and `tmp/`.
- There are 181 untracked porcelain entries, expanding to 307 untracked files via `git ls-files --others --exclude-standard`.
- `git diff --check` reports no whitespace errors, but Git prints many LF-to-CRLF conversion warnings.

## Commands Run

| Check | Command | Result |
| --- | --- | --- |
| build_index | `python tools\build_index.py` | PASS, exit 0; wrote `index/generated.json` with 431 cards |
| build_viewer | `python tools\build_viewer.py` | PASS, exit 0; wrote `viewer/index.html` and `index.html` |
| validate | `python tools\validate.py` | PASS, exit 0; 431 cards, 966 relations, 49 sources |
| check_links | `python tools\check_links.py` | PASS, exit 0 |
| check_encoding | `python tools\check_encoding.py` | PASS, exit 0 |
| check_clusters | `python tools\check_clusters.py` | PASS, exit 0; 34 clusters in 9 files |
| check_cluster_guides | `python tools\check_cluster_guides.py --strict` | PASS, exit 0; 0 errors, 0 warnings, 0 info |
| check_exam_simulation | `python tools\check_exam_simulation.py` | PASS with warnings, exit 0; 81 overlay questions, 47 active, 11 warnings |
| audit_rules | `python tools\audit_rules.py --max-items 50` | PASS with warnings, exit 0; 4 warnings |
| viewer JS syntax sanity | Node `vm.Script` over executable inline scripts in `viewer/index.html`, excluding `type="application/json"` payload | PASS, exit 0; 1 executable inline script parsed |
| git diff check | `git diff --check` | PASS for whitespace; Git emitted LF-to-CRLF warnings |
| remote check | `git ls-remote origin refs/heads/master` | PASS; remote master equals local `HEAD` and `origin/master` at `af9ef5d1bea6c2dde10245544d4d7370ed4f4e3e` |

Note: a naive JS syntax check over every inline `<script>` fails because `viewer/index.html` contains the database payload in `<script id="db-data" type="application/json">...</script>`. The corrected sanity check excludes JSON script tags and validates only executable JS.

## Remaining Warnings

`check_exam_simulation.py` warnings:

- `data/exam_simulation/question_batches/msu-ode-2021-2024.yaml:exam-sim-proposal-msu-2024-6-counterexample`: multiple-choice options must all have ids.
- Same question: multiple-choice question has no correct option.
- `data/exam_simulation/question_batches/msu-ode-archive-old.yaml:exam-sim-proposal-msu-2014-no-entire`: multiple-choice question has no correct option.
- `data/exam_simulation/question_batches/msu-ode-archive-old.yaml:exam-sim-proposal-msu-2019-nonzero-field`: self-check question has no criteria/rubric.
- `data/exam_simulation/question_batches/msu-ode-archive-old.yaml:exam-sim-proposal-msu-2022-oscillatory-stability`: multiple-choice question has no correct option.
- `data/exam_simulation/question_batches/olympiad-standard-course-overlay.yaml:exam-sim-proposal-olympiad-touching-uniqueness`: self-check question has no criteria/rubric.
- `data/exam_simulation/question_batches/olympiad-standard-course-overlay.yaml:exam-sim-proposal-olympiad-lyapunov-periodic-ban`: self-check question has no criteria/rubric.
- `data/exam_simulation/question_batches/written-1998-2000.yaml:exam-sim-proposal-written-1998-lines-envelope`: self-check question has no criteria/rubric.
- `data/exam_simulation/question_batches/written-1998-2000.yaml:exam-sim-proposal-written-1998-bounded-linear`: self-check question has no criteria/rubric.
- Active overlay duplicate: card `one-dimensional-autonomous-no-crossing` has 2 active overlay questions.
- Active overlay duplicate: card `weak-pass-phase-line-semistable` has 2 active overlay questions.

`audit_rules.py` warnings:

- `local-du-written-2014-51-characteristics-pde`: `exam_score` tag with `technical_score > 5`.
- `local-du-written-2014-51-factorized-variable-coeff`: `exam_score` tag with `technical_score > 5`.
- `local-du-written-2014-51-lagrange-singular-curves`: `exam_score` tag with `technical_score > 5`.
- `local-du-written-2024-variational-free-endpoint`: `exam_score` tag with `technical_score > 5`.

## Git Status Grouping

Current branch: `master`, tracking `origin/master`.

Remote state checked with `git ls-remote`: local `HEAD`, local `origin/master`, and remote `refs/heads/master` all point to `af9ef5d1bea6c2dde10245544d4d7370ed4f4e3e`.

Porcelain status summary:

- Total status entries: 342.
- Modified entries: 161.
- Untracked porcelain entries: 181.
- Unmerged conflicts: none found by `git diff --name-only --diff-filter=U`.

Grouped changes:

| Group | Count |
| --- | ---: |
| Data cards under `data/problems/` | 161 |
| Definitions | 1 |
| Task clusters | 9 |
| Relations | 44 |
| Import batches | 38 |
| Exam simulation | 1 porcelain entry, 10 untracked files |
| Taxonomy, sources, standard ideas | 3 |
| Viewer/tools/root generated home | 8 |
| Docs | 73 |
| Generated files (`index.html`, `index/generated.json`, `viewer/index.html`) | 3 |
| Scratch/tmp | 2 porcelain entries |
| README | 1 |

Untracked file expansion from `git ls-files --others --exclude-standard`:

| Area | Files |
| --- | ---: |
| `.scratch/` | 4 |
| `tmp/` | 80 |
| `data/exam_simulation/` | 10 |
| `data/import_batches/` | 27 |
| `data/problems/` | 74 |
| `data/relations/` | 29 |
| `data/task_clusters/` | 8 |
| `docs/reviews/` | 71 |
| `tools/` | 3 |
| Other | 1 |

## Potential Commit Blockers

- Active agents not closed: Boole, Beauvoir, Mendel, Ampere, and Dewey are still in flight by instruction.
- Warning resolution not complete: 15 total warnings across `check_exam_simulation` and `audit_rules`.
- Concurrent activity observed during QA: `docs/reviews/precommit-warning-resolution.md` appeared while this report was being written, consistent with Dewey's warning-resolution lane.
- Untracked scratch/temp material: `.scratch/` and `tmp/` are untracked and not covered by current `.gitignore`.
- Generated files were rebuilt and are modified: `index/generated.json`, `viewer/index.html`, and root `index.html`; final pass should confirm whether all generated outputs correspond to the final data state after active agents finish.
- Large untracked docs/reports and data imports need ownership review before staging.
- LF-to-CRLF warnings appear across many files during Git checks; no whitespace errors were reported, but line-ending policy should be confirmed before commit.

## Final Pass Checklist

- [ ] Wait for Boole, Beauvoir, Mendel, Ampere, and Dewey to finish or explicitly hand off.
- [ ] Re-run `python tools\build_index.py`.
- [ ] Re-run `python tools\build_viewer.py`.
- [ ] Re-run `python tools\validate.py`.
- [ ] Re-run `python tools\check_links.py`.
- [ ] Re-run `python tools\check_encoding.py`.
- [ ] Re-run `python tools\check_clusters.py`.
- [ ] Re-run `python tools\check_cluster_guides.py --strict`.
- [ ] Re-run `python tools\check_exam_simulation.py` and resolve or explicitly accept warnings.
- [ ] Re-run `python tools\audit_rules.py --max-items 50` and resolve or explicitly accept warnings.
- [ ] Re-run executable JS syntax sanity for `viewer/index.html`.
- [ ] Decide whether `.scratch/` and `tmp/` should be deleted, ignored, or intentionally committed.
- [ ] Review all untracked reports in `docs/reviews/` for intentional inclusion.
- [ ] Confirm generated files are up to date after the last data change.
- [ ] Run `git diff --check`.
- [ ] Verify remote again before push.
- [ ] Only then prepare commit and push.
