# Аудит кластера вариационного исчисления

Дата: 2026-05-26.

Зона: `simple-variational-calculus` / «Простейшая задача вариационного исчисления» и ближайшие расширения. Файлы новых карточек: `data/problems/cluster_audit/variational_calculus/`. Связи добавлены только в `data/relations/relations.d/cluster-variational-calculus.yaml`, batch - `data/import_batches/cluster-variational-calculus.yaml`.

## Что просмотрено

- `data/task_clusters/clusters.yaml`
- `docs/TASK_CLUSTERS.md`
- `docs/reviews/local-du-gap-and-dedup-report.md`
- `docs/reviews/local-du-romanko-selection.md`
- `docs/reviews/english-import-qa.md`
- карточки и профили с `variational_calculus`, `euler_lagrange`, `euler_poisson`, `natural_boundary_conditions`, `transversality`, `isoperimetric_problem`, `legendre_condition`, `jacobi_condition`, `second_variation`, `higher_derivatives_functional`.

## Итог по кластеру

`simple-variational-calculus` оставлен в статусе `watch`, но его representatives и политики расширены. В кластер притянуты точные представители:

| тип | representative cards |
|---|---|
| фиксированные концы / базовый Эйлер-Лагранж | `local-du-standard-euler-lagrange-fixed-endpoints`, `local-du-written-2020-variational-log-cross-term` |
| свободный конец / натуральные условия | `local-du-standard-natural-boundary-conditions`, `local-du-written-2014-51-free-endpoint-functional`, `local-du-written-2021-free-endpoint-cubic-variation`, `local-du-written-2024-variational-free-endpoint` |
| подвижный конец / трансверсальность | `cluster-variational-transversality-moving-endpoint` |
| изопериметрия | `local-du-romanko-isoperimetric-linear-constraint`, `local-du-romanko-isoperimetric-energy-normalization` |
| несколько функций | `local-du-romanko-variational-two-functions` |
| высшие производные / Эйлер-Пуассон | `local-du-romanko-variational-higher-derivative`, `cluster-variational-euler-poisson-fixed`, `cluster-variational-euler-poisson-free-end`, `cluster-variational-euler-poisson-general-order` |
| Лежандр, Якоби, вторая вариация | `local-du-standard-legendre-jacobi-conditions`, `local-du-romanko-jacobi-strict-maximum`, `local-du-deficit-variational-quadratic-threshold` |
| глобальная квадратичная теория | `cluster-variational-quadratic-coercive-minimizer` |

Добавлены точные навигационные теги `euler_poisson`, `higher_derivatives_functional`, `second_variation`, `legendre_condition`, `jacobi_condition`; ими помечены новые карточки и ближайшие существующие представители Романко/стандартной теории.

## Новые карточки

| id | роль |
|---|---|
| `cluster-variational-euler-poisson-fixed` | вывод уравнения Эйлера-Пуассона для `F(x,y,y',y'')` при закрепленных `y,y'` на концах |
| `cluster-variational-euler-poisson-free-end` | обязательная карточка: функционал со второй производной и одним свободным правым концом; вывод уравнения и двух естественных граничных условий |
| `cluster-variational-euler-poisson-general-order` | общая формула Эйлера-Пуассона для производных до порядка `m` |
| `cluster-variational-transversality-moving-endpoint` | компактная модельная задача на подвижный правый конец и трансверсальность |
| `cluster-variational-quadratic-coercive-minimizer` | обязательная теорема о существовании, единственности и глобальном минимуме строго выпуклого квадратичного функционала |

## Квадратичная теорема

Ближайшие родственники в базе:

- `local-du-written-2020-variational-log-cross-term`: конкретный положительно-квадратичный пример с фиксированными концами и проверкой минимума.
- `local-du-deficit-variational-quadratic-threshold`: контрастный пример, где знак второй вариации зависит от спектрального порога.
- `local-du-standard-euler-lagrange-fixed-endpoints`: теоретический prerequisite для вывода линейной краевой задачи.

Интернет-поиск точного аналога нормировки

`J[y]=int_a^b (y'^2+q(x)y^2+f(x)y+g(x)y'+r(x)) dx`, `q>0`,

не дал надежного точного источника, поэтому точная постановка в карточке помечена как авторская: М. Дидин. Как внешний надежный источник общей теории добавлен `src-calder-calculus-variations-notes`: J.W. Calder, *The Calculus of Variations*, Chapter 4.4, Theorems 4.25-4.26 and Remark 4.27, где используются прямой метод, коэрцитивность, выпуклость и единственность минимизатора. URL: https://www-users.cse.umn.edu/~jwcalder/CalculusOfVariations.pdf

В карточке доказано:

- коэрцитивность после перехода к `H_0^1`;
- строгая выпуклость функционала;
- существование и единственность глобального минимизатора;
- связь с краевой задачей Эйлера-Лагранжа
  `-y''+q(x)y=(g'(x)-f(x))/2`, `y(a)=A`, `y(b)=B`;
- энергетическая единственность этой краевой задачи.

## Дедупликация

Удалений не выполнялось. Внутри кластера есть несколько задач со свободным концом, но они не являются безопасными чистыми дублями:

- `local-du-written-2014-51-free-endpoint-functional` - базовый письменный представитель;
- `local-du-written-2021-free-endpoint-cubic-variation` - вырожденный кубический функционал и первый интеграл;
- `local-du-written-2024-variational-free-endpoint` - свободный конец с резонансной правой частью;
- `local-du-standard-natural-boundary-conditions` - теоретическая карточка, не вычислительная задача.

`local-du-written-2020-variational-log-cross-term` и новая квадратичная теорема близки по форме, но первая является конкретным расчетом, а вторая закрывает существование/единственность/глобальность в параметрическом классе. Вместо удаления добавлены связи и пометка ближайшего родства.

## Политика дальнейшего пополнения

Кластер теперь насыщен по базовым и ближайшим расширенным вариантам. Не добавлять новые карточки, если меняется только интегранд `F(x,y,y')`, коэффициенты квадратичной формы или элементарная правая часть. Добавлять имеет смысл только при новом механизме: несколько независимых изопериметрических связей, более геометрическая трансверсальность, нетривиальная теория регулярности/глобального минимума или качественно новый тест второй вариации.
