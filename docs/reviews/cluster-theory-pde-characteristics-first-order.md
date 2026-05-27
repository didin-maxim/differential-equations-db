# Методический блок кластера `pde-characteristics-first-order`

Дата: 2026-05-27.

Зона работ: кластер `pde-characteristics-first-order`, теория метода характеристик для линейных ЧП первого порядка, definition links, источники и graph-relations. Новые вычислительные задачи не добавлялись.

## Что добавлено

- `cluster-pde-characteristics-method-guide` в `data/problems/cluster_audit/pde_characteristics_first_order/cluster-pde-characteristics-method-guide.yaml`.
  - Тип: `kind.primary=theorem`, `secondary=["task_cluster","method_guide","cluster_representative"]`, чтобы карточка индексировалась как теория/методический блок.
  - Фрагмент: `first_order`.
  - Теги: `task_cluster`, `cluster_representative`, `first_order_pde_characteristics`, `pde_characteristics`, `linear_first_order_pde`, `transport_equation`, `cauchy_problem`, `noncharacteristic_curve`, `domain_of_dependence`, `characteristic_cauchy_data`, `first_integral`, `theoretical_exam_task`.
  - В `data/task_clusters/clusters.yaml` карточка добавлена в `representative_card_ids` кластера и упомянута в `notes`.
  - В `data/import_batches/cluster-pde-characteristics-first-order.yaml` блок добавлен как `method_guide`, не как новая вычислительная задача.

## Покрытые методы

- Характеристическая система для `a u_x+b u_y+c u=f` и ее многомерного аналога.
- Первые интегралы характеристик: один инвариант для двумерного однородного уравнения, два инварианта для трех независимых переменных.
- Задача Коши на кривой/поверхности: локальная нехарактеристичность как трансверсальность характеристического поля к данным.
- Область продолжения/зависимости: объединение характеристик, выходящих из заданной части начальных данных.
- Единственность, неединственность и несовместность: однократное попадание в данные, повторное попадание одной характеристики, данные на характеристике.
- Геометрический смысл потока: перенос значения и носителя начального профиля, включая сдвиг и растяжение.

## Definition Links

Новые определения не добавлялись. Использованы существующие `definition_ids`:

- `pde_characteristic_first_order`
- `cauchy_problem`
- `integral_curve`
- `first_integral`
- `solution`

Отдельных definition-записей для `noncharacteristic_curve`, `domain_of_dependence` или `domain_of_continuation` в `data/definitions/definitions.yaml` пока нет, поэтому они оставлены как теги/объекты профиля, без дублирования определений.

Definition links также добавлены или расширены у representative-карточек кластера: local_du/written/Romanko/Lebl и шесть модельных карточек аудита.

## Источники

В методическом блоке использованы 6 источников в принятом формате:

- `src-local-du-8-program-or-exam` как локальная граница программы.
- `src-filippov-problem-book`, локатор `§27` по локальному обзору, как задачный фон по характеристическому методу.
- `src-romanko-problem-book`, `§17`, как представитель линейного ЧП первого порядка с двумя инвариантами.
- `src-lebl-diffyqs`, раздел 8.1 по локальному импорту, как открытый источник transport/damping/obstruction-примеров.
- `src-kth-method-characteristics-notes`, новый источник: John Andersson, KTH notes on first order PDE and characteristics.
- `src-umd-first-order-pde-characteristics`, новый источник: University of Maryland Math 462 notes on first-order PDE and characteristics.

## Relations

В `data/relations/relations.d/cluster-pde-characteristics-first-order.yaml` добавлены связи:

- От соседних теоретических блоков:
  - `rel-pde-guide-after-first-integral-criterion`
  - `rel-pde-guide-after-filippov-first-integrals`
  - `rel-pde-guide-after-existence-guide`
- От навигатора к representative-задачам:
  - `rel-pde-guide-to-local-du-deficit`
  - `rel-pde-guide-to-romanko-two-invariants`
  - `rel-pde-guide-to-strip-domain`
  - `rel-pde-guide-to-single-hit`
  - `rel-pde-guide-to-characteristic-incompatible`
  - `rel-pde-guide-to-characteristic-nonunique`
  - `rel-pde-guide-to-flow-geometry`

Прямых graph-relations к определениям не добавлялось, потому что `tools/check_links.py` и `tools/validate.py` требуют, чтобы endpoints relations были карточками. Связь с определениями сделана штатно через `definition_ids`.

## Viewer / Index

После `python tools/build_index.py` карточка найдена в `index/generated.json` как:

- `kind`: `theorem`;
- `secondary_kinds`: `["task_cluster","method_guide","cluster_representative"]`;
- `cluster_ids`: `["pde-characteristics-first-order"]`;
- `source_labels`: `["8.pdf: программа ДУ","Филиппов, сборник ДУ","Романко: задачник ДУ и ВИ","Lebl, Notes on Diffy Qs","KTH characteristics notes","UMD first-order PDE notes"]`.

Значит, блок находится через кластер, через теоретический слой и поиском по `method_guide`, `characteristics`, `cauchy_problem`, `first_integral`, `domain_of_dependence`, `noncharacteristic_curve`.

## Оставшиеся пробелы

- В `data/definitions/definitions.yaml` пока нет отдельных определений для нехарактеристической кривой/поверхности и области зависимости/продолжения. Их стоит добавить отдельным согласованным проходом по definitions layer, если база начнет активно искать эти термины как определения.
- Филиппов §27 отмечен как полезный задачный фон, но отдельная карточка из него не импортировалась, чтобы не плодить однотипные вычислительные задачи при уже закрытых вариантах.
- Semilinear/blow-up characteristics остаются соседней продвинутой темой и сознательно не включались в representative-ядро этого кластера.

## Проверки

Запущены:

- `python tools/build_index.py` - OK, 406 cards.
- `python tools/validate.py`
- `python tools/check_links.py`
- `python tools/check_encoding.py`
- `python tools/check_clusters.py`
- `python tools/build_viewer.py`
- `python tools/audit_rules.py --max-items 80`

Результат: все команды завершились успешно. `audit_rules` сообщил 4 предупреждения, не блокирующие сборку; одно касается уже существующей representative-карточки `local-du-written-2014-51-characteristics-pde` с `exam_score_*` при `technical_score=6`. Сложность не менялась, чтобы не подгонять старую карточку под аудит без содержательной причины.
