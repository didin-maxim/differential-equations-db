# Pre-commit viewer/index audit

Дата: 2026-05-27.

Область проверки: `tools/build_index.py`, `tools/build_viewer.py`, `index/generated.json`, `viewer/index.html`.

## Итог

Индекс и viewer пересобраны. Найдена и исправлена небольшая навигационная недосказанность: viewer показывал общее число карточек и кластеры, но явное число именно задач было доступно только через фасет типа карточки. Теперь `index/generated.json` содержит `meta.problem_count` и `meta.theory_count`, а viewer выводит в шапке и на главной странице количество задач.

Текущие счетчики:

- карточек: 357
- задач: 294
- теорем: 33
- лемм: 29
- определений: 1
- связей: 521
- источников: 38
- кластеров: 32
- image assets: 10 уникальных, битых локальных путей не найдено

## Сложности задач

Идейная сложность среди задач:

| idea_score | count |
|---:|---:|
| 2 | 4 |
| 3 | 13 |
| 4 | 40 |
| 5 | 54 |
| 6 | 71 |
| 7 | 39 |
| 8 | 44 |
| 9 | 11 |
| 10 | 12 |
| 11 | 5 |
| 12 | 1 |

Техническая сложность среди задач:

| technical_score | count |
|---:|---:|
| 1 | 5 |
| 2 | 52 |
| 3 | 76 |
| 4 | 77 |
| 5 | 48 |
| 6 | 14 |
| 7 | 11 |
| 8 | 10 |
| 9 | 1 |

## Viewer

Проверено статически:

- `viewer/index.html` содержит актуальный JSON payload после пересборки.
- Фильтры/фасеты для `ideaScore`, `technicalScore`, источников, авторов, кластеров, стандартных идей и тегов присутствуют.
- Счетчики фасетов вычисляются динамически через `facetCounts`.
- Блоки идей и решений рендерятся через `<details class="reveal">`; в статическом HTML нет открытых `details`, поэтому решения и идеи скрыты по умолчанию.
- Все 10 image assets из индекса имеют существующие локальные файлы и присутствуют в HTML-пейлоаде.
- Встроенный JS успешно парсится через `new Function(...)` без запуска сервера.

## Команды

```powershell
python tools\build_index.py
python tools\build_viewer.py
python tools\validate.py
python tools\check_links.py
node -e "<static JS parse check>"
```

Результат обязательных проверок:

```text
build_index.py  OK: wrote index/generated.json with 357 cards
build_viewer.py OK: wrote viewer/index.html
validate.py     OK: 357 cards, 521 relations, 38 sources
check_links.py  OK: links are consistent
```

Коммит и push не выполнялись.
