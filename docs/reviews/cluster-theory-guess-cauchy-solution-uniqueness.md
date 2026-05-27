# Методический блок кластера `guess-cauchy-solution-uniqueness`

Дата: 2026-05-27.

Зона работ: кластер `guess-cauchy-solution-uniqueness`, методический блок, связи и источники. Новые вычислительные задачи не добавлялись.

## Что добавлено

- Создана карточка `cluster-guess-cauchy-method-guide` в `data/problems/cluster_audit/guess_cauchy_solution_uniqueness/cluster-guess-cauchy-method-guide.yaml`.
- Карточка помечена как теория и методический блок: `kind.primary=theorem`, secondary `task_cluster`, `method_guide`, `theory_bridge`.
- В `data/task_clusters/clusters.yaml` карточка добавлена в `representative_card_ids` кластера, поэтому индексируется с cluster id `guess-cauchy-solution-uniqueness`.
- В `data/import_batches/cluster-guess-cauchy-solution-uniqueness.yaml` блок добавлен в список batch-карточек и отмечен как теория, а не новая вычислительная задача.

## Покрытые методы

- Поиск простого кандидата по данным Коши: равновесие, нулевое решение, прямая `y=t`, движение на инвариантной диагонали/плоскости, симметричная или специально видимая траектория.
- Отказ от общего решения, если конкретная задача Коши уже закрывается подстановкой и единственностью.
- Проверка условий теоремы единственности: нормальная форма `z'=F(t,z)`, область определения, локальная липшицевость по фазовым переменным, `C^1` как достаточный критерий, переход от уравнения высокого порядка к системе первого порядка.
- Продолжение локального совпадения на общий интервал существования через повторное применение локальной единственности.
- Граница метода при нелипшицевости: угаданное решение может существовать, но не быть единственным; типовой сценарий - отложенные решения для `y'=c|y|^alpha`, `0<alpha<1`.
- Примеры и маршруты для первого порядка, систем, нелинейного осциллятора и математического маятника.

## Определения и источники

Новые определения не добавлялись. В карточке использованы `definition_ids`:

- `initial_value_problem`, `cauchy_problem`;
- `solution`, `integral_curve`;
- `equilibrium`;
- `maximal_solution`;
- `lipschitz_condition`;
- дополнительно `ordinary_differential_equation`, `general_solution`, `particular_solution`, `autonomous_equation`, `phase_trajectory`.

Источники в принятом формате добавлены прямо в карточку и references:

- `src-mipt-ode-course`;
- `src-filippov-problem-book`;
- `src-romanko-problem-book`;
- `src-teschl-ode-dynamical-systems`;
- `src-lebl-diffyqs`;
- `src-arnold-ode`.

## Связи

В `data/relations/relations.d/cluster-guess-cauchy-solution-uniqueness.yaml` добавлены связи:

- от `picard-lindelof-theorem`, `peano-existence-theorem`, `maximal-continuation-theorem` к методическому блоку;
- от `cluster-existence-uniqueness-continuation-method-guide` к специализированному блоку;
- от `cluster-phase-stability-method-guide` к блоку для содержательной связи через автономные равновесия;
- от `cluster-guess-cauchy-method-guide` к representative-задачам: автономное равновесие, маятник, нелинейный осциллятор, инвариантная диагональ, прямая `y=t`, `one-dimensional-autonomous-no-crossing`, `two-solutions-touching`, `written-mipt-2000-cauchy-p-of-y-guess`.

## Индексация

После `python tools/build_index.py` карточка найдена в `index/generated.json`:

- `id`: `cluster-guess-cauchy-method-guide`;
- `kind`: `theorem`;
- `secondary_kinds`: `task_cluster`, `method_guide`, `theory_bridge`;
- `cluster_ids`: `guess-cauchy-solution-uniqueness`;
- `in_cluster_reps`: `true`.

## Проверки

- `python tools/build_index.py` - OK, индекс пересобран.
- `python tools/validate.py` - FAILED на чужой зоне `cluster-implicit-ode-discriminant-method-guide.yaml`: неизвестные теги `implicit_ode`, `discriminant_curve`, `singular_solution`, `branch_switching`. Ошибок по новому блоку нет.
- `python tools/check_links.py` - OK.
- `python tools/check_encoding.py` - OK.
- `python tools/check_clusters.py` - OK.
- `python tools/build_viewer.py` - OK, viewer и корневой `index.html` пересобраны.
- `python tools/audit_rules.py --max-items 80` - OK с 4 предупреждениями в чужих карточках про `exam_score tag with technical_score > 5`.

## Оставшиеся пробелы

- Нет отдельного реального источникового примера с формулировкой "не находя общего решения"; текущие representative-модели закрывают метод, а `written-mipt-2000-cauchy-p-of-y-guess` остается ближайшим экзаменационным мостом.
- Симметричная задача Коши пока описана в методическом блоке как вариант, но не выделена отдельной representative-карточкой, чтобы не добавлять новые задачи без необходимости.
- Нелипшицевость покрыта как граница метода и связана с широким existence-uniqueness слоем, но не расширялась новой counterexample-карточкой.
