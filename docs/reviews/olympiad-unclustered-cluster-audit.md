# Аудит олимпиадных задач вне кластеров

Дата: 2026-05-27.

Зона проверки: все problem-карточки с `fragment: olympiad` и все `representative_card_ids` из `data/task_clusters/clusters.yaml`.

## Итог

- Найдено 83 олимпиадные problem-карточки.
- До прохода 47 из них не входили ни в один кластер.
- После прохода 79 из 83 олимпиадных задач входят хотя бы в один кластер.
- Остались вне кластеров 4 задачи: они оставлены уникальными или ожидающими полноценной проверки решения.
- Созданы 2 новых кластера:
  - `integral-equation-to-ode`;
  - `wronskian-nonlinear-transforms`.
- Добавлен файл глубоких связей `data/relations/relations.d/olympiad-unclustered-cluster-audit.yaml`.

## Добавлено в существующие кластеры

`olympiad-transformed-linear-mvt`:

- `imc-2006-p6-real-root-differential-operator`;
- `msu-ode-2023-2-infinite-zeros-linear-ode`;
- `ru-cis-extra-spbgeu-2023-rolle-cubic-operator`.

Основание: линейный дифференциальный оператор превращается в производную после множителя или факторизации, затем применяется Ролль/нулевой аргумент. Связи поставлены к базовому шаблону и между IMC 2006 и СПбГЭУ 2023.

`olympiad-differential-inequalities-barriers`:

- `bme-2023-p3-periodic-high-derivative-bound`;
- `convex-solution-two-zeros`;
- `imc-2019-p3-convex-differential-inequality`;
- `ru-cis-extra-yagtu-2001-sine-barrier`;
- `ru-cis-extra-yagtu-2014-exp-minus-xy-limit`;
- `seemous-2020-p4-pole-fixed-point-series`;
- `smmc-2018-a3-log-ratio-concavity`.

Основание: все эти задачи требуют выбрать барьерную/монотонную величину или правильную выпуклую комбинацию; это не просто общая метка "неравенство". Для близких пар добавлены связи: выпуклость, синус-барьер и экспоненциальный хвост, фазовая прямая для `y/x`.

`olympiad-functional-differential-equations`:

- `bme-2024-p2-composition-ode-nonexistence`;
- `istcim-2023-e-functional-ode-cosine`;
- `ru-cis-extra-yagtu-2001-half-argument-ode`;
- `vjimc-2016-c2-p4-moving-average-delay-variation`.

Основание: существенная связь производной с преобразованным аргументом, композицией или delay/integral условием. Для half-argument и moving-average поставлена contrast-связь, чтобы не смешивать рядовой механизм с delay-оценкой осцилляции.

`sturm-oscillation-comparison`:

- `putnam-early-1955-a7-zero-bounds`;
- `putnam-early-1957-ii6-zero-location`.

Основание: локализация нулей линейного уравнения второго порядка через сравнение/интегральные знаковые тождества. `msu-ode-2023-8-fourth-order-zero-count-review` не добавлена: карточка пока имеет `needs_solution_completion`, а кластер явно просит добавлять high-order zero-count только с проверенным решением.

`matrix-exponential-methods` и `constant-coefficient-linear-systems`:

- `putnam-modern-1995-a5`;
- `putnam-early-1971-b5-hypocycloid-system` добавлена в системы с постоянными коэффициентами;
- `putnam-early-1969-a5-controlled-linear-system` добавлена в системы с постоянными коэффициентами.

Основание: спектральные моды, комплексная форма и инвариантная разность координат. Для Putnam 1995 добавлена связь с чтением следа/мод через матричную экспоненту.

`energy-estimates-second-order-ode`:

- `energy-no-nonconstant-decay-periodic`;
- `msu-ode-2003-3-bounded-exp-oscillator`;
- `ru-misc-spb-itmo-2018-6`.

Основание: монотонная энергия или энергетическая замена является главным механизмом, а не общей темой устойчивости.

`existence-uniqueness-continuation` и `implicit-ode-discriminant`:

- `innopolis-2024-t6-million-cauchy-branches` добавлена в оба кластера;
- `ru-cis-extra-yagtu-2007-max-switch` добавлена в существование/единственность;
- `ru-cis-extra-yagtu-2014-exp-minus-xy-limit` добавлена в продолжение/глобальность;
- `oral-exam-geometry-two-tangent-roots` добавлена в существование/единственность.

Основание: регулярные ветви неявного ОДУ, активная ветвь негладкой правой части, глобальное продолжение через барьеры и обращение теоремы Коши по графику.

## Новые кластеры

`integral-equation-to-ode` создан, потому что нашлось не менее 6 задач с переносимым механизмом:

- `putnam-early-1958-i3-integral-constraint`;
- `putnam-modern-1990-b1`;
- `seemous-2010-p1-iterated-integrals-linear-ode`;
- `istcim-2022-c-integral-identity-ode`;
- `ru-misc-kfu-2015-15-4`;
- `vjimc-2016-c2-p4-moving-average-delay-variation`.

Кластер не собирает интегральные неравенства и не подменяет вариационное исчисление: только случаи, где интегральная запись реально становится ОДУ или условием самосогласованности.

`wronskian-nonlinear-transforms` создан для 3 близких задач:

- `olympiad-level-power-solution-linear-ode-criterion`;
- `ru-misc-nure-8-3`;
- `putnam-early-1975-a5-wronskian-nonlinear-transform`.

Основание: нелинейность возникает из структуры линейного уравнения, логарифмической производной или постоянства Вронскиана. Это не общий кластер нелинейных ОДУ.

## Оставлены вне кластеров

- `msu-ode-2023-8-fourth-order-zero-count-review`: не добавлена в `sturm-oscillation-comparison`, пока нет полноценной проверки решения; это high-order zero-count, а не стандартное применение Штурма второго порядка.
- `periodic-solution-monotone-derivative`: слишком простая одноходовая задача про периодическую функцию и знак производной. Есть смысл держать как отдельный короткий тест, пока не создан специальный кластер "периодические препятствия".
- `putnam-early-1959-a5-pursuit-curve`: близость к separable-задачам поверхностная; главный механизм - вывод ОДУ из геометрии преследования, а не стандартная техника разделения.
- `putnam-modern-1979-b4`: проверены соседи по линейным ОДУ с переменными коэффициентами и краевым условиям; задача уникальна за счет скрытого инвариантного двумерного пространства, не набирает группу из трех близких карточек.

## Проверки

Прогнаны после правок:

- `python tools\validate.py`
- `python tools\check_links.py`
- `python tools\audit_rules.py`
- `python tools\check_clusters.py`
- `python tools\build_index.py`
- `python tools\build_viewer.py`

На момент отчета база зеленая.
