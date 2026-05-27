# Дополнительный обзор международных студенческих соревнований

Область обзора: дополнительный проход по англоязычным или международно удобным архивам студенческих соревнований, которые еще не были хорошо покрыты базой. Фильтр был строгим: включать только задачи, где центральны ОДУ, дифференциальное неравенство, линейный дифференциальный оператор, система или качественный аргумент из теории ОДУ. Близкие задачи из обычного анализа, теоремы Ролля или формулы Тейлора без ОДУ-механизма исключались.

## Включено

| архив | задача | вердикт | краткое условие | идея решения | источник |
|---|---:|---|---|---|---|
| Simon Marais Mathematics Competition official archive | 2018 A3 | include | Решение задачи Коши `y'=ln(y/x)`, `y(1)=2018`; нужно посчитать положительные решения `y=2000`. | Из `ln u<=u-1` следует строгая вогнутость `y''<0`; знак `y'` задается отношением `y/x`, поэтому график имеет одну вершину. Левая часть отсекается интегральной оценкой, справа уровень пересекается один раз. | https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-solutions.pdf |
| ISTCiM official archive | 2022 C | include | Доказать равенство `int_0^infty e^(-tx)/(1+x^2) dx = int_0^infty sin x/(t+x) dx` для `t>0`. | Обе стороны как функции параметра `t` удовлетворяют `y''+y=1/t`; разность решает `H''+H=0` и стремится к нулю на бесконечности, значит равна нулю. | https://istcim.math.us.edu.pl/ISTCiM_2022_problems.pdf |
| ISTCiM official archive | 2023 E | include | Найти дифференцируемые `f`, удовлетворяющие двум функциональным тождествам со сдвигами и условию `f(x)^2+f(x+1)^2=1`. | Функциональные тождества дают четность, `f(x+2)=-f(x)` и после предельного перехода `f'(x)=c f(x+1)`. Еще одно дифференцирование дает `f''=-c^2 f`, откуда косинусы с частотами `(2k+1)pi/2`. | https://istcim.math.us.edu.pl/ISTCiM2023-problems_with_solutions.pdf |
| IMC official archive | 2006 P6 | include | Критерий вещественности всех корней многочлена `A`: для любой функции с `n+1` нулями оператор `A(D)` зануляется в промежуточной точке. | Если корни вещественны, `A(D)` факторизуется в множители `D-c`, каждый обрабатывается Роллем после множителя `e^(-cx)`. Если есть комплексный корень, решение `e^(ux)sin(vx)` дает контрпример после малого полиномиального сдвига. | https://www.imc-math.org.uk/imc2006/day1_solutions.pdf |
| BME Mathematics Contest archive | 2023 P3 | include | Для `L`-периодической `C^(2n)`-функции с нулем доказать `max |f| <= (L^2/8)^n max |f^(2n)|`. | Базовая лемма второго порядка: максимум находится не дальше `L/2` от некоторого нуля, и формула Тейлора дает множитель `L^2/8`. Затем лемма применяется к `f, f'', ..., f^(2n-2)`. | https://math.bme.hu/~mweiner/contest2023.pdf |

## Пограничные случаи

| архив | задача | вердикт | почему не импортировано | источник |
|---|---:|---|---|---|
| Simon Marais Mathematics Competition official archive | 2018 A4 | borderline | В официальном решении используется ОДУ для производящей функции, но исходная задача в первую очередь про вероятностную рекурсию и четность состояний; DE-механизм не является предметом задачи. | https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-solutions.pdf |
| Simon Marais Mathematics Competition official archive | 2024 B4/C4 | borderline | Решение вводит производящую функцию, удовлетворяющую простому ОДУ, но центральная трудность - комбинаторная рекурсия/ожидаемое значение, а не ОДУ как самостоятельный объект. | https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc_2024_solutions.pdf |
| Vojtech Jarnik International Mathematical Competition official archive | 2015 Category II P4 | borderline | После преобразования тройного интеграла получается функционально-дифференциальное условие, но основной объем задачи - редукция кратного интеграла; ранее уже отмечено как borderline. | https://vjimc.osu.cz/storage/uploads/j25problems2.pdf |
| IMC official archive | 2025 P2 | borderline | Равенство в оценке ведет к `f''=lambda(1-x^2)`, но основная идея - Cauchy-Schwarz и интегрирование по частям, не ОДУ. | https://www.imc-math.org.uk/imc2025/imc2025-day1-solutions.pdf |

## Исключено / кандидатов нет

| архив | проверенный материал | вердикт | примечание | источник |
|---|---|---|---|---|
| Simon Marais official archive | 2017-2025 pages/PDFs by keyword and targeted solution review | exclude mostly | Помимо 2018 A3, найденные derivative/differential hits относятся к производящим функциям, дискретным рекурсиям, функциональным уравнениям или обычному анализу без центрального ОДУ. | https://www.simonmarais.org/ |
| Berkeley Math Tournament | official pages and public problem archive search | exclude | Не найден релевантный undergraduate DE archive; доступные BMT материалы в основном high-school competition, поэтому импорт в undergraduate DE-базу не делался. | https://bmt.berkeley.edu/ |
| Traian Lalescu / Romanian student contest references | SSMR/Gazeta visible notes and web search | exclude for this batch | Надежные открытые материалы, найденные в этом проходе, не дали англоязычного международного DE-кандидата; национальные румынские источники оставлены для отдельного локального/национального импорта. | https://ssmr.ro/gazeta/gma/ |
| VJIMC official archive | previous official archive scan plus targeted DE keyword search | exclude except borderline | Чистых include-задач по ОДУ не найдено; производные в сильных hit'ах используются как анализ/выпуклость/интегралы. | https://vjimc.osu.cz/ |
| Putnam archive | current database and Putnam scan cross-check | no new include | Все include-кандидаты из имеющегося Putnam scan уже представлены в `putnam_early` или `putnam_modern`; новых не импортировал, чтобы не дублировать текущую базу. | https://kskedlaya.org/putnam-archive/ |

## Решение об импорте

Импортированы пять карточек в `data/problems/olympiad/international_extra/`:

- `smmc-2018-a3-log-ratio-concavity`
- `istcim-2022-c-integral-identity-ode`
- `istcim-2023-e-functional-ode-cosine`
- `imc-2006-p6-real-root-differential-operator`
- `bme-2023-p3-periodic-high-derivative-bound`

Пачка намеренно выбирает неповторяющиеся механизмы: качественную вогнутость для нелинейного ОДУ первого порядка, интегральное тождество с параметром через ОДУ второго порядка, функциональное уравнение с переходом к гармоническому ОДУ, вещественность корней через факторизацию дифференциального оператора и периодическое дифференциальное неравенство для старших производных.
