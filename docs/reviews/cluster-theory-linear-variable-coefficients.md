# Теоретико-методический блок: линейные уравнения с переменными коэффициентами

Дата прохода: 2026-05-27. Зона: `linear-equations-variable-coefficients`.

## Что добавлено

- Создан методический блок `cluster-linear-variable-method-guide` в `data/problems/cluster_audit/linear_variable_coefficients/`.
- Блок включен в `data/import_batches/cluster-linear-variable-coefficients.yaml` как `method_guide` и добавлен первым representative в `data/task_clusters/clusters.yaml`.
- В `data/relations/relations.d/cluster-linear-variable-coefficients.yaml` добавлены связи от навигатора к ключевым representative-задачам и соседним теоретическим блокам.
- Новые вычислительные задачи не добавлялись; сложности существующих задач не менялись.

## Какие методы покрыты

- ФСР и линейная независимость решений через пространство начальных данных.
- Вронскиан, формула Абеля-Лиувилля и дихотомия `W` либо нигде не ноль, либо тождественно ноль.
- Понижение порядка по известному ненулевому решению через `y=u y1` и формулу второго решения.
- Вариация параметров для второго порядка при заданной фундаментальной системе.
- Структура множества решений неоднородного уравнения как `yp + ker L`; восстановление общего решения по частным решениям.
- Графические следствия единственности: касание, масштабированное касание, общий нуль, экстремум отношения.
- Нули решений: простота, изолированность, отношение решений и содержательная граница со Штурмом.

## Связи

- К определениям блок подключен через `definition_ids`: задача Коши, линейная независимость решений, ФСР, вронскиан, частное и общее решение, спектральная задача.
- К теоремам и representative-карточкам добавлены связи с `liouville-wronskian-formula`, `local-du-standard-abel-wronskian-zero-lemma`, `cluster-existence-uniqueness-continuation-method-guide`, `oral-exam-excellent-reduction-of-order-nonzero-solution`, `cluster-linear-variable-variation-parameters-fundamental-system`, `cluster-linear-variable-inhomogeneous-three-solutions`, графическими representative-задачами и `local-du-standard-sturm-separation-zeros`.
- К соседним кластерам добавлены только содержательные мосты через representative-карточки: `cluster-sturm-method-guide` для `sturm-oscillation-comparison`, `variation-of-parameters-sine` для `variation-of-constants`, `constant-coeff-second-order-resonance` для `scalar-constant-coefficient-linear-ode`.

## Источники

В методическом блоке использованы 6 источников в принятом формате:

- `src-local-du-8-program-or-exam` как локальный программный ориентир.
- `src-romanko-problem-book` как русскоязычный задачный фон.
- `src-filippov-problem-book` как классический задачник.
- `src-teschl-ode-dynamical-systems` как открытая строгая ссылка.
- `src-mit-es1803-topic7` как открытые notes по графическому следствию единственности.
- `src-mit-1803sc-ode` как открытый видеокурс MIT OCW.

## Оставшиеся пробелы

- Нет отдельной проверенной карточки на монодромию скалярного переменно-коэффициентного уравнения без ухода во Флоке; это оставлено в `deficit_policy` кластера.
- Нет новой карточки на зависимость ФСР от параметра: такую задачу стоит добавлять только если она не дублирует общий блок `parameter-dependence-variational-equation`.
- Штурмовская часть намеренно не расширялась: полноценные сравнения, дисконъюгированность и спектральные следствия уже покрываются соседними кластерами.
