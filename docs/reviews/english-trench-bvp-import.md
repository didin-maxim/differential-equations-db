# Импорт Trench BVP / Sturm-Liouville

Дата: 2026-05-26.

Источник: William F. Trench, *Elementary Differential Equations with Boundary Value Problems*, AIM/Open Textbook, Trinity/Digital Commons/LibreTexts. Основные локаторы: Chapter 13, Sections 13.1-13.2 и упражнения 13.1E, 13.2E.

## Отбор

Добавлены 10 карточек в `data/problems/english_sources/trench_bvp/`:

- `trench-bvp-green-function-formula` - теорема о функции Грина для нерезонансной двухточечной задачи.
- `trench-bvp-robin-green-kernel-example` - компактный пример Green kernel для условий Робина.
- `trench-bvp-resonance-solvability-alternative` - конструктивная альтернатива разрешимости в резонансе.
- `trench-bvp-dirichlet-resonance-sine-condition` - минимальная модель условия ортогональности к `sin x`.
- `trench-bvp-sturm-liouville-integrating-factor` - приведение к самосопряженной форме.
- `trench-bvp-green-identity-self-adjoint-boundary` - тождество Грина для разделенных краевых условий.
- `trench-bvp-real-eigenvalues` - вещественность спектра регулярной задачи Штурма-Лиувилля.
- `trench-bvp-weighted-orthogonality` - ортогональность собственных функций с весом.
- `trench-bvp-euler-log-spectrum` - эйлерово уравнение со спектром в переменной `log x`.
- `trench-bvp-energy-no-negative-eigenvalues` - энергетический запрет отрицательных собственных значений.

## Фильтрация дублей

Не импортировались длинные серии упражнений 13.1.16-13.1.30 и 13.2.11-13.2.24: большинство отличаются только краевыми коэффициентами или требуют численного поиска корней.

Не добавлялся еще один базовый шаблон `y''+lambda y=0`, `y(0)=y(pi)=0`: в базе уже есть `dirichlet-eigenvalues-interval`. Вместо этого добавлена резонансная неоднородная версия с условием совместности.

Fourier/PDE-сюжеты из главы 11 и связанные разложения использованы только как контекст; отдельные карточки про ряды Фурье не добавлялись, чтобы не уводить импорт за ODE-фокус.

## Роль в программе

Пачка закрывает мосты, которые часто нужны на границе стандартного курса:

- Green function как обратный оператор для линейной BVP без функционального анализа.
- Одномерная Fredholm alternative в резонансе.
- Самосопряженная форма и тождество Грина.
- Вещественность, ортогональность и простота собственных функций в регулярной Sturm-Liouville задаче.
- Энергетический знак спектра как короткая качественная лемма.

Связи вынесены в `data/relations/relations.d/english-trench-bvp.yaml`, batch - в `data/import_batches/english-trench-bvp.yaml`.
