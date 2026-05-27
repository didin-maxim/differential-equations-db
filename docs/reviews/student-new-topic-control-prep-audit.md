# Student new topic and control prep audit

Дата: 2026-05-27.

Роль проверки: студент, который открывает базу не как редактор, а как учебный навигатор перед контрольной по ДУ.

Проверенный срез: `build_index` dry-run дал 431 карточку, 966 связей, 49 источников и 34 кластера. Полную запись `build_index.py`/`build_viewer.py` в файлы не запускал: в дереве уже были изменены `index/generated.json`, `index.html` и `viewer/index.html`, а запуск перезаписал бы чужие параллельные изменения. Вместо этого проверил сборку без записи: `build_index.build_data()` и `build_viewer.build_html(...)` проходят.

## Короткий вывод

База уже пригодна как учебный каталог: нужные кластеры находятся, почти везде первым представителем стоит методический навигатор, у карточек есть `definition_ids`, источники, уровни сложности и фильтры viewer по кластеру, тегам, определениям, сложности, score-range и "без олимпиадных".

Но для студента это пока скорее мощная картотека, чем готовый маршрут "сначала прочитай это, потом реши 3 простых, 3 средних, 2 сильных". Главный UX-разрыв: после выбора кластера рядом оказываются method guide, базовые задачи, теоретические леммы, advanced-задачи и олимпиадные представители. Фильтры позволяют это разгрести, но студент должен знать внутренние теги и руками собрать маршрут.

## Маленькая правка данных

Исправлено: 11 карточек с `kind.secondary: method_guide` не имели тега `method_guide`, поэтому фильтр по тегу "method_guide" был неполным. Добавил тег в:

- `cluster-variational-method-guide`
- `cluster-green-functions-bvp-method-guide`
- `cluster-integrating-factor-exact-forms-method-guide`
- `cluster-pde-characteristics-method-guide`
- `cluster-existence-uniqueness-continuation-method-guide`
- `cluster-sturm-method-guide`
- `cluster-variation-of-constants-method-guide`
- `cluster-linear-variable-method-guide`
- `cluster-phase-stability-method-guide`
- `cluster-linear-systems-constant-coefficients-method-guide`
- `cluster-matrix-exponential-method-guide`

После правки `method_guide` gaps = 0.

## Сценарии

### 1. Линейные ОДУ первого порядка и интегрирующий множитель

Что хорошо: есть два нужных входа: `linear-first-order-ode` и `integrating-factor-exact-forms`. В обоих кластерах method guide явно объясняет, что делать дальше: стандартная форма, множитель `mu=exp int p`, формула Коши, область определения; отдельно для exact forms есть проверка `M_y=N_x`, `mu(x)`, `mu(y)`, специальные множители и потерянные кривые.

Проблема маршрута: слово "интегрирующий множитель" ведет сразу в два разных смысла - линейное уравнение и точные формы. Method guides это разделяют, но на уровне student route нет кнопки "я впервые учу линейное ОДУ", которая оставила бы только `cluster-linear-first-order-method-guide`, `linear-first-order-formula`, `resit-pass-3-linear-first-order-forcing`, `weak-pass-linear-method-choice`, затем средние задачи.

Риск: в `linear-first-order-ode` 16 representatives, из них 8 имеют `olympiad_style`. Для первого знакомства Putnam/IMC выглядят как соседние учебные карточки, если студент не включил "без олимпиадных".

### 2. Системы и матричная экспонента

Что хорошо: `matrix-exponential-methods` начинается с method guide, дальше есть базовые леммы про обратную экспоненту, производную в нуле, спектр по режимам, жорданову клетку и trace/determinant. Для подготовки к контрольной это полезный набор.

Проблема маршрута: сценарий "системы/матричная экспонента" естественно объединяет минимум два кластера: `matrix-exponential-methods` и `linear-systems-constant-coefficients`. Сейчас студент должен сам понять, что это соседние маршруты. В `matrix-exponential-methods` 21 representative: 15 core, 2 advanced, 4 student_olympiad; олимпиадные MSU-задачи лежат рядом с базовыми леммами.

Нужен явный маршрут: "фундаментальная матрица -> e^{At} -> диагонализация/Жордан -> неоднородная система -> trace/det shortcuts -> сильные задачи".

### 3. Устойчивость и первые интегралы

Что хорошо: `phase-line-stability` и `first-integrals-plane-systems` имеют хорошие method guides. Видны определения устойчивости, асимптотической устойчивости, линейной классификации, прямой метод Ляпунова, отличие первого интеграла от функции Ляпунова.

Проблема маршрута: студенту нужна связка "устойчивость/первый интеграл", а база разделяет ее на два кластера. Это правильно математически, но в контрольной сценарий обычно один: равновесие, фазовый портрет, первый интеграл или Ляпунов. В `phase-line-stability` 40 representatives, среди них 7 advanced и 6 student_olympiad; в `first-integrals-plane-systems` 15 representatives, есть 2 excellent-check и 2 олимпиадных.

Нужен пресет: "устойчивость без монстров": `phase-stability-method-guide`, определения Ляпунова, 1D phase line, saddle/focus/center, потом first-integral-center и только затем advanced/olympiad.

### 4. Краевые задачи и Штурм

Что хорошо: `boundary-spectral-problems` почти идеален как вход в контрольную: method guide, простая задача Дирихле, weak/resit/middle BVP, затем резонанс и Штурм-Лиувилль. Олимпиадных представителей там нет. `sturm-oscillation-comparison` хорошо закрывает сравнение, нули, неосцилляцию, Кнезера, Пруфера и краевой нерезонанс.

Проблема маршрута: студентский сценарий "краевые/Штурм" требует мостика между двумя кластерами. Если начать со `sturm-oscillation-comparison`, маршрут быстро становится теоретически тяжелым: 18 из 30 representatives имеют `course_advanced`. Если начать с `boundary-spectral-problems`, путь мягче, но связь "зачем мне Штурм после собственных значений" не выделена как учебная последовательность.

Нужен маршрут: "простые спектральные BVP -> mixed/Dirichlet resonance -> метод Штурма для нулей -> сравнение/нерезонанс -> advanced Sturm".

### 5. Вариационное исчисление для письменной работы

Что хорошо: `simple-variational-calculus` имеет method guide и покрывает закрепленные концы, натуральные условия, свободный конец, трансверсальность, изопериметрию, несколько функций, высшие производные, вторую вариацию, Лежандра-Якоби. Источники и определения видны.

Проблема маршрута: для письменной работы не хватает явного "шаблона оформления решения". В кластере 20 representatives: 11 core и 9 advanced, олимпиадных нет, но почти нет слабых/средних exam-маркеров. Студенту трудно отделить "обязательный письменный минимум" от расширений вроде высших производных, Якоби и коэрцитивности.

Нужен пресет: "вариационное исчисление: письменная работа" с порядком: первая вариация -> интегрирование по частям -> Euler-Lagrange -> граничные члены -> проверка экстремали -> свободный конец -> только потом вторая вариация/Якоби.

## Что видно студенту

Работает:

- Кластеры и method guides находятся через `nav=clusters`, поиск и фильтр `cluster`.
- Определения и источники индексируются; есть фильтр `definition`, `source`, source badges и definition badges.
- Есть `scoreRange`: easy, middle, exam_middle, strong, excellent.
- Есть фильтр "олимпиадность" и быстрый режим "без олимпиадных".
- Сортировки по идее/технике помогают выстроить задачи от простых к трудным.

Не хватает:

- Кнопки внутри кластера: "Учить тему" = method guide + definitions + non-olympiad + easy-to-middle tasks.
- Кнопки "Готовиться к контрольной" = problem-only + no olympiad + scoreRange easy/middle/exam_middle + source/course core.
- Явного трехступенчатого списка рядом с method guide: простые, средние, сильные.
- Сценарных маршрутов, объединяющих соседние кластеры: systems + matrix exponential, stability + first integrals, boundary spectral + Sturm.
- Визуального отделения theoretical guide от ordinary representative list. Сейчас method guide просто карточка среди карточек.

## Приоритеты исправлений

P1. Добавить cluster study route в viewer: при выбранном кластере показывать сверху method guide, затем три автоматические группы задач: easy, middle, strong. По умолчанию исключать `olympiad_style` для easy/middle.

P1. Добавить готовые сценарные пресеты для пяти маршрутов из этого аудита. Это лучше, чем заставлять студента помнить точные cluster ids.

P1. В representative list визуально помечать "olympiad/advanced" и не показывать такие карточки первыми в учебном режиме.

P2. Для вариационного исчисления добавить или выделить карточку "шаблон письменного решения" как короткий checklist, не новую тяжелую теорию.

P2. Для `sturm-oscillation-comparison` добавить мягкий контрольный подмаршрут от BVP к сравнению Штурма; сам кластер сейчас слишком advanced-heavy для первого входа.

P3. В карточке method guide показывать связанные definitions inline или рядом, а не только через фильтр/бейджи.

## Проверки

Запущено:

- `python tools/validate.py` -> OK: 431 cards, 966 relations, 49 sources.
- `python tools/check_links.py` -> OK: links are consistent.
- `python tools/check_encoding.py` -> OK: UTF-8 text has no obvious mojibake markers.
- `python tools/check_clusters.py` -> OK: 34 task clusters.
- `python tools/audit_rules.py` -> OK with 4 warnings:
  - `local-du-written-2014-51-characteristics-pde`: `exam_score` with `technical_score > 5`
  - `local-du-written-2014-51-factorized-variable-coeff`: `exam_score` with `technical_score > 5`
  - `local-du-written-2014-51-lagrange-singular-curves`: `exam_score` with `technical_score > 5`
  - `local-du-written-2024-variational-free-endpoint`: `exam_score` with `technical_score > 5`

Dry-run без записи:

- `build_index.build_data()` -> OK: 431 cards, 34 clusters.
- `build_viewer.build_home_html(...)` / `build_viewer.build_html(...)` -> OK.

Не запускал с записью:

- `python tools/build_index.py`
- `python tools/build_viewer.py`

Причина: дерево параллельно изменяется, а эти команды перезаписывают `index/generated.json`, `index.html`, `viewer/index.html`, которые уже были изменены до моего аудита.
