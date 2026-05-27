# Проверка покрытия кластеров методическими блоками

Дата: 2026-05-27.

Добавлен отдельный мягкий валидатор `tools/check_cluster_guides.py`. Он не меняет
`data/task_clusters/clusters.yaml` и не требует разбиения кластерного файла.

## Что проверяется

- Скрипт читает все `data/task_clusters/*.yaml` и карточки из
  `data/problems/**/*.yaml` через существующие helper-ы `lib.data_files` и
  `lib.load_problem_files`.
- Для каждого кластера берется `representative_card_ids`.
- Method guide считается найденным только если среди representatives есть
  карточка с маркером `method_guide` в `kind.secondary` или `tags`.
- Для найденного guide проверяется, что он имеет маркеры `task_cluster` и
  `cluster_representative`, источники или references, `definition_ids` и
  `difficulty.technical_score <= 3`.
- Выводится компактная таблица:
  `cluster id`, число representatives, guide id или `none`, status.

## Текущее покрытие

На текущем снимке `python tools/check_cluster_guides.py` проверил 34 кластера:

- errors: 0;
- warnings: 0;
- info: 0;
- кластеров без method guide: 0.

Кластеры без guide на момент проверки отсутствуют.

## Предлагаемые пороги строгого режима

Текущий режим намеренно мягкий и не ломает базу, пока параллельные методические
агенты завершают наполнение.

Предлагаемая эволюция:

- `< 8` representatives без guide: `INFO`, не блокировать.
- `>= 8` representatives без guide: `WARN`, нужен методический навигатор или
  явное исключение.
- `>= 15` representatives без guide: в будущем `ERROR` для неолимпиадных
  кластеров без намеренного исключения.
- Олимпиадные кластеры и явно помеченные исключения оставлять на `WARN`, потому
  что там guide может быть менее естественным или появляться после ручной
  методической группировки.

В скрипте уже есть флаг `--strict`: он переводит неолимпиадные кластеры с
`representative_card_ids >= 15` и без guide в `ERROR`. Обычный запуск пока
оставляет такие случаи warning-отчетом.
