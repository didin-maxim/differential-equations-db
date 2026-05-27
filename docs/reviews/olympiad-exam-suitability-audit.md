# Аудит олимпиадных задач на экзаменационную пригодность

Дата: 2026-05-27.

## Область

Проверен весь видимый слой `data/problems/olympiad/**`: 87 карточек.

Особый фокус:

- свежие MSU ODE 2021-2024: 5 карточек;
- свежие MSU ODE 2025-2026: 7 карточек;
- старый MSU ODE-архив: 10 карточек.

Итого по MSU ODE проверено 22 карточки. Свежий архив уже был в основном согласован: короткие задачи имеют `exam_score_*`, тяжелые или review-only карточки не должны попадать в основной экзаменационный режим.

## Итоги классификации

- `exam_score_*` в олимпиадном слое после правок: 37 карточек.
- `olympiad_above_exam` или `idea_score > 10`: 22 карточки.
- `standard_course_methods`: 42 карточки.
- `advanced_standard_course`: 42 карточки.
- `beyond_standard_course`: 4 карточки.
- `difficulty.main == course_core`: 17 карточек.

Карточек с `technical_score > 5` и одновременно `exam_score_*` после правок не осталось. Это важно для устной симуляции: длинные вычисления могут оставаться в базе, но не должны маскироваться под хорошие короткие экзаменационные вопросы.

## Переведены ближе к экзамену

Семь задач оставлены с `olympiad_style`, но классифицированы как стандартные курсовые задачи (`course_core`) и получили явные `exam_score_*`:

- `bounded-solution-y-prime-y-square` - стандартный взрыв модели `y'=y^2`, `exam_score_6`;
- `convex-solution-two-zeros` - хорда и выпуклость, `exam_score_5`;
- `energy-no-nonconstant-decay-periodic` - функция Ляпунова запрещает непостоянный цикл, `exam_score_6`;
- `global-positive-impossible` - сравнение через `arctan y`, `exam_score_6`;
- `two-solutions-touching` - следствие единственности задачи Коши, `exam_score_5`;
- `periodic-solution-monotone-derivative` - периодичность против строгой монотонности, `exam_score_4`;
- `periodic-linear-equation-zero-mean` - периодическое решение линейного уравнения первого порядка, `exam_score_6`.

Добавлен proposal batch `data/exam_simulation/question_batches/olympiad-standard-course-overlay.yaml` с 4 короткими вопросами: два `self_check`, один `multiple_choice`, один `formula`. В основной `questions.yaml` ничего не переносилось.

## Убраны дальше от устной симуляции

Сняты экзаменационные score-теги там, где задача хорошая, но не подходит под короткий устный режим:

- `msu-ode-2021-2-nonextendable-blowup-coordinates`: снят `exam_score_9`, потому что карточка имеет `needs_human_review` и `public_ready: false`; вопрос удален из proposal batch `msu-ode-2021-2024`.
- `msu-ode-2005-8-six-dimensional-resonance`: снят `exam_score_6`, потому что это длинная вычислительная вариация постоянных (`technical_score=6`).
- `msu-ode-2012-3-recover-autonomous-matrix`: снят `exam_score_8`, потому что нужен спектральный счет с параметром (`technical_score=6`).
- `ru-misc-kfu-2013-13-1`: снят `exam_score_8`, потому что решение требует кусочной сшивки на двух полуосях (`technical_score=7`).

## Оставлены олимпиадными

22 карточки остаются выше обычной экзаменационной границы через `olympiad_above_exam` и/или `idea_score > 10`:

`msu-ode-2023-8-fourth-order-zero-count-review`, `putnam-early-1955-a7-zero-bounds`, `putnam-early-1957-ii6-zero-location`, `putnam-early-1959-a5-pursuit-curve`, `putnam-early-1960-b7-riccati-variational`, `putnam-early-1971-b5-hypocycloid-system`, `putnam-early-1973-a5-nonlinear-system-blowup`, `putnam-early-1975-a5-wronskian-nonlinear-transform`, `putnam-modern-1995-a5`, `putnam-modern-1999-b4`, `putnam-modern-2005-b3`, `putnam-modern-2009-b5`, `putnam-modern-2010-b5`, `putnam-modern-2023-a3`, `ru-cis-extra-spbgeu-2023-rolle-cubic-operator`, `ru-cis-extra-yagtu-2001-half-argument-ode`, `ru-cis-extra-yagtu-2014-exp-minus-xy-limit`, `ru-misc-kfu-2019-19-3`, `ru-misc-nure-8-3`, `ru-misc-spb-itmo-2018-6`, `bme-2024-p2-composition-ode-nonexistence`, `vjimc-2016-c2-p4-moving-average-delay-variation`.

Эти карточки не надо добавлять в обычную экзаменационную симуляцию: там либо внешняя/тонкая техника, либо функционально-дифференциальный глобальный трюк, либо вычислительно и идейно более олимпиадная постановка.

## Родственные связи и теория

Добавлен файл связей `data/relations/relations.d/olympiad-exam-suitability-audit.yaml`:

- `picard-lindelof-theorem -> two-solutions-touching`;
- `blow-up-comparison-y-square -> bounded-solution-y-prime-y-square`;
- `blow-up-comparison-y-square -> global-positive-impossible`;
- `cluster-phase-stability-lyapunov-direct-method -> energy-no-nonconstant-decay-periodic`.

Нужны будущие теоретические/родственные узлы:

- для `msu-ode-2021-2-nonextendable-blowup-coordinates` желательно оформить отдельную лемму о реализации заданной гладкой непересекающейся кривой как траектории непрерывного поля;
- для `msu-ode-2023-8-fourth-order-zero-count-review` по-прежнему нужен самодостаточный факт о дисконъюгированности/фокальных точках четвертого порядка;
- для периодических линейных уравнений первого порядка можно добавить отдельную теоретическую карточку о монодромии/условии периодичности в скалярном случае, если этот сюжет начнет повторяться.

## Проверки

Запущены успешно:

```powershell
python tools/build_index.py
python tools/validate.py
python tools/check_links.py
python tools/check_encoding.py
python tools/check_clusters.py
python tools/build_viewer.py
```

Результаты:

- `build_index.py`: OK, записан `index/generated.json`, 386 cards;
- `validate.py`: OK, 386 cards, 579 relations, 41 sources;
- `check_links.py`: OK, links are consistent;
- `check_encoding.py`: OK, UTF-8 без очевидных mojibake-маркеров;
- `check_clusters.py`: OK, 34 task clusters;
- `build_viewer.py`: OK, записан `viewer/index.html`.

`check_clusters.py` был запущен, потому что добавлен файл relations. `build_viewer.py` был запущен, потому что изменен `data/exam_simulation`.
