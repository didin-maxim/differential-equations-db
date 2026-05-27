# MIT 18.034 Honors ODE: выборочный импорт

Дата: 2026-05-26.

Источник: MIT OpenCourseWare 18.034 Honors Differential Equations, Spring 2009, раздел Assignments: https://ocw.mit.edu/courses/18-034-honors-differential-equations-spring-2009/resources/assignments/

## Что просмотрено

Просмотрены problem sets 1-9 и solution keys 1-9. В импорт не брались задачи, которые являются чистой тренировкой constant coefficients, Laplace transform, Bernoulli/Riccati без новой идеи, а также пункты с внешней ссылкой на Birkhoff-Rota без полного условия в MIT PDF.

## Добавлено

| Карточка | Локатор | Роль |
|---|---|---|
| `mit-18034-pset03-resonance-limit` | Problem Set #3, Problem 1 | Резонанс как предельный переход по частоте. |
| `mit-18034-pset03-one-sided-lipschitz-gronwall` | Problem Set #3, Problem 2 | Односторонний Липшиц и оценка расстояния между решениями. |
| `mit-18034-pset03-bvp-maximum-principle` | Problem Set #3, Problem 5 | Краевая задача через максимум-принцип. |
| `mit-18034-pset05-picard-tail-estimate` | Problem Set #5, Problem 2 | Количественная оценка хвоста итераций Пикара. |
| `mit-18034-pset05-second-order-picard-integral` | Problem Set #5, Problem 3 | Интегральное уравнение для второго порядка и сходимость итераций. |
| `mit-18034-pset07-euler-system-fundamental-matrix` | Problem Set #7, Problem 4 | Переменно-коэффициентная система через уравнение Эйлера. |
| `mit-18034-pset07-periodic-initial-plane` | Problem Set #7, Problem 6 | Подпространство начальных данных, дающее периодическое решение. |
| `mit-18034-pset08-prufer-oscillation-criteria` | Problem Set #8, Problem 6 | Угловые переменные Пруфера и неосцилляция. |
| `mit-18034-pset09-hamiltonian-folium-first-integral` | Problem Set #9, Problem 1(b) | Первый интеграл и фолии Декарта. |
| `mit-18034-pset09-omega-limit-linearization` | Problem Set #9, Problem 2 | Предел траектории и локальная линеаризация. |
| `mit-18034-pset09-lyapunov-nonlinear-stable` | Problem Set #9, Problem 6(b) | Нелинейная устойчивость при неудачной линеаризации. |

## Дедупликация

Проверялись формулы и механизмы по `rg` в `data/problems`: `resonance`, `Picard`, `one-sided`, `Lipschitz`, `maximum principle`, `fundamental matrix`, `periodic`, `Prufer`, `oscillation`, `first_integral`, `Lyapunov`. Задачи из насыщенных областей добавлены только там, где новая роль отличалась от типового счета: например резонанс как предел, периодичность как подпространство начальных данных, и Ляпуновский контраст с неустойчивой линеаризацией.

## Файлы

Карточки: `data/problems/english_sources/mit_18034_honors/`.

Связи: `data/relations/relations.d/english-mit-18034-honors.yaml`.

Batch: `data/import_batches/english-mit-18034-honors.yaml`.
