# Теоретико-методический блок parameter-dependence-variational-equation

Дата: 2026-05-27.

## Что добавлено

Добавлена карточка `cluster-parameter-dependence-method-guide` в `data/problems/cluster_audit/parameter_dependence_variational_equation/`.

Карточка помечена как `theorem` с secondary-метками `task_cluster`, `method_guide`, `cluster_representative`, поэтому индексируется как теоретико-методический блок, а не как новая вычислительная задача.

В `data/task_clusters/clusters.yaml` блок добавлен в `representative_card_ids` кластера `parameter-dependence-variational-equation`; batch `cluster-parameter-dependence-variational-equation` тоже обновлен.

## Покрытые методы

- Дифференцирование задачи Коши по параметру через интегральную форму.
- Уравнение чувствительности `z'=D_x f z+f_lambda` с начальными данными `z(t0)=xi'(lambda)`.
- Зависимость от начальной точки и вариационное уравнение потока `U'=D_x f(t,phi)U`, `U(t0)=I`.
- Связь вариационного уравнения с фундаментальной матрицей вдоль траектории.
- Непрерывная и липшицева зависимость через оценку разности решений и неравенство Гронуолла.
- Переход от уравнений второго порядка к системе первого порядка перед дифференцированием.
- Регулярные возмущения: первая поправка как неоднородное вариационное уравнение, второй порядок как отдельный conceptual-variant.
- Граница с соседями: existence-uniqueness-continuation дает базовую корректность и Гронуолла; fundamental-matrix-linear-systems дает язык фундаментальной матрицы; linear-equations-variable-coefficients дает технику решения получившейся линейной задачи.

## Definition ids и связи

В методическом блоке использованы существующие `definition_ids`, без дублирования слоя `data/definitions/definitions.yaml`:

- `ordinary_differential_equation`, `solution`;
- `initial_value_problem`, `cauchy_problem`;
- `linear_system`, `fundamental_matrix`;
- `gronwall_inequality`, `lipschitz_condition`;
- `variation_of_constants_system`.

Отдельных definition ids для `variational_equation` и `continuous_dependence` в текущем definitions-layer нет; вместо добавления новых определений поставлены relations к theorem-карточкам:

- `teschl-stanford-bridge-flow-derivative-variational-equation`;
- `teschl-stanford-bridge-continuous-dependence-gronwall`;
- `gronwall-inequality`;
- `cluster-parameter-sensitivity-equation-theorem`.

Relations добавлены также к representative-задачам кластера и к содержательным соседям:

- `cluster-existence-uniqueness-continuation-method-guide`;
- `waterloo-fundamental-matrix-flow-inverse`;
- `cluster-linear-variable-method-guide`.

## Источники

В карточку добавлены 6 источников в принятом формате `sources`/`references`:

- `src-local-du-8-program-or-exam`;
- `src-romanko-problem-book`;
- `src-filippov-problem-book`;
- `src-teschl-ode-dynamical-systems`;
- `src-mit-18034-honors-ode`;
- `src-mit-1803sc-ode`.

## Что не добавлялось

Новые вычислительные задачи не добавлялись. Существующие сложности задач массово не менялись.

Не создавались новые определения для вариационного уравнения и непрерывной зависимости: для этого лучше отдельный definitions-layer audit, чтобы не плодить почти-дубли к theorem-карточкам.

## Оставшиеся пробелы

- Аккуратный пример потери дифференцируемости по параметру при сохранении непрерывной зависимости.
- Короткий негладкий пример, где Гронуолл дает только оценку, но sensitivity equation неприменимо.
- Более явная локальная карточка по второй производной потока, если понадобится связать этот блок с устойчивыми/неустойчивыми многообразиями без захода в отдельную динамическую теорию.
