# Студенческий аудит письменника: средний уровень хор(5)-хор(6)

Дата прохода: 2026-05-27. Роль: студент среднего уровня МФТИ, готовящийся к письменному экзамену и целящийся на хор(5)-хор(6).

Смотрел `index/generated.json`, `viewer/index.html` как представление того же индекса, программу `docs/reviews/local-du-program-8.md`, карточки с `idea_score` 5..6, тегами `exam_score_5`/`exam_score_6`, `middle_student_check` и пачку `cluster-mipt-middle-level`. Получился рабочий срез около 150 карточек; дальше я оценивал не полноту теории, а вопрос: "после этих карточек я смогу уверенно писать типовой письменник?"

## Короткий вывод

База в целом закрывает стандартные шаблоны хор(5)-хор(6), но слой не всегда выглядит как траектория подготовки к письменнику. Много сильных карточек являются теоретическими или обзорными, а некоторые реальные письменные шаблоны помечены слишком низким `exam_score` и поэтому могут не попасть студенту в подборку.

Главные риски:

- базовые письменные задачи по постоянным коэффициентам есть, но середина между "очень просто" и "олимпиадно/системы" выражена слабее, чем хотелось бы;
- Штурм покрыт хорошо, но заметно сдвинут в теоретические и продвинутые карточки;
- ЧП методом характеристик уже достаточно представлены, но одна хорошая письменная карточка ошибочно выглядит как `exam_score_3`;
- есть насыщенные кластеры, где новые похожие задачи уже не дают нового умения: угадывание решения по единственности, линеаризация равновесий, свободный конец в вариационном исчислении, простые жордановы клетки.

Новые карточки в этом проходе не добавлял: пробелы ниже лучше сначала закрывать перетегом/навигацией и только потом добавлять 1-2 точечных представителя.

## Покрытие письменных шаблонов

| Шаблон письменника | Хватает ли | Комментарий студента |
|---|---|---|
| Линейные ОДУ с постоянными коэффициентами | Скорее да, но слой 5-6 неровный | Есть `resit-pass-3-*`, `local-du-written-2014-51-constant-coeff-third-order`, резонансные карточки и системные примеры. Но для хор(5)-хор(6) хочется один явно письменный скалярный пример на квазимногочлен/резонанс без ухода в 6-мерные системы или олимпиаду. |
| Линейные ОДУ с переменными коэффициентами | Да | Хорошо работают `cluster-linear-variable-variation-parameters-fundamental-system`, `cluster-linear-variable-inhomogeneous-three-solutions`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2024-linear-y-xu-reduction`, Лиувилль/Вронскиан. |
| Вариация постоянных | Да | Есть и формула для уравнения, и `mipt-middle-cauchy-formula-variable-system` для систем. Для письменника важно не перепутать формульную карточку с вычислительной тренировкой, но прием закрыт. |
| Системы с постоянными коэффициентами | Да | Сильное покрытие: `linear-system-jordan-block`, `local-du-written-2014-51-system-jordan-zero`, `cluster-linear-systems-*`, `oral-middle-triangular-system-jordan`. Риск уже не в пробеле, а в дублях. |
| Жордановы клетки | Да, даже с запасом | Есть обычная клетка, клетка при нулевом собственном, геометрическая кратность 2, резонансная правая часть. Новые задачи на те же клетки лучше не добавлять. |
| Краевые задачи | Достаточно | База покрывает Дирихле, смешанные условия, резонанс, собственные значения, энергетический запрет, Робин/Грин. Для хор(5)-хор(6) лучше показывать подборку от `dirichlet-eigenvalues-interval` к `oral-middle-mixed-boundary-eigenvalues` и `local-du-filippov-763-dirichlet-resonance-no-solution`. |
| Штурм на базовом уровне | Формально да, практически немного top-heavy | Есть стандартные теоремы и локальные T-задачи, но часть карточек сразу `idea_score` 7..9. Для студента полезна отдельная "базовая дорожка": разделение нулей, сравнение, один явный пример на нуль/запрет второй краевой точки. |
| Устойчивость | Да | Есть фазовая прямая, линеаризация, прямой метод Ляпунова, фазовые портреты. Для письменника достаточно; новые числовые системы с тем же Якобианом уже лишние. |
| Интегрирующие множители | Да | Есть `mu(x)`, `mu(y)`, `mu(xy)`, точные формы, линейные первого порядка. `cluster-integrating-factor-mu-xy` полезна, но это верхний край письменника, а не базовый шаблон. |
| Вариационное исчисление | Да | Закрепленные концы, свободные концы, естественные условия, трансверсальность, изопериметрия, высшие производные, две функции. Риск дублей по свободному концу уже высокий. |
| PDE характеристики | Да, но нужна правка видимости | Есть `local-du-deficit-first-order-pde-characteristics`, `local-du-written-2014-51-characteristics-pde`, `lebl-diffyqs-*`. Карточка `local-du-written-2023-characteristics-plane-data` выглядит как хорошая хор(5) письменная задача, но имеет `exam_score_3`. |

## Кандидаты на правку сложности

| Карточка | Сейчас | Что кажется не так |
|---|---:|---|
| `local-du-written-2023-characteristics-plane-data` | `idea_score=5`, `technical_score=4`, `exam_score_3` | Для письменника это не тройка: нужно найти два инварианта и корректно протащить данные с плоскости. Я бы поднял до `exam_score_5`. |
| `local-du-written-2014-51-system-jordan-zero` | `idea_score=5`, `technical_score=5`, `exam_score_4` | Жорданова клетка при нулевом собственном и присоединенный вектор - нормальная хор(5) задача. `exam_score_5` выглядит честнее. |
| `local-du-written-2024-affine-linear-solution-space` | `idea_score=6`, `technical_score=4`, `exam_score_4` | Структурная задача про неоднородное линейное уравнение и Вронскиан сложнее обычного счета; для письменника скорее `exam_score_5`, возможно 6 при строгой проверке объяснений. |
| `oral-middle-mixed-boundary-eigenvalues` | `idea_score=7`, `technical_score=3`, `exam_score_6` | Как письменный шаблон резонансной краевой задачи это скорее `idea_score=6`: идея стандартная, техника короткая. `exam_score_6` нормален. |
| `ru-misc-kfu-2015-15-4` | `idea_score=4`, `technical_score=5`, `exam_score_6` | Для хор(6) может быть завышено: после вычисления внутреннего интеграла остается одно интегрирование. Я бы считал это `exam_score_5`, если нет дополнительной ловушки про область. |
| `cluster-integrating-factor-mu-xy` | `idea_score=6`, `technical_score=2`, `exam_score_6` | Оценка идеи нормальная, но как письменный шаблон это "продвинутый множитель", а не обязательный средний минимум. В подборке хор(5) его лучше показывать после `mu(x)`/`mu(y)`. |

Не считаю ошибкой, что `local-du-written-2014-51-equilibrium-linearization` и `local-du-written-2022-nonlinear-equilibria-linearization` имеют `idea_score=4` при `exam_score_5`: идея стандартная, письменная сложность там в алгебре, производных и аккуратном рисунке.

## Дубли и насыщенные кластеры

Здесь я не предлагаю удалять карточки: многие нужны как разные уровни или разные источники. Но как студент я бы не хотел, чтобы подборка письменника выдала больше двух почти одинаковых задач подряд.

| Кластер | Примеры | Что делать |
|---|---|---|
| "Угадать решение и сослаться на единственность" | `cluster-guess-cauchy-autonomous-equilibrium`, `cluster-guess-cauchy-designed-straight-line`, `cluster-guess-cauchy-nonlinear-oscillator-zero`, `cluster-guess-cauchy-pendulum-inverted-equilibrium`, `cluster-guess-cauchy-system-diagonal-invariant` | Для письменника достаточно 1-2 представителей. Остальные полезны как вариации, но не как новая техника. |
| Линеаризация равновесий | `local-du-written-2014-51-equilibrium-linearization`, `local-du-written-2022-nonlinear-equilibria-linearization`, `cluster-phase-stability-linearization-hyperbolic`, `cluster-phase-stability-linear-plane-classification` | Не добавлять новые "найти равновесия и Якобиан", если нет нового типа: вырожденная линеаризация, функция Ляпунова, глобальный фазовый портрет. |
| Жордановы клетки | `linear-system-jordan-block`, `local-du-written-2014-51-system-jordan-zero`, `cluster-linear-systems-jordan-geometric-two`, `cluster-linear-systems-jordan-resonant-forcing`, `oral-middle-triangular-system-jordan` | Кластер уже полный для хор(5)-хор(6). Новые карточки должны отличаться смыслом, например матричная экспонента с параметром, а не только числами. |
| Свободные концы в вариационном исчислении | `local-du-standard-natural-boundary-conditions`, `cluster-variational-transversality-moving-endpoint`, `cluster-variational-euler-poisson-free-end`, `local-du-written-2014-51-free-endpoint-functional`, `local-du-written-2021-free-endpoint-cubic-variation`, `local-du-written-2024-variational-free-endpoint` | Не добавлять еще один свободный конец без нового условия. Лучше держать дорожку: натуральное условие -> письменная задача -> трансверсальность. |
| Штурм/нули | `local-du-standard-sturm-separation-zeros`, `local-du-standard-sturm-zero-spacing-corollaries`, `local-du-8-sturm-comparison-theorem`, `local-du-8-t5-critical-point-by-sturm`, `local-du-written-2007-81-sturm-zero` | Не дубль в строгом смысле, но студенту нужна сортировка по сложности. Сейчас легко прыгнуть с базовой теоремы в `idea_score=8`. |
| PDE характеристики | `local-du-deficit-first-order-pde-characteristics`, `local-du-written-2014-51-characteristics-pde`, `local-du-written-2023-characteristics-plane-data`, `lebl-diffyqs-damped-transport-characteristics`, `lebl-diffyqs-variable-coefficient-characteristics`, `lebl-diffyqs-characteristic-data-obstruction` | Покрытие достаточное. Добавлять стоит только если нужна русская локальная карточка с очень типовой нехарактеристической кривой/поверхностью. |

## Предложения по карточкам

В этом проходе я бы не добавлял новые карточки автоматически. Сначала полезнее поправить видимость уже существующих письменных задач:

1. Поднять `local-du-written-2023-characteristics-plane-data` до `exam_score_5`.
2. Поднять `local-du-written-2014-51-system-jordan-zero` до `exam_score_5`.
3. Рассмотреть `local-du-written-2024-affine-linear-solution-space` как `exam_score_5`.
4. В viewer/индексе для письменника сделать подборку "middle written path": постоянные коэффициенты -> переменные коэффициенты/Вронскиан -> системы/Jordan -> BVP/Штурм -> устойчивость -> вариационное -> PDE.

Если после этого все еще добавлять 1-2 карточки в `data/problems/student_pass/middle_written/`, я бы выбрал только такие:

| Кандидат | Зачем |
|---|---|
| `middle-written-constant-coeff-quasipolynomial-resonance` | Скалярное линейное ОДУ с постоянными коэффициентами и резонансной квазимногочленной правой частью уровня хор(5): мост между простыми `exam_score_3` и системными/олимпиадными задачами. |
| `middle-written-basic-sturm-application` | Очень прикладная задача на сравнение Штурма без Бесселя, Прюфера и длинной теории: показать существование/отсутствие нуля на отрезке через сравнение с синусом. |

Обе карточки стоит добавлять только после проверки, что они не дублируют уже выбранную дорожку в viewer. Сейчас база скорее нуждается в отборе и перетеге, чем в расширении.

## Итог для подготовки

Как студент на хор(5)-хор(6), я бы мог готовиться по базе, но мне нужен не весь средний слой, а отфильтрованная письменная дорожка. Лучшие уже имеющиеся опоры: `mipt-middle-cauchy-formula-variable-system`, `local-du-written-2014-51-system-jordan-zero`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2014-51-characteristics-pde`, `local-du-written-2024-variational-free-endpoint`, `cluster-integrating-factor-mu-y-short`, `oral-middle-mixed-boundary-eigenvalues`, `local-du-8-sturm-comparison-theorem`.

После небольшой правки `exam_score` у нескольких карточек база станет заметно честнее именно для письменного экзамена: меньше случайных провалов в "слишком легко" и меньше прыжков в "уже почти теория на отлично".
