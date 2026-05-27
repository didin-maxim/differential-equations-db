# Теоретико-методический блок: matrix-exponential-methods

Дата: 2026-05-27.

Зона: кластер `matrix-exponential-methods` - матричная экспонента как самостоятельный метод, а не еще одно вычисление решения `x'=Ax`.

## Что добавлено

- Создана карточка `cluster-matrix-exponential-method-guide` в `data/problems/cluster_audit/matrix_exponential_methods/`.
- Карточка помечена как `theorem`, `task_cluster`, `method_guide`, `cluster_representative`, поэтому должна индексироваться как теоретико-методический блок кластера.
- В `data/task_clusters/clusters.yaml` карточка добавлена первым representative для `matrix-exponential-methods`.
- В `data/import_batches/cluster-matrix-exponential-methods.yaml` добавлен id нового блока.
- В слой определений добавлены недостающие compact definition-id: `matrix_eigenvalue`, `det_exp_trace_identity`, `variation_of_constants_system`.

## Какие методы покрыты

- свойства `e^{At}`: нормировка, производная, коммутирование с `A`, групповое свойство и обратная матрица `e^{-At}`;
- восстановление генератора: `A=E'(0)` для нормированной экспоненты и `A(t)=X'(t)X(t)^{-1}` для фундаментальной матрицы;
- связь с фундаментальной матрицей линейной системы и системами с постоянными коэффициентами;
- спектр, комплексные режимы и жорданова структура через множители `e^{lambda t}`, `cos beta t`, `sin beta t`, `t^k`;
- формула `det(e^{At})=e^{t tr A}` как trace/determinant shortcut и постояннокоэффициентный случай формулы Лиувилля;
- решение неоднородных систем через вариацию постоянных `e^{A(t-s)}`;
- дискретный аналог для матричных рекуррент `x_{n+1}=Mx_n` через степени `M^n`.

## Источники

В карточку добавлены 6 источников в принятом формате:

- `src-mipt-ode-course`;
- `src-local-du-8-program-or-exam`;
- `src-romanko-problem-book`;
- `src-waterloo-amath250-notes`;
- `src-teschl-ode-dynamical-systems`;
- `src-mit-1803sc-ode`.

## Связи

Новые relations добавлены в `data/relations/relations.d/cluster-matrix-exponential-methods.yaml`.

Representative-связи:

- к `cluster-matrix-exp-inverse-by-negative-time`;
- к `cluster-matrix-exp-recover-a-derivative-zero`;
- к `cluster-matrix-exp-spectrum-from-modes`;
- к `cluster-matrix-exp-det-trace-shortcut`;
- к `linear-system-jordan-block`;
- к `inhomogeneous-linear-system-variation`;
- к `waterloo-fundamental-matrix-flow-inverse`.

Соседние кластеры связаны через содержательные representative-card:

- `constant-coefficient-linear-systems` через `cluster-linear-systems-constant-coefficients-method-guide`;
- `fundamental-matrix-linear-systems` через `waterloo-fundamental-matrix-flow-inverse`;
- `variation-of-constants` через `inhomogeneous-linear-system-variation`.

## Оставшиеся пробелы

- Нет отдельной карточки на коммутирующие матрицы `e^{(A+B)t}=e^{At}e^{Bt}` и предупреждение о некоммутирующем случае.
- Нет отдельной карточки на спектральные проекторы или минимальный многочлен для вычисления `f(A)`.
- Дискретная часть пока представлена как мост через `M^n`, а не как самостоятельный большой кластер рекуррент.

## Проверки

Выполнены:

```powershell
python tools/build_index.py
python tools/validate.py
python tools/check_links.py
python tools/check_encoding.py
python tools/check_clusters.py
python tools/build_viewer.py
```

Результат:

- `build_index` - OK: 402 cards, обновлен `index/generated.json`;
- `validate` - OK: 402 cards, 670 relations, 45 sources;
- `check_links` - OK;
- `check_encoding` - OK;
- `check_clusters` - OK: 34 task clusters;
- `build_viewer` - OK, обновлены `viewer/index.html` и `index.html`.
