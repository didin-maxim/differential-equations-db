# Аудит подготовки к простому письменному экзамену глазами слабого студента

Дата прохода: 2026-05-27.

Роль проверки: слабый студент МФТИ, которому нужно уверенно закрыть минимум/3-4 на письменном экзамене по ДУ. Я смотрел не как автор базы, а как пользователь: могу ли я быстро найти простые письменные шаблоны, понять, что учить первым, и не утонуть в теории/олимпиадных карточках.

Использованы: `index/generated.json`, `viewer/index.html`, `docs/reviews/local-du-program-8.md`, предыдущий аудит `docs/reviews/basic-mipt-minimum-difficulty-audit.md`, карточки с `exam_score_3`, `exam_score_4`, `low_technical`, `weak_student_check`, `resit_exam`, а также локальные письменные карточки.

## Итог

По базе можно подготовиться к простым письменным задачам на 3/4, если уже понимать, какие id искать. Нижний слой задач есть почти по всем нужным темам: разделяющиеся, линейное первого порядка, точные, Бернулли, постоянные коэффициенты, фазовая прямая, простая краевая, ряды, простейшая вариация постоянных и характеристики PDE.

Главная проблема не в математике, а в маршруте. Для слабого студента база сейчас больше похожа на склад хороших карточек, чем на тренировочный лист: минимальные задачи смешаны с устными, теоретическими, олимпиадными и `advanced_standard_course`; некоторые простые письменные темы закрыты одной карточкой или карточкой с неочевидным расположением.

Новых карточек я не добавлял: сначала нужен отчет и согласование, потому что очевидный дефицит есть, но он лучше решается маленькой серией тренировочных карточек, а не одной случайной.

## Что Закрыто

| Тема письменного минимума | Рабочие карточки | Оценка глазами слабого студента |
|---|---|---|
| Разделяющиеся | `resit-pass-3-separable-exponential-growth`, `separable-logistic-equation` | Закрыто. Первая карточка очень хороша для старта, логистика - следующий шаг. |
| Линейное 1-го порядка | `resit-pass-3-linear-first-order-forcing`, `weak-pass-linear-method-choice`, `linear-first-order-formula` | Закрыто. Хорошо, что есть и алгоритм, и задача на распознавание метода. |
| Точные уравнения | `resit-pass-3-exact-equation-potential`, `weak-pass-exact-form-recognition`, `exact-equation-potential` | Закрыто. Достаточно для простого письменного уровня. |
| Интегрирующий множитель | `oral-above-three-integrating-factor-x-only`, `cluster-integrating-factor-mu-y-short`, `integrating-factor-y` | Частично закрыто. Есть `mu(x)`, но как слабый студент я бы не понял, что карточка `oral-above-three...` и есть мой базовый письменный шаблон. |
| Бернулли | `resit-pass-3-bernoulli-initial`, `weak-pass-bernoulli-substitution`, `bernoulli-standard` | Закрыто хорошо. |
| Простые постоянные коэффициенты | `resit-pass-3-constant-coeff-real-roots`, `resit-pass-3-undetermined-coefficients`, `weak-pass-resonance-double-root`, `constant-coeff-second-order-resonance` | Закрыто для старта. Для уверенности не хватает отдельной простой карточки на комплексные корни как обычную задачу Коши. |
| Системы 2x2 | `resit-pass-3-diagonal-linear-system`, `weak-pass-linear-system-saddle`, `linear-system-jordan-block`, `oral-middle-triangular-system-jordan` | Частично закрыто. Есть диагональная и жорданова, но нет очевидной простой 2x2 с недиагональной матрицей и двумя разными вещественными собственными значениями. |
| Фазовая прямая | `resit-pass-3-phase-line-logistic-signs`, `weak-pass-phase-line-semistable`, `autonomous-phase-line-stability` | Закрыто хорошо. |
| Простая краевая | `resit-pass-3-dirichlet-sine-bvp`, `weak-pass-mixed-bvp-eigenvalues`, `dirichlet-eigenvalues-interval`, `shooting-linear-bvp` | Закрыто. Есть и "все решения", и собственные значения. |
| Ряды на минимуме | `weak-pass-series-first-coefficients`, `power-series-airy-at-zero`, `regular-singular-euler-frobenius` | Закрыто на минимуме, но тренировочных задач мало. |
| Простейшая вариация постоянных | `basic-mipt-variation-constants-ypp-plus-y`, `variation-of-parameters-sine`, `cluster-linear-variable-variation-parameters-fundamental-system` | Закрыто. `basic-mipt...` очень полезна, но плохо видна как часть письменного маршрута. |
| Простейшая вариационная задача | `local-du-standard-euler-lagrange-fixed-endpoints`, `local-du-standard-natural-boundary-conditions`, `local-du-written-2021-free-endpoint-cubic-variation` | Теория закрыта, вычислительный минимум закрыт слабо. Для письменного экзамена нужна простая карточка "найти экстремаль для конкретного J". |
| Характеристики PDE | `lebl-diffyqs-transport-signal-shift`, `local-du-deficit-first-order-pde-characteristics`, `local-du-written-2023-characteristics-plane-data` | Закрыто, но навигационно не идеально: одна минимальная карточка из английского источника, одна локальная уже idea 6, одна письменная лежит во фрагменте `systems`. |

## Что Мешает Готовиться

1. Нет готового фильтра/маршрута "письменный минимум на 3/4".

   Я могу выбрать `exam_score_3` или `exam_score_4`, но тогда теряю важные базовые карточки без этих тегов: `linear-first-order-formula`, `exact-equation-potential`, `autonomous-phase-line-stability`, `shooting-linear-bvp`, `dirichlet-eigenvalues-interval`. Если выбрать `low_technical`, попадаются карточки с высокой идеей: `local-du-deficit-first-order-pde-characteristics`, `local-du-deficit-sturm-nonpositive-potential-bvp`, `local-du-deficit-variational-quadratic-threshold`, `cluster-existence-inward-barrier-interval`.

2. `basic_mipt_minimum` не выглядит как нормальный навигационный слой.

   В индексе видна карточка `basic-mipt-variation-constants-ypp-plus-y`, но у нее `cluster_ids: []`; через фильтр "Кластер" я не могу открыть "basic MIPT minimum". Предыдущий аудит существует как документ, но во viewer это не превращается в учебный маршрут.

3. Минимальные карточки разбросаны по "устный", "пересдача", "above_three", английские источники и локальные письменные.

   Например, для интегрирующего множителя мне нужна `oral-above-three-integrating-factor-x-only`, но название папки/тег `above_three_check` психологически говорит "это выше тройки". Для характеристик самый простой старт `lebl-diffyqs-transport-signal-shift`, но слабый студент может искать только локальные МФТИ-письменные карточки и пропустить его.

4. Во viewer сортировка помогает найти сложные карточки, но не простые.

   Есть `idea_score ↓` и `technical_score ↓`, а для подготовки на минимум нужен обратный режим: сначала `idea_score ↑`, `technical_score ↑`, затем `exam_score_3`, потом `exam_score_4`.

5. Одновременно выбрать несколько тегов штатно нельзя.

   Мне хочется фильтр вроде `exam_score_3` + `low_technical` + `written_exam` или `mipt_core` + `first_order_pde_characteristics`. Сейчас можно пользоваться поиском по словам, но для слабого студента это неочевидно и легко дает лишнее.

6. `tools/search.py` на Windows упал на Unicode-символе `μ` при поиске "интегрирующий множитель".

   Это не портит сами карточки, но для пользователя-аудитора это навигационная проблема: поиск дошел до `oral-above-three-integrating-factor-x-only`, затем сломался на печати карточки с `μ`.

## Непонятные Или Слишком Сложные Карточки Для Минимума

- `cluster-integrating-factor-mu-y-short`: математически нормальная, но для моей цели это уже не первая карточка. Нужно отдельно сказать, что сначала учить `oral-above-three-integrating-factor-x-only`, потом `mu(y)`.
- `integrating-factor-y`: имеет `idea_score=6`, `technical_score=5`; как первый интегрирующий множитель она слишком тяжелая.
- `local-du-deficit-first-order-pde-characteristics`: хорошая и полезная, но `idea_score=6`; как первая карточка на PDE лучше `lebl-diffyqs-transport-signal-shift`.
- `local-du-deficit-sturm-nonpositive-potential-bvp`: `low_technical`, но идея 7. Для письменного минимума это не "легкая краевая", а доказательная задача.
- `local-du-deficit-variational-quadratic-threshold`: `low_technical`, но идея 7 и нужен спектральный порог/Пуанкаре. Это не простая вариационная задача для слабого студента.
- `local-du-filippov-763-dirichlet-resonance-no-solution`: полезная краевая резонансная задача, но как минимум она сложнее `resit-pass-3-dirichlet-sine-bvp` и `weak-pass-mixed-bvp-eigenvalues`.
- `local-du-written-2014-51-characteristics-pde`: настоящий письменный пример, но `exam_score_6`; для 3/4 его надо оставить как "после базовых характеристик", а не как старт.
- `local-du-standard-euler-lagrange-fixed-endpoints`: хорошая теорема, но она не заменяет простую вычислительную карточку на вариационное исчисление.

## Метаданные И Формулировки, Которые Сбивают

- `dirichlet-eigenvalues-interval`: в `differential_equations_profile.methods` стоит `series_recursion`, хотя решение идет разбором знака `lambda` и стандартным спектром Дирихле. Это сбивает поиск по рядам и краевым задачам.
- `local-du-written-2023-characteristics-plane-data`: `fragment` указан как `systems`, а тег содержит `linear_systems`, хотя это задача на линейное PDE первого порядка методом характеристик. Из-за этого она всплывает среди систем 2x2 и хуже находится как PDE.
- `local-du-written-2014-51-characteristics-pde`: в тегах есть `linear_first_order`, хотя фактически это линейное PDE первого порядка; лучше не смешивать с обычными линейными ОДУ первого порядка.
- `basic-mipt-variation-constants-ypp-plus-y`: карточка важная для минимума, но не имеет кластера/явного маршрута `basic_mipt_minimum` в viewer.
- `oral-above-three-integrating-factor-x-only`: по уровню годится на 4, но имя `above_three` может отпугнуть слабого студента. В отчете/маршруте стоит явно включить ее в письменный минимум.
- `regular-singular-euler-frobenius`: хорошая карточка, но для слабого студента слово "Фробениус" в названии звучит страшнее, чем сама задача Эйлера. Нужна подпись/маршрут: "это минимальный безопасный пример".

## Пропущенные Простые Темы

Самые полезные добавления, если расширять именно письменный минимум:

1. Простая недиагональная система 2x2 с двумя различными вещественными собственными значениями.

   Пример уровня 3/4: найти общее решение `x'=2x+y`, `y'=x+2y` через собственные векторы. Сейчас есть диагональная `resit-pass-3-diagonal-linear-system` и жорданова `linear-system-jordan-block`, но нет промежуточного "найти собственные векторы и собрать решение".

2. Простая задача на комплексные корни постоянных коэффициентов.

   Пример: решить `y''+y=0`, `y(0)=1`, `y'(0)=0` или `y''+2y'+2y=0`. Сейчас комплексные корни встречаются через краевую/энергию/неоднородную задачу, но отдельного письменного шаблона не хватает.

3. Простая вычислительная вариационная задача с фиксированными концами.

   Пример: найти экстремаль `J[y]=int_0^1 ((y')^2+y^2) dx`, `y(0)=0`, `y(1)=1`, без исследования Якоби/Пуанкаре. Теорема `local-du-standard-euler-lagrange-fixed-endpoints` есть, но слабому студенту нужна карточка "подставь F, получи ОДУ, реши краевую".

4. Минимальная карточка на интегрирующий множитель `mu(y)`.

   `cluster-integrating-factor-mu-y-short` уже близко, но стоит пометить/связать как второй шаг после `mu(x)` или добавить еще более учебную карточку с прямым критерием.

5. Еще одна рядовая карточка на первые 5-6 коэффициентов.

   `weak-pass-series-first-coefficients` хорошая, но одна. Для письменного навыка нужно хотя бы два похожих примера, чтобы не казалось, что это частный фокус.

## Рекомендуемый Мини-Маршрут В Текущей Базе

Если ничего не добавлять, я бы учил в таком порядке:

1. Первый порядок: `resit-pass-3-separable-exponential-growth` -> `resit-pass-3-linear-first-order-forcing` -> `weak-pass-linear-method-choice` -> `resit-pass-3-exact-equation-potential` -> `weak-pass-exact-form-recognition` -> `oral-above-three-integrating-factor-x-only` -> `resit-pass-3-bernoulli-initial`.
2. Линейные ОДУ: `resit-pass-3-constant-coeff-real-roots` -> `resit-pass-3-undetermined-coefficients` -> `weak-pass-resonance-double-root` -> `weak-pass-wronskian-zero-dependence` -> `basic-mipt-variation-constants-ypp-plus-y`.
3. Системы и фаза: `resit-pass-3-diagonal-linear-system` -> `weak-pass-linear-system-saddle` -> `linear-system-jordan-block` -> `resit-pass-3-phase-line-logistic-signs` -> `weak-pass-phase-line-semistable`.
4. Краевые и ряды: `resit-pass-3-dirichlet-sine-bvp` -> `weak-pass-mixed-bvp-eigenvalues` -> `weak-pass-series-first-coefficients` -> `regular-singular-euler-frobenius`.
5. PDE и вариационное: `lebl-diffyqs-transport-signal-shift` -> `local-du-deficit-first-order-pde-characteristics` -> `local-du-standard-euler-lagrange-fixed-endpoints`, но для последнего лучше добавить вычислительную карточку.

## Что Исправить В Первую Очередь

- Сделать отдельный документ или viewer-фильтр "written_exam_weak_minimum": 20-30 карточек в порядке изучения, без олимпиадных и advanced-ловушек.
- Исправить метаданные `dirichlet-eigenvalues-interval`, `local-du-written-2023-characteristics-plane-data`, `local-du-written-2014-51-characteristics-pde`.
- Привязать `basic-mipt-variation-constants-ypp-plus-y` к видимому кластеру/маршруту минимума.
- Добавить 2-3 простые письменные карточки: недиагональная 2x2, комплексные корни, вычислительная Эйлер-Лагранж.
- В viewer добавить сортировку по возрастанию `idea_score`/`technical_score` и, по возможности, сохраненные наборы фильтров для `exam_score_3/4`.

Математически критических ошибок в проверенных минимальных решениях я не нашел. Основной риск для слабого студента - не неверный ответ в карточках, а то, что он выберет слишком сложную карточку с `low_technical` и решит, что "минимум" ему не по силам.
