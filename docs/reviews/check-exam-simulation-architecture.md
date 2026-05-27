# Check Exam Simulation Architecture

Date: 2026-05-27.

## What the checker covers

Added `tools/check_exam_simulation.py` as a separate structural gate for the
exam simulation layer.

The script loads card/problem data from `index/generated.json` when it exists,
falling back to source cards through `tools/lib.py`. It also reads every
`data/exam_simulation/**/*.yaml` overlay file through the same JSON-compatible
loader used by the existing tools.

Checks implemented:

- overlay questions reference existing card ids;
- active overlays in `data/exam_simulation/questions.yaml` do not point to
  `needs_human_review`, `public_ready: false`, high-technical, or
  `olympiad_above_exam` cards unless an explicit manual overlay allow marker is
  present;
- proposal batches are checked with the same rules, but content-readiness
  issues are warnings until they are promoted to the active simulation layer;
- `numeric`, `formula`, `formula_slots`, and `multiple_choice` questions have
  machine-checkable answer data;
- `self_check` questions have criteria or a rubric;
- `major_topics` references point to existing fragments, task clusters, and
  taxonomy tags;
- overlay topic ids are known major topic ids;
- duplicate active overlay questions for the same card are reported as warnings.

The checker returns nonzero only for structural errors. Subjective or
not-yet-promoted content issues are printed as `WARN`.

## Current result

After fixing one broken major-topic cluster slug in
`data/exam_simulation/config.yaml`:

```text
python tools/check_exam_simulation.py
Checked exam simulation: 81 overlay questions (47 active), 431 cards from index:index/generated.json.
OK: 11 warnings
```

Current warnings:

- `data/exam_simulation/question_batches/msu-ode-2021-2024.yaml`:
  `exam-sim-proposal-msu-2024-6-counterexample` has multiple-choice options
  without ids and no detected correct option.
- `data/exam_simulation/question_batches/msu-ode-archive-old.yaml`:
  `exam-sim-proposal-msu-2014-no-entire` has no detected correct option.
- `data/exam_simulation/question_batches/msu-ode-archive-old.yaml`:
  `exam-sim-proposal-msu-2019-nonzero-field` has no self-check criteria/rubric.
- `data/exam_simulation/question_batches/msu-ode-archive-old.yaml`:
  `exam-sim-proposal-msu-2022-oscillatory-stability` has no detected correct
  option.
- `data/exam_simulation/question_batches/olympiad-standard-course-overlay.yaml`:
  `exam-sim-proposal-olympiad-touching-uniqueness` has no self-check
  criteria/rubric.
- `data/exam_simulation/question_batches/olympiad-standard-course-overlay.yaml`:
  `exam-sim-proposal-olympiad-lyapunov-periodic-ban` has no self-check
  criteria/rubric.
- `data/exam_simulation/question_batches/written-1998-2000.yaml`:
  `exam-sim-proposal-written-1998-lines-envelope` has no self-check
  criteria/rubric.
- `data/exam_simulation/question_batches/written-1998-2000.yaml`:
  `exam-sim-proposal-written-1998-bounded-linear` has no self-check
  criteria/rubric.
- active overlay card `one-dimensional-autonomous-no-crossing` is used by two
  active questions.
- active overlay card `weak-pass-phase-line-semistable` is used by two active
  questions.

## Fixed in this pass

- `data/exam_simulation/config.yaml` used the non-existent cluster id
  `guess-cauchy-uniqueness`; it now points to
  `guess-cauchy-solution-uniqueness`.

## Next pass

- Normalize proposal multiple-choice data to the same `auto_check` shape used
  by active questions, or add ids plus `is_correct` consistently.
- Add self-check criteria to proposal proof/thinking questions before promotion.
- Decide whether duplicate active overlays on the same card are intentional
  variants or should be split to separate source cards.
- If high-technical or olympiad-above-exam cards are ever promoted, require an
  explicit overlay field such as `manual_exam_allow`,
  `allow_high_technical`, or `strong_exam_question`.
