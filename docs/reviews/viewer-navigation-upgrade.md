# Viewer navigation upgrade

## Что подсмотрено в соседних базах

- `graph-db`: левая рабочая панель с поиском, селектами-фильтрами, счетчиками в опциях и компактным списком карточек.
- `incomplete-info-db`: пересчет facet/count по текущей выборке, быстрые chips для популярных значений, отдельная навигация по кластерам и локальным признакам.

В текущем viewer взят именно паттерн рабочей панели и динамических facets, без копирования большой домашней страницы, комментариев, интерактивов и backend-зависимых частей.

## Реализованные фильтры

- Полнотекстовый поиск по id, title, statement, ideas, solutions, tags, источникам, кластерам и стандартным идеям.
- Отдельные фильтры `idea_score` и `technical_score`.
- Источники.
- Авторы, `created_by` и возможные attributed-author поля.
- Кластеры из `data/task_clusters/clusters.yaml`.
- Стандартные идеи из `standard_idea_ids`.
- Теги.
- Тип карточки: `problem`, `theorem`, `lemma`, `definition` и другие значения из `kind.primary`.
- Уровни `standard_course_methods`, `advanced_standard_course`, `beyond_standard_course`.
- `public_ready`, `review_status`, основная сложность `difficulty.main`.

Все счетчики в dropdown и chips пересчитываются от текущей выборки; для собственного фильтра счетчик считается с временно снятым этим фильтром, чтобы было видно доступные альтернативы.

## Добавленные поля индекса

`index/generated.json` сохраняет прежние сырые разделы (`problems`, `relations`, `sources`, `definitions`, `standard_ideas`) и добавляет:

- `cards`: нормализованный слой для viewer/search.
- `task_clusters`: прочитанные кластеры.
- `taxonomy`: tags/statuses/relation types/fragments/difficulty.
- `meta`: краткие счетчики.

В каждом элементе `cards` добавлены `source_ids/source_labels`, `authors`, `cluster_ids/cluster_labels`, `standard_idea_ids/standard_idea_labels`, `idea_score`, `technical_score`, `course_bucket`, `review_status`, `public_ready`, `statement`, `search_text` и путь к исходной карточке.
