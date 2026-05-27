# Теоретико-методический блок: limit-cycles-qualitative-criteria

Дата: 2026-05-27. Зона: `limit-cycles-qualitative-criteria` - предельные циклы и качественные критерии на фазовой плоскости.

## Что просмотрено

- `data/task_clusters/clusters.yaml`, representatives кластера `limit-cycles-qualitative-criteria`.
- Стартовые карточки `test-limit-cycles-radial-semistable`, `test-limit-cycles-bendixson-quadrants`, `test-limit-cycles-index-inside`.
- Соседние узлы `bendixson-no-cycles`, `putnam-early-1960-b3-fluid-flow`, `msu-ode-2026-5-polar-stable-not-asymptotic`.
- Методические блоки соседних кластеров `phase-line-stability` и `first-integrals-plane-systems`.
- Слой определений `data/definitions/definitions.yaml` и стандартные идеи `bendixson_divergence`, `radial_limit_cycle_stability`, `poincare_index_inside_cycle`.

## Что добавлено

Добавлена отдельная теоретико-методическая карточка:

- `data/problems/cluster_audit/limit_cycles_qualitative_criteria/cluster-limit-cycles-qualitative-criteria-method-guide.yaml`.

Карточка помечена как:

- `kind.primary = theorem`;
- `kind.secondary = task_cluster, method_guide, cluster_representative`;
- теги `task_cluster`, `method_guide`, `cluster_representative`.

В `representative_card_ids` кластера добавлен `cluster-limit-cycles-qualitative-criteria-method-guide` первым элементом, чтобы блок открывал кластер как теоретический навигатор.

Создан batch:

- `data/import_batches/cluster-limit-cycles-qualitative-criteria.yaml`.

## Покрытые темы

- Определение предельного цикла как изолированной замкнутой фазовой траектории.
- Отличие замкнутой траектории от предельного цикла: семейство замкнутых уровней первого интеграла дает периодические траектории, но не изолированные циклы.
- Критерий Бендиксона как уже существующий в базе запретительный критерий.
- Вариант Бендиксона-Дюлака упомянут как расширение: если множитель не дан явно, его подбор отмечен как выход за стандартную программу.
- Радиальная редукция `r'=R(r)` и чтение устойчивости цикла по фазовой прямой для радиуса.
- Связь с устойчивостью: устойчивый, неустойчивый, полуустойчивый цикл; отличие устойчивости цикла от устойчивости равновесия.
- Связь с фазовой плоскостью, первыми интегралами и центрами.
- Теорема Пуанкаре-Бендиксона, отображение Пуанкаре и индекс Пуанкаре отмечены как продвинутый слой, особенно если требуется доказательство.

## Определения

В `data/definitions/definitions.yaml` добавлены:

- `closed_phase_trajectory`;
- `limit_cycle`;
- `bendixson_criterion`;
- `poincare_index`.

Новые определения нужны, чтобы method guide и существующие задачи на предельные циклы ссылались на общий слой терминов, а не повторяли определения в тексте каждой карточки.

## Связи

Добавлен файл:

- `data/relations/relations.d/cluster-limit-cycles-qualitative-criteria.yaml`.

Связи от навигатора поставлены к representative-задачам и соседним теоретическим узлам:

- `test-limit-cycles-radial-semistable`;
- `test-limit-cycles-bendixson-quadrants`;
- `test-limit-cycles-index-inside`;
- `putnam-early-1960-b3-fluid-flow`;
- `bendixson-no-cycles`;
- `msu-ode-2026-5-polar-stable-not-asymptotic`;
- `cluster-first-integrals-plane-systems-method-guide`;
- `cluster-phase-stability-method-guide`.

## Что не добавлялось

- Новые вычислительные задачи на предельные циклы не добавлялись.
- Новая отдельная карточка на критерий Дюлака не добавлялась: в текущей базе уже есть Бендиксон, а Дюлак оставлен как упоминание продвинутого расширения.
- Теорема Пуанкаре-Бендиксона не оформлялась отдельным theorem-card, потому что задача была создать методический блок кластера, а не расширять теоретическую базу динамических систем.

## Оставшиеся пробелы

- Можно позже добавить отдельную короткую карточку на ловящую область и применение Пуанкаре-Бендиксона без доказательства.
- Можно добавить визуальную карточку, где рядом показаны центр с семейством замкнутых траекторий и изолированный предельный цикл.
- Если в локальной программе появится конкретный конспект по критерию Дюлака, стоит заменить общее упоминание на отдельную теорему или стандартный факт.
