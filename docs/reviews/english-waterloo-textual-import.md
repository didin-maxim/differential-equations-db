# Waterloo AMATH 250 textual import

Дата: 2026-05-26.

Источник: `src-waterloo-amath250-notes`, J. Wainwright and J. West, *Introduction to Differential Equations: Course Notes for AMath 250*, edition 2.0, July 2023, https://www.math.uwaterloo.ca/~jjwest/course_notes/AMath250_Course_Notes.pdf .

## Что добавлено

- 8 карточек в `data/problems/english_sources/waterloo_textual/`.
- Темы: восстановление ОДУ по семейству кривых, qualitative sketches, демпфированные осцилляторы, фазовые портреты, фундаментальная матрица, зависимость от параметров.
- Связи вынесены в `data/relations/relations.d/english-waterloo-textual.yaml`.
- Batch: `data/import_batches/english-waterloo-textual.yaml`.

## Отбор

Я использовал Waterloo notes как источник постановок и стиля, но не переносил длинные списки однотипных упражнений. Отфильтрованы:

- массовые separable/linear first-order computations;
- Laplace transform и Fourier-related материал;
- задачи, где вся новизна только в подстановке других коэффициентов.

Оставлены задачи, где есть короткая качественная идея: исключение параметра, анализ сингулярной прямой, фазовая изоклина, потоковая интерпретация фундаментальной матрицы, порог по параметру.

## Карточки

- `waterloo-family-circles-recover-ode` - восстановление ОДУ по семейству окружностей, касающихся оси.
- `waterloo-log-family-qualitative-recover` - логарифмическое семейство, асимптоты и выпуклость.
- `waterloo-singular-linear-qualitative-sketch` - линейное уравнение с особой прямой `x=0`.
- `waterloo-second-order-pq-stability` - параметрическая область затухания для `y''+p y'+q y=0`.
- `waterloo-critical-damping-crossing-threshold` - критическое демпфирование и порог начальной скорости.
- `waterloo-oscillator-speed-before-crossing` - максимум скорости перед первым пересечением равновесия.
- `waterloo-spiral-phase-portrait-isoclines` - устойчивый фокус через спектр, направление вращения и изоклины.
- `waterloo-fundamental-matrix-flow-inverse` - `Phi(t+s)=Phi(t)Phi(s)` и `Phi(-t)=Phi(t)^{-1}`.

## QA

Проверки:

- `python tools/validate.py` - OK: 262 cards, 263 relations, 21 sources.
- `python tools/check_links.py` - OK: links are consistent.
- `python tools/audit_rules.py` - OK: audit finished with 0 warnings.
- `python tools/check_clusters.py` - OK: 7 task clusters in 1 file(s).

Чужие параллельные изменения не откатывались и не правились.
