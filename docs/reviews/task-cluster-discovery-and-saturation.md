# Discovery новых кластеров и перегруженность типовыми задачами

Дата прохода: 2026-05-27.

Зона: `data/task_clusters/clusters.yaml`, `docs/TASK_CLUSTERS.md`, обязательные review-документы, все карточки `data/problems/**`, `data/taxonomy/tags.yaml`.

## Что изменено

- В `clusters.yaml` уже был добавлен параллельным аудитом кластер `linear-equations-variable-coefficients`; я его не перезаписывал и работал вокруг его политики.
- Добавлены новые кластеры:
  - `sturm-oscillation-comparison`;
  - `green-functions-bvp`;
  - `first-integrals-plane-systems`;
  - `pde-characteristics-first-order`;
  - `riccati-bernoulli-reductions`;
  - `existence-uniqueness-continuation`;
  - `floquet-periodic-linear-systems`;
  - `parameter-dependence-variational-equation`;
  - `recover-ode-from-family`;
  - `implicit-ode-discriminant`.
- Новые карточки не создавались и старые карточки не удалялись.

## Вывод

База уже не выглядит дефицитной по базовым вычислительным типам. Главный риск теперь - перегрузка однотипными задачами: линейные первого порядка, Бернулли/Риккати, постоянные коэффициенты, Sturm-нуль/сравнение, вариационное исчисление, phase portrait/stability. Новые кластеры нужны не для массового импорта, а как тормоза: они фиксируют, когда похожую карточку лучше не добавлять.

Наиболее полезные новые границы:

- `sturm-oscillation-comparison` отделяет нули/сравнение от saturated `boundary-spectral-problems`.
- `green-functions-bvp` отделяет Green kernel/identity от спектральной BVP и общей вариации постоянных.
- `floquet-periodic-linear-systems` отделяет монодромию периодических систем от постоянных матриц.
- `parameter-dependence-variational-equation` отделяет sensitivity/variational equation от общего existence/Gronwall.
- `riccati-bernoulli-reductions` отделяет нелинейную редукцию от прямого `linear-first-order-ode`.

## Перегруженность по кластерам

Оценки ниже приблизительные: `exact` - карточки, которые попадают в ядро кластера; `close` - ближайшие соседи, которые нужно учитывать при дедупликации.

| cluster | статус | exact / close | перегруженные шаблоны | остающиеся дефициты |
|---|---:|---:|---|---|
| `simple-variational-calculus` | watch | 18 / 18+ | Euler-Lagrange с фиксированными/свободными концами, квадратичные функционалы, higher derivatives | только редкие механизмы: несколько связей, нетривиальная регулярность, новая transversality |
| `linear-first-order-ode` | watch | 6 / 30+ | прямой integrating factor, cooling/forcing, disguised first-order linear | почти не дефицитен; Riccati/Bernoulli и PDE вынесены отдельно |
| `linear-equations-variable-coefficients` | watch | 20 / 25+ | Wronskian/Abel, reduction of order, графические касания, affine solution space | редкие A(t) fundamental matrix и особые точки без ухода в Sturm/Floquet |
| `integrating-factor-exact-forms` | active | 4 / 13+ | exact forms и integrating factor по x/y | один-два нестандартных integrating-factor criteria, но без массового импорта |
| `constant-coefficient-linear-systems` | watch | 12 / 20+ | Jordan, matrix exponential, 2x2 phase portraits, resonant forcing | почти насыщен; Floquet и variable coefficients вынесены отдельно |
| `boundary-spectral-problems` | saturated | 6 / 20+ | eigenvalues for interval BVP, resonance, weighted orthogonality | низкий дефицит; Green kernel и Sturm-нуль вынесены отдельно |
| `phase-line-stability` | watch | 18 / 30+ | phase-line signs, 2x2 portraits, Lyapunov definitions, linearization | только редкие bifurcation/barrier tasks; не добавлять массовые portraits |
| `variation-of-constants` | watch | 6 / 15+ | scalar/system variation of parameters, resonant forcing | сузить будущие добавления: Green, Floquet, sensitivity имеют свои кластеры |
| `sturm-oscillation-comparison` | saturated | 16 / 25+ | comparison with sin, separation, zero spacing, Pruefer, Bessel zeros | low: сопряженные точки или higher-order zero-count с полноценным решением |
| `green-functions-bvp` | watch | 7 / 8+ | кусочное Green kernel, Robin/mixed example, Green identity | знак Green function, maximum principle, singular BVP |
| `first-integrals-plane-systems` | watch | 10 / 16+ | energy ovals, Lotka-Volterra, first-integral center, periodic levels | несколько интегралов, сепаратрисы, полный глобальный портрет |
| `pde-characteristics-first-order` | watch | 7 / 7+ | transport shift, variable speed, damping, characteristic data obstruction | low: квазилинейный пример и higher-dimensional invariants |
| `riccati-bernoulli-reductions` | watch | 10 / 10+ | Bernoulli substitution, Riccati with known solution, hidden Riccati | low: qualitative Riccati and Riccati-to-second-order |
| `existence-uniqueness-continuation` | watch | 29 / 30+ | Picard/Peano, Lipschitz checks, nonunique counterexamples, continuation, Gronwall | medium: blow-up alternative, implicit IVP, nontrivial parameter dependence |
| `floquet-periodic-linear-systems` | watch | 5 / 5+ | monodromy iteration, determinant, multiplier stability, periodic forcing | Hill/Mathieu-like scalar example and multiplier 1 solvability |
| `parameter-dependence-variational-equation` | watch | 8 / 8+ | derivative by parameter, variational equation, regular perturbation, Gronwall dependence | second derivative of flow, loss of differentiability |
| `recover-ode-from-family` | active | 2 / 2+ | differentiate and eliminate parameter | one geometric tangent/envelope variant at most |
| `implicit-ode-discriminant` | deficit | 1 / 3+ | discriminant F=0, F_p=0 | branch switching and singular solution outside standard Clairaut/Lagrange |

## Кандидаты и решения

- `linear-equations-variable-coefficients`: уже был создан параллельным агентом. Учитывал его как existing cluster, не редактировал.
- `sturm-oscillation-comparison`: создан. Реальная польза высокая, потому что Sturm-нуль/сравнение иначе конфликтуют с `boundary-spectral-problems`.
- `green-functions-bvp`: создан. Реальная польза средняя, но важная для Trench/BVP imports: Green kernel не должен теряться в variation-of-constants.
- `first-integrals-plane-systems`: создан. Нужен, чтобы не смешивать first-integral geometry с общим phase-stability.
- `pde-characteristics-first-order`: создан. Тема уже близка к насыщению, поэтому кластер нужен именно как ограничитель дублей.
- `riccati-bernoulli-reductions`: создан. Это частый источник учебных дублей, отдельная политика полезнее, чем держать все в `linear-first-order-ode`.
- `existence-uniqueness-continuation`: создан. Широкий, но уже перегруженный блок, где нужна единая политика остановки однотипных Lipschitz/Peano/Gronwall cards.
- `floquet-periodic-linear-systems`: создан. Не конфликтует с constant-coefficient systems: ключевой объект - monodromy for periodic A(t).
- `parameter-dependence-variational-equation`: создан. Отделяет цель sensitivity от технической variation-of-constants.
- `recover-ode-from-family`: создан как малый active cluster с target 3.
- `implicit-ode-discriminant`: создан как малый deficit cluster, потому что текущий representative один, но тип задач не должен сливаться с обычным Clairaut.

## Близкие дубли для будущих аудитов

Удалений не делалось. Для human review стоит держать следующие группы:

- `weak-pass-resonance-double-root` и `constant-coeff-second-order-resonance`: близкие scalar constant-coeff resonance cards.
- `trench-bvp-dirichlet-resonance-sine-condition` и `trench-bvp-resonance-solvability-alternative`: частный пример против общей Fredholm alternative.
- Teschl Floquet chain: `floquet-determinant-liouville`, `monodromy-period-iterate`, `floquet-multiplier-stability`; полезная цепочка, но будущие добавления должны быть очень точечными.
- Lebl characteristics cards: `transport-signal-shift`, `damped-transport-characteristics`, `variable-coefficient-characteristics`, `characteristic-data-obstruction`; не дубли, но тема уже насыщается.
- Bernoulli cards: `bernoulli-standard`, `resit-pass-3-bernoulli-initial`, `weak-pass-bernoulli-substitution`, `oral-middle-bernoulli-log-term`; оставить как разные уровни, но не добавлять еще такие же.
- Riccati known-solution cards: `riccati-known-solution`, `oral-above-three-riccati-shift-known-solution`, `oral-middle-riccati-known-inverse-x`; близки по механизму.
- Reduction of order cards: `oral-above-three-reduction-order-known-solution` и `oral-exam-excellent-reduction-of-order-nonzero-solution`.
- Phase visual cards против вычислительных portraits: `weak-pass-linear-system-saddle` vs visual saddle, `waterloo-spiral-phase-portrait-isoclines` vs visual sink.
- Waterloo recover-family pair: `waterloo-family-circles-recover-ode` и `waterloo-log-family-qualitative-recover`; не дубли, но достаточно как representatives малого кластера.

## Практическая политика дальше

1. Не добавлять новые карточки в saturated или near-saturated зоны, если меняются только коэффициенты.
2. Для будущих imports сначала искать ближайший кластер по механизму, а не по теме курса.
3. Если карточка попадает сразу в два кластера, выбирать более узкий: Floquet вместо constant systems, Green kernel вместо variation-of-constants, Sturm zeros вместо boundary spectral, parameter dependence вместо general Gronwall.
4. Новые deficit cards допустимы только точечно: `implicit-ode-discriminant`, rare Green-sign/maximum-principle, branch switching, nontrivial parameter regularity.

