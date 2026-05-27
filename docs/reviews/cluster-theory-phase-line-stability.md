# Теоретико-методический блок: phase-line-stability

Дата: 2026-05-27.

Зона работы: кластер `phase-line-stability` и ближайший слой `data/problems/cluster_audit/phase_stability/`.

## Что добавлено

- Добавлена карточка `cluster-phase-stability-method-guide`: методический навигатор по фазовой прямой, фазовой плоскости и устойчивости.
- Карточка имеет `kind.primary = theorem`, вторичные типы `task_cluster` и `method_guide`; это не новая вычислительная задача и не очередной пример классификации матрицы.
- Карточка добавлена в `representative_card_ids` кластера и в `data/import_batches/cluster-phase-stability.yaml`.
- Добавлены graph-relations от навигатора к ключевым теоретическим карточкам и задачам кластера в `data/relations/relations.d/cluster-phase-stability.yaml`.
- Источники подключены в принятом формате карточки через существующие `source_id`: МФТИ ДУ, Арнольд, Teschl, Lebl, Waterloo AMATH 250, MIT 18.03SC как видеокурс.

## Покрытые методы

- Фазовая прямая для `y'=f(y)`: равновесия, интервалы знакопостоянства, стрелки, устойчивость, неустойчивость и полуустойчивость.
- Устойчивость по Ляпунову и асимптотическая устойчивость: отдельная проверка удержания в окрестности и сходимости.
- Линейная классификация на плоскости: седло, узел, фокус, центр, кратные и нулевые собственные значения.
- Линеаризация гиперболического равновесия: когда спектр Якобиана переносит вывод на нелинейную систему и где метод перестает работать.
- Первый интеграл: замкнутые уровни, центр, устойчивость без асимптотической устойчивости.
- Прямой метод Ляпунова: положительно определенная функция, знак производной вдоль поля, различие между `Vdot<=0` и `Vdot<0`.

## Связи

Определения подключены через `definition_ids` новой карточки:

- `equilibrium`;
- `phase_trajectory`;
- `lyapunov_stability`;
- `asymptotic_stability`;
- `phase_line`;
- `linear_system`;
- `first_integral`;
- `lyapunov_function`;
- `autonomous_equation`.

Отдельные relations добавлены к теоретическим карточкам:

- `cluster-phase-stability-lyapunov-definitions`;
- `cluster-phase-stability-linear-plane-classification`;
- `cluster-phase-stability-linearization-hyperbolic`;
- `cluster-phase-stability-lyapunov-direct-method`;
- `cluster-phase-stability-first-integral-center`.

И к ключевым задачам и иллюстрациям:

- `autonomous-phase-line-stability`;
- `weak-pass-phase-line-semistable`;
- `cluster-phase-stability-visual-asymptotic-sink`;
- `local-du-filippov-889-attractive-not-lyapunov-stable`;
- `lyapunov-linearization-example`;
- `local-du-romanko-first-integral-center`;
- `lebl-diffyqs-degenerate-linearization-critical-point`.

## Поиск и отображение

Карточка должна находиться:

- по кластеру `phase-line-stability`, потому что добавлена в representatives;
- по тегам `task_cluster`, `cluster_representative`, `phase_line`, `phase_plane`, `stability`, `lyapunov`, `first_integral`;
- в теоретическом слое viewer, так как `kind.primary = theorem`, а не `problem`.

## Оставшиеся пробелы

- Не добавлялись новые однотипные задачи на классификацию матриц 2x2: кластер уже насыщен такими представителями.
- Параметрическое рождение равновесий и аккуратные барьерные аргументы на фазовой прямой остаются редкими программными связками, но они лучше требуют отдельных задач только при новой идее.
- Видеоматериалы пока представлены существующим MIT OCW video course; отдельный русскоязычный видеокурс не добавлялся, чтобы не расширять схему источников без точной проверенной ссылки.

## Проверки

Предварительно после правок прошли:

```powershell
python tools\validate.py
python tools\check_links.py
python tools\check_clusters.py
```

Полный обязательный прогон выполнен после отчета в порядке из задачи.
