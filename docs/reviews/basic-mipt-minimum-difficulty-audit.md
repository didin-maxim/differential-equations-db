# Аудит базового минимума МФТИ по ДУ

Дата прохода: 2026-05-27. Область проверки: карточки с `difficulty.idea_score <= 4`, а также карточки с тегами `exam_score_3`, `low_technical`, `resit_exam`, `weak_student_check`. Цель прохода - не расширять базу массово, а проверить нижний порог: что студент на 3/4 действительно должен уметь по стандартному курсу МФТИ.

## Итог

Покрытие базовых тем в целом есть. Новая карточка добавлена только одна: `basic-mipt-variation-constants-ypp-plus-y`, потому что существующие представители вариации постоянных были либо общей формулой, либо технически тяжелее минимального применения.

Точечно переоценены 4 существующие карточки:

| Карточка | Было | Стало | Причина |
|---|---:|---:|---|
| `riccati-known-solution` | idea 5, tech 3 | idea 4, tech 3 | В условии уже дано частное решение; это минимальная проверка замены Риккати, а не задача "найти удачное решение". Добавлены `mipt_core`, `exam_score_4`. |
| `regular-singular-euler-frobenius` | idea 5, tech 4 | idea 4, tech 4 | Уравнение Эйлера является минимальной моделью индикаторного уравнения Фробениуса; техника остается на 4 из-за разбора корней. Добавлены `mipt_core`, `exam_score_4`. |
| `lebl-diffyqs-transport-signal-shift` | idea 5, tech 2 | idea 4, tech 2 | Это самый простой перенос профиля вдоль характеристик; для программы МФТИ годится как нижний представитель PDE-блока. Добавлены `mipt_core`, `exam_score_4`. |
| `oral-above-three-integrating-factor-x-only` | idea 5, tech 4 | idea 4, tech 4 | Условие прямо просит множитель `mu(x)`, поэтому остается стандартный критерий одной переменной, без самостоятельного угадывания типа. Добавлен `exam_score_4`. |

## Покрытие Минимума

| Тема | Представитель нижнего уровня | Оценка |
|---|---|---|
| Существование/единственность | `resit-pass-3-cauchy-uniqueness-check`, `weak-pass-existence-interval-singular-coeff`, `weak-pass-nonunique-continuous-counterexample` | exam 3, idea 4 |
| Разделяющиеся | `resit-pass-3-separable-exponential-growth` | exam 3, idea 2 |
| Линейное 1-го порядка | `resit-pass-3-linear-first-order-forcing`, `weak-pass-linear-method-choice` | exam 3, idea 3 |
| Точные уравнения | `resit-pass-3-exact-equation-potential`, `weak-pass-exact-form-recognition` | exam 3, idea 3 |
| Интегрирующий множитель | `oral-above-three-integrating-factor-x-only` | exam 4, idea 4 |
| Бернулли | `resit-pass-3-bernoulli-initial`, `weak-pass-bernoulli-substitution` | exam 3, idea 4 |
| Риккати с известным решением | `riccati-known-solution` | exam 4, idea 4 |
| Линейные ОДУ с постоянными коэффициентами | `resit-pass-3-constant-coeff-real-roots`, `resit-pass-3-undetermined-coefficients` | exam 3, idea 2-3 |
| Вронскиан/фундаментальная система | `weak-pass-wronskian-zero-dependence`, `local-du-standard-abel-wronskian-zero-lemma` | exam 3/idea 4 |
| Системы 2x2 | `resit-pass-3-diagonal-linear-system`, `weak-pass-linear-system-saddle` | exam 3, idea 2-3 |
| Простая матричная экспонента | `resit-pass-3-diagonal-linear-system` | exam 3, idea 2 |
| Фазовая прямая | `resit-pass-3-phase-line-logistic-signs`, `weak-pass-phase-line-semistable` | exam 3, idea 3-4 |
| Устойчивость простого равновесия | `weak-pass-linear-system-saddle`, `cluster-phase-stability-visual-asymptotic-sink` | idea 3-4 |
| Краевая задача/собственные значения | `resit-pass-3-dirichlet-sine-bvp`, `weak-pass-mixed-bvp-eigenvalues` | exam 3, idea 3-4 |
| Ряды | `weak-pass-series-first-coefficients` | exam 3, idea 3 |
| Фробениус на минимальном уровне | `regular-singular-euler-frobenius` | exam 4, idea 4 |
| Вариация постоянных | `basic-mipt-variation-constants-ypp-plus-y` | exam 4, idea 4 |
| Простейшая вариационная задача | `local-du-standard-euler-lagrange-fixed-endpoints` | idea 4 |
| Характеристики линейного PDE 1-го порядка | `lebl-diffyqs-transport-signal-shift` | exam 4, idea 4 |

## Добавлено

`basic-mipt-variation-constants-ypp-plus-y` в `data/problems/cluster_audit/basic_mipt_minimum/`.

Карточка проверяет только нижний навык: взять ФСР `cos x, sin x`, посчитать `W=1`, подставить в формулу вариации постоянных и получить частное решение. Это не дубль `variation-of-parameters-sine`: там та же идея, но технически выше из-за тригонометрических интегралов.

Связи добавлены только в `data/relations/relations.d/cluster-basic-mipt-minimum.yaml`, batch - только в `data/import_batches/cluster-basic-mipt-minimum.yaml`.

## Спорные, Но Не Исправленные

- Карточки с `low_technical`, но `idea_score >= 6` (`local-du-deficit-first-order-pde-characteristics`, `local-du-deficit-sturm-nonpositive-potential-bvp`, `local-du-deficit-variational-quadratic-bound` и похожие) оставлены как есть: там действительно низкая техника, но идея не является минимальной для оценки 3.
- Олимпиадные карточки с `idea_score <= 4` не переводились в `exam_score_3`: низкая идея сама по себе не означает минимальный экзаменационный порог, если формат или техника не типичны для слабого устного ответа.
- `oral-above-three-riccati-shift-known-solution` оставлена с idea 5: в отличие от `riccati-known-solution`, там нужно сначала заметить частное решение `y=x`.
