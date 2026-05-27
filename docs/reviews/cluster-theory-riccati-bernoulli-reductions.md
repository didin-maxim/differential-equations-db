# Теоретико-методический блок: riccati-bernoulli-reductions

Дата: 2026-05-27.

Зона: кластер `riccati-bernoulli-reductions` — редукции Риккати и Бернулли к линейным уравнениям. Новые вычислительные варианты Бернулли/Риккати не добавлялись.

## Что добавлено

- Создана карточка `cluster-riccati-bernoulli-method-guide` в `data/problems/cluster_audit/riccati_bernoulli_reductions/`.
- Карточка помечена как `theorem` + `task_cluster`, `method_guide`, `cluster_representative`.
- Карточка добавлена в representatives кластера `riccati-bernoulli-reductions`.
- Создан batch `data/import_batches/cluster-riccati-bernoulli-reductions.yaml`.
- Создан relations-файл `data/relations/relations.d/cluster-riccati-bernoulli-reductions.yaml`.

## Содержательное покрытие

- Бернулли: стандартная замена `z=y^{1-n}` после проверки допустимости деления на `y^n`.
- Риккати с известным частным решением: `y=y0+1/u` и линейное уравнение `u'+(2a y0+b)u=-a`.
- Риккати без данного частного решения: частное решение сначала надо угадать; иначе естественная полная линеаризация ведет к линейному уравнению второго порядка через логарифмическую производную.
- Потеря решений: нулевая ветвь Бернулли, отдельное решение `y0` в Риккати, полюса после обратной замены, рабочие интервалы и ветви степеней.
- Границы: прямой `linear-first-order-ode`, `separable-homogeneous-first-order`, `implicit-ode-discriminant`, матричное Риккати.

## Definition IDs

В карточке использованы существующие определения:

- `ordinary_differential_equation`, `solution`, `initial_value_problem`, `cauchy_problem`;
- `linear_first_order_equation`, `integrating_factor`;
- `general_solution`, `particular_solution`, `integral_curve`;
- `bernoulli_equation`, `riccati_equation`;
- `linear_system`, `discriminant_curve`.

Новые определения не добавлялись, чтобы не расширять общий слой терминов без необходимости.

## Relations

Добавлены связи от методического блока к representative-задачам:

- `bernoulli-standard`;
- `weak-pass-bernoulli-substitution`;
- `riccati-known-solution`;
- `oral-above-three-riccati-shift-known-solution`;
- `msu-ode-2013-9-riccati-inverse-square`;
- `putnam-early-1960-b7-riccati-variational`;
- `local-du-programs-other-years-riccati-global-continuation`.

Добавлены связи к соседним маршрутам:

- `cluster-linear-first-order-method-guide`;
- `homogeneous-first-order-substitution` как representative соседнего `separable-homogeneous-first-order`;
- `cluster-implicit-ode-discriminant-method-guide`;
- `msu-ode-2025-6-global-matrix-riccati-invertible` как граница с матричным Риккати.

## Дедупликационная политика

Кластер оставлен в режиме `watch`: базовые Bernoulli/Riccati representatives уже есть. Новые карточки стоит добавлять только при новой роли условия, качественной проверке, связи со вторым порядком или аккуратной области допустимости. Очередные варианты с заменой коэффициентов и тем же интегрирующим множителем не добавлять.

## Проверки

Финальный прогон выполнен после добавления карточки, batch, relations и отчета:

- `python tools/build_index.py` — OK, 418 cards.
- `python tools/validate.py` — OK, 418 cards, 846 relations, 49 sources.
- `python tools/check_links.py` — OK.
- `python tools/check_encoding.py` — OK.
- `python tools/check_clusters.py` — OK, 34 task clusters.
- `python tools/build_viewer.py` — OK, обновлены `viewer/index.html` и `index.html`.
- `python tools/audit_rules.py` — OK с 4 предупреждениями по существующим карточкам вне зоны `riccati-bernoulli-reductions`: `local-du-written-2014-51-characteristics-pde`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2014-51-lagrange-singular-curves`, `local-du-written-2024-variational-free-endpoint`.

Ошибки по зоне `riccati-bernoulli-reductions` отсутствуют.
