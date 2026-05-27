# Теоретико-методический блок: integral-equation-to-ode

Дата: 2026-05-27.

## Что добавлено

- Создана карточка `cluster-integral-equation-to-ode-method-guide`.
- Карточка помечена как `theorem`, `task_cluster`, `method_guide`, `cluster_representative`, `theory_bridge`.
- Добавлен batch `data/import_batches/cluster-integral-equation-to-ode.yaml`.
- Добавлен файл связей `data/relations/relations.d/cluster-integral-equation-to-ode.yaml`.
- В слой определений добавлены `integral_equation`, `volterra_integral_equation`, `fredholm_integral_equation`.

## Покрытие

Блок фиксирует общий маршрут: сначала распознать тип интеграла, затем дифференцировать или ввести скрытую интегральную константу, получить ОДУ, решить его и обязательно вернуться к исходному интегральному условию. Отдельно отмечены:

- перенос начальных условий из `int_a^x` для уравнений Вольтерра;
- самосогласованность констант для фиксированных пределов Фредгольма;
- потеря постоянных при дифференцировании;
- параметрические интегралы и условия на бесконечности;
- граница с чистыми интегральными уравнениями вне фокуса базы.

## Relations

Связи добавлены к представителям кластера:

- `putnam-early-1958-i3-integral-constraint`;
- `putnam-modern-1990-b1`;
- `seemous-2010-p1-iterated-integrals-linear-ode`;
- `istcim-2022-c-integral-identity-ode`;
- `ru-misc-kfu-2015-15-4`;
- `vjimc-2016-c2-p4-moving-average-delay-variation`.

Соседние теоретические связи добавлены к:

- `cluster-existence-uniqueness-continuation-method-guide`;
- `cluster-linear-variable-method-guide`;
- `cluster-green-functions-bvp-method-guide`.

## Граница кластера

Карточка оставляет в кластере только задачи, где интегральное условие является входом к ОДУ. Если основной объект - интегральный оператор, резольвента, компактность, спектр ядра или сжимающее отображение без перехода к ОДУ, задача считается чистым интегральным уравнением и не расширяет этот кластер.
