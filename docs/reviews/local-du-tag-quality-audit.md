# Аудит качества меток local_du

Дата прохода: 2026-05-26. Зона прохода: `data/taxonomy/tags.yaml` и фактические `tags` в `data/problems/**`, с правками только в `data/problems/local_du/**`.

## Правило хорошей метки

Хорошая содержательная метка выделяет небольшой переносимый класс задач и заранее говорит, какой механизм надо распознать. Она должна быть однозначной без чтения всей карточки: `integrating_factor`, `free_endpoint_variational`, `implicit_ode_discriminant`, `first_order_pde_characteristics`, `prufer_angle`, `sturm_zero_count`.

Плохая содержательная метка слишком широкая, описывает целый раздел курса или только внешний вид задачи: `boundary_value`, `linear_higher_order`, `comparison`, `stability`, `asymptotic`, `nonlinear_transform`, если она стоит без более точного уточнения. Такие метки можно временно оставлять как верхнеуровневые навигационные рубрики, но они не должны быть единственным содержательным описанием новой карточки.

Служебные метки другого типа допустимы, но их нельзя смешивать с математическими механизмами при оценке качества: `local_du`, `written_exam`, `mipt_core`, `standard_course_methods`, `advanced_standard_course`, `complete_proof`, `exam_score_*`, `program_deficit`, `cluster_representative`. Это фильтры источника, уровня, статуса или редакционного назначения, а не математические классы.

## Что оставлять верхним уровнем

Оставить как верхнеуровневые рубрики и не ломать валидатор сейчас:

- Разделы курса: `linear_first_order`, `linear_higher_order`, `linear_systems`, `boundary_value`, `sturm_liouville`, `phase_plane`, `stability`, `first_integral`, `existence_uniqueness`.
- Общие методы-облака: `comparison`, `energy_method`, `differential_inequality`, `zero_location`, `asymptotic`, `nonlinear_transform`, `wronskian`.
- Служебные фильтры: `local_du`, `written_exam`, `mipt_core`, `standard_course_methods`, `advanced_standard_course`, `complete_proof`, `source_solution_checked`, `exam_score_*`.

Для новых local_du карточек правило такое: если оставлена широкая рубрика, рядом должна стоять хотя бы одна точная метка из механизма. Например, `comparison` + `sturm_comparison` или `zero_location` + `sturm_zero_count`.

## Добавленные точные метки

В `data/taxonomy/tags.yaml` добавлены только метки, сразу использованные в local_du карточках:

- `first_order_pde_characteristics`, `characteristic_cauchy_data`
- `implicit_ode_discriminant`
- `parameter_sensitivity_ivp`
- `change_independent_variable`, `order_reduction_substitution`, `p_of_y_reduction`
- `free_endpoint_variational`, `second_variation_test`, `quadratic_variational_threshold`
- `sturm_comparison`, `sturm_zero_count`, `liouville_transform`, `prufer_angle`, `bessel_equation`
- `equilibrium_linearization`
- `affine_solution_space`, `wronskian_obstruction`

## Исправления в local_du

Точечно исправлены широкие или неудачные метки:

- `local-du-deficit-first-order-pde-characteristics`: заменена слишком общая `differential_operator` на `first_order_pde_characteristics` и `characteristic_cauchy_data`.
- `local-du-written-2014-51-characteristics-pde`, `local-du-written-2023-characteristics-plane-data`: добавлена `first_order_pde_characteristics`.
- `local-du-written-2022-implicit-discriminant`: заменена ошибочная/слишком близкая к другому классу `clairaut` на `implicit_ode_discriminant`.
- `local-du-written-2011-21-parameter-variations`, `local-du-written-2023-parameter-sensitivity`: добавлена `parameter_sensitivity_ivp`.
- `local-du-written-2022-inverse-square-change`: добавлена `change_independent_variable`.
- `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2024-linear-y-xu-reduction`, `local-du-written-2024-nonlinear-p-of-y`: добавлены точные метки редукции порядка; для p(y) отдельно `p_of_y_reduction`.
- Вариационные local_du карточки получили `variational_calculus`/`euler_lagrange` там, где раньше оставался только `boundary_value`, плюс точные `free_endpoint_variational`, `second_variation_test`, `quadratic_variational_threshold` по фактическому механизму.
- Штурмовские и бесселевы карточки `theory_8` получили `sturm_comparison`, `sturm_zero_count`, `liouville_transform`, `prufer_angle`, `bessel_equation` там, где эти методы уже были явно записаны в профиле.
- Карточки на равновесия и линеаризацию получили `equilibrium_linearization`.
- Карточка про аффинное пространство решений получила `affine_solution_space` и `wronskian_obstruction`.

## Мертвые или спорные метки

На момент прохода не используются:

- `mean_value_theorem`
- `exam_score_9`
- `theoretical_exam_task`
- `transversality`
- `isoperimetric_problem`
- `task_cluster`
- `duplicate_filtered`

Не удалял их, чтобы не ломать чужой ожидаемый словарь. `transversality` и `isoperimetric_problem` выглядят хорошими будущими точными метками для вариационного блока. `exam_score_9` симметрична шкале экзамена. `task_cluster` и `duplicate_filtered` выглядят скорее редакционными статусами; лучше решить отдельно, должны ли они жить в `tags` или в batch/editorial metadata.

## Нерешенные вопросы

1. Часть карточек в `data/problems/local_du/**` не имеет top-level `local_du`, хотя источник и путь локальные. Я не стал массово добавлять эту служебную метку: надо решить, является ли `local_du` обязательным фильтром для всех локальных карточек или достаточно `sources`/пути/`kind.secondary`.
2. В профилях есть много значений вроде `keywords: local_du_8`, `objects: mipt_core`, `methods: comparison_argument`. Это полезный сырой профиль, но не все такие значения надо продвигать в taxonomy. Продвигать стоит только переносимые механизмы, которые будут использоваться хотя бы небольшим классом задач.
3. Широкие математические метки пока остаются в базе ради совместимости. Для будущей миграции лучше пройти по старым карточкам отдельным отчетом: `comparison -> sturm_comparison / asymptotic_comparison / energy_comparison`, `boundary_value -> eigenvalue_bvp / free_endpoint_variational / shooting_parameter`, `nonlinear_transform -> p_of_y_reduction / riccati_substitution / invariant_transform`.

## Проверки

После правок запускались:

```powershell
python tools\validate.py
python tools\check_links.py
python tools\audit_rules.py
```

Финальный результат: `validate` - OK: 190 cards, 168 relations, 14 sources; `check_links` - OK; `audit_rules` - OK, 0 warnings.
