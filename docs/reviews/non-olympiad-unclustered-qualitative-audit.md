# Аудит неолимпиадных qualitative/stability задач вне кластеров

Дата: 2026-05-27.

## Область прохода

Проверялись problem-карточки, которые:

- не входят ни в один `representative_card_ids`;
- имеют `fragment != olympiad`;
- относятся к `qualitative` или близким темам: устойчивость, фазовая прямая/плоскость, первые интегралы, энергия, инвариантные множества, линеаризация.

На входе найдено 22 релевантные неолимпиадные задачи вне кластеров.

## Решения по кластеризации

### Добавлены в `phase-line-stability`

Добавлены точные попадания на устойчивость, фазовые портреты, линеаризацию, функции Ляпунова и инвариантные линии:

- `lyapunov-linearization-example`
- `oral-middle-nonlinear-system-lyapunov`
- `weak-pass-phase-line-semistable`
- `local-du-written-2014-51-equilibrium-linearization`
- `local-du-filippov-132-linear-stability-translation`
- `lebl-diffyqs-degenerate-linearization-critical-point`
- `lebl-diffyqs-invariant-half-plane-two-sinks`
- `lebl-diffyqs-radial-monotone-spiral-source`
- `mit-18034-pset09-lyapunov-nonlinear-stable`
- `mit-18034-pset09-omega-limit-linearization`
- `waterloo-second-order-pq-stability`
- `waterloo-critical-damping-crossing-condition`
- `waterloo-oscillator-speed-before-crossing`

Кластер стал крупнее, но это содержательно оправдано: у него уже есть политика ближайшего слоя фазовой плоскости и устойчивости, а добавленные задачи представляют разные механизмы, а не только замену коэффициентов.

### Добавлены в `first-integrals-plane-systems`

Добавлены:

- `resit-pass-3-energy-oscillator-check`
- `local-du-written-2016-global-first-integrals-source`

Первый пример нужен как минимальная экзаменационная версия энергии осциллятора, второй - как линейно-алгебраический пример глобальных первых интегралов. Карточка `local-du-written-2014-51-nonlinear-cauchy-total-derivative` оставлена вне кластера: это скорее одноразовый ход с полной производной в задаче Коши первого порядка, чем представитель кластера фазовых траекторий на плоскости.

### Создан `energy-estimates-second-order-ode`

Новый кластер создан, потому что в базе уже было не менее трех близких задач с общим переносимым планом:

1. выбрать энергию или интегральное тождество;
2. продифференцировать вдоль решения или проинтегрировать по частям;
3. использовать знак производной/интеграла;
4. получить ограниченность, невозможность периодичности или краевой запрет.

Представители:

- `energy-integral-oscillator`
- `resit-pass-3-energy-oscillator-check`
- `oral-exam-excellent-damped-periodic-zero`
- `oral-exam-excellent-endpoint-combination-no-two-zeros`
- `local-du-8-t2-exponential-coefficient-energy-bound`
- `local-du-written-2020-energy-monotonicity-exp-inverse`

Это не дубль `first-integrals-plane-systems`: там геометрия уровней и фазовые траектории, здесь качественные оценки и запреты для уравнений второго порядка.

### Добавлена в `existence-uniqueness-continuation`

- `oral-middle-comparison-inverse-bound`

Это учебный, не олимпиадный представитель сравнения через производную обратной функции, ближайший родственник `blow-up-comparison-y-square`.

## Оставлены уникальными

Остались вне кластеров 2 задачи из проверенной области.

- `oral-above-three-liouville-area-preservation`: близка к линейным системам и формуле Лиувилля, но главный объект - сохранение площади фундаментального параллелограмма при нулевом следе. Для отдельного qualitative/stability-кластера пока недостаточно близких неолимпиадных задач.
- `local-du-written-2014-51-nonlinear-cauchy-total-derivative`: использует первый интеграл вида полной производной, но это одиночная задача Коши первого порядка, не фазовая плоскость и не энергетический кластер второго порядка. Добавлять ее в `first-integrals-plane-systems` было бы размыванием темы.

## Связи

Добавлен файл `data/relations/relations.d/non-olympiad-unclustered-qualitative-audit.yaml`.

Связи поставлены между:

- прямым методом Ляпунова и новыми задачами на локальную устойчивость;
- линеаризацией и задачами на гиперболические/вырожденные равновесия;
- энергией осциллятора и новым кластером энергетических оценок;
- сравнением `y'=y^2` и устной задачей на производную обратной функции;
- первыми интегралами и линейным источником с глобальными инвариантами.

## Итог

После прохода:

- релевантных неолимпиадных qualitative/stability задач вне кластеров осталось 2;
- создан 1 новый кластер;
- обновлены `phase-line-stability`, `first-integrals-plane-systems`, `existence-uniqueness-continuation`;
- карточки задач не редактировались и не удалялись.

