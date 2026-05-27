# Precommit Warning Resolution

Дата прохода: 2026-05-27.

## Что исправлено

### `audit_rules.py`

Сняты 4 предупреждения `exam_score tag with technical_score > 5`.

Правка содержательная: у карточек оставлены `written_exam`, профиль источника и техническая сложность, но снят `exam_score_6`, потому что `technical_score=6` означает письменную техническую тренировку, а не короткий вопрос для устной симуляции или быстрый студенческий маршрут.

- `local-du-written-2014-51-characteristics-pde`
- `local-du-written-2014-51-factorized-variable-coeff`
- `local-du-written-2014-51-lagrange-singular-curves`
- `local-du-written-2024-variational-free-endpoint`

В каждую карточку добавлена editorial-note о причине снятия `exam_score_6`. Checker не ослаблялся.

### `check_exam_simulation.py`

Сняты 9 структурных предупреждений proposal-layer:

- `exam-sim-proposal-msu-2024-6-counterexample`: добавлены ids вариантам ответа и приведен correct-marker к `is_correct`.
- `exam-sim-proposal-msu-2014-no-entire`: `correct` заменен на `is_correct`.
- `exam-sim-proposal-msu-2022-oscillatory-stability`: `correct` заменен на `is_correct`.
- `exam-sim-proposal-msu-2019-nonzero-field`: `self_check_rubric` приведен к `rubric`.
- `exam-sim-proposal-olympiad-touching-uniqueness`: добавлена self-check rubric.
- `exam-sim-proposal-olympiad-lyapunov-periodic-ban`: добавлена self-check rubric.
- `exam-sim-proposal-written-1998-lines-envelope`: `self_check_rubric` приведен к `rubric`.
- `exam-sim-proposal-written-1998-bounded-linear`: `self_check_rubric` приведен к `rubric`.

Сняты 2 предупреждения по активным дублям карточек:

- из активного `data/exam_simulation/questions.yaml` удален `exam-sim-test-lyap-01-autonomous-after-simplification`, потому что он был привязан к карточке `one-dimensional-autonomous-no-crossing`, но проверяет другой сюжет и создавал вторую активную overlay-привязку;
- из активного overlay удален `exam-sim-test-lyap-07-y-minus-square-stability`, потому что он был привязан к уже покрытой карточке `weak-pass-phase-line-semistable` и дублировал активную выдачу этой карточки.

Активный overlay после этого: 45 вопросов. Общий overlay вместе с proposal: 79 вопросов.

## Оставленные предупреждения

Оставленных warnings нет. Спорные proposal-вопросы не переводились в активный слой; исправлены только структурные поля, которые checker уже ожидает.

## Проверки

- `python tools/build_index.py` - OK, `index/generated.json`, 431 cards.
- `python tools/build_viewer.py` - OK, обновлены `viewer/index.html` и `index.html`.
- `python tools/validate.py` - OK: 431 cards, 966 relations, 49 sources.
- `python tools/check_links.py` - OK.
- `python tools/check_encoding.py` - OK.
- `python tools/check_clusters.py` - OK: 34 task clusters in 9 files.
- `python tools/check_cluster_guides.py` - OK: 34 clusters, 0 errors, 0 warnings, 0 info.
- `python tools/check_exam_simulation.py` - OK: 0 warnings.
- `python tools/audit_rules.py --max-items 80` - OK: 0 warnings.

Падений из-за активных чужих правок не зафиксировано.
