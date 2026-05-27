# Разведка англоязычных источников для третьего эшелона

Дата: 2026-05-26.

Цель: подготовить источники для следующего агентного прохода. Приоритет не в массовом импорте упражнений, а в выборе задач, которые:

- решаются методами стандартного курса МФТИ по ДУ;
- не попадают полностью в уже насыщенные шаблонные кластеры;
- дают студенту понятный мост к темам за пределами курса без перегруза тяжелой теорией;
- почти не уходят в PDE, кроме линейных однородных уравнений первого порядка и метода характеристик.

## Главные источники

### MIT 18.034 Honors Differential Equations

Источник: https://ocw.mit.edu/courses/18-034-honors-differential-equations-spring-2009/resources/assignments/

Статус: высокий приоритет для третьего эшелона.

Почему полезен:

- открытые problem sets и solution keys;
- уровень ближе к сильному undergraduate/honors, то есть похож на верхний край МФТИ и олимпиадные устные задачи;
- есть материал по Штурму, краевым задачам, качественным свойствам, системам, устойчивости.

Что искать:

- задачи на Sturm comparison/separation и число нулей;
- задачи на резонанс и условия разрешимости;
- качественные задачи на фазовую плоскость без длинного счета;
- задачи, где решение строится через правильную идею, а не через громоздкую формулу.

Что фильтровать:

- чисто вычислительные constant coefficients и Laplace transform;
- задачи, совпадающие с устными кластерами `linear_first_order`, `constant_coefficients`, `linear_systems_constant_coefficients`.

Рекомендуемый агент: `english_mit_honors_ode`.

### Trench, Elementary Differential Equations with Boundary Value Problems

Источник: https://textbooks.aimath.org/textbooks/approved-textbooks/trench-de/

Статус: высокий приоритет как открытый задачник и источник краевых/Штурмовских задач.

Достоинства:

- AIM Open Textbook Initiative;
- есть упражнения и student manual с решениями для выбранных задач;
- хорошо покрывает boundary value problems, Green functions, Sturm-Liouville, eigenvalues.

Что искать:

- задачи на существование/единственность краевой задачи в зависимости от параметра;
- Green function без тяжелой функциональной теории;
- регулярные Sturm-Liouville задачи, ортогональность, простота собственных значений;
- короткие критерии разрешимости при резонансе.

Что не импортировать:

- длинные списки однотипных BVP с разными числами;
- Fourier/PDE задачи, где ODE лишь технический хвост разделения переменных.

Рекомендуемый агент: `english_trench_bvp`.

### Jiří Lebl, Notes on Diffy Qs

Источник: https://www.jirka.org/diffyqs/

Статус: средне-высокий приоритет.

Достоинства:

- открытый OER; есть PDF, HTML, LaTeX source;
- много упражнений, включая избранные ответы;
- хорошо покрывает first-order PDE characteristics на ровно допустимом уровне, eigenvalue problems, nonlinear systems.

Что искать:

- метод характеристик для линейных однородных PDE первого порядка;
- нелинейные системы, фазовая плоскость, устойчивость, первые интегралы;
- eigenvalue problems beyond the basic Dirichlet template;
- задачи с интерактивной/качественной идеей, которую можно переписать без вычислительной тяжести.

Что фильтровать:

- engineering forcing/resonance с длинной алгеброй;
- Laplace transform и Fourier series, если это не дефицит базы;
- WebWork-типовые задачи.

Рекомендуемый агент: `english_lebl_diffyqs`.

### Teschl, Ordinary Differential Equations and Dynamical Systems

Источник: https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode

Статус: источник для аккуратного выхода за стандартную программу.

Достоинства:

- официальный авторский доступ к онлайн-версии с разрешения AMS;
- сильная теория IVP, линейных систем, Floquet, Sturm-Liouville, oscillation theory, dynamical systems;
- хорош для теоретических карточек и небольшого числа задач с меткой `advanced_standard_course` или `beyond_standard_course`.

Что искать:

- Floquet theorem: простые следствия и задачи на монодромию, не тяжелые доказательства;
- regular perturbation и dependence on initial conditions;
- oscillation/nonoscillation beyond basic Sturm comparison;
- Hartman-Grobman/stable manifold только как обзорные карточки, если формулировка понятна студенту после линейной устойчивости.

Что не делать:

- не тащить KAM, chaos, Smale-Birkhoff, Melnikov;
- не перегружать базу доказательствами функционального анализа;
- не импортировать задачи, где требуется аппарат, которого у студента МФТИ 2 курса еще нет.

Рекомендуемый агент: `english_teschl_theory_bridge`.

### Stanford Math 63CM / Brendle ODE notes

Источник: https://web.stanford.edu/class/math63cm/63cm-solutions/ode.pdf

Статус: средний приоритет, особенно для Sturm-Liouville and oscillation.

Достоинства:

- аккуратные notes с доказательствами;
- есть Sturm-Liouville theory через фазовый угол и счет нулей;
- полезно для лемм вокруг Штурма и сравнения с уже добавленной T3.

Что искать:

- задачи/леммы про число нулей n-го собственного решения;
- монотонность фазового угла по параметру;
- простота и упорядоченность собственных значений.

Рекомендуемый агент: можно объединить с `english_teschl_theory_bridge`.

### Waterloo AMATH 250 notes

Источник: https://www.math.uwaterloo.ca/~jjwest/course_notes/AMath250_Course_Notes.pdf

Статус: средний приоритет для текстовых и качественных задач стандартного курса.

Достоинства:

- много problem sets;
- есть qualitative sketch, modeling, systems, mechanical oscillators;
- хорошо подходит для задач без длинных формул, где надо совместить решение и качественное описание.

Что искать:

- задачи на восстановление ОДУ по семейству кривых;
- качественные эскизы решений линейного/автономного уравнения;
- mechanical oscillator questions, где есть концептуальный вопрос, а не только решение характеристического уравнения;
- фундаментальная матрица и фазовый портрет.

Что фильтровать:

- длинные списки почти одинаковых задач;
- простые линейные/разделяющиеся задачи без новой идеи.

Рекомендуемый агент: `english_waterloo_textual`.

### Georgia Tech Math 2552 / Honors DE pages

Источники:

- https://glivshyts6.math.gatech.edu/Diff-equations.html
- https://mccuan.math.gatech.edu/courses/2413/old-syllabus.html

Статус: разведочный источник, полезен для тематических ориентиров и worksheet-style задач.

Что искать:

- qualitative analysis of logistic/autonomous equations without solving;
- non-intersection property from uniqueness;
- phase portraits, bifurcation, forcing/resonance;
- concise honors tasks on geometry of solution space.

Что фильтровать:

- Canvas/worksheet задачи без публичных условий;
- numerical methods and Laplace transform unless явно дефицит.

## Источники второго порядка

### MIT 18.03SC Differential Equations

Источник: https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/

Использовать как источник стандартных тем и отдельных applied tasks. Там много типового материала: first order, integrating factors, constant coefficients, pure resonance, matrix exponentials, nonlinear systems. Из-за насыщенности соответствующих кластеров импортировать осторожно: скорее искать необычную постановку или качественный вопрос.

### Paul’s Online Notes

Источник: https://tutorial.math.lamar.edu/

Использовать как справочник/проверку стандартных формулировок и отдельных BVP notes. Как источник карточек слабее: много задач типовые и шаблонные, поэтому импортировать только если нужна ясная иллюстрация theorem/definition card или short conceptual example.

### UC Davis ODE course pages

Источник: https://www.math.ucdavis.edu/~romik/teaching-pages/mat119b/

Использовать точечно: есть домашние задания/решения и qualitative nonlinear ODE orientation. Хорошо для задач на dynamics beyond the course, но нужно сильно фильтровать chaos/discrete dynamics.

## Темы для третьего эшелона

Приоритетные дефицитные направления:

1. Sturm-Liouville without PDE overload: counting zeros, simplicity, ordering, comparison, Green function, resonance solvability.
2. Linear periodic systems: Floquet multipliers, monodromy, periodic forcing; помечать как `advanced_standard_course`, если выходит за обычный курс.
3. Dependence on initial data and parameter: sensitivity equations, Gronwall estimates, variational equation.
4. First-order PDE by characteristics: только линейные однородные уравнения первого порядка, без классификации PDE второго порядка.
5. Qualitative autonomous systems: first integrals, trapping regions, linearization, phase portraits with short reasoning.
6. Variational calculus beyond simplest cluster: natural boundary conditions, transversality, Jacobi/Legendre, isoperimetric constraint, but not long Euler-Lagrange computations.
7. Boundary value resonance and Fredholm alternative in 1D elementary form.

Темы, которые стоит ограничить:

- Laplace transform: кластер быстро становится техническим и не входит в главный фокус базы.
- Constant coefficient ODEs: добавлять только при новой идее, например resonance/annihilator/operator view.
- Simple separable/linear first-order equations: почти всегда дубли.
- Fourier/PDE separation: не углубляться; ODE-компонент можно использовать только если задача сама про Sturm-Liouville.
- Heavy dynamical systems: KAM, chaos, stable manifold theorem с доказательством, Melnikov; максимум обзорные связи, не задача для экзаменационной базы.

## Предложение по агентам третьего эшелона

1. `english_mit_honors_ode`: MIT 18.034, 8-12 задач/теорем, high reasoning, строгая фильтрация дублей.
2. `english_trench_bvp`: Trench chapters on BVP/Sturm-Liouville/Green functions, 8-10 карточек, часть theorem/lemma.
3. `english_lebl_diffyqs`: Lebl, 6-10 карточек на characteristics, nonlinear systems, eigenvalue problems.
4. `english_teschl_theory_bridge`: Teschl + Stanford notes, 6-8 теоретических мостов за программу, с `advanced_standard_course`/`beyond_standard_course`.
5. `english_waterloo_textual`: Waterloo AMATH 250, 6-8 текстовых/качественных задач без шаблонной лавины.
6. `english_import_qa`: отдельный QA после импорта: проверка кластеров, сложности, меток и источников.

## Правила импорта

- На один источник: не больше 8-12 карточек за проход.
- Для каждой candidate-задачи сначала искать в базе по формуле, идее и тегам.
- Если задача попадает в насыщенный кластер, импортировать только при новой идее или новой диагностической ценности.
- Если источник содержит solution key, использовать его только для проверки идеи; писать собственное краткое решение в стиле базы.
- В `sources` фиксировать конкретный URL и локатор: course/problem set/chapter/section, но не копировать длинные условия дословно.
- Для advanced-задач обязательно ставить метку выхода за программу и кратко объяснять, какой факт выходит за стандартный курс.

