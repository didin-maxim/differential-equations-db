# Cross-source аудит неолимпиадных задач вне кластеров

Дата: 2026-05-27.

Зона аудита: задачи из `data/problems/oral_exam`, `data/problems/local_du`, `data/problems/english_sources`, плюс проверка пропущенных представителей существующих кластеров. Олимпиадные карточки не трогались.

## Итоговые числа

- Проверено целевых задач: 147.
- Уже или теперь представлены в кластерах: 142.
- Остались вне `representative_card_ids`: 5.
- Задач из этой зоны, входящих более чем в один кластер: 24.
- Кластеров после аудита: 30.

Разбивка целевых задач по источникам:

- `oral_exam`: 60 задач.
- `local_du`: 55 задач.
- `english_sources`: 32 задачи.

Вне кластеров после аудита:

- `oral_exam`: 3 задачи.
- `local_du`: 2 задачи.
- `english_sources`: 0 задач.

## Исправления кластеров

Добавлена пропущенная задача `oral-middle-integrating-factor-x` в `integrating-factor-exact-forms`: это точное попадание по критерию интегрирующего множителя `mu(x)`, хотя первообразная после множителя неэлементарна.

Не создавался новый дубль для скалярных линейных уравнений с постоянными коэффициентами: параллельный аудит уже добавил `scalar-constant-coefficient-linear-ode`. В этом проходе был снят дублирующий кластер `constant-coefficient-linear-equations`, а существующий кластер оставлен единственным.

Почищена битая кириллица в новых/обновленных cluster notes и в кластерах:

- `scalar-constant-coefficient-linear-ode`
- `linear-bvp-solvability-resonance`
- `fundamental-matrix-linear-systems`
- `power-series-linear-ode`

Также уточнены notes у пересекающихся кластеров, чтобы membership не читался как общий тег: `matrix-exponential-methods`, `boundary-spectral-problems`, `phase-line-stability`, `variation-of-constants`, `sturm-oscillation-comparison`, `green-functions-bvp`, `floquet-periodic-linear-systems`, `parameter-dependence-variational-equation`.

## Глубокие родственные связи

Добавлен файл `data/relations/relations.d/non-olympiad-cross-source-audit.yaml`.

Связи поставлены только по переносимому механизму:

- `exact-equation-potential` -> `resit-pass-3-exact-equation-potential`: точная форма, проверка `M_y=N_x`, восстановление потенциала.
- `exact-equation-potential` -> `weak-pass-exact-form-recognition`: тот же механизм точной формы.
- `oral-above-three-integrating-factor-x-only` -> `oral-middle-integrating-factor-x`: тот же критерий множителя `mu(x)`.
- `local-du-written-2014-51-nonlinear-cauchy-total-derivative` -> `local-du-written-2024-nonlinear-p-of-y`: родственная редукция порядка, но разные замены.
- `linear-first-order-formula` -> `local-du-written-2024-nonlinear-p-of-y`: после замены получается линейное уравнение первого порядка.
- `cluster-phase-stability-lyapunov-direct-method` -> `oral-exam-strong-10-symmetric-part-stability`: прямой метод Ляпунова через производную нормы.
- `waterloo-second-order-pq-stability` -> `oral-exam-strong-10-symmetric-part-stability`: контраст спектрального критерия постоянных коэффициентов и неавтономной оценки через симметрическую часть.

Связи по источнику, уровню экзамена или широкой теме не добавлялись.

## Оставленные вне кластеров

`local-du-written-2014-51-nonlinear-cauchy-total-derivative`

Проверены ближайшие механизмы: `energy-estimates-second-order-ode`, `first-integrals-plane-systems`, `riccati-bernoulli-reductions`, `linear-first-order-ode`. В кластер не добавлена: задача держится на специальном сворачивании `yy''+(y')^2=(yy')'`, а не на энергетической оценке, фазовом интеграле или стандартной Бернулли/Риккати-редукции. Поставлена relation к задаче `p(y)` как близкой редукции порядка.

`local-du-written-2024-nonlinear-p-of-y`

Проверены ближайшие механизмы: `riccati-bernoulli-reductions`, `linear-first-order-ode`, `energy-estimates-second-order-ode`. В кластер не добавлена: после замены действительно возникает линейное уравнение, но главный ход - автономная редукция второго порядка `p=p(y)`, а не стандартный кластер Бернулли/Риккати. Поставлены relations к линейному уравнению первого порядка и к предыдущей задаче редукции порядка. Для нового кластера пока только 2 близкие задачи, меньше порога 3 из разных источников.

`resit-pass-3-exact-equation-potential`

Проверен кластер `integrating-factor-exact-forms`. В representatives не добавлена сознательно: политика кластера уже говорит, что слабые/пересдачные exact-form карточки являются дублями базового `exact-equation-potential`. Поставлена relation same_method.

`weak-pass-exact-form-recognition`

Проверен кластер `integrating-factor-exact-forms`. В representatives не добавлена по той же причине: это хороший минимальный устный дубль метода точной формы, но не новый вариант. Поставлена relation same_method.

`oral-exam-strong-10-symmetric-part-stability`

Проверены ближайшие механизмы: `phase-line-stability`, `energy-estimates-second-order-ode`, `fundamental-matrix-linear-systems`, `matrix-exponential-methods`. В кластер не добавлена как representative: это не фазовая прямая, не фазовая плоскость и не матричная экспонента; это неавтономная оценка нормы через симметрическую часть. Поставлены две relations: generalization от прямого метода Ляпунова и contrast со спектральным критерием постоянных коэффициентов. Если позже появятся еще 2-3 задачи из разных источников на логарифмические нормы/симметрическую часть, стоит создать отдельный кластер.

## Пересечения кластеров

Много-кластерные задачи после аудита в основном оправданы переносимыми механизмами:

- `trench-bvp-dirichlet-resonance-sine-condition`: spectral/resonance/Green-Fredholm пересечение.
- `local-du-written-2016-global-first-integrals-source`: поток линейной системы, `det(e^{At})`, первый интеграл и фундаментальная матрица.
- `oral-exam-excellent-two-point-fundamental-matrix`: постоянная система, вариация постоянных/краевое условие и фундаментальная матрица.
- `local-du-8-t2-exponential-coefficient-energy-bound`, `local-du-written-2020-energy-monotonicity-exp-inverse`: энергетический аргумент, который одновременно дает штурмовский/нулевой вывод.

Неудачных пересечений вида "общий тег вместо метода" в целевой зоне после правки не найдено; пограничные места отмечены в notes кластеров.

## Проверки

Пройдены:

```text
python tools\validate.py
python tools\check_clusters.py
python tools\check_links.py
python tools\check_encoding.py
```

Результат `validate`: 357 cards, 498 relations, 38 sources.
