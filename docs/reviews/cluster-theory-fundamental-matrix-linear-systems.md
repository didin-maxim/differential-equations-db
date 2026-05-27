# Теоретико-методический блок: fundamental-matrix-linear-systems

Дата: 2026-05-27.

Зона: кластер `fundamental-matrix-linear-systems` - фундаментальная матрица линейной системы, матрица перехода и операторный язык линейного потока.

## Что добавлено

- Создана карточка `cluster-fundamental-matrix-method-guide` в `data/problems/cluster_audit/fundamental_matrix_linear_systems/`.
- Карточка помечена как `theorem`, `task_cluster`, `method_guide`, `cluster_representative`.
- В `data/task_clusters/clusters.yaml` карточка добавлена первым representative для `fundamental-matrix-linear-systems`.
- Создан batch `data/import_batches/cluster-fundamental-matrix-linear-systems.yaml`.
- Создан слой связей `data/relations/relations.d/cluster-fundamental-matrix-linear-systems.yaml`.

## Покрытие

- определение фундаментальной матрицы `X'=A(t)X`, `det X(t) != 0`;
- нормированная фундаментальная матрица `Phi(t,t0)` с `Phi(t0,t0)=I`;
- матрица перехода `Phi(t,s)=X(t)X(s)^{-1}` и ее независимость от выбора `X`;
- композиция, обратимость и обратный ход времени для `Phi(t,s)`;
- формула Коши для `x'=A(t)x+b(t)`;
- обратимость фундаментальной матрицы и формула Лиувилля;
- связь с матричной экспонентой при постоянной `A`: `Phi(t,s)=e^{A(t-s)}`;
- вариация постоянных `x=Xc`, `c'=X^{-1}b`;
- граница с вариационными уравнениями как производными нелинейного потока.

## Definition IDs

Использованы существующие определения:

- `linear_system`;
- `fundamental_matrix`;
- `matrix_exponential`;
- `det_exp_trace_identity`;
- `variation_of_constants_system`;
- `initial_value_problem`;
- `cauchy_problem`.

Добавлены новые компактные определения:

- `normalized_fundamental_matrix`;
- `transition_matrix`;
- `cauchy_matrix`;
- `cauchy_formula_linear_system`;
- `liouville_formula_linear_system`.

## Связи

Representative-связи добавлены к:

- `oral-above-three-fundamental-matrix-change-basis`;
- `waterloo-fundamental-matrix-flow-inverse`;
- `oral-exam-excellent-two-point-fundamental-matrix`;
- `oral-above-three-liouville-area-preservation`;
- `oral-exam-excellent-trace-zero-no-total-decay`;
- `mit-18034-pset07-euler-system-fundamental-matrix`;
- `msu-ode-2011-12-orthogonal-fundamental-matrix`;
- `oral-above-three-recover-system-from-fundamental-matrix`.

Соседние кластеры связаны через методические карточки:

- `matrix-exponential-methods` через `cluster-matrix-exponential-method-guide`;
- `constant-coefficient-linear-systems` через `cluster-linear-systems-constant-coefficients-method-guide`;
- `variation-of-constants` через `cluster-variation-of-constants-method-guide`;
- `parameter-dependence-variational-equation` через `cluster-parameter-dependence-method-guide`.

## Остаточные границы

- Не добавлялись новые вычислительные задачи: кластер уже имел representatives на смену базиса, формулу Лиувилля, двухточечное условие, потоковую обратимость, переменно-коэффициентное построение и ортогональную фундаментальную матрицу.
- Если задача требует только построить `e^{At}` или прочитать спектр постоянной матрицы, она ближе к `matrix-exponential-methods` или `constant-coefficient-linear-systems`.
- Если главная трудность в интеграле правой части, owner - `variation-of-constants`.
- Если фундаментальная матрица появляется как производная нелинейного потока по начальному состоянию или параметру, owner - `parameter-dependence-variational-equation`.

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

- `build_index` - OK: 423 cards, обновлен `index/generated.json`;
- `validate` - OK: 423 cards, 897 relations, 49 sources;
- `check_links` - OK;
- `check_encoding` - OK;
- `check_clusters` - OK: 34 task clusters;
- `build_viewer` - OK, обновлены `viewer/index.html` и `index.html`;
- `audit_rules` - OK с 4 существующими предупреждениями про `exam_score tag with technical_score > 5`:
  - `local-du-written-2014-51-characteristics-pde`;
  - `local-du-written-2014-51-factorized-variable-coeff`;
  - `local-du-written-2014-51-lagrange-singular-curves`;
  - `local-du-written-2024-variational-free-endpoint`.
