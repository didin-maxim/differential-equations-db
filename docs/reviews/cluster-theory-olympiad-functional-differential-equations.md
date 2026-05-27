# Теоретико-методический блок: olympiad-functional-differential-equations

Дата: 2026-05-27.

## Что добавлено

- Создана карточка `cluster-olympiad-functional-differential-method-guide`.
- Карточка помечена как `theorem`, `task_cluster`, `method_guide`, `cluster_representative`, `theory_bridge`.
- Добавлен batch `data/import_batches/cluster-olympiad-functional-differential-equations.yaml`.
- Добавлен файл связей `data/relations/relations.d/cluster-olympiad-functional-differential-equations.yaml`.
- В `data/task_clusters/clusters.yaml` методический блок поставлен первым representative кластера.
- В слой определений добавлены `functional_differential_equation`, `argument_involution`, `function_composition`.

Новые олимпиадные задачи не добавлялись.

## Покрытие

Блок фиксирует, что задача остается в базе ДУ, если производная является не декорацией, а рабочим механизмом: функциональное условие после повторной подстановки, дифференцирования, итерации или оценки сводится к ОДУ, системе, дифференциальному неравенству, рекурсии производных или глобальному противоречию.

Отдельно покрыты:

- инволюция аргумента `T(T(x))=x`, включая `x -> a/x` и логарифмическую замену;
- отражение, сдвиг и симметрии перед дифференцированием функционального тождества;
- композиционные уравнения вида `f'=f(f(x))` и ростовые/blow-up рассуждения;
- редукция к ОДУ или системе только после проверки замкнутости выражений;
- область определения: допустимость `T(x)`, логарифма, деления на `f`, обратной функции, глобальности;
- причина уровня выше экзамена: сначала надо распознать функциональную динамику, а не решить уже готовое ОДУ.

## Relations

Связи добавлены к представителям:

- `olympiad-level-involution-functional-differential`;
- `putnam-modern-2005-b3`;
- `ru-misc-kfu-2019-19-3`;
- `istcim-2023-e-functional-ode-cosine`;
- `putnam-modern-2010-b5`;
- `bme-2024-p2-composition-ode-nonexistence`;
- `solve-functional-ode-composition`;
- `ru-cis-extra-yagtu-2001-half-argument-ode`;
- `vjimc-2016-c2-p4-moving-average-delay-variation`.

Соседние связи добавлены к стандартным кластерам:

- `cluster-integral-equation-to-ode-method-guide`;
- `cluster-scalar-constant-coefficients-method-guide`;
- `cluster-existence-uniqueness-continuation-method-guide`;
- `cluster-power-series-linear-ode-method-guide`.

## Граница темы

В кластер не надо добавлять чистые функциональные уравнения, где производная используется только как гладкость. Не надо также переносить сюда все интегральные условия, задачи на стандартное решение `f''+cf=0` или задачи на степенные ряды: если главный метод принадлежит `integral-equation-to-ode`, `scalar-constant-coefficient-linear-ode`, `power-series-linear-ode` или `existence-uniqueness-continuation`, связь должна идти через relations, а не через новый representative.

## Проверки

- `python tools/build_index.py` - OK, индекс пересобран (`428 cards`).
- `python tools/validate.py` - не прошел из-за уже существующих broken endpoints к `cluster-olympiad-transformed-linear-mvt-*`; новый блок в ошибках не фигурирует.
- `python tools/check_links.py` - не прошел по тем же broken endpoints `cluster-olympiad-transformed-linear-mvt-*`.
- `python tools/check_encoding.py` - OK.
- `python tools/check_clusters.py` - не прошел: в кластере `olympiad-transformed-linear-mvt` отсутствуют representative ids `cluster-olympiad-transformed-linear-mvt-method-guide`, `cluster-olympiad-transformed-linear-mvt-factor-rolle-theorem`, `cluster-olympiad-transformed-linear-mvt-zero-sign-exam`.
- `python tools/build_viewer.py` - OK, пересобраны `viewer/index.html` и `index.html`.
- `python tools/audit_rules.py` - OK с 4 предупреждениями по ранее существующим `exam_score`/`technical_score` карточкам local DU.
