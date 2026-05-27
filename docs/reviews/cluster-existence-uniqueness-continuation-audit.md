# Аудит кластера `existence-uniqueness-continuation`

Дата: 2026-05-27.

Зона: `data/task_clusters/clusters.yaml`, карточки с тегами и объектами `existence_uniqueness`, `picard_iteration`, `peano`, `continuation`, `gronwall`, `counterexample`, `global_solution`, `blow_up`, `one_sided_lipschitz`, `parameter_dependence`, а также соседние карточки, где эти идеи находятся только в `methods/objects/keywords`.

## Итог

Кластер не дефицитен по базовым темам, но прежняя политика была слишком узкой: в representatives было 14 карточек и почти не были явно видны blow-up, линейный рост, барьеры и регулярная неявная задача Коши. Добавлены 4 компактные карточки в `data/problems/cluster_audit/existence_uniqueness_continuation/`:

- `cluster-existence-linear-growth-global` - глобальное существование из линейного роста и Гронуолла.
- `cluster-existence-blow-up-alternative` - конечный конец максимального решения означает выход из любого компакта.
- `cluster-existence-inward-barrier-interval` - инвариантный отрезок и глобальность через барьер.
- `cluster-existence-implicit-ivp-local` - регулярная неявная задача Коши через теорему о неявной функции и Пикара-Линделефа.

## Точные попадания

Ядро кластера после аудита:

- Пикар-Линделеф и локальная единственность: `picard-lindelof-theorem`, `resit-pass-3-cauchy-uniqueness-check`, `mit-18034-pset05-picard-tail-estimate`, `mit-18034-pset05-second-order-picard-integral`.
- Пеано и потеря единственности: `peano-existence-theorem`, `weak-pass-nonunique-continuous-counterexample`, `oral-above-three-nonunique-nonlipschitz-delayed`.
- Продолжение и максимальные решения: `maximal-continuation-theorem`, `mipt-middle-maximal-solution-continuation`, `weak-pass-existence-interval-singular-coeff`, `oral-above-three-global-continuation-bounded-on-strips`, `local-du-written-2022-global-arctan-continuation`, `local-du-programs-other-years-riccati-global-continuation`.
- Глобальность через оценки: `local-du-filippov-239-one-sided-global-existence`, `local-du-filippov-240-radial-global-system`, `cluster-existence-linear-growth-global`.
- Blow-up и конечная непродолжимость: `cluster-existence-blow-up-alternative`, `blow-up-comparison-y-square`, `global-positive-impossible`, `ru-misc-nure-8-5`, `bounded-solution-y-prime-y-square`.
- Гронуолл и зависимость от данных: `gronwall-inequality`, `teschl-stanford-bridge-continuous-dependence-gronwall`, `oral-exam-excellent-gronwall-perturbed-solution`, `mit-18034-pset03-one-sided-lipschitz-gronwall`, `oral-exam-strong-10-one-sided-gronwall-uniqueness`.
- Барьеры и непересечение: `one-dimensional-autonomous-no-crossing`, `two-solutions-touching`, `oral-exam-excellent-nonautonomous-sign-barrier`, `cluster-existence-inward-barrier-interval`.
- Регулярная неявная IVP: `cluster-existence-implicit-ivp-local`.

## Источники

- Локальная программа МФТИ и локальные карточки покрывают базовые формулировки Пикара, Пеано, Гронуолла, продолжения, а также письменные задачи про ограниченную правую часть и барьерное продолжение.
- Филиппов уже представлен задачами 239* и 240*: это хорошие representatives для односторонних/радиальных априорных оценок, поэтому новые близкие задачи из Филиппова не добавлялись.
- Teschl, §2.4 и §2.6, использован для непрерывной зависимости, альтернативы продолжения и линейного роста.
- MIT OCW 18.034 уже дает Picard iteration и one-sided Lipschitz/Gronwall; новые MIT-задачи не нужны, чтобы не превратить кластер в набор однотипных Lipschitz checks.
- Lebl/Trench просмотрены как ориентиры первого курса и системной версии Picard/existence-uniqueness; дополнительных задач оттуда не добавлено, потому что соответствующие идеи уже покрыты или принадлежат соседним кластерам.

## Дефициты после аудита

Статус: `watch`, не `deficit`. Закрыты основные недостающие представители:

- blow-up alternative;
- линейный рост как стандартная достаточная теорема глобальности;
- барьерный первый выход;
- регулярная неявная задача Коши.

Осторожно добавлять в будущем:

- Carathéodory existence только если курс явно требует слабую/абсолютно непрерывную постановку;
- Osgood uniqueness/nonuniqueness только как один advanced representative;
- зависимость второго порядка по параметру лучше держать в `parameter-dependence-variational-equation`;
- вырожденные неявные уравнения лучше держать в `implicit-ode-discriminant`.

## Дубли-кандидаты

Удалений не делалось. Близкие пары для human review:

- `weak-pass-nonunique-continuous-counterexample` и `oral-above-three-nonunique-nonlipschitz-delayed`: один и тот же нелипшицев механизм, но разные уровни и степень параметризации отложенных решений.
- `maximal-continuation-theorem`, `mipt-middle-maximal-solution-continuation`, `cluster-existence-blow-up-alternative`: общая теорема, учебное доказательство через компактность и диагностическая отрицательная форма; оставить как разные роли.
- `mit-18034-pset03-one-sided-lipschitz-gronwall` и `oral-exam-strong-10-one-sided-gronwall-uniqueness`: близкие по методу, но MIT дает количественную оценку расстояния, oral card - чистую единственность.
- `local-du-written-2022-global-arctan-continuation`, `oral-above-three-global-continuation-bounded-on-strips`, `cluster-existence-linear-growth-global`: все используют продолжение, но различаются типом априорной оценки.
- `blow-up-comparison-y-square`, `global-positive-impossible`, `ru-misc-nure-8-5`, `bounded-solution-y-prime-y-square`: оставить как разные уровни и формы сравнения, новые задачи такого вида не добавлять без новой идеи.

## Граница с соседними кластерами

- Линейные графические задачи на единственность (`cluster-linear-variable-graph-*`, `weak-pass-wronskian-zero-dependence`, `oral-exam-geometry-linear-second-order-uniqueness`) считать близкими, но не точным ядром: их основной объект - линейные уравнения с переменными коэффициентами.
- `teschl-stanford-bridge-flow-derivative-variational-equation` и `local-du-written-2011-21-parameter-variations` полезны для зависимости от данных, но будущие пополнения такого типа должны идти в `parameter-dependence-variational-equation`.
- PDE/characteristics blow-up (`mipt-excellent-semilinear-characteristics-blowup`) не включать в этот кластер как representative: основной механизм там характеристики.
