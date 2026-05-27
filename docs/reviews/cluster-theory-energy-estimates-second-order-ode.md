# Теоретико-методический блок: energy-estimates-second-order-ode

Дата: 2026-05-27

## Что добавлено

- Создана карточка `cluster-energy-estimates-second-order-method-guide`.
- Карточка помечена как `theorem`, `method_guide`, `task_cluster`, `cluster_representative`.
- Добавлен batch `data/import_batches/cluster-energy-estimates-second-order-ode.yaml`.
- Добавлены связи `data/relations/relations.d/cluster-energy-estimates-second-order-ode.yaml`.
- Карточка добавлена в `representative_card_ids` кластера `energy-estimates-second-order-ode`.

## Покрытие

Блок фиксирует переносимый метод: домножение на `y'`, энергия `T+V`, проверка знака `E'`, априорные оценки, ограниченность, запрет нетривиальной периодичности, краевые энергетические невозможности, связь с фазовой плоскостью, первыми интегралами и функциями Ляпунова.

## Definition IDs

Новые определения не вводились. Использованы существующие `definition_ids`: `ordinary_differential_equation`, `solution`, `autonomous_equation`, `first_integral`, `phase_trajectory`, `equilibrium`, `lyapunov_function`, `lyapunov_stability`, `asymptotic_stability`.

## Relations

Связи ведут к representative-задачам кластера: `energy-integral-oscillator`, `resit-pass-3-energy-oscillator-check`, `oral-exam-excellent-damped-periodic-zero`, `oral-exam-excellent-endpoint-combination-no-two-zeros`, `local-du-8-t2-exponential-coefficient-energy-bound`, `written-mipt-2009-92-airy-bounded-positive-axis`, `energy-no-nonconstant-decay-periodic`, `msu-ode-2003-3-bounded-exp-oscillator`.

Соседи связаны явно: `first-integrals-plane-systems`, `phase-line-stability`, `nonlinear-second-order-order-reductions`.

## Дедупликационная граница

Карточка не добавляет очередной осциллятор с другой первообразной. Она служит навигатором: сохраняющаяся энергия относится к первым интегралам и фазовым овалам, монотонная энергия относится к функциям Ляпунова и запретам возврата, а редукция `p=p(y)` остается соседним кластером понижения порядка.

## Проверки

Запущены `build_index`, `validate`, `check_links`, `check_encoding`, `check_clusters`, `build_viewer`, `audit_rules`.

Результат: `build_index`, `validate`, `check_links`, `check_encoding`, `build_viewer` прошли; `audit_rules` завершился штатно с уже имеющимися предупреждениями по exam_score/technical_score. `check_clusters` остановился на соседней незакрытой ссылке `cluster-nonlinear-second-order-order-reductions-method-guide` в кластере `nonlinear-second-order-order-reductions`; энергетический блок этой ошибкой не затронут.
