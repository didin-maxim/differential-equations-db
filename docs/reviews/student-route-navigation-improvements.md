# Улучшение учебной навигации после method guide

Дата: 2026-05-27.

## Что изменено

В `tools/build_viewer.py` добавлен небольшой viewer-only блок для карточек с тегом `method_guide`.

Для методического блока теперь автоматически строится секция `После методического блока`:

- `Начать` - короткие представители кластера с `idea_score <= 5` и `technical_score <= 5`;
- `Средний уровень` - следующие задачи по идее/технике, без технически тяжелых вариантов;
- `Сложнее` - задачи с `technical_score > 5` или `idea_score >= 8`.

Источник данных - уже существующие `cluster_ids` карточки и `representative_card_ids` соответствующего task cluster. Данные карточек не менялись.

Кнопка задачи в этой секции ставит поиск по `card.id`, оставляет текущий учебный режим и сортирует по возрастанию сложности. Это не затрагивает обычный поиск, definition facet, exam simulation и reveal controls.

## Какие маршруты стали понятнее

- `cluster-variational-method-guide`: после навигатора студент видит стартовую вариационную задачу, затем средние свободные/подвижные концы, а технически тяжелые письменные варианты уходят в `Сложнее`.
- `cluster-pde-characteristics-method-guide`: сначала предлагаются короткие задачи на характеристичность и неединственность, потом перенос данных, а `local-du-written-2014-51-characteristics-pde` с техникой 6 показывается как сложный вариант.
- `cluster-linear-variable-method-guide`: старт начинается с Вронскиана/редукции порядка, средний уровень держит графические и аффинные задачи, а `local-du-written-2014-51-factorized-variable-coeff` с техникой 6 уходит в `Сложнее`.
- `cluster-implicit-ode-discriminant-method-guide`: `local-du-written-2014-51-lagrange-singular-curves` с техникой 6 также попадает в сложную корзину.

Итого четыре уже известные карточки с `exam_score_*` и `technical_score > 5` не предлагаются как первые задачи после методического блока.

## Что осталось

- Разбиение пока эвристическое и полностью viewer-side. Если позже появятся явные `route_start` / `route_middle` / `route_hard` метки, генератор можно переключить на них.
- В кластерах с малым числом представителей отдельные колонки могут быть пустыми; сейчас это честно показывается как отсутствие подходящих карточек.
- Блок не меняет ранжирование общего списка карточек, только добавляет маршрут внутри method guide.

## Проверки

- `python tools\build_index.py` - OK, 431 cards.
- `python tools\build_viewer.py` - OK.
- JS sanity для встроенного viewer script - OK.
- Browser sanity через `http://127.0.0.1:8766/viewer/index.html?mode=clusters&q=cluster-variational-method-guide` - блок виден, колонки `Начать` / `Средний уровень` / `Сложнее` есть, клик по задаче фильтрует список до выбранной карточки.
- `python tools\validate.py` - OK, 431 cards, 966 relations, 49 sources.
- `python tools\check_links.py` - OK.
- `python tools\check_encoding.py` - OK.
- `python tools\check_clusters.py` - OK, 34 task clusters in 9 files.
- `python tools\audit_rules.py` - OK с 4 ожидаемыми предупреждениями про `exam_score tag with technical_score > 5`: `local-du-written-2014-51-characteristics-pde`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2014-51-lagrange-singular-curves`, `local-du-written-2024-variational-free-endpoint`.
