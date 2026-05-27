# Граница письменного экзамена на отлично и олимпиадного слоя

Дата: 2026-05-27.

Зона проверки: `index/generated.json`, `viewer/index.html` как производное представление, отчеты `docs/reviews/mipt-excellent-level-audit.md` и `docs/reviews/olympiad-level-audit.md`, карточки с `idea_score >= 8`, карточки с `idea_score > 10`, теги `written_exam`, `exam_score_8`, `exam_score_9`, `exam_score_10`, `olympiad_style`, `olympiad_above_exam`, `advanced_standard_course`, `beyond_standard_course`.

## Короткий итог

Строгий локальный письменный слой `written_exam` не загрязнен олимпиадными задачами: найдено 10 карточек, максимум `idea_score=7`, меток `olympiad_style`, `olympiad_above_exam`, `beyond_standard_course` и `idea_score>10` среди них нет.

Риск находится не в `written_exam`, а в расширенном селекторе "сильный экзамен" по `exam_score_8/9/10`: там 19 карточек, из них 6 имеют `olympiad_style`. Для устного excellent это допустимо, но для письменного экзамена такой селектор без дополнительных фильтров смешивает хорошие письменные задачи с олимпиадной эстетикой.

Карточек с `idea_score > 10`, которые одновременно имеют `written_exam` или `exam_score_8/9/10`, не найдено. Все 6 карточек `idea_score>10` отделены `olympiad_above_exam` и/или `beyond_standard_course`.

Карточки не редактировались: спорные случаи зависят от политики письменного экзамена, поэтому ниже даны точечные рекомендации.

## Граница отбора для письменника

Для письменного экзамена на отлично разумная граница:

- основной слой: `written_exam` или специально созданные `model_exam_task` с `exam_score_8/9/10`, `idea_score` 8-10, `technical_score` обычно до 5-6;
- допустимый advanced: `advanced_standard_course`, если решение опирается на один явно курсовой прием и не требует догадки олимпиадного барьера;
- исключать по умолчанию: `olympiad_above_exam`, `beyond_standard_course`, `needs_solution_completion`, `functional_differential`, а также `olympiad_style` без ручного allow-list;
- отдельно держать технические длинные задачи: высокий `technical_score` сам по себе не делает задачу excellent-письменником.

## Проблемы и рекомендации

| card | наблюдение | рекомендация |
|---|---|---|
| `msu-ode-2023-2-infinite-zeros-linear-ode` | Имеет `olympiad_style` и `exam_score_8`. Пункт а) является хорошей курсовой идеей Ролля + единственность, но пункт б) требует контрпример с гладкой осциллирующей функцией и восстановление уравнения под заданное решение. | Не включать в обычный письменный excellent без явной пометки "олимпиадный контрпример". Если генератор письменника берет `exam_score_8`, нужен фильтр `-olympiad_style` или ручной allow-list. |
| `msu-ode-2012-3-recover-autonomous-matrix` | `olympiad_style`, `student_olympiad`, `exam_score_8`. Содержательно это восстановление матрицы через `e^A=-2I` и все вещественные логарифмы; для письменника это скорее мини-олимпиада по матричной экспоненте. | Рассмотреть снятие `exam_score_8` для письменного слоя либо оставить только для oral/olympiad-excellent подборки. |
| `msu-ode-2012-9-negative-instant-spectrum` | `olympiad_style`, `exam_score_8`, но идея является важным стандартным предупреждением: мгновенный спектр не контролирует неавтономную устойчивость. | Можно оставить как письменный excellent-counterexample, если тема неавтономных систем входит в программу; в селекторе лучше пометить как "контрпример", а не как типовую вычислительную задачу. |
| `ru-misc-nure-8-5` | `olympiad_style`, `exam_score_8`. Замена `z=arctan y` и оценка blow-up короткие; это хорошая верхняя письменная задача, если студент уже видел сравнение и продолжение. | Оставить как допустимый письменный excellent по allow-list. Не повышать выше 8: главная догадка все же олимпиадная. |
| `ru-misc-kfu-2013-13-1` | `idea_score=7`, `technical_score=7`, но стоит `exam_score_8`. Это сшивка решений на полуосях для `(D-1)^2y=e^{-|x|}`: больше техника и аккуратность, чем новая идея. | Для письменника на отлично не использовать как идейную 8. Рассмотреть метаданные `exam_score_7` вместо `exam_score_8` или отдельную пометку "technical drill". |
| `oral-exam-geometry-two-tangent-roots` | `exam_score_8`, `olympiad_style`, `oral_exam_geometry`, источник `needs_human_review`. Идея отличная, но формат "по рисунку линейкой построить" не письменный. | Исключить из письменного экзаменационного слоя. Оставить в устно-геометрическом/олимпиадном блоке; не выдавать как обычную письменную задачу. |
| `ru-misc-spb-itmo-2018-6` | Имеет `olympiad_above_exam`, хотя решение через энергию `y^2+(y')^2` и монотонность на двух хвостах выглядит как хороший advanced written. | Кандидат на понижение с `olympiad_above_exam` до `olympiad_style` или на добавление в ручной allow-list письменника. Не править автоматически: глобальность на всей прямой может быть вне обычного письменного формата. |
| `ru-misc-kfu-2019-19-3` | `idea_score=8`, но есть `functional_differential` и `olympiad_above_exam`. | Разметка корректна: не переносить в письменный слой, даже несмотря на короткое сведение к `f''+f=0`. |

## Тематическая проверка high-level

### Green functions

Слой в целом чистый. Базовые Trench-карточки на Green function, Green identity и резонанс отмечены `advanced_standard_course` или `standard_course_methods` в зависимости от глубины. `trench-bvp-resonance-solvability-alternative` с `idea_score=8` хорошо подходит для advanced bridge, но не имеет exam-тега.

`putnam-early-1963-a3-euler-operator-kernel` использует `green_kernel` и `olympiad_style`, но без `exam_score_*`; это правильно для письменной границы. Если когда-нибудь включать ее в письменник, давать только как bonus/advanced operator identity.

### Floquet basics

Граница выставлена хорошо. `mipt-excellent-periodic-system-resonant-monodromy` имеет `exam_score_9`, но решение фактически использует фундаментальную матрицу, отображение за период и линейную алгебру, а не полную теорему Флоке. Teschl-карточки по multipliers, determinant Liouville и period iterate остаются `advanced_standard_course` без экзаменационного тега.

Рекомендация: в письменном экзамене формулировать как "монодромия/периодическое решение", а не как полный Floquet theory.

### Sturm oscillation

Стандартный письменный excellent представлен корректно: `oral-exam-strong-10-sturm-comparison-one-zero` является нормальным `exam_score_10`. Продвинутые Bessel/Prufer и zero-count карточки (`local-du-8-t6*`, `mit-18034-pset08-prufer-oscillation-criteria`, Teschl phase cards) помечены `advanced_standard_course` и не имеют exam-тегов.

Олимпиадные zero-location случаи `putnam-early-1955-a7-zero-bounds`, `putnam-early-1957-ii6-zero-location`, `msu-ode-2023-8-fourth-order-zero-count-review` отделены `olympiad_above_exam`/`beyond_standard_course`. Это правильная граница.

### Lyapunov and Stability

Базовый и средний слой хороший: есть прямой метод Ляпунова, фазовая устойчивость, first integral center, линейная классификация. Верхний письменный слой представлен `oral-exam-strong-10-symmetric-part-stability` и MIT/Filippov карточками.

Основной спорный случай - `ru-misc-spb-itmo-2018-6`: по математике это ближе к сильному письменному energy/Lyapunov, чем к настоящему `olympiad_above_exam`. Его стоит пересмотреть вручную.

### Variational second variation / Jacobi

Разметка аккуратная. `mipt-excellent-legendre-violation-no-minimum` как `exam_score_8` проверяет одну отрицательную вариацию и годится для письменного excellent. `local-du-standard-legendre-jacobi-conditions` и `local-du-romanko-jacobi-strict-maximum` остаются `advanced_standard_course` без exam-тегов; это верно, потому что Jacobi-сопряженные точки легко становятся теоретическим advanced/beyond.

Рекомендация: для письменника отдавать Legendre/second variation threshold, а Jacobi condition - только если оно явно было в программе.

### Variable coefficients

Кластер линейных уравнений с переменными коэффициентами смешивает стандартные и олимпиадные идеи, поэтому здесь особенно важен фильтр. Нормальные written/excellent представители: Liouville/Wronskian, reduction of order, graph tangency/ratio, `cluster-linear-variable-graph-ratio-maximum`.

Олимпиадные представители с тем же широким тегом `linear_higher_order` уже отделены: `olympiad-level-power-solution-linear-ode-criterion`, `putnam-early-1975-a5-wronskian-nonlinear-transform`, `ru-misc-nure-8-3`, `msu-ode-2023-8-fourth-order-zero-count-review`. Нельзя строить письменный слой только по `linear_higher_order` + высокий score.

### Parameter dependence

Граница хорошая. `local-du-written-2011-21-parameter-variations` и `local-du-written-2023-parameter-sensitivity` покрывают письменный слой, `teschl-stanford-bridge-*` дают advanced bridge, `mipt-excellent-second-parameter-correction` закрывает верхний `exam_score_8`.

Рекомендация: вторую поправку по параметру давать как high-level письменную только с явной подсказкой "искать разложение по параметру"; без подсказки это уже ближе к олимпиадной догадке.

## Практическая политика селектора

Для генерации письменного экзамена на отлично:

1. Брать `written_exam` без дополнительных олимпиадных источников.
2. Добавлять `exam_score_8/9/10` только при `difficulty_main != student_olympiad` или через allow-list.
3. Исключать `olympiad_above_exam`, `beyond_standard_course`, `needs_solution_completion`, `functional_differential`, `oral_exam_geometry`.
4. Для `olympiad_style` требовать ручный allow-list: сейчас хорошие кандидаты для допуска - `ru-misc-nure-8-5` и, условно, `msu-ode-2012-9-negative-instant-spectrum`; нежелательные для обычного письменника - `msu-ode-2012-3-recover-autonomous-matrix`, `msu-ode-2023-2-infinite-zeros-linear-ode`, `oral-exam-geometry-two-tangent-roots`.
5. Не повышать задачу в excellent только за техническую длину: `ru-misc-kfu-2013-13-1` показывает этот риск.

## Проверки

Карточки и индекс не редактировались, поэтому `build_index.py` и `build_viewer.py` не запускались. После добавления отчета достаточно проверить кодировку и общую валидность базы.
