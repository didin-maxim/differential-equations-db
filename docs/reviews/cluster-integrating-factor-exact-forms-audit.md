# Аудит кластера `integrating-factor-exact-forms`

Дата прохода: 2026-05-27.

Зона: `data/task_clusters/clusters.yaml`, документация по кластерам, обзор saturation, карточки `data/problems/**` с тегами и объектами `integrating_factor`, `exact_equation`, `homogeneous_first_order`, `differential_form`, `first_integral`, `linear_first_order`, а также локальные письменные, олимпиадные, English imports, Романко и Филиппов.

## Что найдено в базе

Точные представители формы `M dx+N dy`:

| карточка | роль в кластере | решение |
|---|---|---|
| `exact-equation-potential` | базовая точная форма | восстановление потенциала |
| `oral-above-three-integrating-factor-x-only` | короткий `mu(x)` | стандартный критерий `(M_y-N_x)/N=f(x)` |
| `oral-middle-integrating-factor-x` | более технический `mu(x)` | тот же критерий, но с неэлементарной первообразной в потенциале |
| `integrating-factor-y` | однородная форма | множитель `1/(xM+yN)`; название уточнено в этом аудите |
| `msu-ode-2008-11-integrating-factor-family` | олимпиадная теория множителей | все множители через функцию первого интеграла |
| `putnam-early-1956-b1-homogeneous-exact-first-integral` | точная однородная форма и первый интеграл | формула Эйлера плюс точность |

Близкие, но не включенные как representatives:

- `weak-pass-exact-form-recognition` и `resit-pass-3-exact-equation-potential`: полезные уровневые дубли базового восстановления потенциала.
- IMC/олимпиадные задачи на множитель в линейном первом порядке или линейном операторе (`imc-2023-p7-boundary-linear-expression`, `imc-2025-p6-derivative-of-f-over-x`, `imc-1994-p3-rolle-integrating-factor`, `ru-misc-nure-8-4`): главный объект там не форма `M dx+N dy`, поэтому оставлены вне этого кластера.
- First-integral/phase-plane карточки Романко, Филиппова и local_du: относятся к кластерам фазовой плоскости, PDE characteristics или first integrals systems, а не к точным 1-формам.

## Покрытие после аудита

| вариант | статус |
|---|---|
| простое точное уравнение | покрыто `exact-equation-potential` |
| множитель `mu(x)` | покрыто `oral-above-three-integrating-factor-x-only`; технический дубль `oral-middle-integrating-factor-x` не повышает идею |
| множитель `mu(y)` | добавлено `cluster-integrating-factor-mu-y-short` |
| степенной множитель `x^a y^b` | добавлено `cluster-integrating-factor-power-monomial` |
| множитель `mu(xy)` | добавлено `cluster-integrating-factor-mu-xy` |
| однородная форма | покрыто `integrating-factor-y` и Putnam 1956 B1 |
| олимпиадный трюк с множителем | покрыто `msu-ode-2008-11-integrating-factor-family` |
| связь с первым интегралом | покрыто `msu-ode-2008-11-integrating-factor-family`, Putnam 1956 B1 и новыми карточками |

## Что изменено

- В `clusters.yaml` allowed variants разделены на `mu_x`, `mu_y`, `homogeneous_form`, `power_monomial`, `special_product_or_ratio`, `family_of_multipliers`.
- В representatives добавлены `oral-above-three-integrating-factor-x-only`, `cluster-integrating-factor-mu-y-short`, `cluster-integrating-factor-power-monomial`, `cluster-integrating-factor-mu-xy`.
- Добавлены три компактные карточки в `data/problems/cluster_audit/integrating_factor_exact_forms/`.
- Добавлены связи в `data/relations/relations.d/cluster-integrating-factor-exact-forms.yaml`.
- Добавлен batch `data/import_batches/cluster-integrating-factor-exact-forms.yaml`.
- У карточки `integrating-factor-y` уточнены title и метаданные: это представитель однородной формы, а не `mu(y)`.

## Политика сложности

Длинная первообразная не повышает `idea_score`: `oral-middle-integrating-factor-x` остается техническим вариантом стандартного `mu(x)`. Новые карточки оценивают именно идею выбора множителя:

- `mu(y)`: идея 5, техника 3.
- `x^a y^b`: идея 7, техника 4.
- `mu(xy)`: идея 6, техника 2.

Дальше кластер лучше считать почти закрытым: новые карточки добавлять только при реально новом коротком критерии интегрирующего множителя или существенной области определения.

## Проверки

Финальный прогон после правок:

- `python tools\validate.py` - OK: 308 cards, 351 relations, 27 sources.
- `python tools\check_links.py` - OK: links are consistent.
- `python tools\audit_rules.py` - OK: audit finished with 0 warnings.
- `python tools\check_clusters.py` - OK: 22 task clusters in 1 file.
- `python tools\build_index.py` - OK: rebuilt `index/generated.json` with 308 cards.
- `python tools\build_viewer.py` - OK: rebuilt `viewer/index.html`.
