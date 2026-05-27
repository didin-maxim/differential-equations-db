# Аудит кластера: Штурм, сравнение, осцилляция и нули

Дата прохода: 2026-05-27. Зона: `sturm-oscillation-comparison`.

## Что добавлено

- Добавлены 5 карточек в `data/problems/cluster_audit/sturm_oscillation_comparison/`:
  - `cluster-sturm-dirichlet-nonresonance-interpolation-lemma`;
  - `cluster-sturm-disconjugacy-strict-upper-bound-lemma`;
  - `cluster-sturm-bvp-unit-endpoints-safe-threshold`;
  - `cluster-sturm-bvp-unit-endpoints-sharp-threshold`;
  - `cluster-sturm-bvp-unit-endpoints-threshold-counterexample`.
- Добавлены связи в `data/relations/relations.d/cluster-sturm-oscillation-comparison.yaml`.
- Добавлен batch `data/import_batches/cluster-sturm-oscillation-comparison.yaml`.
- Обновлена политика кластера в `data/task_clusters/clusters.yaml`: добавлены варианты `dirichlet_disconjugacy_threshold`, `bvp_interpolation_nonresonance`, `sharpness_counterexample`; уточнены duplicate-сигналы, representative ids, deficit policy и notes.

## Пороговая тема

Для задачи

`y''+f(x)y=0`, `f(x)<C`, `y(0)=y(L)=1`

получен точный универсальный ответ:

`C<=pi^2/L^2`.

Достаточность: при `f<C` и `C<=pi^2/L^2` сравнение Штурма запрещает ненулевое решение однородной задачи Дирихле с двумя нулями на `[0,L]`. Значит краевая задача с заданными концами нерезонансна и имеет единственное решение.

Острота: если `C>pi^2/L^2`, то выбор `f=(pi/L)^2` дает `f<C`, но решение `y=A cos(pi x/L)+B sin(pi x/L)` с `y(0)=1` имеет `y(L)=-1`, поэтому условие `y(L)=1` невыполнимо.

Масштабирование: на `[a,b]` длина `L=b-a`, а замена `t=(x-a)/L` переводит порог в `pi^2/(b-a)^2`.

## Покрытие

| Идея | Представители |
|---|---|
| Теорема сравнения и разделение нулей | `local-du-8-sturm-comparison-theorem`, `local-du-standard-sturm-separation-zeros`, `local-du-standard-sturm-zero-spacing-corollaries` |
| Осцилляция/неосцилляция и Кнезер | `local-du-standard-oscillation-nonoscillation-tests`, `local-du-standard-kneser-criterion` |
| Краевые следствия без вычисления спектра | `local-du-8-t3-nonpositive-q-bvp-sturm`, `local-du-romanko-sturm-short-interval-bvp`, `local-du-deficit-sturm-nonpositive-potential-bvp` |
| Конкретные задачи на нули | `local-du-written-2007-81-sturm-zero`, `local-du-written-2018-zero-count-quadratic-potential`, `oral-exam-strong-10-sturm-comparison-one-zero` |
| Лиувилль/Прюфер/Бессель | `local-du-8-t4-three-zeros-after-liouville-transform`, `local-du-8-t6a-bessel-infinite-zeros`, `local-du-8-t6b-bessel-zero-spacing-prufer`, `mit-18034-pset08-prufer-oscillation-criteria` |
| Новый порог `f<C`, `y(a)=y(b)=1` | три новые threshold-карточки и две новые леммы |

## Разграничение

- Boundary spectral: простые шаблоны на вычисление собственных значений не добавлялись в представители. `dirichlet-eigenvalues-interval` связан только как объяснение порога в контрпримере.
- Green-functions BVP: новые карточки не строят ядро Грина; используется только конечномерная нерезонансная логика через стрельбу.
- Linear variable coefficients: общие свойства линейных ОДУ остаются соседним кластером; сюда включены только нули, сравнение, дисконъюгированность и их краевые следствия.

## Дедупликация

Безопасных удалений не найдено.

Близкие, но оставленные карточки:

- `local-du-romanko-sturm-short-interval-bvp`: шире новой пороговой темы, потому что включает произвольную правую часть и условие через `p_*`.
- `local-du-deficit-sturm-nonpositive-potential-bvp`: неположительный потенциал и энергетический ход; теперь используется как сосед безопасного порога.
- `local-du-standard-sturm-zero-spacing-corollaries`: общий набор следствий; новая строгая лемма выделена потому, что критический случай `f<C`, `C=pi^2/L^2` важен для точного ответа.

Новые карточки помечены как self-authored/model, автор `М. Дидин`, поскольку точный внешний источник для этих формулировок не найден.

## Проверки

После правок выполнены:

```powershell
python tools\validate.py
python tools\check_links.py
python tools\audit_rules.py
python tools\check_clusters.py
python tools\build_index.py
python tools\build_viewer.py
python tools\check_encoding.py
```
