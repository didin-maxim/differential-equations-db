# Аудит верхнего уровня МФТИ: отличник vs олимпиадное

Дата: 2026-05-27. Зона аудита: документы `docs/reviews/local-du-program-8.md`, `oral-exam-generation-rules.md`, `local-du-gap-and-dedup-report.md`, `english-import-qa.md`, кластеры `data/task_clusters/clusters.yaml`, карточки `data/problems/**` с верхними `idea_score`, экзаменационными тегами и олимпиадными метками.

## Граница уровня

Экзамен на отлично: `idea_score` 8-10, `technical_score` обычно не выше 5-6, один переносимый прием из стандартного курса или `advanced_standard_course` с явным мостом. Подходящие сюжеты: прямое доказательство сравнения Штурма, вронскианное тождество, фундаментальная матрица и монодромия, функция Ляпунова, первая/вторая вариация в простейшей постановке, характеристики первого порядка, Гронуолл и продолжение.

Только олимпиадное/внепрограммное: `idea_score > 10`, неполные решения, функционально-дифференциальные уравнения, тонкая дисконъюгированность высоких порядков, глобальные трюки роста, внешняя спектральная или специальная теория. Такие карточки должны иметь `olympiad_above_exam` и/или `beyond_standard_course`; экзаменационные теги на них нежелательны.

Техническая сложность оценивалась отдельно: если задача тяжела только длинным интегралом или алгеброй, это не повышает `idea_score`. Такие задачи не стоит поднимать в excellent слой без качественной идеи.

## Точечные правки

- `msu-ode-2023-8-fourth-order-zero-count-review`: снята метка `exam_score_10`, добавлена `olympiad_above_exam`. Причина: `idea_score=11`, `solutions=[]`, ключевой шаг требует внепрограммной леммы о дисконъюгированности/фокальных точках четвертого порядка.
- `putnam-modern-2010-b5`: оставлен `beyond_standard_course`, в editorial добавлено явное объяснение, что композиционное уравнение `f'(x)=f(f(x))` и глобальный blow-up argument выше стандартного экзамена.

Массовых удалений не делалось: спорные олимпиадные карточки с `technical_score=8` оставлены, потому что они уже не имеют экзаменационных тегов или явно отмечены `olympiad_above_exam`.

## Покрытие тем

Сильное покрытие уже есть:

- Штурм, сравнение, нули: `oral-exam-strong-10-sturm-comparison-one-zero`, локальные T3/T4/T6, Romanko/Trench/MIT bridge.
- Линейные переменные коэффициенты и Вронскиан: Liouville, reduction of order, quotient/graph cards, bounded-solutions obstruction.
- Системы, матричная экспонента, монодромия: constant coefficient systems, `oral-exam-excellent-monodromy-periodic-forcing`, Teschl Floquet chain.
- Устойчивость, Ляпунов, первые интегралы: oral excellent/strong cards, Filippov radial estimate, MIT nonlinear stability, phase/first integral cards.
- Краевые задачи, резонанс, Green function: Trench BVP import and local Filippov resonance card.
- Вариационное исчисление: Euler-Lagrange, natural/free endpoints, isoperimetric, Euler-Poisson, Jacobi/Legendre, second variation threshold.
- Зависимость от параметра и Гронуолл: local written sensitivity, Teschl regular perturbation/flow derivative/continuous dependence, MIT one-sided Lipschitz, Filippov continuation cards.

Найденные узкие дефициты верхнего слоя:

- semilinear characteristics as a bridge: линейные PDE первого порядка покрыты, но excellent-level связь характеристик с максимальной областью существования была слабой;
- monodromy at multiplier 1: нерезонансный случай был, но совместность при `1 in spec M` отсутствовала;
- second parameter correction: первая производная по параметру была, второй порядок почти отсутствовал;
- прикладная карточка на нарушение Лежандра без длинного Euler-Lagrange счета.

## Добавлено

Новые карточки лежат в `data/problems/cluster_audit/mipt_excellent_level/`:

| id | idea | tech | уровень | зачем |
|---|---:|---:|---|---|
| `mipt-excellent-semilinear-characteristics-blowup` | 9 | 4 | `exam_score_9`, `advanced_standard_course` | Характеристики + максимальная область/взрыв, без тяжелых вычислений. |
| `mipt-excellent-periodic-system-resonant-monodromy` | 9 | 5 | `exam_score_9`, `advanced_standard_course` | Резонансная монодромия: `b in Im(I-M)`, ядро периодических решений. |
| `mipt-excellent-second-parameter-correction` | 8 | 4 | `exam_score_8`, `advanced_standard_course` | Вторая поправка по параметру, нелинейность входит только на втором порядке. |
| `mipt-excellent-legendre-violation-no-minimum` | 8 | 3 | `exam_score_8`, `advanced_standard_course` | Проверка смысла условия Лежандра одной отрицательной вариацией. |

Batch: `data/import_batches/cluster-mipt-excellent-level.yaml`.

Relations: `data/relations/relations.d/cluster-mipt-excellent-level.yaml`.

## Спорные, но не исправленные

- Олимпиадные карточки Putnam с `idea_score` 10-11 и `technical_score=8` оставлены: у них нет роли обычного экзаменационного excellent, а `olympiad_above_exam` уже отделяет их от выдачи сильному студенту на стандартном устном экзамене.
- `putnam-modern-2009-a2` имеет `idea_score=8`, `technical_score=8`, `advanced_standard_course`, но без exam tags. Можно позже решить, нужна ли метка `olympiad_above_exam`; автоматической правки не делал, потому что задача не загрязняет excellent selection напрямую.
- Floquet/Teschl цепочка полезна, но при необходимости ее можно сжать до 1-2 representative cards; сейчас это не ошибка, а вопрос политики насыщения.

## Проверки

После внесения изменений выполнены:

```powershell
python tools\validate.py       # OK: 298 cards, 331 relations, 26 sources
python tools\check_links.py    # OK
python tools\audit_rules.py    # OK, 0 warnings
python tools\check_clusters.py # OK: 19 task clusters
python tools\build_index.py    # OK: rebuilt index/generated.json
python tools\build_viewer.py   # OK: rebuilt viewer/index.html
```
