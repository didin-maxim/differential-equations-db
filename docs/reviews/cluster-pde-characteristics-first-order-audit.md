# Аудит кластера PDE characteristics first order

Дата прохода: 2026-05-27. Зона: линейные однородные уравнения в частных производных первого порядка и метод характеристик; без углубления в PDE второго порядка.

## Что проверено

Смотрел `data/task_clusters/clusters.yaml`, карточки с тегами и объектами `first_order_pde_characteristics`, `pde_characteristics`, `linear_first_order_pde`, `characteristics`, `transport_equation`, `cauchy_problem`, `existence_uniqueness`, а также отчеты `local-du-program-8.md`, `local-du-gap-and-dedup-report.md`, `english-lebl-diffyqs-import.md`, `student-written-exam-weak-audit.md`, `student-written-exam-middle-audit.md`, `student-written-exam-strong-audit.md`.

## Найденные точные попадания

- `local-du-deficit-first-order-pde-characteristics`: базовая диагностика характеристических и нехарактеристических данных.
- `local-du-written-2014-51-characteristics-pde`: письменная задача 2014/51 с двумя инвариантами и поверхностью данных.
- `local-du-written-2023-characteristics-plane-data`: письменная задача ДУ_В_23; перенесена из `fragment=systems` в `first_order`, `exam_score_3` заменен на `exam_score_5`.
- `local-du-romanko-pde-two-invariants`: Романко, §17, пример с двумя инвариантами и поверхностью Коши; добавлен в representatives.
- `lebl-diffyqs-transport-signal-shift`, `lebl-diffyqs-variable-coefficient-characteristics`, `lebl-diffyqs-damped-transport-characteristics`, `lebl-diffyqs-characteristic-data-obstruction`: английские базовые представители transport/variable speed/damping/obstruction.

`mipt-excellent-semilinear-characteristics-blowup` оставлен вне representatives: это полезная соседняя excellent-level карточка, но ее главный механизм уже semilinear blow-up/maximal domain, а не базовый линейный однородный PDE-кластер.

## Добавленный блок

Добавлено 6 компактных модельных карточек в `data/problems/cluster_audit/pde_characteristics_first_order/`:

- `cluster-pde-characteristics-strip-domain`: область продолжения данных с отрезка, полоса `|y-x|<1`.
- `cluster-pde-characteristics-characteristic-incompatible`: несовместимые данные на характеристике, решения нет.
- `cluster-pde-characteristics-characteristic-nonunique`: совместимые данные на характеристике, существование без единственности.
- `cluster-pde-characteristics-incompatible-double-hit`: начальная кривая дважды пересекает одну характеристику, данные конфликтуют.
- `cluster-pde-characteristics-single-hit-criterion`: критерий однократного пересечения через инъективность номера характеристики.
- `cluster-pde-characteristics-flow-geometry`: простая геометрия transport flow, движение носителя `[1,2] -> [e^t,2e^t]`.

Созданы простые SVG:

- `data/assets/images/pde_characteristics/strip-domain.svg`
- `data/assets/images/pde_characteristics/parabola-double-hit.svg`

## Метаданные и политика

В taxonomy добавлены теги `pde_characteristics`, `linear_first_order_pde`, `transport_equation`, `cauchy_problem`, `noncharacteristic_curve`, `domain_of_dependence`; `existence_uniqueness` уже был.

Кластер `pde-characteristics-first-order` усилен: цель теперь явно ограничена линейными однородными ЧП первого порядка; добавлены варианты `finite_initial_arc_domain`, `single_hit_noncharacteristic`, `double_hit_incompatibility`; representatives расширены до 14 карточек.

Политика насыщения: кластер теперь близок к насыщенному учебному блоку. Новые карточки добавлять только при новом диагностическом типе данных или новой геометрии характеристик. Не добавлять задачи, где меняются только коэффициенты, а план остается тем же.

Связи добавлены только в `data/relations/relations.d/cluster-pde-characteristics-first-order.yaml`, batch - в `data/import_batches/cluster-pde-characteristics-first-order.yaml`.
