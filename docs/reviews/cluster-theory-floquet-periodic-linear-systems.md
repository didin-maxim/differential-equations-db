# Теоретико-методический блок: floquet-periodic-linear-systems

Дата: 2026-05-27.

Зона: кластер `floquet-periodic-linear-systems` - периодические линейные системы, монодромия, мультипликаторы Флоке и периодические решения.

## Что добавлено

- Создана карточка `cluster-floquet-periodic-linear-systems-method-guide` в `data/problems/cluster_audit/floquet_periodic_linear_systems/`.
- Карточка помечена как `theorem`, `task_cluster`, `method_guide`, `cluster_representative`.
- В `data/task_clusters/clusters.yaml` карточка добавлена первым representative для `floquet-periodic-linear-systems`.
- Добавлена пачка `data/import_batches/cluster-floquet-periodic-linear-systems.yaml`.
- В слой определений добавлены compact definition-id: `periodic_linear_system`, `monodromy_matrix`, `floquet_multiplier`, `periodic_solution`, `poincare_map_period`.

## Покрытие

- матрица монодромии `M=X(T)` и формула `X(t+T)=X(t)M`;
- мультипликаторы Флоке как собственные значения `M`;
- фундаментальная матрица за период и инвариантность мультипликаторов при смене начального момента;
- устойчивость через спектр `M`: `|mu|<1`, `|mu|>1` и отдельная проверка границы `|mu|=1`;
- периодические решения неоднородной системы через `(I-M)x0=b`;
- граница со стандартной программой: базовый слой - монодромия, Лиувилль и линейная алгебра; полная нормальная форма Флоке отмечена как выход за базовый курс.

## Связи

Новые relations добавлены в `data/relations/relations.d/cluster-floquet-periodic-linear-systems.yaml`.

Representative-связи:

- `teschl-stanford-bridge-monodromy-period-iterate`;
- `teschl-stanford-bridge-floquet-determinant-liouville`;
- `teschl-stanford-bridge-floquet-multiplier-stability`;
- `oral-exam-excellent-monodromy-periodic-forcing`;
- `mipt-excellent-periodic-system-resonant-monodromy`;
- `local-du-filippov-127-monodromy-gronwall-bound`.

Соседние кластеры связаны через representative-card:

- `fundamental-matrix-linear-systems` через `waterloo-fundamental-matrix-flow-inverse`;
- `matrix-exponential-methods` через `cluster-matrix-exponential-method-guide`;
- `phase-line-stability` через `cluster-phase-stability-method-guide`.

## Границы

- Не добавлялись новые вычислительные задачи: кластер уже имеет Teschl-цепочку и локальные representatives.
- Не переносились карточки из соседних кластеров; добавлены только содержательные связи.
- Полная теорема Флоке с логарифмом монодромии и показателями Флоке оставлена как advanced/beyond-слой, чтобы не смешивать ее с базовым курсом линейных систем.

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

- `build_index` - OK: 424 cards, обновлен `index/generated.json`;
- `validate` - OK: 424 cards, 906 relations, 49 sources;
- `check_links` - OK;
- `check_encoding` - OK;
- `check_clusters` - OK: 34 task clusters;
- `build_viewer` - OK, обновлены `viewer/index.html` и `index.html`;
- `audit_rules` - OK с 4 существующими предупреждениями не из Floquet-зоны: `local-du-written-2014-51-characteristics-pde`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2014-51-lagrange-singular-curves`, `local-du-written-2024-variational-free-endpoint` имеют `exam_score` при `technical_score > 5`.
