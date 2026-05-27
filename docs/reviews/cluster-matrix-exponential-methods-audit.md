# Аудит кластера matrix-exponential-methods

Дата: 2026-05-27.

Зона: матричная экспонента как самостоятельный метод, а не просто способ решить очередную систему `x'=Ax`.

## Итог

Создан новый кластер `matrix-exponential-methods` в `data/task_clusters/clusters.yaml`.

Граница кластера:

- входит: свойства и операции с `e^{At}`, обратный поток, производная в нуле, `det(e^{At})=e^{t tr A}`, чтение спектра по режимам, жордановы множители, операторная вариация постоянных, дискретный аналог через `A^n`;
- не входит как ядро: массовые задачи "решить систему по собственным значениям" - это `constant-coefficient-linear-systems`;
- не входит как ядро: неоднородная формула ради интеграла - это `variation-of-constants`;
- не входит как ядро: настоящая монодромия периодической `A(t)` - это `floquet-periodic-linear-systems`.

## Подтянутые представители

В representatives включены существующие карточки, где матричная экспонента является методом или объектом:

- `waterloo-fundamental-matrix-flow-inverse`: групповое свойство фундаментальной матрицы и обратный ход времени.
- `oral-above-three-recover-system-from-fundamental-matrix`: восстановление `A` по фундаментальной матрице через `X'X^{-1}`.
- `msu-ode-2012-3-recover-autonomous-matrix`: продвинутое восстановление автономной матрицы по одной траектории.
- `linear-system-jordan-block`: минимальный жорданов блок и формула `e^{(lambda I+N)t}`.
- `msu-ode-2006-2-det-integral-matrix-exp`: determinant-level мышление для интеграла матричной экспоненты.
- `inhomogeneous-linear-system-variation`: операторная формула вариации постоянных через `e^{A(t-s)}`.
- `teschl-stanford-bridge-monodromy-period-iterate`: соседний операторный пример степеней монодромии; кластер Флоке остается владельцем периодической темы.

## Добавлено

| Карточка | Что закрывает | Почему не дубль |
|---|---|---|
| `cluster-matrix-exp-inverse-by-negative-time` | По заданному `e^{At}` найти `e^{-At}` через замену `t -> -t`. | Не решает систему и не обращает матрицу: учит свойству потока. |
| `cluster-matrix-exp-recover-a-derivative-zero` | Lemma-card `(d/dt)e^{At}|_{t=0}=A` и устное восстановление `A`. | Существующая устная карточка использует `X'X^{-1}`; новая выделяет нормированный быстрый случай. |
| `cluster-matrix-exp-spectrum-from-modes` | Базовое spectral mapping чтение: рост, осцилляции, множитель `t`. | Не вычисляет характеристический многочлен; восстанавливает спектр из формы экспоненты. |
| `cluster-matrix-exp-det-trace-shortcut` | Lemma-card `det(e^{At})=e^{t tr A}` и быстрый пример. | Не дублирует MSU determinant-card: там главный член интеграла, здесь trace/determinant law. |
| `cluster-matrix-exp-discrete-rotation-recurrence` | Дискретная система и линейная рекуррента через `A^n`, комплексное умножение и Кэли-Гамильтон. | Закрывает дискретный аналог без тяжелого счета степеней матрицы. |

Все пять новых карточек лежат в `data/problems/cluster_audit/matrix_exponential_methods/` и помечены как self-authored/model через `src-cluster-matrix-exponential-methods-audit`.

## Теоретические узлы

- `e^{-At}=(e^{At})^{-1}`: аналог уже был в `waterloo-fundamental-matrix-flow-inverse`; добавлена прикладная карточка и связь.
- `(d/dt)e^{At}|_{t=0}=A`: добавлена отдельная lemma-card `cluster-matrix-exp-recover-a-derivative-zero`.
- `det(e^{At})=e^{t tr A}`: добавлена lemma-card `cluster-matrix-exp-det-trace-shortcut`.
- Базовое spectrum mapping чтение для экспоненты: добавлена lemma-card `cluster-matrix-exp-spectrum-from-modes`.

## Связи и batch

Новые связи записаны только в `data/relations/relations.d/cluster-matrix-exponential-methods.yaml`.

Batch записан в `data/import_batches/cluster-matrix-exponential-methods.yaml`.

Дополнительно в taxonomy добавлены точные теги:

- `trace_determinant`;
- `linear_recurrence`.

## Проверки

После добавления карточек, связей, кластера и отчета выполнены:

```powershell
python tools\validate.py
python tools\check_links.py
python tools\audit_rules.py
python tools\check_clusters.py
python tools\build_index.py
python tools\build_viewer.py
```

Результат:

- `validate` - OK: 332 cards, 387 relations, 29 sources.
- `check_links` - OK.
- `audit_rules` - OK, 0 warnings.
- `check_clusters` - OK: 24 task clusters.
- `build_index` - OK, rebuilt `index/generated.json` with 332 cards.
- `build_viewer` - OK, rebuilt `viewer/index.html`.
