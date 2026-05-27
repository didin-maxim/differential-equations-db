# Аудит кластера неразрешенных ОДУ и дискриминанта

Дата: 2026-05-27.

## Что проверено

- Кластер `implicit-ode-discriminant` в `data/task_clusters/clusters.yaml`.
- Общие правила из `docs/TASK_CLUSTERS.md` и discovery-отчет `docs/reviews/task-cluster-discovery-and-saturation.md`.
- Карточки `data/problems/**` по тегам и словам: `implicit_ode_discriminant`, `clairaut`, `envelope`, `singular_solution`, `first_order`, `written_exam`.
- Локальные обзоры `local_du`: письменные экзамены 2007-2025, `local-du-programs-other-years.md`, Романко/Филиппов selection reports.

## Найденные точные попадания

- `local-du-written-2022-implicit-discriminant`: базовая письменная задача на `F=0`, `F_p=0` и проверку, когда дискриминант содержит решение.
- `local-du-written-2014-51-lagrange-singular-curves`: Лагранж-Клеро с двумя особыми кривыми/огибающими.
- `local-du-written-2020-clairaut-shifted-envelope`: локальный письменный вариант Клеро с огибающей.
- `clairaut-envelope`: seed-карточка Клеро; оставлена как дедупликационный якорь, а не повод добавлять новые коэффициентные варианты.

## Добавлено

- `cluster-implicit-branch-switch-square-root`: `(y')^2=y`, дискриминант `y=0`, переключение ветвей и неединственность через `(0,0)`.
- `cluster-implicit-discriminant-not-solution`: `(y')^2=x`, дискриминант `x=0` как граница поля направлений, но не интегральная кривая.

Обе карточки компактные, без длинного исключения параметра. Клеро/Лагранж заново не импортировались: существующих представителей достаточно.

## Отфильтровано

- Новые варианты Клеро с другими коэффициентами: дублируют `clairaut-envelope` и `local-du-written-2020-clairaut-shifted-envelope`.
- Задачи из локальных программ вида `(y')^2=4y^3(1-y)` и ссылки на Филиппова 287: уже отмечены в `local-du-programs-other-years.md` как близкие к существующим Клеро/Лагранжу и письменной огибающей; без новой идеи их не добавлять.
- Длинные задачи, где вся сложность в исключении параметра, а не в статусе дискриминанта, ветвлении или геометрии.

## Политика после аудита

Кластер больше не дефицитный по базовым представителям: есть письменный дискриминант, Клеро, Лагранж, branch switching и геометрический контрпример "дискриминант не равен решению". Дальше добавлять только точечные задачи с новым механизмом: cusp/discriminant caustic, задача Коши для неразрешенного уравнения с проверкой локальной обратимости, или качественная геометрия ветвей без вычислительного раздувания.

Связи записаны только в `data/relations/relations.d/cluster-implicit-ode-discriminant.yaml`, batch - в `data/import_batches/cluster-implicit-ode-discriminant.yaml`.
