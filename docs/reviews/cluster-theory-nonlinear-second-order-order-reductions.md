# Теоретико-методический блок: nonlinear-second-order-order-reductions

Дата: 2026-05-27. Зона: `nonlinear-second-order-order-reductions` - нелинейные ОДУ второго порядка и понижение порядка.

## Что добавлено

- `data/problems/cluster_audit/nonlinear_second_order_order_reductions/cluster-nonlinear-second-order-order-reductions-method-guide.yaml`.
- `data/import_batches/cluster-nonlinear-second-order-order-reductions.yaml`.
- `data/relations/relations.d/cluster-nonlinear-second-order-order-reductions.yaml`.
- Новый representative id добавлен в `data/task_clusters/clusters.yaml`.

## Покрытие

Карточка закрывает методический минимум кластера:

- отсутствие `y` явно: замена `p(x)=y'`, редуцированная задача для `p`, восстановление `y`;
- отсутствие `x` явно: замена `p(y)=y'`, формула `y''=p dp/dy`;
- автономные и квазиконсервативные формы `y''=f(y)`, `y''+V'(y)=0`;
- энергия как первый интеграл `p^2/2+V(y)=C`;
- перенос начальных условий в `p(x0)` или `p(y0)`;
- выбор знака ветви после перехода от `p^2` к `p`;
- потеря ветвей при делении на `p`, `y'`, `y` или другой множитель.

## Definition ids

Новые определения не добавлялись. Использованы существующие `definition_ids`:

`ordinary_differential_equation`, `solution`, `initial_value_problem`, `cauchy_problem`, `maximal_solution`, `autonomous_equation`, `first_integral`, `phase_trajectory`, `separable_equation`, `linear_first_order_equation`, `equilibrium`.

## Relations

Добавлены связи к representative-задачам кластера:

- `local-du-written-2024-nonlinear-p-of-y`;
- `local-du-written-2014-51-nonlinear-cauchy-total-derivative`;
- `written-mipt-2000-cauchy-p-of-y-guess`;
- `written-mipt-2002-v1-nonlinear-p-of-y-cauchy`;
- `written-mipt-2000-cauchy-log-derivative`;
- `written-mipt-2003-v2-invariant-derivative-cauchy`.

Соседние кластеры связаны через их representatives:

- `energy-estimates-second-order-ode`: `energy-integral-oscillator`, `oral-exam-excellent-duffing-energy-periodic`;
- `separable-homogeneous-first-order`: `separable-logistic-equation`, `oral-above-three-homogeneous-ratio-substitution`;
- `first-integrals-plane-systems`: `cluster-first-integrals-plane-systems-method-guide`, `cluster-phase-stability-first-integral-center`.

## Границы

Блок не заменяет `energy-estimates-second-order-ode`: если задача состоит только в знаке `E'`, запрете периодичности или априорной оценке, она остается энергетической. Он не заменяет `separable-homogeneous-first-order`: разделение переменных может быть финальным шагом после редукции, но не является диагностикой второго порядка. Он не заменяет `first-integrals-plane-systems`: энергия здесь выводится из редукции, а фазовая геометрия уровней остается соседним слоем.

## Проверки

Запущены после добавления:

- `python tools/build_index.py` - OK, собрано 418 карточек.
- `python tools/validate.py` - OK, 418 карточек, 846 relations, 49 sources.
- `python tools/check_links.py` - OK.
- `python tools/check_encoding.py` - OK.
- `python tools/check_clusters.py` - OK, 34 task clusters.
- `python tools/build_viewer.py` - OK, обновлены `viewer/index.html` и `index.html`.
- `python tools/audit_rules.py` - OK с 4 предупреждениями по уже существующим карточкам вне зоны этого кластера: `local-du-written-2014-51-characteristics-pde`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2014-51-lagrange-singular-curves`, `local-du-written-2024-variational-free-endpoint`.
