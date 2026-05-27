# Аудит неолимпиадных вне-кластерных задач первого порядка

Дата: 2026-05-27.

Область аудита: problem-карточки вне `representative_card_ids`, исключая `fragment: olympiad`; основной фокус - `fragment: first_order` и близкие простые задачи первого порядка.

## Что изменено

- Создан кластер `separable-homogeneous-first-order`.
- В него добавлены четыре точных представителя:
  - `separable-logistic-equation`;
  - `resit-pass-3-separable-exponential-growth`;
  - `homogeneous-first-order-substitution`;
  - `oral-above-three-homogeneous-ratio-substitution`.
- Добавлены связи в `data/relations/relations.d/cluster-separable-homogeneous-first-order.yaml`.
- В кластер `implicit-ode-discriminant` добавлен `clairaut-envelope` как явный дедупликационный якорь для задач Клеро/Лагранжа.
- Добавлен файл глубоких методических связей `data/relations/relations.d/non-olympiad-unclustered-first-order-audit.yaml`: связи поставлены не по общей теме, а по переносимым приемам `mu(x)`, точная форма, полная производная, редукция к линейному уравнению через `p(y)`, и переход от линейных характеристик к semilinear-взрыву.

## Решения по оставшимся задачам

`oral-middle-integrating-factor-x` оставлена вне representatives. Проверены близкие карточки `oral-above-three-integrating-factor-x-only`, `cluster-integrating-factor-mu-y-short`, `cluster-integrating-factor-power-monomial`, `cluster-integrating-factor-mu-xy`, `exact-equation-potential`. Поставлена связь с `oral-above-three-integrating-factor-x-only`, потому что совпадает конкретный метод: критерий для множителя `mu(x)`, затем восстановление потенциала. В representatives не добавлена: отличие главным образом в неэлементарной первообразной, а не в новой идее ДУ.

`resit-pass-3-exact-equation-potential` и `weak-pass-exact-form-recognition` оставлены вне representatives как тренировочные дубли базовой карточки `exact-equation-potential`. Проверены также `oral-middle-integrating-factor-x` и `oral-above-three-integrating-factor-x-only`: там сначала подбирается множитель, поэтому методический шаг другой. Для обеих exact-form карточек поставлены связи с `exact-equation-potential`: конкретный переносимый механизм - распознать полный дифференциал и восстановить функцию потенциала.

`local-du-written-2014-51-nonlinear-cauchy-total-derivative` оставлена вне нового кластера. Проверены `resit-pass-3-energy-oscillator-check`, `energy-integral-oscillator`, `linear-first-order-formula`, `local-du-written-2024-nonlinear-p-of-y`. Поставлены связи с `resit-pass-3-energy-oscillator-check` и `linear-first-order-formula`: переносимый механизм - увидеть полную производную `(yy')'`, ввести `v=yy'`, затем решить линейное уравнение первого порядка. Нового кластера не создано: точных задач на свертку второй производной в полную производную найдено меньше трех; энергетические карточки родственны по правилу цепочки, но не являются тем же шаблоном.

`local-du-written-2024-nonlinear-p-of-y` оставлена уникальной в рамках текущего прохода. Проверены `local-du-written-2024-linear-y-xu-reduction`, `local-du-written-2014-51-factorized-variable-coeff`, `riccati-known-solution`, `oral-middle-riccati-known-inverse-x`, `bernoulli-standard`. Поставлены связи с `local-du-written-2024-linear-y-xu-reduction` и `riccati-known-solution`: общий переносимый механизм - нелинейная/структурная замена, после которой возникает линейное уравнение первого порядка. Кластера недостаточно, потому что точный метод `p=p(y)` представлен одной карточкой; линейные замены `y=xu` и Риккати/Бернулли слишком разные, чтобы объединять их в один кластер без превращения кластера в широкий тег.

`mipt-excellent-semilinear-characteristics-blowup` оставлена вне `pde-characteristics-first-order`: существующая политика этого кластера специально не включает semilinear/blow-up characteristics как representatives. Проверены `cluster-pde-characteristics-flow-geometry`, `local-du-deficit-first-order-pde-characteristics`, `cluster-pde-characteristics-strip-domain`, `cluster-pde-characteristics-single-hit-criterion`. Поставлены связи с `cluster-pde-characteristics-flow-geometry` и `local-du-deficit-first-order-pde-characteristics`: общий метод - параметризовать характеристики; отличие - вдоль характеристики решается ОДУ `v'=v^2`, поэтому появляется максимальная область до взрыва. Это скорее мост к будущему semilinear-кластеру, чем точное попадание в линейный PDE-кластер.

`mipt-excellent-legendre-violation-no-minimum` попала в фильтр как ложноположительный результат из-за слова `first_order` в служебном профиле/метках, но относится к вариационному исчислению. В рамках этого аудита вариационные кластеры не редактировались.

## Итоговая оценка

После правки в зоне первого порядка стало меньше случайных seed-карточек вне кластеров: базовые разделяющиеся и однородные уравнения получили собственный узкий кластер, а Клеро закреплен в кластере неразрешенных ОДУ. Оставшиеся вне representatives карточки либо являются осознанными дублями уже насыщенных кластеров, либо пока не имеют трех близких родственников с общим планом решения.
