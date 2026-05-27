# differential-equations

Черновая база по дифференциальным уравнениям, устроенная по образцу `graph-db` и
`incomplete-info-db`: источник истины лежит в JSON-совместимых YAML-файлах
в `data/`, а инструменты строят индекс, поиск и статический viewer.

## Что внутри

- `data/problems/` - карточки задач, теорем, лемм и стандартных примеров;
- `data/definitions/` - основные определения;
- `data/standard_ideas/` - повторяющиеся методы решения;
- `data/relations/` - связи между карточками;
- `data/sources/` - нормализованный реестр источников;
- `data/taxonomy/` - закрытые словари фрагментов, тегов, статусов, типов связей;
- `docs/` - правила работы и архитектурные заметки;
- `tools/` - валидация, проверка ссылок, поиск, сборка индекса и viewer.

Файлы `*.yaml` в `data/` намеренно записаны как валидный JSON: двойные кавычки,
без YAML-якорей и без многострочных YAML-блоков. LaTeX в строках хранится с
экранированными обратными слешами.

## Быстрый старт

```powershell
python tools\check_encoding.py
python tools\validate.py
python tools\check_links.py
python tools\audit_rules.py
python tools\build_index.py
python tools\build_viewer.py
python tools\search.py query "Пикара"
python tools\search.py card picard-lindelof-theorem
python tools\search.py neighbors picard-lindelof-theorem
```

После сборки viewer можно открыть `viewer/index.html`.

## Текущий статус

Это первый проход: задана архитектура, добавлены основные определения, стандартные
теоремы с доказательствами и стартовый корпус задач уровня от типового курса МФТИ
до студенческих олимпиад. При расширении базы важнее сохранять проверяемость
решений и точность формулировок, чем быстро наращивать число карточек.

## Текущие проходы по источникам

- [docs/BASE_WORKFLOW_RULES.md](docs/BASE_WORKFLOW_RULES.md) - редакционные
  правила отбора задач, кластеров, сложностей и интеграции перед коммитом.
- [docs/reviews/olympiad-selection-criteria.md](docs/reviews/olympiad-selection-criteria.md) - граница темы для отбора задач из студенческих олимпиад.
