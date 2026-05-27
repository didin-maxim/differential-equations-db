# Теоретико-методический блок orthogonal-trajectories

Дата: 2026-05-27.

## Что добавлено

- Добавлена карточка `cluster-orthogonal-trajectories-method-guide` как отдельный теоретико-методический блок кластера.
- Карточка помечена как `primary=theorem`, `task_cluster`, `method_guide`, `cluster_representative`.
- В `data/task_clusters/clusters.yaml` методический блок добавлен в `representative_card_ids`; notes кластера обновлены.
- В `data/import_batches/cluster-orthogonal-trajectories.yaml` блок добавлен в batch.
- В `data/relations/relations.d/cluster-orthogonal-trajectories.yaml` добавлены связи от method-guide к representative-задачам и соседним методическим блокам:
  - `orthogonal-trajectories-circles`;
  - `cluster-orthogonal-coaxal-real-base-points`;
  - `cluster-orthogonal-coaxal-imaginary-base-points`;
  - `cluster-orthogonal-confocal-conics-gradient`;
  - `cluster-recover-ode-from-family-method-guide`;
  - `cluster-integrating-factor-exact-forms-method-guide`;
  - `cluster-separable-homogeneous-method-guide`.

## Покрытые методы

- Восстановление дифференциального уравнения исходного семейства через дифференцирование при фиксированном параметре.
- Замена наклона на отрицательно обратный и обработка вертикальных/горизонтальных предельных случаев.
- Геометрические пучки окружностей: концентрические окружности, коаксиальный пучок через две точки, непересекающийся коаксиальный пучок и сопряженный пучок.
- Софокусные коники через уровни `r1+r2` и `r1-r2` и сравнение градиентов.
- Случаи, где ортогональное поле дальше сводится к разделяющемуся, линейному для `x^2`/`y^2` или точному уравнению.
- Правило короткого ответа: не разворачивать геометрически прозрачную задачу в тяжелую алгебру.

## Определения

Новые определения не добавлялись. В карточке использованы `definition_ids`:

- `ordinary_differential_equation`;
- `solution`;
- `integral_curve`;
- `direction_field`;
- `orthogonal_trajectories`;
- `separable_equation`;
- `exact_equation`;
- `integrating_factor`.

Дополнительно у базовой representative-карточки `orthogonal-trajectories-circles` расширены `definition_ids`: добавлены `direction_field`, `orthogonal_trajectories`, `separable_equation`.

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

- `build_index.py`: OK, собрано `index/generated.json` на 422 карточки.
- `check_encoding.py`: OK.
- `check_clusters.py`: OK, 34 кластера.
- `build_viewer.py`: OK, пересобраны `viewer/index.html` и `index.html`.
- `audit_rules.py --max-items 80`: OK с 4 предупреждениями вне orthogonal-зоны:
  - `local-du-written-2014-51-characteristics-pde`;
  - `local-du-written-2014-51-factorized-variable-coeff`;
  - `local-du-written-2014-51-lagrange-singular-curves`;
  - `local-du-written-2024-variational-free-endpoint`.
- `validate.py`: FAIL из-за чужой карточки `data/problems/cluster_audit/integral_equation_to_ode/cluster-integral-equation-to-ode-method-guide.yaml`, где сейчас используются неизвестные definitions `integral_equation`, `volterra_integral_equation`, `fredholm_integral_equation`.
- `check_links.py`: FAIL по той же чужой зоне `integral_equation_to_ode` и тем же неизвестным definition ids.

Дополнительная проверка `python -m json.tool` для новой карточки, orthogonal-relations и batch прошла без ошибок.
