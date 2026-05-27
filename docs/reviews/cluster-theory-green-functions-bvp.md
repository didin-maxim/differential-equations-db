# Теоретико-методический блок: green-functions-bvp

Дата прохода: 2026-05-27. Зона: `green-functions-bvp`.

## Что добавлено

- Создана карточка `cluster-green-functions-bvp-method-guide` в `data/problems/cluster_audit/green_functions_bvp/`.
- Карточка помечена как `theorem`, `method_guide`, `task_cluster`, `cluster_representative`, `theory_bridge`.
- Добавлены определения `green_function_bvp`, `self_adjoint_boundary_problem`, `fredholm_alternative`.
- Добавлен batch `data/import_batches/cluster-green-functions-bvp.yaml`.
- Добавлен файл связей `data/relations/relations.d/cluster-green-functions-bvp.yaml`.
- Карточка добавлена в representatives кластера `green-functions-bvp`.

## Покрытие

- Построение функции Грина через левую и правую фундаментальные функции.
- Непрерывность ядра и скачок производной/потока.
- Проверка краевых условий по переменной `x`.
- Самосопряженность и симметрия ядра, где применимо.
- Резонанс, отсутствие обычного обратного Green-оператора и альтернатива Фредгольма.
- Диагностика случаев, где функция Грина избыточна по сравнению с прямым решением.

## Связи

- Representative-задачи: `trench-bvp-green-function-formula`, `trench-bvp-robin-green-kernel-example`, `trench-bvp-green-identity-self-adjoint-boundary`, `trench-bvp-resonance-solvability-alternative`, `trench-bvp-dirichlet-resonance-sine-condition`, `putnam-early-1963-a3-euler-operator-kernel`.
- Соседи: `cluster-boundary-spectral-method-guide`, `dirichlet-eigenvalues-interval`, `local-du-standard-resonant-linear-bvp-solvability`, `cluster-sturm-method-guide`, `cluster-sturm-dirichlet-nonresonance-interpolation-lemma`.

## Границы кластера

- `boundary-spectral-problems`: собственные значения, спектральная ортогональность и спектральная классификация.
- `linear-bvp-solvability-resonance`: условие совместности конкретной неоднородной BVP при резонансе.
- `sturm-oscillation-comparison`: нули, сравнение, дисконъюгированность и нерезонанс через запрет двух нулей.

## Проверки

- `python tools/build_index.py` - OK, индекс пересобран: 415 карточек.
- `python tools/validate.py` - OK: 415 карточек, 799 связей, 49 источников.
- `python tools/check_links.py` - OK.
- `python tools/check_encoding.py` - OK.
- `python tools/check_clusters.py` - FAILED на существующей вне зоны проблеме: `nonlinear-second-order-order-reductions` с отсутствующим representative `cluster-nonlinear-second-order-order-reductions-method-guide`.
- `python tools/build_viewer.py` - OK, пересобраны `viewer/index.html` и `index.html`.
- `python tools/audit_rules.py --max-items 80` - OK с 4 существующими предупреждениями вне зоны `green-functions-bvp`: `local-du-written-2014-51-characteristics-pde`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2014-51-lagrange-singular-curves`, `local-du-written-2024-variational-free-endpoint`.

Дополнительно проверено по `index/generated.json`: `cluster-green-functions-bvp-method-guide` попал в индекс, имеет `method_guide`, `cluster_representative`, новые definition_ids и связи с representatives/соседями.
