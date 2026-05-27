# Аудит кластера: линейные уравнения с переменными коэффициентами

Дата прохода: 2026-05-27. Зона: `linear-equations-variable-coefficients`.

## Что добавлено

- Создан кластер `linear-equations-variable-coefficients` в `data/task_clusters/clusters.yaml`.
- Добавлены 6 карточек в `data/problems/cluster_audit/linear_variable_coefficients/`:
  - `cluster-linear-variable-variation-parameters-fundamental-system`;
  - `cluster-linear-variable-inhomogeneous-three-solutions`;
  - `cluster-linear-variable-graph-direct-tangency`;
  - `cluster-linear-variable-graph-scaled-tangency`;
  - `cluster-linear-variable-graph-ratio-maximum`;
  - `cluster-linear-variable-graph-common-zero`.
- Добавлены 4 SVG-рисунка в `data/assets/images/linear_variable_coefficients/` и связаны через поле `assets` в графических карточках.
- Добавлены связи в `data/relations/relations.d/cluster-linear-variable-coefficients.yaml` и batch `data/import_batches/cluster-linear-variable-coefficients.yaml`.

## Покрытие

| Идея | Представители |
|---|---|
| Формула Вронскиана / Абеля-Лиувилля | `liouville-wronskian-formula`, `local-du-standard-abel-wronskian-zero-lemma`, `weak-pass-wronskian-zero-dependence`, `oral-middle-wronskian-liouville-check` |
| Редукция порядка по одному решению | `oral-exam-excellent-reduction-of-order-nonzero-solution`, `oral-above-three-reduction-order-known-solution`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2024-linear-y-xu-reduction` |
| Фундаментальная система и вариация параметров | `cluster-linear-variable-variation-parameters-fundamental-system` |
| Неоднородное уравнение как аффинное пространство | `local-du-written-2024-affine-linear-solution-space`, `cluster-linear-variable-inhomogeneous-three-solutions` |
| Невозможность касания / графические задачи | четыре новые графические карточки и существующая лемма `oral-exam-geometry-linear-second-order-uniqueness` как prerequisite |
| Сравнение и нули без спектральной нагрузки | `oral-exam-strong-10-wronskian-ratio-zeros`, `local-du-standard-sturm-separation-zeros`, `local-du-standard-sturm-zero-spacing-corollaries`, `local-du-8-sturm-comparison-theorem`, `local-du-8-t4-three-zeros-after-liouville-transform` |

## Разграничение кластеров

- Постоянные коэффициенты: задачи, решаемые характеристическим многочленом, не притягивались, кроме существующих карточек-контрастов вне representatives.
- Boundary spectral: регулярные спектральные задачи, собственные значения, ортогональность и функции Грина оставлены в `boundary-spectral-problems` / BVP-карточках. Штурм включен сюда только как локальная теория нулей решений линейного ОДУ.
- Variation of constants: новая карточка по вариации параметров добавлена не как еще один вычислительный пример, а как переменно-коэффициентная формула через фундаментальную систему и W.

## Дедупликация

Безопасных удалений не найдено. Близкие, но оставленные пары:

- `oral-above-three-reduction-order-known-solution` и `oral-exam-excellent-reduction-of-order-nonzero-solution`: вычислительный пример против общей формулы второго решения.
- `local-du-written-2014-51-factorized-variable-coeff` и `local-du-written-2024-linear-y-xu-reduction`: оба про замену/снижение порядка, но разные экзаменационные роли и разный уровень явности множителя.
- `local-du-written-2024-affine-linear-solution-space` и `cluster-linear-variable-inhomogeneous-three-solutions`: первая карточка с двумя частными решениями и вопросом невозможности, новая - чистая формула общего решения по трем независимым частным решениям.

Задачи, где вся сложность сводится к тяжелой первообразной в редукции порядка или вариации параметров, не добавлялись.

## Источники

- MIT OCW ES.1803 Topic 7 Notes: использована как надежная открытая ссылка на графическое следствие единственности для линейного ОДУ второго порядка, см. https://ocw.mit.edu/courses/es-1803-differential-equations-spring-2024/mites_1803_s24_topic7.pdf.
- Точные внешние источники для четырех новых графических вариантов не найдены; они помечены как модельные/self-authored, автор `М. Дидин`.
- Для стандартной формулы вариации параметров использован `src-mipt-ode-course`; внешняя ссылка не выдумывалась.
