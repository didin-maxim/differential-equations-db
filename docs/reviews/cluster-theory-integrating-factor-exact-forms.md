# Теоретико-методический блок кластера `integrating-factor-exact-forms`

Дата: 2026-05-27.

## Что добавлено

- Добавлена карточка `cluster-integrating-factor-exact-forms-method-guide` в `data/problems/cluster_audit/integrating_factor_exact_forms/`.
- Карточка помечена как теоретико-методический блок: `kind.primary=theorem`, `kind.secondary=[task_cluster, method_guide, cluster_representative]`, теги `task_cluster` и `cluster_representative`.
- В `data/task_clusters/clusters.yaml` карточка добавлена в `representative_card_ids` кластера `integrating-factor-exact-forms`.
- В `data/relations/relations.d/cluster-integrating-factor-exact-forms.yaml` добавлены связи от методического блока к representative-задачам и содержательным соседям.

## Покрытые методы

- Критерий точности формы `M dx + N dy`: `M_y=N_x`.
- Восстановление потенциала `F`: сначала интегрирование по одной переменной, затем подбор функции другой переменной.
- Интегрирующий множитель `mu(x)` через критерий `(M_y-N_x)/N=f(x)`.
- Интегрирующий множитель `mu(y)` через критерий `(N_x-M_y)/M=g(y)`.
- Однородные формы и множитель `1/(xM+yN)` на допустимой области.
- Специальные анзацы `h(xy)`, `h(y/x)` и степенной множитель `x^a y^b` как прямое применение условия `(mu M)_y=(mu N)_x`.
- Выбор вида множителя без тяжелых первообразных: сначала смотреть на зависимость от одной переменной, однородность, мономные степени и выражения через `xy` или `y/x`.
- Домены, компоненты области, нули множителя и потеря решений при делении или умножении.

## Определения и источники

Новые определения не добавлялись. В карточке проставлены `definition_ids`: `exact_equation`, `integrating_factor`, `first_integral`, `general_solution`, `particular_solution`, `integral_curve`, `initial_value_problem`, `cauchy_problem`, а также базовые `ordinary_differential_equation` и `solution`.

В методическом блоке указаны 6 источников в принятом формате: локальный курс МФТИ, Романко, Филиппов, Арнольд, MIT OCW 18.03SC и Lebl Diffy Qs.

## Связи

Добавлены relations от методического блока к:

- `exact-equation-potential` как базовой точной форме;
- `oral-above-three-integrating-factor-x-only` и `cluster-integrating-factor-mu-y-short` как веткам `mu(x)` и `mu(y)`;
- `integrating-factor-y`, `cluster-integrating-factor-power-monomial`, `cluster-integrating-factor-mu-xy` как однородному, степенному и специальному множителям;
- `msu-ode-2024-1-integrating-factor-sine-log` как задаче про потерянное решение после деления;
- `msu-ode-2008-11-integrating-factor-family` как обобщению про все множители через первый интеграл;
- `linear-first-order-formula`, `homogeneous-first-order-substitution`, `orthogonal-trajectories-circles` как содержательным соседним кластерам, где методы похожи, но цель другая.

## Оставшиеся пробелы

- Нет отдельной общей теоремной карточки только про локальную точность замкнутой 1-формы на односвязной области; сейчас это покрыто методическим блоком и определением `exact_equation`.
- Нет отдельного representative для множителя `h(y/x)`; добавлять стоит только если будет короткий пример с новой диагностикой, а не длинным интегралом.
- Источники Романко/Филиппов/локальная программа подключены на уровне методического блока; точные локаторы по параграфам можно уточнить при отдельной библиографической сверке.
