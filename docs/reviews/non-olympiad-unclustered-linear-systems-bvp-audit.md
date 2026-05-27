# Аудит неолимпиадных задач вне кластеров: линейные ОДУ, системы, краевые задачи

Дата: 2026-05-27.

Область прохода: неолимпиадные problem-карточки во фрагментах `linear_equations`, `systems`, `boundary_value` и `series_methods`, если задача реально относится к линейным ОДУ. Кластерный слой рассматривался как `representative_card_ids` в `data/task_clusters/clusters.yaml`.

## Итог

До прохода в указанной области было 38 неолимпиадных задач вне всех кластеров.

После прохода в указанной области осталось 0 неолимпиадных задач вне кластеров.

Уникальных задач в этой области не оставлено: у каждой найден близкий методический родственник либо в уже существующем кластере, либо в одном из новых узких кластеров. Новые кластеры создавались только там, где было не меньше трех близких задач с общим планом решения.

Дополнительный проход по родственным связям: добавлен файл `data/relations/relations.d/non-olympiad-unclustered-linear-systems-bvp-audit.yaml` с глубокими связями именно по переносимым методам, а не по общей теме. Использованные механизмы: характеристический многочлен, резонансный подбор частного решения, вариация постоянных, фундаментальная матрица, формула Лиувилля, матричная экспонента, резонансная альтернатива, тождество Грина, энергетическая оценка, логарифмическая замена Эйлера и рекурсия степенного ряда.

Параллельно уже существующий кластер `energy-estimates-second-order-ode` учтен: энергетическая карточка `oral-exam-excellent-endpoint-combination-no-two-zeros` не получила отдельного конкурирующего энергетического кластера, а связана с ближайшими энергетическими и штурмовскими карточками.

## Новые кластеры

Создан `scalar-constant-coefficient-linear-ode`: скалярные линейные ОДУ с постоянными коэффициентами.

Представители:

- `resit-pass-3-constant-coeff-real-roots`
- `resit-pass-3-undetermined-coefficients`
- `weak-pass-resonance-double-root`
- `constant-coeff-second-order-resonance`
- `euler-cauchy-equation`
- `local-du-written-2014-51-constant-coeff-third-order`
- `local-du-written-2020-parameter-limit-modes`
- `local-du-programs-other-years-bounded-periodic-oscillator`
- `local-du-written-2022-inverse-square-change`
- `mit-18034-pset03-resonance-limit`
- `waterloo-second-order-pq-stability`
- `waterloo-critical-damping-crossing-condition`

Основание: общий механизм через характеристический многочлен, кратность корней, резонанс правой части, устойчивость/ограниченность по корням или замену, сводящую задачу к постоянным коэффициентам. Это не дубль `constant-coefficient-linear-systems`, потому что там объектом является матрица и спектр системы.

Создан `linear-bvp-solvability-resonance`: разрешимость линейных краевых задач и резонанс.

Представители:

- `shooting-linear-bvp`
- `resit-pass-3-dirichlet-sine-bvp`
- `local-du-filippov-763-dirichlet-resonance-no-solution`
- `trench-bvp-dirichlet-resonance-sine-condition`
- `trench-bvp-resonance-solvability-alternative`
- `oral-exam-excellent-two-point-fundamental-matrix`

Основание: общий план через конечномерное условие разрешимости, параметр стрельбы, ранг двухточечных условий или условие совместности в резонансном случае. Это сосед, а не замена для `boundary-spectral-problems` и `green-functions-bvp`.

Создан `fundamental-matrix-linear-systems`: фундаментальная матрица линейной системы.

Представители:

- `oral-above-three-fundamental-matrix-change-basis`
- `oral-above-three-liouville-area-preservation`
- `oral-exam-excellent-trace-zero-no-total-decay`
- `oral-exam-excellent-two-point-fundamental-matrix`
- `local-du-filippov-132-linear-stability-translation`
- `local-du-written-2016-global-first-integrals-source`
- `mit-18034-pset07-euler-system-fundamental-matrix`
- `waterloo-fundamental-matrix-flow-inverse`

Основание: общий объект `X(t)`: замена базиса решений, формула Лиувилля, перенос свойств между решениями, двухточечные условия через фундаментальную матрицу. Кластер не забирает чистую классификацию фазовых портретов и не заменяет кластер Флоке.

Создан `power-series-linear-ode`: степенные ряды для линейных ОДУ.

Представители:

- `power-series-airy-at-zero`
- `weak-pass-series-first-coefficients`
- `mipt-middle-power-series-recurrence`
- `regular-singular-euler-frobenius`

Основание: общий механизм подстановки степенного ряда или ряда Фробениуса, рекурсия для коэффициентов и индикаторное уравнение. Кластер намеренно малый: дальше добавлять только задачи с новой идеей, а не с большим числом коэффициентов.

## Добавлено в существующие кластеры

В `linear-first-order-ode` добавлена:

- `oral-middle-linear-first-order-resonance`

В `variation-of-constants` добавлены:

- `basic-mipt-variation-constants-ypp-plus-y`
- `oral-exam-excellent-two-point-fundamental-matrix`

В `constant-coefficient-linear-systems` добавлены:

- `oral-middle-triangular-system-jordan`
- `local-du-written-2016-global-first-integrals-source`

В `matrix-exponential-methods` добавлены:

- `oral-middle-triangular-system-jordan`
- `local-du-written-2016-global-first-integrals-source`

В `simple-variational-calculus` добавлена:

- `mipt-excellent-legendre-violation-no-minimum`

В `boundary-spectral-problems` добавлены:

- `trench-bvp-euler-log-spectrum`
- `lebl-diffyqs-weighted-sturm-exponential`

В `green-functions-bvp` добавлена:

- `trench-bvp-dirichlet-resonance-sine-condition`

В `sturm-oscillation-comparison` добавлена:

- `oral-exam-excellent-endpoint-combination-no-two-zeros`

В `floquet-periodic-linear-systems` добавлена:

- `mipt-excellent-periodic-system-resonant-monodromy`

В `parameter-dependence-variational-equation` добавлена:

- `mit-18034-pset03-resonance-limit`

Эта карточка отмечена в notes как пограничная: она про резонансный предел близких частот и близка к параметрической чувствительности, но не должна открывать массовый импорт parameter-adjacent задач без уравнения чувствительности.

В `phase-line-stability` добавлены:

- `waterloo-second-order-pq-stability`
- `waterloo-critical-damping-crossing-condition`

## Уникальные задачи

В рамках указанной области уникальных задач не оставлено. Причина: найденные orphan-карточки образовали четыре методически связных группы, а остальные были точными попаданиями в уже существующие кластеры.

Поэтому отдельного списка "оставлена уникальной" нет. Для проверки близости были просмотрены ближайшие representatives существующих кластеров `variation-of-constants`, `constant-coefficient-linear-systems`, `matrix-exponential-methods`, `boundary-spectral-problems`, `green-functions-bvp`, `sturm-oscillation-comparison`, `floquet-periodic-linear-systems`, `parameter-dependence-variational-equation`, `phase-line-stability`, а после параллельного изменения также `energy-estimates-second-order-ode`. Если связь была слабее общей темы и не давала переносимого метода, она не добавлялась.

## Добавленные родственные связи

Скалярные постоянные коэффициенты:

- `weak-pass-resonance-double-root` связан с `resit-pass-3-undetermined-coefficients` и `constant-coeff-second-order-resonance` по резонансному/нерезонансному подбору частного решения.
- `local-du-written-2014-51-constant-coeff-third-order` связан с `local-du-written-2020-parameter-limit-modes` по чтению мод из характеристического многочлена.
- `euler-cauchy-equation` связан с `local-du-written-2022-inverse-square-change` по замене независимой переменной к постоянным коэффициентам.
- `trench-bvp-euler-log-spectrum` связан с `euler-cauchy-equation` по логарифмической замене Эйлера.

Вариация постоянных и фундаментальная матрица:

- `variation-of-parameters-sine` связан с `basic-mipt-variation-constants-ypp-plus-y` по одной формуле вариации постоянных.
- `inhomogeneous-linear-system-variation` связан с `oral-exam-excellent-two-point-fundamental-matrix` как подготовка к двухточечному условию через фундаментальную матрицу.
- `oral-above-three-fundamental-matrix-change-basis` связан с `waterloo-fundamental-matrix-flow-inverse` по фундаментальной матрице как оператору потока.
- `oral-above-three-liouville-area-preservation` связан с `oral-exam-excellent-trace-zero-no-total-decay` и `cluster-matrix-exp-det-trace-shortcut` по trace/determinant механизму.
- `local-du-filippov-132-linear-stability-translation` связан с `oral-exam-excellent-trace-zero-no-total-decay` как контраст двух линейных механизмов: разность решений против определителя фундаментальной матрицы.

Матричная экспонента и системы:

- `oral-middle-triangular-system-jordan` связан с `linear-system-jordan-block` по жорданову множителю `t`.
- `local-du-written-2016-global-first-integrals-source` связан с `cluster-matrix-exp-det-trace-shortcut` по чтению вронскиана и инвариантов из `e^{tA}`.

Краевые задачи, резонанс и функции Грина:

- `local-du-filippov-763-dirichlet-resonance-no-solution` связан с `trench-bvp-dirichlet-resonance-sine-condition` по резонансной альтернативе.
- `trench-bvp-dirichlet-resonance-sine-condition` связан с `trench-bvp-resonance-solvability-alternative` как частный случай и с `trench-bvp-green-identity-self-adjoint-boundary` через тождество Грина.
- `shooting-linear-bvp` связан с `oral-exam-excellent-two-point-fundamental-matrix` как одномерная стрельба против матричного двухточечного условия.

Энергетические и штурмовские оценки:

- `oral-exam-excellent-endpoint-combination-no-two-zeros` связан с `local-du-8-t3-nonpositive-q-bvp-sturm` по энергетическому доказательству запрета двух нулей.
- `oral-exam-excellent-endpoint-combination-no-two-zeros` связан с `local-du-8-t2-exponential-coefficient-energy-bound` как родственный энергетический метод второго порядка.

Спектральные и степенные методы:

- `lebl-diffyqs-weighted-sturm-exponential` связан с `trench-bvp-weighted-orthogonality` по самосопряженной весовой форме.
- `power-series-airy-at-zero`, `weak-pass-series-first-coefficients` и `mipt-middle-power-series-recurrence` связаны по рекурсии степенного ряда.
- `regular-singular-euler-frobenius` связан с `euler-cauchy-equation` как обобщение индикаторного уравнения.

## Ограничения прохода

Не трогались олимпиадные задачи, даже если они лежат рядом тематически.

Не создавался широкий кластер "линейные ОДУ вообще": для базы полезнее узкие кластеры по рабочему механизму.

Не удалялись карточки и не менялись сами условия/решения задач.
