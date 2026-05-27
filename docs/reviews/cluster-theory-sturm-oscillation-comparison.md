# Теоретико-методический блок: Штурм, сравнение, осцилляция и нули

Дата прохода: 2026-05-27. Зона: `sturm-oscillation-comparison`.

## Что добавлено

- Добавлена методическая карточка `cluster-sturm-method-guide` в `data/problems/cluster_audit/sturm_oscillation_comparison/`.
- Карточка помечена как `kind.primary = theorem`, `kind.secondary = task_cluster, method_guide, cluster_representative`, поэтому она индексируется как теоретический навигатор, а не как обычная вычислительная задача.
- Карточка добавлена в representatives кластера `sturm-oscillation-comparison` и в batch `cluster-sturm-oscillation-comparison`.
- В `data/relations/relations.d/cluster-sturm-oscillation-comparison.yaml` добавлены связи от guide-блока к ключевым теоремам, леммам, representative-задачам и соседним кластерам.

## Покрытые методы

- Теорема сравнения Штурма: когда есть порядок коэффициентов и эталонное уравнение с известными нулями.
- Теорема разделения нулей: когда сравниваются два решения одного уравнения через вронскиан и отношение решений.
- Дисконъюгированность на конечном отрезке: запрет двух нулей через сравнение с `y'' + C y = 0`, энергетическую идентичность при неположительном потенциале и расстояние между нулями синуса.
- Краевой нерезонанс: отсутствие ненулевого решения однородной задачи Дирихле как критерий существования и единственности двухточечной краевой задачи.
- Осцилляция и неосцилляция на бесконечном хвосте: повторение локальных сравнений и отличие хвостовых утверждений от конечной дисконъюгированности.
- Критерий Кнезера: асимптотическое сравнение с порогом `1/(4x^2)`.
- Угол Пруфера: выбор фазового описания, когда удобнее считать вращение и нули как прохождения угла через кратные `pi`.
- Графические и нулевые аргументы: отделены от общего кластера `linear-equations-variable-coefficients`; они включаются в Sturm-блок только при явной связи с нулями, вронскианом, единственностью или дисконъюгированностью.

## Источники

В guide-карточке добавлены 6 качественных ориентиров через существующий формат `sources`/`references`:

- `src-local-du-8-program-or-exam` как локальная программа МФТИ по теореме Штурма и следствиям.
- `src-romanko-problem-book` как русскоязычный задачный фон.
- `src-filippov-problem-book` как классический задачник по ДУ и краевым задачам.
- `src-teschl-ode-dynamical-systems` как открытая строгая теория.
- `src-stanford-math63cm-ode` как открытые lecture notes по Sturm-Liouville и фазовому счету нулей.
- `src-trench-ode-bvp` как открытый учебник по boundary value problems и Sturm-Liouville problems.

## Relations

Добавлены связи от `cluster-sturm-method-guide` к:

- `local-du-8-sturm-comparison-theorem`;
- `local-du-standard-sturm-separation-zeros`;
- `local-du-standard-sturm-zero-spacing-corollaries`;
- `local-du-standard-oscillation-nonoscillation-tests`;
- `local-du-standard-kneser-criterion`;
- `cluster-sturm-disconjugacy-strict-upper-bound-lemma`;
- `cluster-sturm-dirichlet-nonresonance-interpolation-lemma`;
- `cluster-sturm-bvp-unit-endpoints-exact-bound`;
- `local-du-written-2007-81-sturm-zero`;
- `local-du-romanko-sturm-short-interval-bvp`;
- `mit-18034-pset08-prufer-oscillation-criteria`;
- `teschl-stanford-bridge-sturm-liouville-zero-count-phase`;
- соседним representative-карточкам `dirichlet-eigenvalues-interval`, `liouville-wronskian-formula`, `cluster-linear-variable-graph-ratio-maximum`.

## Оставшиеся пробелы

- Нет отдельного определения `disconjugacy` или `nonoscillation`; новые определения не добавлялись намеренно, чтобы не конфликтовать с текущим слоем определений.
- Блок не расширяет high-order zero-count: такие задачи стоит добавлять только при полностью проверенном решении.
- Сопряженные точки остаются на границе с вариационным Jacobi-блоком; отдельную связь можно усилить позже, если появится явная Sturm-Jacobi карточка вне вариационного исчисления.
- Видеолекции именно по Sturm comparison в локальной МФТИ-зоне не добавлены: текущий набор опирается на локальную программу, русские задачники и открытые конспекты/учебники.

## Проверки

После добавления карточки, relations и пересборки выполнен полный требуемый набор:

```powershell
python tools\build_index.py
python tools\validate.py
python tools\check_links.py
python tools\check_encoding.py
python tools\check_clusters.py
python tools\build_viewer.py
```

Все проверки прошли успешно.
