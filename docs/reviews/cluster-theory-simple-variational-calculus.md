# Теоретико-методический блок simple-variational-calculus

Дата: 2026-05-27.

Зона: `simple-variational-calculus` / "Простейшая задача вариационного исчисления". Коммит и пуш не выполнялись.

## Что просмотрено

- `data/task_clusters/clusters.yaml`: политика насыщения и representatives кластера.
- `data/problems/local_du/standard_theory/local-du-standard-euler-lagrange-fixed-endpoints.yaml`
- `data/problems/local_du/standard_theory/local-du-standard-natural-boundary-conditions.yaml`
- `data/problems/local_du/standard_theory/local-du-standard-legendre-jacobi-conditions.yaml`
- `data/problems/local_du/romanko_selected/`: высшие производные, две функции, изопериметрия, Якоби.
- `data/problems/cluster_audit/variational_calculus/`: Эйлер-Пуассон, трансверсальность, коэрцитивный квадратичный минимум.
- `data/definitions/definitions.yaml`: использованы существующие definition_ids, новые определения не добавлялись.
- `data/relations/relations.d/cluster-variational-calculus.yaml`
- `docs/reviews/cluster-variational-calculus-audit.md`
- `docs/reviews/local-du-romanko-selection.md`

## Что добавлено

Добавлена карточка `cluster-variational-method-guide`:

- файл: `data/problems/cluster_audit/variational_calculus/cluster-variational-method-guide.yaml`;
- тип: `kind.primary=theorem`, `secondary=[task_cluster, method_guide, cluster_representative]`;
- tags: `task_cluster`, `cluster_representative`, `variational_calculus`, `euler_lagrange`, `natural_boundary_conditions`, `transversality`, `isoperimetric_problem`, `euler_poisson`, `second_variation`, `legendre_condition`, `jacobi_condition`, `sturm_liouville`, `eigenvalues`;
- включена в `representative_card_ids` кластера и в `data/import_batches/cluster-variational-calculus.yaml`.

Карточка покрывает:

- первую вариацию и основную лемму;
- уравнение Эйлера-Лагранжа для закрепленных концов;
- натуральные граничные условия;
- свободный и подвижный конец, условие трансверсальности;
- изопериметрическую задачу и множитель Лагранжа;
- несколько неизвестных функций и систему уравнений Эйлера;
- функционалы от высших производных и уравнение Эйлера-Пуассона;
- вторую вариацию;
- условия Лежандра и Якоби, сопряженные точки;
- различие стационарности, локального минимума и глобального минимума;
- границы с краевыми, спектральными и штурмовскими соседними кластерами.

## Определения и связи

В карточке проставлены `definition_ids` к уже существующим определениям:

- `functional`
- `extremal`
- `variation`
- `transversality_condition`
- `isoperimetric_problem`
- `conjugate_point`
- `jacobi_condition`
- `boundary_value_problem`
- `eigenvalue_problem`
- `eigenvalue_of_boundary_value_problem`

Новые graph-relations добавлены в `data/relations/relations.d/cluster-variational-calculus.yaml`:

- от guide к representative-блокам Эйлера-Лагранжа, натуральных условий, трансверсальности, изопериметрии, нескольким функциям, Эйлеру-Пуассону, Лежандру-Якоби, квадратичному порогу и глобальному коэрцитивному минимуму;
- содержательные контрастные связи к `boundary-spectral-problems` через `dirichlet-eigenvalues-interval`;
- связь к `linear-bvp-solvability-resonance` через `local-du-standard-resonant-linear-bvp-solvability`;
- связь к `sturm-oscillation-comparison` через `cluster-sturm-method-guide`.

## Источники

В принятом формате добавлены и использованы источники:

- `src-gelfand-fomin-calculus-variations`: классический русскоязычный теоретический источник.
- `src-sagan-calculus-variations`: классический учебник по вариационному исчислению.
- `src-mit-18086-calculus-variations-video`: MIT OCW, Lecture 23, видео по calculus of variations / weak form.

Также в guide использованы уже существующие:

- `src-local-du-8-program-or-exam`: локальная программа, раздел 7.
- `src-romanko-problem-book`: §§19-22 по вариационному исчислению.
- `src-calder-calculus-variations-notes`: открытый конспект для прямого метода, выпуклости и глобального минимума.

## Что не добавлялось

- Новые вычислительные вариационные задачи не добавлялись.
- Сложности существующих задач массово не менялись.
- Новые определения не дублировались в `data/definitions/definitions.yaml`.
- Соседние кластеры не расширялись новыми representative-карточками; добавлены только содержательные relations.

## Оставшиеся пробелы

- В базе пока нет отдельного курса/конспекта на русском языке с открытой URL-ссылкой именно по всему блоку вариационного исчисления; локальная программа и Романко закрывают русскоязычную часть как локальные/классические источники.
- Условие Вейерштрасса и сильный минимум сознательно не разворачивались: текущая зона ограничена простейшей задачей и ближайшими учебными расширениями.
- Поля экстремалей и достаточные условия глобального минимума вне квадратично-выпуклого случая оставлены как возможный будущий продвинутый слой, если курс потребует.
