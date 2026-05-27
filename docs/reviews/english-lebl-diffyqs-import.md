# Jiří Lebl, Notes on Diffy Qs: выборочный импорт

Дата: 2026-05-26.

Источник: https://www.jirka.org/diffyqs/ , web/PDF version 6.11 от 18 мая 2026 года.

## Что добавлено

Добавлено 9 карточек в `data/problems/english_sources/lebl_diffyqs/`.

1. `lebl-diffyqs-transport-signal-shift` - базовый перенос профиля `f(x-alpha t)` по характеристикам.
2. `lebl-diffyqs-damped-transport-characteristics` - вдоль характеристики появляется ОДУ `du/dt+u=0`.
3. `lebl-diffyqs-characteristic-data-obstruction` - начальные данные на характеристике могут быть несовместимы.
4. `lebl-diffyqs-variable-coefficient-characteristics` - первый шаг к характеристической системе с переменным коэффициентом.
5. `lebl-diffyqs-degenerate-linearization-critical-point` - нулевая линеаризация, квадратичная фазовая информация.
6. `lebl-diffyqs-invariant-half-plane-two-sinks` - два локальных стока и глобальный инвариантный барьер.
7. `lebl-diffyqs-radial-monotone-spiral-source` - линейный центр, который нелинейно становится источником.
8. `lebl-diffyqs-robin-dirichlet-transcendental-spectrum` - смешанная спектральная задача с уравнением на частоту.
9. `lebl-diffyqs-weighted-sturm-exponential` - весовая Sturm-Liouville задача, сводимая экспоненциальной заменой.

## Фильтр

Не импортировались:

- WeBWorK/Edfinity templates и однотипные тренировочные списки;
- длинные вычисления рядов Фурье и separation of variables;
- нелинейные PDE и PDE второго порядка;
- chaos/Lorenz/Duffing из главы 8.5;
- прикладные инженерные задачи, где новая идея тонет в вычислениях.

## Связь с базой

PDE-блок намеренно не уходит глубже local_du: это только линейные однородные уравнения первого порядка и диагностика начальных данных методом характеристик. Спектральные карточки выбраны как короткие расширения уже существующего `dirichlet-eigenvalues-interval`. Нелинейные системы закрывают качественные идеи, которые слабо представлены в чисто экзаменационных задачах: неинформативная линеаризация, инвариантная область, радиальная монотонность.

Связи добавлены только в `data/relations/relations.d/english-lebl-diffyqs.yaml`.
