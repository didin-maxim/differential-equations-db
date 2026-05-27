# Теоретико-методический блок: linear-first-order-ode

Дата: 2026-05-27.

Зона: кластер `linear-first-order-ode` — линейное ОДУ первого порядка. Новые шаблонные задачи вида `y'+p(x)y=q(x)` не добавлялись.

## Что добавлено

- Добавлена карточка `cluster-linear-first-order-method-guide` как отдельный теоретико-методический навигатор кластера.
- Карточка помечена как `theorem` с `task_cluster`, `method_guide`, `cluster_representative`, поэтому индексируется как теоретический методический блок и подключена первым representative в `data/task_clusters/clusters.yaml`.
- Усилена базовая теорема `linear-first-order-formula`: добавлены `definition_ids` для ОДУ, решения, линейного уравнения первого порядка, интегрирующего множителя, общего/частного решения, задачи Коши и интегральной кривой; идея и профиль метода исправлены на `integrating_factor_linear`.
- Добавлен файл relations `data/relations/relations.d/cluster-linear-first-order-ode.yaml` с 12 связями от методического блока к базовой формуле, representative-задачам и соседним методам.

## Покрытые методы и акценты

- Стандартная форма `y'+p(x)y=q(x)` на рабочем промежутке непрерывности коэффициентов.
- Интегрирующий множитель `mu=exp(int p)` и свертка `(mu y)'=mu q`.
- Формула общего решения и формула задачи Коши с нижним пределом `x0`.
- Роль начального условия, периодического условия, двухточечного/краевого условия и ограниченности на полуоси как условий на константу.
- Область определения: разрывы коэффициентов, нули старшего коэффициента, ограничения после деления и замен.
- Содержательные границы с `integrating-factor-exact-forms`, `riccati-bernoulli-reductions` и `separable-homogeneous-first-order`.
- Геометрическое чтение семейства интегральных кривых как частное решение плюс однородная часть.

## Источники

В карточке использованы существующие source ids в принятом формате:

- `src-local-du-8-program-or-exam`
- `src-mipt-ode-course`
- `src-romanko-problem-book`
- `src-filippov-problem-book`
- `src-mit-1803sc-ode`
- `src-lebl-diffyqs`

## Связи

Добавлены связи к representative-задачам:

- `linear-first-order-formula`
- `weak-pass-linear-method-choice`
- `resit-pass-3-linear-first-order-forcing`
- `oral-middle-linear-first-order-resonance`
- `periodic-linear-equation-zero-mean`
- `written-mipt-1998-bounded-linear-halfline`
- `waterloo-singular-linear-qualitative-sketch`
- `putnam-early-1954-i3-concurrent-tangents`

Добавлены содержательные соседние связи:

- contrast с `cluster-integrating-factor-exact-forms-method-guide`;
- teaches_before к `bernoulli-standard` и `riccati-known-solution` только как к линейному этапу после замены;
- contrast с `homogeneous-first-order-substitution`.

## Оставшиеся пробелы

- Нет отдельной карточки на общую линейную периодическую задачу при `mu(T)!=1`; сейчас есть представитель нулевого среднего/совместимости.
- Нет отдельного representative для параметрической краевой задачи первого порядка, где меняется существование решения на отрезке.
- Нужна будущая ручная сверка локаторов по Романко/Филиппову, если база перейдет от seed/source_verified к точным страницам и номерам.

## Проверки

Финальный прогон:

- `python tools/build_index.py` — OK, 412 cards; индекс содержит `cluster-linear-first-order-method-guide` и representative-связь с `linear-first-order-ode`.
- `python tools/validate.py` — OK, 412 cards, 781 relations, 49 sources.
- `python tools/check_links.py` — OK.
- `python tools/check_encoding.py` — OK.
- `python tools/check_clusters.py` — OK, 34 task clusters.
- `python tools/build_viewer.py` — OK, пересобраны `viewer/index.html` и `index.html`.
- `python tools/audit_rules.py --max-items 80` — OK с 4 предупреждениями по уже существующим карточкам вне зоны `linear-first-order-ode`: `local-du-written-2014-51-characteristics-pde`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2014-51-lagrange-singular-curves`, `local-du-written-2024-variational-free-endpoint`.
