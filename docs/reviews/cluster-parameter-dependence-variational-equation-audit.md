# Аудит кластера parameter-dependence-variational-equation

Дата: 2026-05-27.

Зона: `data/task_clusters/clusters.yaml`, `docs/TASK_CLUSTERS.md`, карточки `data/problems/**` с тегами/методами `parameter_dependence`, `variational_equation`, `sensitivity_equation`, `regular_perturbation`, `initial_data_parameter`, `variation_of_parameters`, `gronwall`, а также отчеты `mipt-middle-level-difficulty-audit.md`, `mipt-excellent-level-audit.md`, `english-import-qa.md`.

## Точные попадания

Кластер уточнен как зона задач, где цель - чувствительность решения: продифференцировать уравнение, решение, поток или начальные данные по параметру и получить линейную задачу для производной по параметру. Обычная `variation_of_parameters` без параметрической цели сюда не входит.

Точные representatives после аудита:

| id | Роль |
|---|---|
| `cluster-parameter-sensitivity-equation-theorem` | Базовая theorem-карточка: `z'=D_x f z+f_lambda`, `z(t0)=xi'(lambda)`. |
| `cluster-parameter-initial-data-first-order` | Первый порядок, параметр в коэффициенте и начальном условии. |
| `cluster-parameter-second-order-coefficient-forcing` | Второй порядок, параметр в коэффициенте, правой части и начальных данных. |
| `cluster-parameter-system-sensitivity` | Система и векторная чувствительность. |
| `local-du-written-2011-21-parameter-variations` | Первая и вторая производные по параметру в письменной задаче. |
| `local-du-written-2023-parameter-sensitivity` | Локальная письменная задача на первую производную по параметру. |
| `teschl-stanford-bridge-flow-derivative-variational-equation` | Производная потока по начальной точке. |
| `teschl-stanford-bridge-regular-perturbation-first-correction` | Первая регулярная поправка как неоднородное вариационное уравнение. |
| `mipt-excellent-second-parameter-correction` | Вторая поправка, где нелинейность впервые входит во втором порядке. |
| `cluster-parameter-gronwall-lipschitz-dependence` | Качественная оценка чувствительности по параметру через Гронуолла. |

## Покрытие вариантов

- Уравнение первого порядка с параметром в правой части: `local-du-written-2023-parameter-sensitivity`, `local-du-written-2011-21-parameter-variations`.
- Уравнение второго порядка: `cluster-parameter-second-order-coefficient-forcing`.
- Система: `cluster-parameter-system-sensitivity`, плюс теоретический bridge `teschl-stanford-bridge-flow-derivative-variational-equation`.
- Зависимость начальных условий от параметра: `cluster-parameter-initial-data-first-order`, `cluster-parameter-second-order-coefficient-forcing`, `cluster-parameter-sensitivity-equation-theorem`.
- Параметр в коэффициентах и в правой части: `cluster-parameter-second-order-coefficient-forcing`; в первом порядке также `cluster-parameter-initial-data-first-order` показывает параметр в коэффициенте.
- Первая поправка: `teschl-stanford-bridge-regular-perturbation-first-correction`.
- Вторая поправка: `local-du-written-2011-21-parameter-variations`, `mipt-excellent-second-parameter-correction`.
- Качественная оценка через Гронуолла: `cluster-parameter-gronwall-lipschitz-dependence`; соседний общий источник - `teschl-stanford-bridge-continuous-dependence-gronwall`.

## Добавлено

Новые карточки лежат в `data/problems/cluster_audit/parameter_dependence_variational_equation/`:

| id | idea | tech | Зачем |
|---|---:|---:|---|
| `cluster-parameter-sensitivity-equation-theorem` | 7 | 4 | Короткая базовая формула чувствительности с параметром в поле и начальных данных. |
| `cluster-parameter-second-order-coefficient-forcing` | 6 | 3 | Закрывает второй порядок и параметр одновременно в коэффициенте, правой части и начальных данных. |
| `cluster-parameter-system-sensitivity` | 6 | 4 | Конкретная система без тяжелой матричной экспоненты. |
| `cluster-parameter-initial-data-first-order` | 5 | 2 | Минимальный пример, где важно продифференцировать начальное условие. |
| `cluster-parameter-gronwall-lipschitz-dependence` | 6 | 3 | Не производная, а чистая оценка sensitivity через Гронуолла. |

Batch: `data/import_batches/cluster-parameter-dependence-variational-equation.yaml`.

Relations: `data/relations/relations.d/cluster-parameter-dependence-variational-equation.yaml`.

## Нежелательные представители

Без удаления из базы:

- `mit-18034-pset03-resonance-limit` - parameter-adjacent, но главный ход это резонансный предел близких частот, а не уравнение чувствительности.
- `waterloo-critical-damping-crossing-condition` и `waterloo-second-order-pq-stability` - полезны для параметрической устойчивости, но решаются анализом корней/порогов, не вариационным уравнением.
- Карточки с чистой `variation_of_parameters` для линейных неоднородных уравнений (`variation-of-parameters-sine`, `inhomogeneous-linear-system-variation`, BVP Green-kernel карточки) должны оставаться в соседних кластерах, если параметрическая чувствительность не является целью.

Technical monster candidates в просмотренной зоне не удалялись. Потенциально нежелательный тип для будущих импортов: задача, где после корректного дифференцирования по параметру остается длинное интегрирование фундаментальной матрицы без новой идеи.

## Изменения политики

В `clusters.yaml` обновлены `goal`, `duplicate_signals`, `canonical_solution_plan`, `allowed_variants`, `saturation_policy`, `deficit_policy`, `representative_card_ids` и `notes`.

Кластер оставлен в `watch`, но дефицит по базовой палитре понижен до `low`: теперь покрыты разные экзаменационные формы. Будущие добавления стоит делать только при новой идее, например потеря дифференцируемости по параметру или аккуратный негладкий пример.
