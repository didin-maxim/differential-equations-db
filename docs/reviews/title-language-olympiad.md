# Языковая редактура названий олимпиадных задач

Дата: 2026-05-27.

## Объем

Просмотрено примерно 87 карточек из `data/problems/olympiad/`. Основной фокус был на свежих импортах `msu_ode_2021_2024` и `msu_ode_2025_2026`, но дополнительно проверены старые MSU, Putnam, IMC/ISTCiM/BME, русские региональные и геометрические карточки.

Метод прохода: сначала оценивался только корневой `title`, затем для подозрительных карточек открывались условие, идеи и решение. В нескольких местах исправлены также внутренние заголовки идей, если там был явный языковой дефект.

## Что найдено

- Импортные префиксы в свежих MSU ODE дублировали источник и утяжеляли названия задач.
- Несколько заголовков прямо раскрывали отрицательный ответ: "нет", "невозможность", "запрещает", "не гарантирует".
- Были отдельные англоязычные или полурусские элементы в заголовках: `epsilon`, `lambda`, `Boundedness`.
- Некоторые названия были слишком длинными и пересказывали условие вместо короткой навигационной темы.
- В одном Putnam-заголовке встречалась неестественная калька "конкурентность касательных".

## Измененные файлы

- `data/problems/olympiad/energy-no-nonconstant-decay-periodic.yaml`
- `data/problems/olympiad/global-positive-impossible.yaml`
- `data/problems/olympiad/periodic-linear-equation-zero-mean.yaml`
- `data/problems/olympiad/periodic-solution-monotone-derivative.yaml`
- `data/problems/olympiad/international_extra/istcim-2022-c-integral-identity-ode.yaml`
- `data/problems/olympiad/international_extra/istcim-2023-e-functional-ode-cosine.yaml`
- `data/problems/olympiad/msu_ode/msu-ode-2012-9-negative-instant-spectrum.yaml`
- `data/problems/olympiad/msu_ode_2021_2024/msu-ode-2021-2-nonextendable-blowup-coordinates.yaml`
- `data/problems/olympiad/msu_ode_2021_2024/msu-ode-2021-5-inhomogeneous-second-order-span.yaml`
- `data/problems/olympiad/msu_ode_2021_2024/msu-ode-2024-1-integrating-factor-sine-log.yaml`
- `data/problems/olympiad/msu_ode_2021_2024/msu-ode-2024-6-variable-coeff-characteristic-root.yaml`
- `data/problems/olympiad/msu_ode_2025_2026/msu-ode-2025-2-min-order-polynomial-solutions.yaml`
- `data/problems/olympiad/msu_ode_2025_2026/msu-ode-2025-3-gyroscopic-stabilization.yaml`
- `data/problems/olympiad/msu_ode_2025_2026/msu-ode-2025-6-global-matrix-riccati-invertible.yaml`
- `data/problems/olympiad/msu_ode_2025_2026/msu-ode-2025-7-superstable-second-order-impossible.yaml`
- `data/problems/olympiad/msu_ode_2025_2026/msu-ode-2026-3-decoupled-phase-curves-count.yaml`
- `data/problems/olympiad/msu_ode_2025_2026/msu-ode-2026-5-polar-stable-not-asymptotic.yaml`
- `data/problems/olympiad/msu_ode_2025_2026/msu-ode-2026-6-singular-linear-system-epsilon.yaml`
- `data/problems/olympiad/oral_exam_geometry/oral-exam-geometry-linear-second-order-uniqueness.yaml`
- `data/problems/olympiad/putnam_early/putnam-early-1954-i3-concurrent-tangents.yaml`
- `data/problems/olympiad/putnam_modern/putnam-modern-2010-b5.yaml`
- `data/problems/olympiad/ru_misc/ru-misc-nure-8-5.yaml`
- `data/problems/olympiad/vjimc_europe/bme-2024-p2-composition-ode-nonexistence.yaml`

## Оставлено без изменения

- Contest-префиксы `Putnam`, `IMC`, `SEEMOUS`, `BME`, `ISTCiM` в большинстве международных импортов оставлены: это уже устойчивый стиль этих карточек и полезный источник навигации.
- Формульные элементы вроде `f'=f`, `A(D)`, `xD` и `y''` оставлены там, где без них название становилось слишком общим.
- Заголовки вроде "Ортогональная фундаментальная матрица и кососимметричность A(t)" и "Все интегрирующие множители через первый интеграл" выглядят техническими, но оставлены: они короткие, точные и соответствуют содержанию.
- Несколько внутренних текстов решений по-прежнему содержат латиницу в математических обозначениях или англоязычные технические слова вне `title`; этот проход был ограничен редактурой заголовков.
