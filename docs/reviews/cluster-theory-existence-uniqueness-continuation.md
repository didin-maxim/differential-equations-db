# Методический блок кластера `existence-uniqueness-continuation`

Дата: 2026-05-27.

Зона работ: кластер `existence-uniqueness-continuation`, методическая теория, связи и источники. Новые вычислительные задачи не добавлялись.

## Добавленные карточки

- `cluster-existence-uniqueness-continuation-method-guide` в `data/problems/cluster_audit/existence_uniqueness_continuation/cluster-existence-method-guide.yaml`.
  - Тип: `kind.primary=theorem`, `secondary=["task_cluster","method_guide"]`, чтобы карточка отображалась как теория, а не как задача.
  - Фрагмент: `foundations`.
  - Теги: `task_cluster`, `cluster_representative`, `existence_uniqueness`, `picard_iteration`, `peano`, `continuation`, `gronwall`, `comparison`, `global_solution`, `blow_up`, `boundedness`, `counterexample`, `standard_course_methods`.
  - В `data/task_clusters/clusters.yaml` карточка добавлена в `representative_card_ids` кластера и упомянута в `notes`.

## Покрытые методы

- Выбор между Пеано и Пикаром-Линделефом по регулярности правой части.
- Приведение уравнений высокого порядка к системе первого порядка перед применением теорем существования и единственности.
- Гронуолл для единственности, непрерывной зависимости и глобальности при линейном росте.
- Максимальное решение, критерий продолжения и альтернатива выхода из компактов.
- Барьерный аргумент и инвариантные области через первый момент выхода.
- Регулярная неявная задача Коши `F(t,y,y')=0` при `F_p != 0`.
- Типовые ловушки: Пеано без единственности, проверка Липшица только на одной кривой, смешение взрыва с выходом к границе области, применение Пикара к неявному уравнению без выбора регулярной ветви.

## Источники

В методический блок добавлены 5 компактных источников:

- `src-mipt-ode-course` как базовая русскоязычная программа.
- `src-arnold-ode` как классический русскоязычный источник.
- `src-teschl-ode-dynamical-systems`, §§2.4-2.6, как открытый строгий источник по максимальным решениям, продолжению и непрерывной зависимости.
- `src-lebl-diffyqs` как открытый англоязычный вводный конспект.
- `src-mit-1803sc-ode` как новый источник в `data/sources/sources.yaml`: MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011, видеокурс и материалы.

## Добавленные relations

В `data/relations/relations.d/cluster-existence-uniqueness-continuation.yaml` добавлены связи:

- От теорем к навигатору:
  - `rel-cluster-existence-guide-picard`
  - `rel-cluster-existence-guide-peano`
  - `rel-cluster-existence-guide-gronwall`
  - `rel-cluster-existence-guide-continuation`
- От навигатора к ключевым представителям:
  - `rel-cluster-existence-guide-linear-growth`
  - `rel-cluster-existence-guide-blowup-alt`
  - `rel-cluster-existence-guide-barrier`
  - `rel-cluster-existence-guide-implicit`
  - `rel-cluster-existence-guide-continuous-dependence`
  - `rel-cluster-existence-guide-nonunique`

Эти связи покрывают Пикара-Линделефа, Пеано, продолжение максимального решения, альтернативу взрыва/выхода из компактов, Гронуолла, непрерывную зависимость, барьеры/инвариантные области и регулярную неявную задачу Коши.

## Viewer

После сборки `index/generated.json` карточка находится в индексе как:

- `kind`: `theorem`;
- `cluster_ids`: `["existence-uniqueness-continuation"]`;
- `cluster_labels`: `["Существование, единственность и продолжение решений"]`;
- `source_labels`: `["МФТИ: ДУ", "Арнольд, ОДУ", "Teschl ODE/DS", "Lebl, Notes on Diffy Qs", "MIT 18.03SC ODE"]`.

Следовательно, блок находится через кластер, через режим теории и поиском по теме; он не попадает в viewer как обычная вычислительная задача.

## Оставшиеся пробелы

- Определения вроде `инвариантная область`, `односторонний Липшиц`, `линейный рост` пока не выделялись отдельно, чтобы не конфликтовать с параллельной работой по определениям. В методическом блоке они используются текстом и через существующие карточки.
- Для будущего прохода можно добавить одну advanced-карточку на критерий Осгуда или существование Каратеодори, если программа явно потребует слабые условия, но текущий кластер уже закрывает основной учебный маршрут.
- Источник `src-mipt-ode-course` остается seed-ссылкой; при наличии конкретного русскоязычного пособия/листка его стоит заменить более точным локатором.

## Проверки

Запущены и прошли:

- `python tools/build_index.py`
- `python tools/validate.py`
- `python tools/check_links.py`
- `python tools/check_encoding.py`
- `python tools/check_clusters.py`
- `python tools/build_viewer.py`

