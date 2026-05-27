# QA англоязычных импортов

Дата: 2026-05-26.

Зона проверки: `data/problems/english_sources/**`, `data/taxonomy/tags.yaml`, `data/task_clusters/clusters.yaml`. Waterloo включен в проход: на момент QA каталог `data/problems/english_sources/waterloo_textual` уже существовал.

## Что проверено

- Дедупликация новых english cards между собой и против `local_du`, `oral_exam`, `olympiad` по формулировкам, тегам, `differential_equations_profile`, методам и объектам.
- Особое внимание: группы characteristics/PDE, Sturm-Liouville/BVP/resonance, Floquet/monodromy, Gronwall/continuous dependence, nonlinear stability/Lyapunov, Waterloo qualitative sketches.
- Consistency `idea_score` / `technical_score`: явной подмены идейной сложности вычислительной не найдено. Карточки с `advanced_standard_course` в целом объясняют, какой факт или язык выходит за минимальный курс; `beyond_standard_course` в новых english imports не используется.
- Метки: широкие метки оставлены там, где они являются служебными (`complete_proof`, `standard_course_methods`, `source_solution_checked`), но добавлены более точные малые теги для навигации.

## Что исправлено

- Исправлена очевидно неверная метка в `waterloo-family-circles-recover-ode`: заменено `orthogonal_trajectories` на `recover_ode_from_family`.
- В taxonomy добавлены точные теги: `recover_ode_from_family`, `singular_point_analysis`, `nullcline_analysis`, `isocline_analysis`, `critical_damping`, `maximum_principle`, `fredholm_alternative`, `green_identity`, `floquet_theory`.
- Уточнены теги Waterloo textual:
  - `waterloo-log-family-qualitative-recover`: `recover_ode_from_family`;
  - `waterloo-singular-linear-qualitative-sketch`: `singular_point_analysis`;
  - `waterloo-oscillator-speed-before-crossing`: `nullcline_analysis`;
  - `waterloo-spiral-phase-portrait-isoclines`: `isocline_analysis`;
  - `waterloo-critical-damping-crossing-condition`: `critical_damping`.
- Уточнены теги BVP/Floquet cards: `maximum_principle`, `fredholm_alternative`, `green_identity`, `floquet_theory`.
- Обновлены representatives/policies в `clusters.yaml`:
  - `linear-first-order-ode`: добавлен `waterloo-singular-linear-qualitative-sketch`, кластер переведен в `watch`;
  - `constant-coefficient-linear-systems`: добавлен `waterloo-spiral-phase-portrait-isoclines`, кластер переведен в `watch`;
  - `boundary-spectral-problems`: добавлены `lebl-diffyqs-robin-dirichlet-transcendental-spectrum`, `trench-bvp-resonance-solvability-alternative`, `teschl-stanford-bridge-sturm-liouville-zero-count-phase`; кластер помечен `saturated`;
  - `variation-of-constants`: добавлен `trench-bvp-green-function-formula`, кластер переведен в `watch`.

## Дедупликация

Явных дублей, которые безопасно удалить или переписать без human review, не найдено.

Проверенные близкие группы:

- Lebl characteristics cards против `local-du-deficit-first-order-pde-characteristics`, `local-du-written-2014-51-characteristics-pde`, `local-du-written-2023-characteristics-plane-data`: общий метод один, но роли разные: перенос профиля, переменные характеристики, damping along characteristics, obstruction by characteristic data.
- BVP/Sturm cards против `weak-pass-mixed-bvp-eigenvalues`, `oral-middle-mixed-boundary-eigenvalues`, `local-du-filippov-763-dirichlet-resonance-no-solution`: новые карточки добавляют Green identity, Fredholm alternative, weighted/phase-angle variants. Базовый spectral cluster теперь насыщен.
- MIT one-sided Lipschitz/Gronwall против `oral-exam-strong-10-one-sided-gronwall-uniqueness`: близко, но MIT дает оценку расстояния между двумя решениями, oral card - uniqueness через квадрат разности.
- Teschl Floquet cards между собой: это цепочка lemma-level facts around monodromy, determinant, multiplier stability, а не точный повтор одной задачи.
- Waterloo recover-family cards между собой: общий прием `differentiate and eliminate parameter`, но разные геометрические роли: tangent circles vs log-family asymptotics/convexity.

## Human Review Candidates

- `trench-bvp-dirichlet-resonance-sine-condition` и `trench-bvp-resonance-solvability-alternative`: специальный пример и общий факт. Оставлены оба, но человек может решить, не достаточно ли relation/prerequisite вместо двух самостоятельных карточек.
- `teschl-stanford-bridge-floquet-determinant-liouville`, `teschl-stanford-bridge-monodromy-period-iterate`, `teschl-stanford-bridge-floquet-multiplier-stability`: полезная цепочка, но если база должна держать минимум Floquet facts, можно сжать до 1-2 representative cards.
- `lebl-diffyqs-transport-signal-shift`, `lebl-diffyqs-damped-transport-characteristics`, `lebl-diffyqs-variable-coefficient-characteristics`: не дубли, но first-order PDE characteristics быстро становится насыщенной темой; будущие imports лучше добавлять только при новой диагностике данных или новом типе характеристик.
- `waterloo-family-circles-recover-ode` и `waterloo-log-family-qualitative-recover`: не дубли, но если появится отдельный saturated cluster для `recover_ode_from_family`, это первые кандидаты на representatives, а не повод добавлять много похожих семейств.

## Проверки

- `python tools\validate.py` - OK: 262 cards, 263 relations, 21 sources.
- `python tools\check_links.py` - OK.
- `python tools\audit_rules.py` - OK, 0 warnings.
- `python tools\check_clusters.py` - OK: 7 clusters.
- `python tools\build_index.py` - OK, rebuilt `index/generated.json`.
- `python tools\build_viewer.py` - OK, rebuilt `viewer/index.html`.
