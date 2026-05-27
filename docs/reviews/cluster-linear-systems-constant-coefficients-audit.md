# Аудит кластера constant-coefficient-linear-systems

Дата: 2026-05-26.

Зона: кластер `constant-coefficient-linear-systems` / "Линейные системы с постоянными коэффициентами". Просмотрены кластерные документы, отчеты `local-du-gap-and-dedup-report.md`, `english-import-qa.md` и карточки с тегами `linear_systems`, `matrix_exponential`, `jordan_form`, `constant_coefficients`, `variation_of_parameters`, `monodromy`, `floquet_multiplier`.

## Итог по покрытию

Кластер был неплохо покрыт, но список representatives не отражал часть уже имеющихся точных попаданий. В итоговый набор representatives включены:

- `resit-pass-3-diagonal-linear-system`: базовый 2x2 диагональный вещественный случай.
- `putnam-early-1939-a5-1-linear-system`: 2x2 неоднородная система с постоянными коэффициентами и комплексной парой после исключения.
- `linear-system-jordan-block`: минимальная жорданова клетка 2x2.
- `local-du-written-2014-51-system-jordan-zero`: 3x3 жорданова структура с нулевым собственным значением.
- `cluster-linear-systems-jordan-geometric-two`: 3x3 тройное собственное значение, два собственных вектора и присоединенный к `v1+v2`.
- `cluster-linear-systems-repeated-complex-four-dimensional`: компактный 4D представитель кратной комплексной пары.
- `waterloo-spiral-phase-portrait-isoclines`: комплексная пара и фазовый портрет фокуса.
- `mit-18034-pset07-periodic-initial-plane`: 3D система, где надо выделить инвариантную периодическую плоскость.
- `waterloo-fundamental-matrix-flow-inverse`: концептуальная карточка о фундаментальной матрице как потоке.
- `inhomogeneous-linear-system-variation`: общая формула вариации постоянных через `exp(At)`.
- `cluster-linear-systems-jordan-resonant-forcing`: малый неоднородный резонанс на жордановой клетке.
- `msu-ode-2006-2-det-integral-matrix-exp`: хорошая короткая матрично-экспоненциальная identity-card.

`msu-ode-2005-8-six-dimensional-resonance` оставлена в базе как красивая олимпиадная задача на комплексную блочную цепочку, но не должна быть основным representative для стандартного курса: это скорее advanced/olympiad card с `technical_score=6`.

## Проверка специальных случаев

- Различные вещественные собственные значения: есть слабые и базовые представители (`resit-pass-3-diagonal-linear-system`, `weak-pass-linear-system-saddle`).
- Кратные вещественные собственные значения и жорданова клетка: есть `linear-system-jordan-block`, `oral-middle-triangular-system-jordan`, `local-du-written-2014-51-system-jordan-zero`.
- Комплексная пара 2x2: есть `waterloo-spiral-phase-portrait-isoclines`, `putnam-early-1939-a5-1-linear-system`.
- Размерность 3: есть `local-du-written-2014-51-system-jordan-zero`, `mit-18034-pset07-periodic-initial-plane`.
- Размерность 4: до аудита не было компактного представителя с хорошей учебной ролью; добавлена `cluster-linear-systems-repeated-complex-four-dimensional`.
- Неоднородные системы: общая формула есть, но малый вычислительный пример с жордановым резонансом отсутствовал; добавлена `cluster-linear-systems-jordan-resonant-forcing`.
- Матричная экспонента: покрыта seed-картой, Waterloo flow-card и MSU determinant-card.
- Жорданова форма: покрыта 2x2, 3x3 local DU и новым специальным 3x3 случаем.
- Вариация постоянных: покрыта общей формулой и новым малым резонансным примером.
- Монодромия/Floquet: это соседняя теория периодических коэффициентов, не точное ядро кластера постоянных коэффициентов; карточки Teschl/Filippov лучше держать рядом, но не считать дублями.

## Обязательная проверка: тройное собственное значение

В базе не найдено однородной системы с постоянными коэффициентами 3 порядка, у которой одно собственное значение имеет алгебраическую кратность 3, собственных векторов ровно два, а присоединенный вектор присоединен к нетривиальной линейной комбинации этих двух собственных векторов.

Добавлена карточка `cluster-linear-systems-jordan-geometric-two`:

`A=[[1,0,1],[0,1,1],[0,0,1]]`.

Для `lambda=1` собственные векторы можно взять `v1=(1,0,0)^T`, `v2=(0,1,0)^T`. Присоединенный вектор `w=(0,0,1)^T` удовлетворяет `(A-I)w=v1+v2`. Решение:

`x(t)=e^t(C1 v1+C2 v2+C3(w+t(v1+v2)))`.

## Добавлено

| Карточка | Что закрывает | Почему не дубль |
|---|---|---|
| `cluster-linear-systems-jordan-geometric-two` | 3x3, одно собственное значение кратности 3, геометрическая кратность 2, присоединенный к `v1+v2`. | В существующих 3x3 задачах нет такого распределения кратностей и такой явной проверки присоединенного вектора. |
| `cluster-linear-systems-jordan-resonant-forcing` | Малый неоднородный резонанс на жордановой клетке; появление `t^2`. | В базе была общая формула вариации и 6D олимпиадный пример, но не было короткого стандартного вычислительного представителя. |
| `cluster-linear-systems-repeated-complex-four-dimensional` | 4D система с кратной комплексной парой и множителями `t cos t`, `t sin t`. | Не просто новая размерность: закрывает кратные комплексные собственные значения без громоздкой матрицы. |

## Дедупликация и оценки сложности

Удалений не делалось. Точных дублей, которые безопасно удалить без human review, не найдено.

Близкие группы:

- `linear-system-jordan-block`, `oral-middle-triangular-system-jordan`, `local-du-written-2014-51-system-jordan-zero`: близкие по методу, но отличаются уровнем и структурой матрицы; оставить.
- `weak-pass-resonance-double-root` и `constant-coeff-second-order-resonance`: очень близки для скалярных уравнений; это соседний скалярный кластер, не причина удалять системные задачи.
- Floquet/monodromy cards Teschl и Filippov: связаны с линейными системами, но относятся к периодическим коэффициентам, а не к постоянным коэффициентам.

Оценки `idea_score`/`technical_score` в новых карточках выставлены так, чтобы идея была видна, а техника не доминировала:

- 3x3 special Jordan: `idea_score=6`, `technical_score=3`.
- 2x2 inhomogeneous Jordan resonance: `idea_score=6`, `technical_score=3`.
- 4D repeated complex pair: `idea_score=6`, `technical_score=4`.

Нежелательные вычислительные монстры: новых не добавлено. `msu-ode-2005-8-six-dimensional-resonance` отмечена как advanced/olympiad representative only, не как шаблон для массового пополнения.

## Связи

Новые связи записаны только в `data/relations/relations.d/cluster-linear-systems-constant-coefficients.yaml`. Batch записан только в `data/import_batches/cluster-linear-systems-constant-coefficients.yaml`.
