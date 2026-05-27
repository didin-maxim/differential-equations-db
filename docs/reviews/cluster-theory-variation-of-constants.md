# Теоретико-методический блок: variation-of-constants

Дата: 2026-05-27.

Зона: кластер `variation-of-constants` - вариация постоянных для неоднородных линейных ОДУ и систем.

## Что добавлено

- Создана карточка `cluster-variation-of-constants-method-guide` в `data/problems/cluster_audit/variation_of_constants/`.
- Карточка помечена как `theorem`, `task_cluster`, `method_guide`, `cluster_representative`.
- В `data/task_clusters/clusters.yaml` карточка добавлена первым representative для `variation-of-constants`.
- Создан batch `data/import_batches/cluster-variation-of-constants.yaml`.
- Создан слой связей `data/relations/relations.d/cluster-variation-of-constants.yaml`.

## Покрытие

- вариация постоянной для `y'+p(x)y=q(x)` как форма интегрирующего множителя;
- вариация параметров для уравнений высших порядков через ФСР и Вронскиан;
- формула Коши для систем `x'=A(t)x+b(t)`;
- фундаментальная матрица и матрица перехода `Phi(t,s)=X(t)X(s)^{-1}`;
- постояннокоэффициентный случай через `e^{A(t-s)}`;
- резонанс и появление множителей `t`, `t^2`, ... из интеграла;
- выбор между вариацией постоянных и методом неопределенных коэффициентов.

## Definition IDs

В карточке использованы существующие определения:

- `linear_first_order_equation`;
- `integrating_factor`;
- `linear_system`;
- `fundamental_matrix`;
- `wronskian`;
- `fundamental_system_solutions`;
- `particular_solution`;
- `general_solution`;
- `matrix_exponential`;
- `variation_of_constants_system`;
- `initial_value_problem`;
- `cauchy_problem`.

Новые определения не добавлялись: текущий слой `definitions.yaml` уже содержит нужные компактные id.

## Связи

Representative-связи добавлены к:

- `linear-first-order-formula`;
- `variation-of-parameters-sine`;
- `basic-mipt-variation-constants-ypp-plus-y`;
- `inhomogeneous-linear-system-variation`;
- `oral-exam-excellent-two-point-fundamental-matrix`;
- `constant-coeff-second-order-resonance`;
- `cluster-linear-systems-jordan-resonant-forcing`;
- `cluster-linear-variable-variation-parameters-fundamental-system`.

Соседние кластеры связаны через методические или representative-карточки:

- `linear-equations-variable-coefficients` через `cluster-linear-variable-method-guide`;
- `fundamental-matrix-linear-systems` через `waterloo-fundamental-matrix-flow-inverse`;
- `constant-coefficient-linear-systems` через `cluster-linear-systems-constant-coefficients-method-guide`;
- `matrix-exponential-methods` через `cluster-matrix-exponential-method-guide`.

## Остаточные границы

- Не добавлялась отдельная вычислительная задача на новую правую часть: кластер уже имеет representatives для скалярного второго порядка, систем, резонанса и двухточечной фундаментальной матрицы.
- Если новая задача проверяет только свойства `X(t)` или `e^{At}`, ее лучше держать в соседних кластерах фундаментальной матрицы или матричной экспоненты.
- Если постоянные коэффициенты и правая часть конечного типа дают короткий анзац, это не обязательно новый representative variation-of-constants.

## Проверки

Выполнены:

```powershell
python tools/build_index.py
python tools/validate.py
python tools/check_links.py
python tools/check_encoding.py
python tools/check_clusters.py
python tools/build_viewer.py
python tools/audit_rules.py
```

Результат:

- `build_index` - OK: 416 cards, обновлен `index/generated.json`;
- `validate` - OK: 416 cards, 823 relations, 49 sources;
- `check_links` - OK;
- `check_encoding` - OK;
- `check_clusters` - FAILED на уже существующем внешнем для этого блока representative id `cluster-nonlinear-second-order-order-reductions-method-guide`;
- `build_viewer` - OK, обновлены `viewer/index.html` и `index.html`;
- `audit_rules` - OK с 4 существующими предупреждениями про `exam_score tag with technical_score > 5`.
