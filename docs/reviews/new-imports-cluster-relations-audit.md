# Аудит кластеров и связей свежих импортов

Дата: 2026-05-27.

Зона: `data/problems/olympiad/msu_ode_2025_2026/`, `data/problems/olympiad/msu_ode_2021_2024/`, свежие `data/problems/written_exam_import/**`, `data/problems/test_import/**`, а также существующие MSU ODE карточки только как якоря связей.

## Что добавлено в кластеры

Уже были подхвачены предыдущими импортными проходами:

| карточки | кластер |
| --- | --- |
| `msu-ode-2021-2-nonextendable-blowup-coordinates` | `existence-uniqueness-continuation` |
| `msu-ode-2021-5-inhomogeneous-second-order-span`, `msu-ode-2024-6-variable-coeff-characteristic-root` | `linear-equations-variable-coefficients` |
| `msu-ode-2024-1-integrating-factor-sine-log` | `integrating-factor-exact-forms` |
| `msu-ode-2024-8-trace-average-bounded-change` | `matrix-exponential-methods` |
| `test-implicit-*` | `implicit-ode-discriminant` |
| `test-limit-cycles-*` | `limit-cycles-qualitative-criteria` |

В этом проходе добавлены точные попадания:

| карточка | кластер(ы) |
| --- | --- |
| `msu-ode-2025-3-gyroscopic-stabilization` | `constant-coefficient-linear-systems`, `phase-line-stability` |
| `msu-ode-2025-7-superstable-second-order-impossible` | `phase-line-stability` |
| `msu-ode-2026-3-decoupled-phase-curves-count` | `phase-line-stability` |
| `msu-ode-2026-5-polar-stable-not-asymptotic` | `phase-line-stability`, `limit-cycles-qualitative-criteria` |
| `msu-ode-2026-6-singular-linear-system-epsilon` | `parameter-dependence-variational-equation` |
| `written-mipt-1998-bounded-linear-halfline` | `linear-first-order-ode`, `variation-of-constants` |
| `written-mipt-1998-lines-distance-one-envelope` | `recover-ode-from-family`, `implicit-ode-discriminant` |
| `written-mipt-2000-cauchy-p-of-y-guess` | `nonlinear-second-order-order-reductions`, `guess-cauchy-solution-uniqueness` |
| `written-mipt-2000-cauchy-log-derivative` | `nonlinear-second-order-order-reductions` |
| `written-mipt-2002-v1-nonlinear-p-of-y-cauchy` | `nonlinear-second-order-order-reductions` |
| `written-mipt-2002-v4-implicit-log-singular` | `implicit-ode-discriminant` |
| `written-mipt-2003-v1-pde-circle-characteristics` | `pde-characteristics-first-order` |
| `written-mipt-2003-v2-invariant-derivative-cauchy` | `nonlinear-second-order-order-reductions` |
| `written-mipt-2009-91-pde-positive-characteristics` | `pde-characteristics-first-order` |
| `written-mipt-2009-92-airy-bounded-positive-axis` | `energy-estimates-second-order-ode` |
| `written-mipt-2010-01-matrix-sine-spectrum` | `matrix-exponential-methods` |

## Новый кластер

Создан `nonlinear-second-order-order-reductions`.

Причина: свежие письменные задачи МФТИ 2000-2003 образуют устойчивый небольшой класс: нелинейное ОДУ второго порядка понижается до первого порядка через `p=p(y)`, логарифмическую производную `y'/y` или специальный инвариант вроде `y'/y^2`. До этого эти карточки были связаны точечно с локальными задачами, но не имели собственного дедупликационного контейнера.

Представители: `local-du-written-2024-nonlinear-p-of-y`, `local-du-written-2014-51-nonlinear-cauchy-total-derivative`, `written-mipt-2000-cauchy-p-of-y-guess`, `written-mipt-2002-v1-nonlinear-p-of-y-cauchy`, `written-mipt-2000-cauchy-log-derivative`, `written-mipt-2003-v2-invariant-derivative-cauchy`.

## Добавленные связи

MSU 2025/2026:

- `msu-ode-2025-2-min-order-polynomial-solutions` -> `msu-ode-2021-5-inhomogeneous-second-order-span`: общий ход через размерность пространства решений.
- `cluster-phase-stability-linear-plane-classification` -> `msu-ode-2025-3-gyroscopic-stabilization`: прямое применение следа/определителя.
- `local-du-programs-other-years-riccati-global-continuation` -> `msu-ode-2025-6-global-matrix-riccati-invertible`: контраст скалярного барьерного Риккати и матричной линеаризации через обратную матрицу.

Письменные импорты:

- `written-mipt-2000-cauchy-p-of-y-guess` -> `written-mipt-2002-v1-nonlinear-p-of-y-cauchy`: близкая редукция `p=p(y)`, но не дубль.
- `written-mipt-1998-lines-distance-one-envelope` -> `written-mipt-2002-v4-implicit-log-singular`: общий механизм параметра наклона, дискриминанта и огибающей.
- `written-mipt-2000-cauchy-log-derivative` -> `written-mipt-2003-v2-invariant-derivative-cauchy`: соседние инварианты производной для понижения порядка.
- `written-mipt-2003-v1-pde-circle-characteristics` -> `written-mipt-2009-91-pde-positive-characteristics`: общий метод характеристик для линейного ЧП первого порядка.
- `written-mipt-2010-01-matrix-sine-spectrum` -> `msu-ode-2024-8-trace-average-bounded-change`: контраст двух determinant-level матричных инвариантов.

## Оставлены уникальными

- `msu-ode-2025-2-min-order-polynomial-solutions`: близка к `recover-ode-from-family` и MSU 2021/5 по размерностному счету, но не является восстановлением ОДУ по семейству кривых в прямом смысле. Оставлена без cluster representative, связана relation.
- `msu-ode-2025-6-global-matrix-riccati-invertible`: точного кластера для матричных Riccati-трюков нет; связь с матричной экспонентой и скалярным Риккати оставлена через relations.

## Дубли и почти дубли

Удалять ничего не предлагаю.

Почти-дубли, требующие только редакторского наблюдения:

- `written-mipt-2000-cauchy-p-of-y-guess` и `written-mipt-2002-v1-nonlinear-p-of-y-cauchy`: один метод `p=p(y)`, но разная роль начальных данных и разная редукция после перехода.
- `written-mipt-1998-lines-distance-one-envelope` и `written-mipt-2002-v4-implicit-log-singular`: обе про неявное уравнение и огибающую, но первая строит уравнение по геометрическому семейству прямых, вторая исследует готовое логарифмическое `F(x,y,p)=0`.
- `written-mipt-2003-v1-pde-circle-characteristics` и `written-mipt-2009-91-pde-positive-characteristics`: общий метод характеристик, но разные размерности характеристической системы и геометрия данных.

## Проверки

Запущенный набор:

```powershell
python tools/build_index.py
python tools/validate.py
python tools/check_links.py
python tools/check_clusters.py
python tools/check_encoding.py
python tools/build_viewer.py
```

Результат: все проверки прошли. `build_index.py` записал `index/generated.json` с 386 карточками; `validate.py` подтвердил 386 карточек, 579 связей и 41 источник; `check_clusters.py` подтвердил 34 кластера. Viewer регенерирован после обновления индекса.
