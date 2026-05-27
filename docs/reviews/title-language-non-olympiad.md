# Редактура названий неолимпиадных задач

Дата: 2026-05-27.

## Объем просмотра

Проверено примерно 299 верхних названий карточек в `data/problems/**` вне `data/problems/olympiad/**`, включая:

- `data/problems/oral_exam/**`;
- `data/problems/written_exam_import/**`;
- `data/problems/test_import/**`;
- остальные неолимпиадные разделы: `cluster_audit`, `english_sources`, `local_du`, `first_order`, `linear_equations`, `qualitative`, `systems`, `foundations`, `boundary_value`, `series_methods`.

Сначала просматривались только верхние `title`; для подозрительных случаев затем сверялись условие и идея/решение. Битой кириллицы в содержимом файлов не обнаружено: похожий на mojibake вывод был артефактом PowerShell, а не самих карточек.

## Что найдено

- Экзаменационные названия местами слишком явно подсказывали ход решения: `p=p(y) приводит...`, `явное продолжение данных`, `по критерию Бендиксона`.
- Встречались служебные или импортные формулировки: `шаблон`, `использовать инволюцию дважды`, `mu(y)`.
- Часть названий была длинной и тяжеловесной, особенно в `cluster_audit`, `english_sources` и `local_du`.
- В нескольких местах были неестественные обороты или кальки: `След ноль`, `Максимум-принцип`, `переменно-коэффициентная система`, `фолии Декарта`.

## Измененные файлы

- `data/problems/written_exam_import/mipt_1998_2000/written-mipt-2000-cauchy-p-of-y-guess.yaml`
- `data/problems/written_exam_import/mipt_2002_2004/written-mipt-2002-v1-nonlinear-p-of-y-cauchy.yaml`
- `data/problems/written_exam_import/mipt_2006_2010/written-mipt-2009-91-pde-positive-characteristics.yaml`
- `data/problems/written_exam_import/mipt_2006_2010/written-mipt-2010-01-matrix-sine-spectrum.yaml`
- `data/problems/test_import/limit_cycles/test-limit-cycles-bendixson-quadrants.yaml`
- `data/problems/test_import/limit_cycles/test-limit-cycles-radial-semistable.yaml`
- `data/problems/oral_exam/middle_5_7/oral-middle-integrating-factor-x.yaml`
- `data/problems/oral_exam/resit_pass_3/resit-pass-3-diagonal-linear-system.yaml`
- `data/problems/oral_exam/strong_10/oral-exam-strong-10-bounded-solutions-wronskian-obstruction.yaml`
- `data/problems/oral_exam/strong_10/oral-exam-strong-10-trace-zero-area-obstruction.yaml`
- `data/problems/oral_exam/weak_pass_3/weak-pass-bernoulli-substitution.yaml`
- `data/problems/cluster_audit/integrating_factor_exact_forms/cluster-integrating-factor-mu-xy.yaml`
- `data/problems/cluster_audit/integrating_factor_exact_forms/cluster-integrating-factor-mu-y-short.yaml`
- `data/problems/cluster_audit/linear_variable_coefficients/cluster-linear-variable-graph-direct-tangency.yaml`
- `data/problems/cluster_audit/linear_variable_coefficients/cluster-linear-variable-graph-ratio-maximum.yaml`
- `data/problems/cluster_audit/linear_variable_coefficients/cluster-linear-variable-variation-parameters-fundamental-system.yaml`
- `data/problems/cluster_audit/mipt_excellent_level/mipt-excellent-semilinear-characteristics-blowup.yaml`
- `data/problems/cluster_audit/olympiad_level/olympiad-level-involution-functional-differential.yaml`
- `data/problems/cluster_audit/olympiad_level/olympiad-level-rolle-after-homogeneous-factor.yaml`
- `data/problems/cluster_audit/orthogonal_trajectories/cluster-orthogonal-coaxal-imaginary-base-points.yaml`
- `data/problems/cluster_audit/parameter_dependence_variational_equation/cluster-parameter-second-order-coefficient-forcing.yaml`
- `data/problems/english_sources/mit_18034_honors/mit-18034-pset03-bvp-maximum-principle.yaml`
- `data/problems/english_sources/mit_18034_honors/mit-18034-pset07-euler-system-fundamental-matrix.yaml`
- `data/problems/english_sources/mit_18034_honors/mit-18034-pset09-hamiltonian-folium-first-integral.yaml`
- `data/problems/english_sources/waterloo_textual/waterloo-fundamental-matrix-flow-inverse.yaml`
- `data/problems/local_du/romanko_selected/local-du-romanko-pde-two-invariants.yaml`
- `data/problems/local_du/theory_8/local-du-8-t1-bessel-bounded-wronskian.yaml`
- `data/problems/local_du/written_2007_2015/local-du-written-2014-51-constant-coeff-third-order.yaml`

Менялись только верхние `title`. Идентификаторы, условия, решения, идеи, сложности и связи не менялись.

## Оставлено без изменения

- Названия с явными методами оставлены там, где сам формат карточки учебно-теоретический или метод прямо заявлен в условии: например формула Лиувилля, метод характеристик, теоремы Штурма.
- Математическая запись в названиях (`y''+...`, `p(y)`, `sin x`, `sec x`) оставлена, когда она делает название короче и точнее.
- `data/problems/cluster_audit/olympiad_level/**` находится вне `data/problems/olympiad/**`, поэтому был просмотрен; переносить карточки или менять `fragment: olympiad` не стал, так как это уже структурное решение, а не языковая редактура названия.
- `data/problems/olympiad/**` не редактировался. В рабочем дереве уже были чужие изменения в олимпиадной зоне; они не относятся к этому проходу.
