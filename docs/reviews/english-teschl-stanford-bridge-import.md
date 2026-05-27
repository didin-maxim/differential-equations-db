# Импорт Teschl + Stanford bridge

Дата: 2026-05-26.

Зона: `data/problems/english_sources/teschl_stanford_bridge/`.

## Источники

- Teschl, *Ordinary Differential Equations and Dynamical Systems*: `src-teschl-ode-dynamical-systems`, использованы §§2.4-2.5 и §3.6.
- Stanford Math 63CM ODE notes: `src-stanford-math63cm-ode`, использован раздел 7 по Sturm-Liouville theory и фазовому углу.

## Добавленные карточки

1. `teschl-stanford-bridge-continuous-dependence-gronwall` - непрерывная зависимость от начальных данных через Гронуолла.
2. `teschl-stanford-bridge-flow-derivative-variational-equation` - производная потока по начальной точке и вариационное уравнение.
3. `teschl-stanford-bridge-regular-perturbation-first-correction` - первый член регулярного возмущения.
4. `teschl-stanford-bridge-monodromy-period-iterate` - базовая лемма о монодромии и итерации периода.
5. `teschl-stanford-bridge-floquet-multiplier-stability` - устойчивость по мультипликаторам Флоке без полной нормальной формы Флоке.
6. `teschl-stanford-bridge-floquet-determinant-liouville` - произведение мультипликаторов через формулу Лиувилля.
7. `teschl-stanford-bridge-sturm-liouville-phase-eigenvalue` - критерий собственного значения через фазовый угол.
8. `teschl-stanford-bridge-sturm-liouville-zero-count-phase` - счет нулей собственных функций через фазовый угол.

## Фильтрация

Не импортировались KAM, chaos, stable manifold theorem, Melnikov, Hartman-Grobman и функционально-аналитическая полнота системы собственных функций. Существующая карточка `oral-exam-excellent-monodromy-periodic-forcing` не дублировалась; вместо этого добавлена связь от базовой монодромии.

Все новые карточки имеют `advanced_standard_course`: они выходят за минимальный вычислительный курс, но доказательства опираются на уже знакомые инструменты: Гронуолла, фундаментальную матрицу, формулу Лиувилля, жорданову форму, shooting и фазовый угол.

## Связи и batch

- Связи: `data/relations/relations.d/english-teschl-stanford-bridge.yaml`.
- Batch: `data/import_batches/english-teschl-stanford-bridge.yaml`.

## QA

Выполнено:

- `python tools/validate.py` - OK: 248 cards, 234 relations, 20 sources.
- `python tools/check_links.py` - OK: links are consistent.
- `python tools/audit_rules.py` - OK, но есть 1 существующее предупреждение вне этой пачки: `trench-bvp-green-function-formula#proof-main` содержит слово "аналогично".
- `python tools/check_clusters.py` - OK: 7 task clusters in 1 file(s).
