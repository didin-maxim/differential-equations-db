# Теоретико-методический блок scalar-constant-coefficient-linear-ode

Дата прохода: 2026-05-27. Зона: `scalar-constant-coefficient-linear-ode`.

## Что добавлено

- Создана карточка `cluster-scalar-constant-coefficients-method-guide` в `data/problems/cluster_audit/scalar_constant_coefficient_linear_ode/`.
- Карточка помечена как `theorem` + `task_cluster`, `method_guide`, `cluster_representative`.
- ID блока добавлен в `representative_card_ids` кластера `scalar-constant-coefficient-linear-ode`, поэтому блок находится через кластерный слой и индексируется вместе с representative-задачами.
- Добавлен файл relations `data/relations/relations.d/cluster-scalar-constant-coefficient-linear-ode.yaml`.

## Покрытые методы

- Характеристический многочлен `P(lambda)` для скалярного оператора `P(D)`.
- Простые, кратные и комплексные корни; вещественная форма решений.
- ФСР, линейная независимость, вронскиан, общее решение однородного уравнения.
- Неоднородные уравнения с квазимногочленной правой частью: полиномы, экспоненты, синусы/косинусы и произведения с полиномами.
- Резонанс и множитель `t^s` по кратности соответствующего характеристического корня.
- Аннигилятор и метод неопределенных коэффициентов как короткий маршрут для конечномерных классов правых частей.
- Связь с вариацией постоянных и переходом к системе первого порядка через companion-матрицу.

## Definition IDs и связи

В карточку добавлены `definition_ids` без дублирования текстов из `data/definitions/definitions.yaml`:

- `ordinary_differential_equation`, `solution`;
- `initial_value_problem`, `cauchy_problem`;
- `linear_first_order_equation` как ближайшее существующее определение линейного scalar-уравнения;
- `linear_system` для системной формы;
- `wronskian`, `linear_independence_solutions`, `fundamental_system_solutions`;
- `general_solution`, `particular_solution`.

Relations добавлены к:

- базовым теоретическим карточкам `picard-lindelof-theorem`, `liouville-wronskian-formula`;
- representative-задачам на вещественные корни, неопределенные коэффициенты, двойной резонанс, резонанс второго порядка, третий порядок, параметрические моды и ограниченно-периодический осциллятор;
- соседним методическим блокам `cluster-linear-systems-constant-coefficients-method-guide`, `cluster-linear-variable-method-guide`;
- соседним вычислительным представителям `variation-of-parameters-sine`, `inhomogeneous-linear-system-variation`.

## Источники

В принятом формате подключены 6 источников:

- `src-local-du-8-program-or-exam`;
- `src-mipt-ode-course`;
- `src-romanko-problem-book`;
- `src-filippov-problem-book`;
- `src-coddington-levinson`;
- `src-mit-1803sc-ode`.

## Оставшиеся пробелы

- В `data/definitions/definitions.yaml` нет отдельного общего определения "линейное ОДУ n-го порядка"; блок использует существующие определения и не добавляет новое, чтобы не дублировать слой definitions.
- Аннигилятор описан как методический маршрут, но не выделен отдельной теоремой-карточкой; это можно сделать позже, если появится несколько задач, где именно аннигилятор является главным объектом.
- Не добавлялись новые однотипные вычислительные задачи: текущие representatives уже покрывают основные ветки кластера.
