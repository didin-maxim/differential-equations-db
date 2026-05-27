# Pre-commit аудит: сложности и course-теги

Дата: 2026-05-27.

Область проверки: все problem-карточки в `data/problems/**`, с отдельным
вниманием к свежим `data/problems/olympiad/**` и
`data/problems/cluster_audit/**`.

## Итог

- Всего карточек: 357.
- Задач: 294.
- Кластеров: 32.
- Все 294 задачи имеют обе шкалы сложности: `idea_score` и
  `technical_score`.
- Все 294 задачи имеют хотя бы одну course-level метку:
  `standard_course_methods`, `advanced_standard_course` или
  `beyond_standard_course`.
- Явных перепутываний идейной и технической сложности не найдено.
- Вычислительных монстров в стандартных неолимпиадных кластерах не найдено:
  нет задач с `technical_score >= 8`, которые одновременно не являются
  олимпиадными или письменными вычислительными задачами.

## Исправления

Добавлены недостающие course-level метки:

- `bounded-solution-y-prime-y-square` -> `standard_course_methods`;
- `convex-solution-two-zeros` -> `standard_course_methods`;
- `energy-no-nonconstant-decay-periodic` -> `standard_course_methods`;
- `global-positive-impossible` -> `standard_course_methods`;
- `periodic-linear-equation-zero-mean` -> `standard_course_methods`;
- `periodic-solution-monotone-derivative` -> `standard_course_methods`;
- `solve-functional-ode-composition` -> `standard_course_methods`;
- `two-solutions-touching` -> `standard_course_methods`;
- `cluster-sturm-bvp-unit-endpoints-sharp-threshold` ->
  `advanced_standard_course`;
- `cluster-sturm-bvp-unit-endpoints-threshold-counterexample` ->
  `standard_course_methods`.

Эти правки безопасны: решения используют стандартные приемы курса
дифференциальных уравнений, кроме острого штурмовского порога, который
естественно помечен как продвинутый стандартный блок.

## Распределение по course-level меткам

Сумма больше числа задач, потому что часть карточек остается мостовой и имеет
две course-level метки.

| Метка | Количество задач |
|---|---:|
| `standard_course_methods` | 207 |
| `advanced_standard_course` | 96 |
| `beyond_standard_course` | 4 |

Найдено 13 задач с двумя course-level метками
`standard_course_methods` + `advanced_standard_course`. Это не исправлялось
автоматически: в текущих правилах базы эти метки не объявлены строго
взаимоисключающими, а многие такие карточки являются мостами между стандартным
приемом и продвинутой формулировкой. Перед публичным релизом можно решить,
нужна ли отдельная политика ровно одной course-level метки.

## Матрица сложности

| idea \\ technical | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | всего |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| 3 | 0 | 8 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 13 |
| 4 | 3 | 9 | 19 | 7 | 2 | 0 | 0 | 0 | 0 | 40 |
| 5 | 2 | 12 | 17 | 16 | 7 | 0 | 0 | 0 | 0 | 54 |
| 6 | 0 | 14 | 19 | 18 | 14 | 6 | 0 | 0 | 0 | 71 |
| 7 | 0 | 5 | 10 | 12 | 9 | 2 | 1 | 0 | 0 | 39 |
| 8 | 0 | 0 | 7 | 22 | 9 | 1 | 4 | 1 | 0 | 44 |
| 9 | 0 | 0 | 0 | 1 | 6 | 2 | 2 | 0 | 0 | 11 |
| 10 | 0 | 0 | 0 | 0 | 1 | 2 | 2 | 6 | 1 | 12 |
| 11 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 3 | 0 | 5 |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| всего | 5 | 52 | 76 | 77 | 48 | 14 | 11 | 10 | 1 | 294 |

Распределение выглядит содержательно согласованным: основная масса находится в
зоне `idea_score` 4-8 и `technical_score` 2-5; олимпиадный хвост по идее есть,
но он не тащит за собой массовые тяжелые вычисления.

## Олимпиадные задачи вне кластеров

После олимпиадного кластерного аудита вне кластеров остаются 4 задачи:

- `periodic-solution-monotone-derivative`;
- `msu-ode-2023-8-fourth-order-zero-count-review`;
- `putnam-early-1959-a5-pursuit-curve`;
- `putnam-modern-1979-b4`.

Для них есть явное объяснение в
`docs/reviews/olympiad-unclustered-cluster-audit.md`: одна задача слишком
одноходовая для отдельного кластера, одна ожидает завершения решения, две
содержательно уникальны и пока не имеют трех близких родственников.

## Проверка предыдущих аудитов

Проблемы, найденные предыдущими агентами, отражены в отчетах и служебных
слоях:

- неолимпиадные qualitative/stability задачи разобраны в
  `docs/reviews/non-olympiad-unclustered-qualitative-audit.md`;
- первый порядок разобран в
  `docs/reviews/non-olympiad-unclustered-first-order-audit.md`;
- линейные ОДУ, системы и краевые задачи разобраны в
  `docs/reviews/non-olympiad-unclustered-linear-systems-bvp-audit.md`;
- cross-source аудит описан в
  `docs/reviews/non-olympiad-unclustered-cross-source-audit.md`;
- олимпиадная кластеризация описана в
  `docs/reviews/olympiad-unclustered-cluster-audit.md`;
- свежий языковой и course-tag аудит олимпиадного импорта описан в
  `docs/reviews/olympiad-import-quality-audit.md`.

В этих проходах добавлены отдельные files в `data/relations/relations.d/` и
обновлены `representative_card_ids` в `data/task_clusters/clusters.yaml`.

## Риски

- 13 мостовых карточек имеют одновременно `standard_course_methods` и
  `advanced_standard_course`; это не ошибка валидатора, но для более строгой
  навигации можно позже ввести правило "ровно одна course-level метка".
- `msu-ode-2023-8-fourth-order-zero-count-review` остается с незавершенной
  проверкой решения и поэтому не должен попадать в публичный маршрут без
  ручной доработки.
