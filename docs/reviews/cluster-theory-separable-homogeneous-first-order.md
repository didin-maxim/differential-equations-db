# Теоретико-методический блок: separable-homogeneous-first-order

Дата: 2026-05-27.

Зона: кластер `separable-homogeneous-first-order` — разделение переменных и однородная замена первого порядка. Новые однотипные задачи на замену чисел или элементарные первообразные не добавлялись.

## Что добавлено

- Добавлена карточка `cluster-separable-homogeneous-method-guide` как отдельный теоретико-методический навигатор кластера.
- Карточка помечена как `theorem` с `task_cluster`, `method_guide`, `cluster_representative` и подключена первой representative-карточкой в `data/task_clusters/clusters.yaml`.
- Создан batch `data/import_batches/cluster-separable-homogeneous-first-order.yaml`, содержащий только методический блок.
- Расширен `data/relations/relations.d/cluster-separable-homogeneous-first-order.yaml`: добавлены связи от навигатора к representative-задачам и соседним методическим зонам.

## Покрытые методы и акценты

- Распознавание разделяющейся формы `y'=a(x)b(y)` и эквивалентной записи `A(x) dx+B(y) dy=0`.
- Потеря стационарных решений при делении на `b(y)`; равновесия выписываются до разделения переменных.
- Область определения и максимальный рабочий промежуток задачи Коши: запрещенные уровни, разрывы, логарифмы, корни и знаменатели.
- Однородная замена `y=xv`, формула `y'=v+xv'` и уравнение `xv'=Phi(v)-v`.
- Выбор рабочего промежутка `x>0` или `x<0`, а при особых отношениях `y/x` — выбор рабочего конуса/сектора.
- Потеря прямых решений `y=cx` при делении на `Phi(v)-v`.
- Связь логистического уравнения с фазовой прямой, равновесиями, монотонностью и простыми качественными выводами.
- Границы с `linear-first-order-ode`, `integrating-factor-exact-forms` и `orthogonal-trajectories`.

## Definition IDs

Использованы существующие определения без расширения `definitions.yaml`:

- `ordinary_differential_equation`
- `solution`
- `separable_equation`
- `initial_value_problem`
- `cauchy_problem`
- `maximal_solution`
- `general_solution`
- `particular_solution`
- `integral_curve`
- `autonomous_equation`
- `equilibrium`
- `phase_line`
- `linear_first_order_equation`
- `exact_equation`

## Связи

Добавлены связи к representative-задачам:

- `resit-pass-3-separable-exponential-growth`
- `separable-logistic-equation`
- `homogeneous-first-order-substitution`
- `oral-above-three-homogeneous-ratio-substitution`

Добавлены соседние связи:

- contrast с `cluster-linear-first-order-method-guide`;
- contrast с `cluster-integrating-factor-exact-forms-method-guide`;
- contrast с `orthogonal-trajectories-circles` как базовым representative соседнего кластера ортогональных траекторий.

## Оставшиеся пробелы

- Отдельная вычислительная карточка на потерянное стационарное решение при делении не добавлялась сознательно: методический блок закрывает этот риск без размножения шаблонных separable-задач.
- Отдельная вычислительная карточка на выбор конуса для однородного уравнения также не добавлялась: существующая устная representative-карточка уже показывает запретный уровень `y=0`, а навигатор фиксирует общий принцип.
- Если позже появится источник с неоднотипной задачей, где область/конус является главным вопросом, ее можно добавить как conceptual representative, а не как очередную замену чисел.

## Проверки

Финальный прогон:

- `python tools/build_index.py` — OK, индекс пересобран: 416 cards.
- `python tools/validate.py` — OK, 416 cards, 823 relations, 49 sources.
- `python tools/check_links.py` — OK.
- `python tools/check_encoding.py` — OK.
- `python tools/check_clusters.py` — FAIL вне зоны этого блока: `nonlinear-second-order-order-reductions` ссылается на неизвестный representative id `cluster-nonlinear-second-order-order-reductions-method-guide`. Этот кластер не относится к `separable-homogeneous-first-order` и не правился в рамках задачи.
- `python tools/build_viewer.py` — OK, пересобраны `viewer/index.html` и `index.html`.
- `python tools/audit_rules.py --max-items 80` — OK с 4 уже существующими предупреждениями вне зоны `separable-homogeneous-first-order`: `local-du-written-2014-51-characteristics-pde`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2014-51-lagrange-singular-curves`, `local-du-written-2024-variational-free-endpoint`.
