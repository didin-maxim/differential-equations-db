# Теоретико-методический блок: wronskian-nonlinear-transforms

Дата: 2026-05-27.

## Что добавлено

- `cluster-wronskian-nonlinear-transforms-method-guide` как компактный `theorem` + `method_guide` + `cluster_representative`.
- `data/import_batches/cluster-wronskian-nonlinear-transforms.yaml`.
- `data/relations/relations.d/cluster-wronskian-nonlinear-transforms.yaml`.
- Карточка добавлена первой в `representative_card_ids` кластера `wronskian-nonlinear-transforms`.

## Содержательная рамка

Блок покрывает только малый кластер, где главная идея - нелинейная величина, построенная из решения или пары решений линейного уравнения: `y^m`, отношение решений, логарифмическая производная, произведение пары решений и преобразование типа Пинни.

Из линейной теории явно перенесены:

- формула Абеля-Лиувилля и постоянство W в форме без `y'`;
- связь W с линейной независимостью и ФСР;
- простота нулей ненулевого решения;
- формула `(y2/y1)' = W/y1^2` на интервале без нулей `y1`.

Границы зафиксированы с соседними темами:

- обычная ФСР, вариация параметров и формула Абеля остаются в `linear-equations-variable-coefficients`;
- полноценные задачи на разделение/сравнение/осцилляцию нулей остаются в `sturm-oscillation-comparison`;
- Бернулли/Риккати не смешиваются с этим кластером, если главный ход - стандартная линеаризация, а не Вронскиан пары решений.

## Определения

Новые определения не добавлялись. Использованы существующие `wronskian`, `linear_independence_solutions`, `fundamental_system_solutions`, `ordinary_differential_equation`, `solution`.

## Проверка

Плановая проверка для этой правки: `build_index`, `validate`, `check_links`, `check_encoding`, `check_clusters`, `build_viewer`, `audit_rules`.
