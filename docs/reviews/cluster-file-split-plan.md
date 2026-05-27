# План безопасного разбиения task clusters

Дата прохода: 2026-05-27.

## Контекст

На момент начала прохода `data/task_clusters/clusters.yaml` содержал 34 кластера в одном JSON-compatible YAML файле. Это создает лишние конфликты для параллельных агентов: разные тематические аудиты меняют один и тот же большой файл, хотя работают с независимыми методическими зонами.

Во время этого подготовительного прохода параллельный агент уже сделал фактическое разбиение: `clusters.yaml` стал пустым файлом-оболочкой, а рядом появились тематические файлы. Я это состояние не откатывал и не перекладывал кластеры повторно.

Разбиение уже частично поддержано инфраструктурой:

- `tools/check_clusters.py` читает все `data/task_clusters/**/*.yaml`, валидирует каждый файл и проверяет уникальность `id` между файлами.
- `tools/check_cluster_guides.py` тоже читает все файлы в `data/task_clusters/`.
- `docs/TASK_CLUSTERS.md` уже говорит, что источник истины находится в `data/task_clusters/*.yaml`.

На старте прохода был важный блокер для фактического применения:

- `tools/build_index.py` читал только `data/task_clusters/clusters.yaml`.
- `tools/check_exam_simulation.py` в fallback-ветке тоже обращался напрямую к `data/task_clusters/clusters.yaml`.

Параллельный агент уже обновил оба загрузчика на обход `data_files("task_clusters")`. Это снимает главный технический блокер, но риск остается как правило для будущих похожих разбиений: данные и загрузчики должны переключаться в одном интеграционном изменении.

## Предлагаемая структура

Фактически появившаяся схема из 8 тематических файлов выглядит приемлемой: она снижает конфликты, но не превращает слой кластеров в десятки микрофайлов. Ее лучше не менять механически в том же окне, чтобы не создавать второй конфликтный split.

| Файл | Кластеры |
| --- | --- |
| `linear.yaml` | `linear-first-order-ode`, `linear-equations-variable-coefficients`, `variation-of-constants`, `floquet-periodic-linear-systems`, `scalar-constant-coefficient-linear-ode`, `power-series-linear-ode`, `wronskian-nonlinear-transforms` |
| `systems.yaml` | `constant-coefficient-linear-systems`, `matrix-exponential-methods`, `first-integrals-plane-systems`, `fundamental-matrix-linear-systems` |
| `first_order.yaml` | `separable-homogeneous-first-order`, `integrating-factor-exact-forms`, `pde-characteristics-first-order`, `riccati-bernoulli-reductions`, `recover-ode-from-family`, `implicit-ode-discriminant`, `orthogonal-trajectories`, `guess-cauchy-solution-uniqueness` |
| `qualitative.yaml` | `phase-line-stability`, `energy-estimates-second-order-ode`, `existence-uniqueness-continuation`, `limit-cycles-qualitative-criteria` |
| `bvp.yaml` | `boundary-spectral-problems`, `sturm-oscillation-comparison`, `green-functions-bvp`, `linear-bvp-solvability-resonance` |
| `variational.yaml` | `simple-variational-calculus`, `parameter-dependence-variational-equation` |
| `olympiad.yaml` | `olympiad-transformed-linear-mvt`, `olympiad-differential-inequalities-barriers`, `olympiad-functional-differential-equations` |
| `misc.yaml` | `nonlinear-second-order-order-reductions`, `integral-equation-to-ode` |

## Почему так

- `linear.yaml` отделяет линейные скалярные техники и линейные методы без выраженной системной геометрии.
- `systems.yaml` выносит матричные и системные сюжеты, где чаще редактируются фундаментальные матрицы, экспоненты, фазовая плоскость и линейные системы.
- `first_order.yaml` собирает задачи, где редактор обычно думает через замены, точные формы, характеристики или восстановление уравнения из семейства.
- `qualitative.yaml` держит качественную теорию: устойчивость, энергетические оценки, продолжение решений и предельные циклы.
- `bvp.yaml` покрывает краевые, спектральные, Штурмовские и Green-function кластеры, которые часто редактируются одним тематическим проходом.
- `variational.yaml` сейчас маленький, но это отдельная методическая область и частый источник крупных правок.
- `olympiad.yaml` отделяет кластеры, где критерий похожести определяется олимпиадным приемом, а не только курсом ДУ.
- `misc.yaml` лучше оставить маленьким карантином для межтематических редукций, которые плохо ложатся в основной набор.

## Dry-run скрипт

Добавлен вспомогательный скрипт:

```powershell
python tools\plan_split_clusters.py
```

Он читает `data/task_clusters/clusters.yaml` и печатает план разнесения cluster id по тематическим файлам. По умолчанию он ничего не пишет.

Если `clusters.yaml` уже пуст, скрипт читает соседние тематические файлы и печатает текущую карту. Это сделано специально для текущего параллельного состояния репозитория.

Для безопасной подготовки файлов в staging-каталог:

```powershell
python tools\plan_split_clusters.py --write --output-dir .scratch\task-cluster-split --force
```

Это не меняет `data/task_clusters/clusters.yaml` и не включает split-файлы в рабочий слой данных.

## Точная команда для будущего применения

Фактическое применение или исправление уже сделанного split нужно делать только в интеграционном окне, когда никто не правит `data/task_clusters/`.

Минимальный безопасный порядок:

1. Обновить `tools/build_index.py`, чтобы `load_task_clusters()` читал все `data/task_clusters/**/*.yaml`, а не только `clusters.yaml`.
2. Обновить fallback в `tools/check_exam_simulation.py`, если этот скрипт входит в обязательный набор проверок.
3. Сгенерировать тематические файлы в staging:

```powershell
python tools\plan_split_clusters.py --write --output-dir .scratch\task-cluster-split --force
```

4. После review перенести staged-файлы в `data/task_clusters/` и в том же изменении удалить или заменить пустым старый `data/task_clusters/clusters.yaml`, чтобы не было дубликатов cluster id. В текущем рабочем дереве пункты 1, 2 и 4 уже частично выполнены параллельным агентом.
5. Запустить:

```powershell
python tools\check_clusters.py
python tools\build_index.py
```

Команду записи сразу в production-каталог можно использовать только после пунктов 1-2 и при эксклюзивном lock на кластерный слой:

```powershell
python tools\plan_split_clusters.py --write --output-dir data\task_clusters --force
```

После нее старый `clusters.yaml` должен быть удален или очищен в том же commit/change set до запуска `check_clusters.py`; иначе валидатор корректно упадет на duplicate cluster id.

## Риски

- Потеря кластеров в viewer/index: если разбить данные, но оставить `build_index.py` на одном `clusters.yaml`, `index/generated.json` получит неполный `task_clusters`. В текущем рабочем дереве `build_index.build_data()` уже видит 34 кластера.
- Дубликаты id: если новые файлы положить рядом со старым монолитом, `check_clusters.py` найдет все кластеры дважды.
- Параллельные правки: текущая MVT/cluster-зона уже изменяется другими агентами, поэтому применять split сейчас нельзя.
- Порядок кластеров: при split нужно сохранить порядок внутри тематических файлов; глобальный порядок после склейки должен быть стабильным и документированным.
- Ссылки в документах: многие review-документы исторически называют `data/task_clusters/clusters.yaml`; это не блокер, но новые инструкции лучше писать как `data/task_clusters/*.yaml`.

## Проверки для будущего PR

Минимум после реального split:

```powershell
python tools\check_encoding.py
python tools\validate.py
python tools\check_links.py
python tools\audit_rules.py
python tools\check_clusters.py
python tools\build_index.py
```

Если `validate.py` или `check_clusters.py` падают из-за параллельно незавершенных карточек/relations, нужно фиксировать точные ошибки и не смешивать их с механическим разбиением.
