# Теоретико-методический блок: linear-bvp-solvability-resonance

Дата прохода: 2026-05-27. Зона: `linear-bvp-solvability-resonance`.

## Что добавлено

- Создана карточка `cluster-linear-bvp-solvability-resonance-method-guide` в `data/problems/cluster_audit/linear_bvp_solvability_resonance/`.
- Карточка помечена как `kind.primary = theorem`, `kind.secondary = task_cluster, method_guide, cluster_representative, theory_bridge`.
- Карточка добавлена в representatives кластера `linear-bvp-solvability-resonance`.
- Добавлен batch `data/import_batches/cluster-linear-bvp-solvability-resonance.yaml`.
- Добавлен отдельный файл связей `data/relations/relations.d/cluster-linear-bvp-solvability-resonance.yaml`.
- В `definition_ids` использованы существующие определения: `boundary_value_problem`, `eigenvalue_problem`, `eigenvalue_of_boundary_value_problem`, `fundamental_system_solutions`, `wronskian`, `green_function_bvp`, `self_adjoint_boundary_problem`, `fredholm_alternative`, `linear_system`, `fundamental_matrix`.

## Покрытые методы

- Диагностика однородной краевой задачи: нулевое ядро против резонанса.
- Резонанс как потеря единственности и появление условия совместности.
- Ортогональность правой части к сопряженному ядру; самосопряженный случай как `int f phi = 0`.
- Учебная альтернатива Фредгольма без лишнего функционального анализа.
- Линейно-алгебраическая форма через фундаментальную матрицу и образ матрицы двухточечного условия.
- Связь с функцией Грина: обычное Green-ядро существует на нерезонансной стороне.
- Связь с собственными значениями: резонанс возникает при попадании в спектр однородной BVP, но вычисление спектра остается в `boundary-spectral-problems`.
- Связь со Штурмом: сравнение и дисконъюгированность используются только как способ доказать нулевое ядро.
- Связь с вариационными задачами: уравнение Якоби и вторая вариация приводят к той же проверке линейной BVP.

## Relations

Добавлены связи от `cluster-linear-bvp-solvability-resonance-method-guide` к representative-задачам и соседям:

- `shooting-linear-bvp`;
- `resit-pass-3-dirichlet-sine-bvp`;
- `local-du-filippov-763-dirichlet-resonance-no-solution`;
- `trench-bvp-dirichlet-resonance-sine-condition`;
- `trench-bvp-resonance-solvability-alternative`;
- `local-du-standard-resonant-linear-bvp-solvability`;
- `oral-exam-excellent-two-point-fundamental-matrix`;
- `cluster-boundary-spectral-method-guide`;
- `dirichlet-eigenvalues-interval`;
- `cluster-green-functions-bvp-method-guide`;
- `trench-bvp-green-function-formula`;
- `cluster-sturm-method-guide`;
- `cluster-sturm-dirichlet-nonresonance-interpolation-lemma`;
- `cluster-variational-method-guide`;
- `local-du-standard-legendre-jacobi-conditions`.

## Границы кластера

- `boundary-spectral-problems`: если цель - найти собственные значения или собственные функции.
- `green-functions-bvp`: если главный объект - построить кусочную функцию Грина.
- `sturm-oscillation-comparison`: если главный вопрос - нули, сравнение, дисконъюгированность или осцилляция.
- `simple-variational-calculus`: если линейная BVP появляется как следствие вариационной постановки, а центральная цель - экстремаль или знак второй вариации.

## Проверки

Выполнен полный требуемый набор:

```powershell
python tools\build_index.py
python tools\validate.py
python tools\check_links.py
python tools\check_encoding.py
python tools\check_clusters.py
python tools\build_viewer.py
python tools\audit_rules.py --max-items 80
```

Результат:

- `build_index.py` - OK, индекс пересобран, 421 карточка.
- `validate.py` - FAILED на чужой зоне `data/problems/cluster_audit/integral_equation_to_ode/cluster-integral-equation-to-ode-method-guide.yaml`: неизвестные definition_ids `integral_equation`, `volterra_integral_equation`, `fredholm_integral_equation`.
- `check_links.py` - FAILED по той же чужой зоне `integral_equation_to_ode`; ошибок по `linear-bvp-solvability-resonance` нет.
- `check_encoding.py` - OK.
- `check_clusters.py` - OK: 34 task clusters.
- `build_viewer.py` - OK, пересобраны `viewer/index.html` и корневой `index.html`.
- `audit_rules.py --max-items 80` - OK с 4 существующими предупреждениями вне зоны `linear-bvp-solvability-resonance`: `local-du-written-2014-51-characteristics-pde`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2014-51-lagrange-singular-curves`, `local-du-written-2024-variational-free-endpoint`.

Дополнительно проверено по `index/generated.json`: `cluster-linear-bvp-solvability-resonance-method-guide` попал в индекс, имеет `method_guide`, `cluster_representative`, definition_ids и связи с representative-задачами/соседними кластерами.
