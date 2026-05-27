# Теоретико-методический блок: краевые спектральные задачи

Дата прохода: 2026-05-27. Зона: `boundary-spectral-problems`.

## Что добавлено

- Добавлена методическая карточка `cluster-boundary-spectral-method-guide` в `data/problems/cluster_audit/boundary_spectral_problems/`.
- Карточка помечена как `kind.primary = theorem`, `kind.secondary = task_cluster, method_guide, cluster_representative, theory_bridge`, поэтому она индексируется как теоретико-методический блок, а не как новая вычислительная задача.
- Карточка добавлена в representatives кластера `boundary-spectral-problems`.
- Добавлен batch `data/import_batches/cluster-boundary-spectral-problems.yaml`.
- Добавлен отдельный файл связей `data/relations/relations.d/cluster-boundary-spectral-problems.yaml`.
- В `definition_ids` использованы существующие определения: `boundary_value_problem`, `eigenvalue_problem`, `eigenvalue_of_boundary_value_problem`, `fundamental_system_solutions`, `wronskian`, `ordinary_differential_equation`, `solution`.

## Покрытые методы

- Постановка краевой спектральной задачи: параметр является собственным значением только при существовании ненулевого решения однородной BVP.
- Явный детерминантный маршрут для `y''+lambda y=0`: случаи `lambda>0`, `lambda=0`, `lambda<0`, краевая система на константы, собственные функции.
- Регулярная Sturm-Liouville постановка: самосопряженная форма, весовой скалярный продукт, вещественность собственных значений.
- Ортогональность собственных функций через тождество Грина.
- Резонанс и условие разрешимости: ортогональность правой части собственному решению/сопряженному ядру.
- Связь с функцией Грина: вне резонанса существует обратный Green-оператор; если главный объект - ядро, это соседний `green-functions-bvp`.
- Связь со Штурмом: сравнение, нули и фазовый счет помогают упорядочивать спектр, но не заменяют краевые условия.
- Связь с вариационными задачами: спектральный порог появляется в знаке второй вариации, уравнении Якоби и условиях на сопряженные точки.

## Источники

В guide-карточке добавлены 6 ориентиров в принятом формате `sources`/`references`:

- `src-local-du-8-program-or-exam` - локальная программа/экзаменационный ориентир.
- `src-romanko-problem-book` - русскоязычный задачный фон по ДУ и вариационному исчислению.
- `src-filippov-problem-book` - классический задачник по линейным и краевым задачам.
- `src-coddington-levinson` - классическая строгая теория линейных ОДУ.
- `src-teschl-ode-dynamical-systems` - открытая ссылка на Sturm-связь, нули и фазовый угол.
- `src-trench-ode-bvp` - открытый учебник по BVP, Green function и Sturm-Liouville.

## Relations

Добавлены связи от `cluster-boundary-spectral-method-guide` к representative- и theorem-карточкам:

- `dirichlet-eigenvalues-interval`;
- `weak-pass-mixed-bvp-eigenvalues`;
- `lebl-diffyqs-robin-dirichlet-transcendental-spectrum`;
- `trench-bvp-euler-log-spectrum`;
- `trench-bvp-weighted-orthogonality`;
- `trench-bvp-real-eigenvalues`;
- `trench-bvp-resonance-solvability-alternative`;
- `trench-bvp-dirichlet-resonance-sine-condition`;
- `local-du-standard-resonant-linear-bvp-solvability`;
- `trench-bvp-green-function-formula`;
- `trench-bvp-green-identity-self-adjoint-boundary`;
- `cluster-sturm-method-guide`;
- `teschl-stanford-bridge-sturm-liouville-zero-count-phase`;
- `liouville-wronskian-formula`;
- `cluster-variational-method-guide`;
- `local-du-standard-legendre-jacobi-conditions`.

## Оставшиеся пробелы

- В `data/definitions/definitions.yaml` пока нет отдельных определений `green_function` и `fredholm_alternative`; новые определения не добавлялись, чтобы не дублировать слой definitions. Связь сделана через существующие theorem-карточки.
- Нет отдельного локального видеокурса именно по краевым спектральным задачам; текущий набор опирается на локальную программу, Романко/Филиппова и открытые Coddington/Teschl/Trench-ориентиры.
- Кластер остается `saturated`: новые варианты `y''+lambda y=0` с теми же границами добавлять не нужно без новой совместности, веса, самосопряженной структуры или содержательного резонанса.

## Проверки

Выполнен полный требуемый набор:

```powershell
python tools\build_index.py
python tools\validate.py
python tools\check_links.py
python tools\check_encoding.py
python tools\check_clusters.py
python tools\build_viewer.py
python tools\audit_rules.py --max-items 80
```

Результат:

- `build_index.py` - OK, индекс пересобран, 406 карточек.
- `validate.py` - OK: 406 cards, 716 relations, 47 sources.
- `check_links.py` - OK.
- `check_encoding.py` - OK.
- `check_clusters.py` - OK: 34 task clusters.
- `build_viewer.py` - OK, пересобраны `viewer/index.html` и корневой `index.html`.
- `audit_rules.py --max-items 80` - OK с 4 существующими предупреждениями вне зоны `boundary-spectral-problems`: `local-du-written-2014-51-characteristics-pde`, `local-du-written-2014-51-factorized-variable-coeff`, `local-du-written-2014-51-lagrange-singular-curves`, `local-du-written-2024-variational-free-endpoint`.

Дополнительно проверено по `index/generated.json`: `cluster-boundary-spectral-method-guide` попал в индекс, имеет `method_guide` и связан с кластером `boundary-spectral-problems`.
