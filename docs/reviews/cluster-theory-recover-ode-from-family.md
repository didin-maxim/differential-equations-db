# Теоретико-методический блок recover-ode-from-family

Дата: 2026-05-27.

## Что добавлено

- Добавлена карточка `cluster-recover-ode-from-family-method-guide` как отдельный теоретико-методический блок кластера.
- Карточка помечена как `primary=theorem`, `task_cluster`, `method_guide`, `cluster_representative`, поэтому индексируется как теория/методический слой и находится через кластер `recover-ode-from-family`.
- В `data/task_clusters/clusters.yaml` методический блок добавлен в `representative_card_ids`; в notes кластера зафиксирована его роль.
- В `data/import_batches/cluster-recover-ode-from-family.yaml` блок добавлен в batch как `method_guide`.
- В `data/relations/relations.d/cluster-recover-ode-from-family.yaml` добавлены связи от method-guide к representative-задачам и соседям:
  - `waterloo-family-circles-recover-ode`;
  - `cluster-recover-parameter-count-order-diagnostic`;
  - `cluster-recover-translated-parabolas-envelope`;
  - `written-mipt-1998-lines-distance-one-envelope`;
  - `linear-first-order-formula`;
  - `orthogonal-trajectories-circles`;
  - `cluster-implicit-discriminant-not-solution`.

## Покрытые методы

- Подсчет числа независимых параметров и ожидаемого минимального порядка ОДУ.
- Дифференцирование семейства по независимой переменной при фиксированных параметрах.
- Исключение параметров из исходного семейства и его производных.
- Проверка обратного включения, области, делений и вырожденных кривых.
- Огибающие и особые решения, возникающие после восстановления ОДУ.
- Граница с соседними кластерами:
  - `orthogonal-trajectories`: recover-шаг является только подготовкой к ортогональному семейству;
  - `implicit-ode-discriminant`: исходно дано `F(x,y,p)=0`, а не семейство кривых;
  - `linear-first-order-ode`: линейное уравнение может возникнуть как результат восстановления, но стандартный интегрирующий множитель является отдельным сюжетом.

## Определения и источники

Новые определения не добавлялись. В карточке использованы `definition_ids`:

- `ordinary_differential_equation`;
- `solution`;
- `general_solution`;
- `particular_solution`;
- `integral_curve`;
- `singular_solution`;
- `discriminant_curve`;
- `orthogonal_trajectories`;
- `linear_first_order_equation`.

Источники в карточке:

- `src-mipt-ode-course`;
- `src-romanko-problem-book`;
- `src-filippov-problem-book`;
- `src-waterloo-amath250-notes`;
- `src-mit-1803sc-ode`;
- `src-lebl-diffyqs`.

## Индексация

После `python tools/build_index.py` карточка присутствует в `index/generated.json`:

- `kind`: `theorem`;
- `secondary_kinds`: `task_cluster`, `method_guide`, `cluster_representative`;
- `cluster_ids`: содержит `recover-ode-from-family`;
- search text содержит `recover-ode-from-family`, `recover_ode_from_family`, `method_guide`, `minimal order`, `envelope`, `orthogonal trajectories boundary`, `implicit discriminant boundary`.

## Проверки

Запущены команды:

```powershell
python tools/build_index.py
python tools/validate.py
python tools/check_links.py
python tools/check_encoding.py
python tools/check_clusters.py
python tools/build_viewer.py
python tools/audit_rules.py --max-items 80
```

Результат:

- `build_index.py`: OK, собрано `index/generated.json` на 412 карточек.
- `check_links.py`: OK.
- `check_encoding.py`: OK.
- `check_clusters.py`: OK, 34 кластера.
- `build_viewer.py`: OK, пересобраны `viewer/index.html` и `index.html`.
- `audit_rules.py --max-items 80`: OK с 4 предупреждениями вне recover-зоны (`local-du-written-2014-51-characteristics-pde`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2014-51-lagrange-singular-curves`, `local-du-written-2024-variational-free-endpoint`).
- `validate.py`: FAIL из-за чужой карточки `data/problems/cluster_audit/linear_first_order_ode/cluster-linear-first-order-method-guide.yaml`, где сейчас используются неизвестные теги `boundary_value_problem` и `integral_curve`. Файл не относится к зоне `recover-ode-from-family` и не редактировался в этом проходе.

## Оставшиеся пробелы

- В кластере уже достаточно представителей для watch-состояния; новые вычислительные задачи с громоздким исключением параметров не нужны.
- Потенциально полезна только одна будущая компактная карточка с новым геометрическим заданием семейства через касательные или область, если она не дублирует Waterloo-окружности, прямые на расстоянии 1 и сдвинутые параболы.
- Можно отдельно вычистить чужой `validate.py` blocker в `linear_first_order_ode`, но это вне текущей recover-зоны.
