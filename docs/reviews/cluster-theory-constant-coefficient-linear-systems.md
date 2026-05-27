# Теоретико-методический блок constant-coefficient-linear-systems

Дата: 2026-05-27.

Зона: `constant-coefficient-linear-systems`, без массового добавления новых вычислительных задач и без изменения сложностей existing representatives.

## Что добавлено

Добавлена карточка `cluster-linear-systems-constant-coefficients-method-guide` в `data/problems/cluster_audit/linear_systems_constant_coefficients/`.

Карточка помечена как:

- `kind.primary = theorem`;
- `kind.secondary = task_cluster, method_guide, cluster_representative`;
- tags: `linear_systems`, `constant_coefficients`, `matrix_exponential`, `jordan_form`, `variation_of_parameters`, `trace_determinant`, `task_cluster`, `cluster_representative`.

ID блока добавлен в `representative_card_ids` кластера `constant-coefficient-linear-systems`, поэтому блок находится через кластерный слой и индексируется вместе с representative-задачами.

## Покрытые методы

Блок закрывает методический маршрут для однородных систем `x'=Ax`: спектр матрицы, собственные векторы, кратные собственные значения, жордановы цепочки и присоединенные векторы.

Отдельно прописаны комплексные собственные значения и переход к вещественной форме через действительную и мнимую части комплексного решения. Для кратных комплексных пар указаны дополнительные множители `t^k`.

Для неоднородных систем `x'=Ax+f(t)` добавлен маршрут через вариацию постоянных и через подбор частного решения для правых частей типа константа, полином, `e^{mu t}p(t)`, `sin`, `cos`, с проверкой резонанса по спектру и жордановой структуре.

Связь с матричной экспонентой и фундаментальной матрицей дана через `X(t)=e^{At}`, формулу вариации постоянных и determinant/trace identity `det(e^{At})=e^{t tr A}` как частный случай формулы Лиувилля.

## Источники

В карточке добавлены 6 источников в принятом формате `source_id`:

- `src-mipt-ode-course`;
- `src-romanko-problem-book`;
- `src-filippov-problem-book`;
- `src-coddington-levinson`;
- `src-teschl-ode-dynamical-systems`;
- `src-mit-1803sc-ode`.

MIT OCW выбран как видео- и notes-источник по matrix exponentials; Teschl как открытая строгая ссылка; Романко и Филиппов как локальные русскоязычные задачники.

## Связи

В `data/relations/relations.d/cluster-linear-systems-constant-coefficients.yaml` добавлены связи от методического блока к ключевым representatives:

- `resit-pass-3-diagonal-linear-system`;
- `linear-system-jordan-block`;
- `cluster-linear-systems-jordan-geometric-two`;
- `waterloo-spiral-phase-portrait-isoclines`;
- `cluster-linear-systems-repeated-complex-four-dimensional`;
- `inhomogeneous-linear-system-variation`;
- `cluster-linear-systems-jordan-resonant-forcing`;
- `waterloo-fundamental-matrix-flow-inverse`;
- `cluster-matrix-exp-det-trace-shortcut`;
- `liouville-wronskian-formula`;
- `cluster-phase-stability-method-guide`.

Соседние кластеры связаны только через содержательные representative-карточки: `matrix-exponential-methods` через determinant/trace identity, `fundamental-matrix-linear-systems` через фундаментальную матрицу как поток, `phase-line-stability` через фазовую классификацию и устойчивость.

## Остаточные пробелы

Не добавлялись новые вычислительные монстры и однотипные задачи на очередную матрицу 2x2 или 3x3.

Возможный будущий пробел: короткая conceptual-card про спектральные проекторы или минимальный многочлен, если курс явно захочет этот язык. Сейчас этот материал намеренно не добавлен, чтобы не расширять базовый кластер за пределы стандартного маршрута.

Еще один возможный пробел: отдельный компактный пример на преобразование Лапласа для систем. В текущем кластере это не основной механизм и лучше добавлять только при появлении локального требования курса.
