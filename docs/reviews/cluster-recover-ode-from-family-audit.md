# Аудит кластера recover-ode-from-family

Дата: 2026-05-27.

## Что проверено

- Точные попадания в базе: `waterloo-family-circles-recover-ode`, `waterloo-log-family-qualitative-recover`.
- Близкие, но не ядро кластера: `orthogonal-trajectories-circles` и новые карточки `cluster-orthogonal-*`; там recover-ODE является только подготовкой к ортогональному семейству.
- Письменные `local_du` и программы: прямых заданий "восстановить ОДУ по однопараметрическому/двухпараметрическому семейству" в извлеченном тексте не найдено. Есть соседние задачи на уравнения Клеро/Лагранжа, особые решения и дискриминанты: `clairaut-envelope`, `local-du-written-2014-51-lagrange-singular-curves`, `local-du-written-2020-clairaut-shifted-envelope`, `local-du-written-2022-implicit-discriminant`.
- Waterloo и отчет по ортогональным траекториям использованы как граница: окружности Waterloo остаются recover-family, а ортогональные trajectories не смешиваются с этим кластером.

## Добавлено

- `cluster-recover-exponential-particular-family`: однопараметрическое явное семейство `y=e^x+C e^{-x}` и восстановление линейного ОДУ `y'+y=2e^x`.
- `cluster-recover-two-parameter-parabolas-second-order`: двухпараметрическое семейство `y=ax^2+bx`, минимальный порядок 2, уравнение `x^2y''-2xy'+2y=0`.
- `cluster-recover-parameter-count-order-diagnostic`: диагностическая карточка на число независимых параметров и минимальный порядок ОДУ.
- `cluster-recover-translated-parabolas-envelope`: семейство `y=(x-a)^2`, восстановление `(y')^2=4y` и особая огибающая `y=0`.

## Дедупликация

Не добавлялись задачи, отличающиеся только формой кривой при том же удалении одного параметра. Параболы добавлены не как "еще одна форма", а потому что одна карточка дает двухпараметрический второй порядок, а другая дает огибающую, отсутствующую в исходном семействе.

Задачи Клеро/Лагранжа и implicit-discriminant связаны отношениями как соседи, но не включены в representatives этого кластера: там исходная постановка другая.

Связи записаны только в `data/relations/relations.d/cluster-recover-ode-from-family.yaml`, batch - в `data/import_batches/cluster-recover-ode-from-family.yaml`.

## Проверки

Выполнены:

```powershell
python tools\validate.py
python tools\check_links.py
python tools\audit_rules.py
python tools\check_clusters.py
python tools\build_index.py
python tools\build_viewer.py
```

Результат контрольного прогона сразу после recover-аудита: проверки прошли, индекс был собран на 312 карточек, viewer пересобран.

Позднее в рабочем дереве появились параллельные карточки другой зоны (`existence_uniqueness_continuation`), из-за которых общий `validate/check_links/audit_rules` в текущем состоянии уже требует отдельной правки вне этого кластера: неизвестные `compactness_argument`, `implicit_function_theorem`, `implicit_ode`, `barrier_argument` и связь на отсутствующий `implicit-ode-discriminant-basic`. Эти файлы не редактировались в recover-аудите.
