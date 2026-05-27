# Теоретико-методический блок: first-integrals-plane-systems

Дата: 2026-05-27. Зона: `first-integrals-plane-systems` - первые интегралы и фазовые траектории на плоскости.

## Что просмотрено

- `data/task_clusters/clusters.yaml`, representatives кластера `first-integrals-plane-systems`.
- Карточки `lotka-volterra-first-integral`, `energy-integral-oscillator`, `local-du-romanko-first-integral-center`, `local-du-filippov-1166-intersection-first-integrals`, `mit-18034-pset09-hamiltonian-folium-first-integral`, `cluster-phase-stability-first-integral-center`.
- Соседние кластеры и отчеты по `phase-line-stability`, `energy-estimates-second-order-ode`, `pde-characteristics-first-order`.
- Слой определений `data/definitions/definitions.yaml`: первый интеграл, фазовая траектория, положение равновесия, устойчивость по Ляпунову, асимптотическая устойчивость, функция Ляпунова, интегральная кривая.

## Что добавлено

Добавлен отдельный методический блок:

- `data/problems/cluster_audit/first_integrals_plane_systems/cluster-first-integrals-plane-systems-method-guide.yaml`.

Карточка помечена как:

- `kind.primary = theorem`;
- `kind.secondary = task_cluster, method_guide, cluster_representative`;
- теги `task_cluster`, `method_guide`, `cluster_representative`.

В `representative_card_ids` кластера добавлен `cluster-first-integrals-plane-systems-method-guide`, поэтому блок индексируется как представитель кластера и находится через `first-integrals-plane-systems`.

## Покрытые методы

- Поиск первого интеграла через уравнение `H_x P + H_y Q = 0`.
- Проверка `dH/dt = grad H dot F = 0` без явного решения системы.
- Чтение фазовых кривых как связных компонент уровней `H=C`.
- Разбор регулярных и особых уровней: равновесия, сепаратрисы, инвариантные оси, самопересечения.
- Центр и замкнутые траектории: строгий экстремум первого интеграла плюс замкнутые уровни дают устойчивость по Ляпунову, но не асимптотическую устойчивость.
- Энергия уравнения второго порядка `x''+V'(x)=0` как первый интеграл фазовой системы.
- Отличие первого интеграла от функции Ляпунова: `Hdot=0` против знака `Vdot`.
- Связь с устойчивостью и границы переноса метода на соседние кластеры.

## Источники

В карточку добавлены 6 источников в принятом формате:

- `src-mipt-ode-course` - базовая программа курса.
- `src-romanko-problem-book` - локальная задача на центр из первого интеграла.
- `src-filippov-problem-book` - геометрия нескольких первых интегралов и интегральных кривых.
- `src-teschl-ode-dynamical-systems` - открытая строгая теория автономных систем.
- `src-waterloo-amath250-notes` - открытые заметки по фазовым портретам и механическим осцилляторам.
- `src-mit-1803sc-ode` - видеокурс MIT OCW по фазовой плоскости и устойчивости.

Новые глобальные записи в `data/sources/sources.yaml` не добавлялись: все 6 источников уже существуют в слое источников и переиспользованы без дублей.

## Связи

Добавлен файл `data/relations/relations.d/cluster-first-integrals-plane-systems.yaml`.

Связи от методического блока поставлены к representative-задачам кластера:

- `energy-integral-oscillator`;
- `lotka-volterra-first-integral`;
- `local-du-romanko-first-integral-center`;
- `local-du-filippov-1166-intersection-first-integrals`;
- `mit-18034-pset09-hamiltonian-folium-first-integral`.

Содержательные связи к соседним кластерам:

- `phase-line-stability`: через `cluster-phase-stability-first-integral-center`, `cluster-phase-stability-method-guide`, `cluster-phase-stability-lyapunov-direct-method`;
- `energy-estimates-second-order-ode`: через `energy-integral-oscillator` как общий представитель сохраняющейся энергии;
- `pde-characteristics-first-order`: через `local-du-romanko-pde-two-invariants`, где инварианты характеристической системы играют роль первых интегралов.

## Что не добавлялось

- Новые однотипные задачи на угадывание энергии не добавлялись.
- Массовые сложности задач не менялись.
- Определения не дублировались в карточке как новые сущности; использованы `definition_ids` и связи к уже существующим теоретическим карточкам.

## Оставшиеся пробелы

- Нет отдельной визуальной карточки именно для особого уровня первого интеграла с сепаратрисой; сейчас этот мотив покрывается текстом методического блока и MIT folium-card.
- Нет отдельного методического блока для гамильтоновых систем как самостоятельного подкластера; пока гамильтонов случай включен как способ поиска `H`.
- Для локальной программы МФТИ можно позже заменить `src-mipt-ode-course` на более конкретный листок/конспект, если он будет выделен в источниках.
