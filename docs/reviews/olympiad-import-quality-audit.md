# Аудит качества олимпиадного импорта

Дата: 2026-05-27.

## Область проверки

Проверены карточки `data/problems/olympiad/**`, с основным вниманием к последним пачкам:

- `data/problems/olympiad/ru_cis_extra`
- `data/problems/olympiad/international_extra`
- `data/problems/olympiad/vjimc_europe`

Также просмотрены связанные `import_batches`, `scan reports` и relation-файлы `olympiad-*.yaml`.

## Исправления

- Исправлена опечатка в идее VJIMC 2016: `f'=f-f(.-1)` заменено на `f'(x)=f(x)-f(x-1)`.
- Убраны англоязычные служебные хвосты из keywords/notes последних пачек там, где они не являются названием источника: `moving average`, `delay differential equation`, `f prime over f squared`, `fixed point near pole`, `countable branch/implicit ODE`.
- Убрано дублирование тега `existence_uniqueness` в карточке `innopolis-2024-t6-million-cauchy-branches`.
- Для последних карточек без явной метки соответствия программе добавлены аккуратные метки:
  - `innopolis-2024-t6-million-cauchy-branches`: `standard_course_methods`;
  - `seemous-2020-p4-pole-fixed-point-series`: `advanced_standard_course`;
  - `vjimc-2016-c2-p4-moving-average-delay-variation`: `beyond_standard_course`;
  - `bme-2024-p2-composition-ode-nonexistence`: `beyond_standard_course`.
- В карточке BME 2024 P2 усилено решение: отдельно доказано, что функция не может быть ограниченной, затем корректно обоснован выход за диагональ `f(x)>x+1` и только после этого используется обратная функция и blow-up.
- Русифицированы заметки в `ru_cis_extra`: страницы PDF, проверка текстового слоя, глобальная заданность на `[0,+∞)`.

## Родственные связи

Добавлен отдельный relation-файл `data/relations/relations.d/olympiad-import-quality-audit.yaml`, чтобы QA-связи были отделены от первичного импорта.

Добавлены глубокие связи:

- `mipt-middle-power-series-recurrence` -> `ru-cis-extra-yagtu-2001-half-argument-ode`: рекурсия коэффициентов степенного ряда.
- `blow-up-comparison-y-square` -> `bme-2024-p2-composition-ode-nonexistence`: финальный механизм конечного взрыва после сравнения.
- `putnam-modern-1990-b1` -> `seemous-2010-p1-iterated-integrals-linear-ode`: интегральная конструкция превращается в линейное ОДУ.
- `periodic-solution-monotone-derivative` -> `bme-2023-p3-periodic-high-derivative-bound`: периодичность и нули производных как основа оценки.

Связи по одной только общей теме не добавлялись.

## Сложность и тематическая уместность

Явного завышения олимпиадности в последних пачках не найдено: часть задач имеет экзаменационный метод после распознавания приема, но сама упаковка задачи олимпиадная. Для таких задач сохранены умеренные `idea_score` и технические оценки.

Пограничные случаи:

- `seemous-2010-p1-iterated-integrals-linear-ode` формулируется через ряд интегралов, но главный ход базы - получить `F'=F+f0`, поэтому карточка уместна.
- `istcim-2022-c-integral-identity-ode` выглядит как интегральное тождество, но центральный механизм - сравнение двух функций параметра как решений одного ОДУ.
- `vjimc-2016-c2-p4-moving-average-delay-variation` выходит за стандартный курс из-за уравнения с запаздыванием и ограниченной вариации; оставлена как редкая олимпиадная задача с настоящим дифференциальным механизмом.

## Кластеры

Последние 15 импортированных карточек пока не являются representatives существующих кластеров. Это не обязательно ошибка QA-слоя: у всех есть хотя бы одна содержательная relation-связь, а кластеризацию лучше делать отдельным проходом, чтобы не превращать широкие кластеры в свалки по общей теме.

Кандидаты для следующего кластерного прохода:

- `integral_equation_to_ode`: SEEMOUS 2010, ISTCiM 2022, Putnam 1990 B1, VJIMC 2016.
- `functional_differential`: ISTCiM 2023, BME 2024, Putnam 2010 B5, ЯГТУ 2001 half-argument.
- `differential_operator_rolle`: IMC 1994, IMC 2006, СПбГЭУ 2023.

## Проверки

Пройдены:

```text
python tools\validate.py        # OK: 357 cards, 468 relations, 38 sources
python tools\check_links.py     # OK
python tools\audit_rules.py     # OK, 0 warnings
python tools\check_clusters.py  # OK: 30 task clusters
python tools\check_encoding.py  # OK
```

## Оставшиеся риски

- Названия источников в keywords/notes вроде `SEEMOUS 2020 Problem 4` и `IMC 2006 Day 1 Solutions` оставлены на английском как библиографические указатели, а не как непереведенный текст карточки.
- Кластеризация олимпиадных задач вне clusters требует отдельного содержательного прохода: часть задач явно группируется, но добавлять representatives без аудита насыщенности кластера сейчас было бы преждевременно.
- Для задач, где официальное решение не найдено или источник содержит только условие, сохранен статус самостоятельного решения; при будущем источниковедческом проходе стоит сверить их с альтернативными разборами.
