# Аудит кластера phase-line-stability

Дата: 2026-05-26. Зона: `phase-line-stability` и ближайший слой фазовой плоскости/устойчивости.

## Что просмотрено

- `data/task_clusters/clusters.yaml`, `docs/TASK_CLUSTERS.md`.
- Предыдущие отчеты: `local-du-gap-and-dedup-report.md`, `local-du-filippov-selection.md`, `english-import-qa.md`.
- Карточки по тегам и объектам: `phase_line`, `phase_plane`, `stability`, `equilibrium_linearization`, `lyapunov`, `first_integral`, `nonlinear_system`, `center`, `saddle`, `limit_cycle`; также поиском по объектам `focus`, `node`.

## Изменения кластера

`phase-line-stability` оставлен с прежним id, но в notes явно расширен до ближайшего слоя фазовой плоскости и устойчивости. Статус переведен в `watch`: базовая фазовая прямая уже была покрыта, а после этого прохода закрыты обязательные визуальные/теоретические пробелы.

В representatives добавлены:

- теоретические узлы: определения устойчивости, классификация линейных равновесий на плоскости, гиперболическая линеаризация, прямой метод Ляпунова, первый интеграл и центр;
- существующие точные попадания: `weak-pass-linear-system-saddle`, `waterloo-spiral-phase-portrait-isoclines`, `local-du-written-2022-nonlinear-equilibria-linearization`, `local-du-romanko-first-integral-center`;
- новые визуальные карточки и Филиппов 889.

Политика насыщения теперь запрещает массовые новые `2x2` phase portrait cards, если меняются только коэффициенты и тип уже представлен.

## Покрытие линейных равновесий на плоскости

До прохода были отдельные представители: седло (`weak-pass-linear-system-saddle`), устойчивый фокус (`waterloo-spiral-phase-portrait-isoclines`), неустойчивый узел в нелинейных экзаменационных карточках, центр через первый интеграл, несколько задач на линеаризацию. Не было компактной справочной карточки, где вместе названы все стандартные случаи.

Добавлена `cluster-phase-stability-linear-plane-classification`, которая закрывает:

- седло;
- устойчивый и неустойчивый узел;
- кратный собственный корень: собственный, вырожденный и дикритический/звездный узел;
- устойчивый и неустойчивый фокус;
- центр;
- нулевые собственные значения и негиперболические ограничения метода.

## Филиппов 889

Добавлена карточка `local-du-filippov-889-attractive-not-lyapunov-stable`.

Локальный файл: `C:\Users\Admin\Desktop\ДУ\Filippov-AF-Sbornik-zadach-po-differentsialnym-uravneniyam.djvu`. В окружении отсутствуют `djvutxt`, `ddjvu`, `djvused`; PyMuPDF/DjVu extraction не использовался. Поэтому условие и рисунок сверены по онлайн-представлению задачи 889 на Решу.РФ:

- страница задачи: https://xn--e1avkt.xn--p1ai/математика/Филиппов/889/
- изображение решения/рисунка сохранено локально как `data/assets/images/phase_stability/filippov-889-figure-solution.jpg`;
- обрезанный фазовый портрет сохранен как `data/assets/images/phase_stability/filippov-889-phase-portrait.jpg`.

Ограничение: точная страница локального DjVu не извлечена штатными инструментами; локальный asset основан на онлайн-изображении. В карточке это зафиксировано в `source_note` и `sources.note`.

Смысл задачи: все изображенные траектории стремятся к нулю, но нуль неустойчив по Ляпунову, значит не является асимптотически устойчивым. Это важный контраст к неверной эвристике "притягивает значит асимптотически устойчиво".

## Визуальные задачи

Интернет-поиск дал надежные справочные и учебные источники по фазовым портретам и линеаризации, но не готовый набор свободно переиспользуемых постановок ровно формата "посмотри на картинку и назови устойчивость". Использованные ориентиры:

- Jiří Lebl, Notes on Diffy Qs, linearization and critical points: https://www.jirka.org/diffyqs/html/linearization_section.html
- LibreTexts / Herman, Linear Systems, examples of stable node, center, focus: https://math.libretexts.org/Bookshelves/Differential_Equations/A_First_Course_in_Differential_Equations_for_Scientists_and_Engineers_%28Herman%29/06%3A_Linear_Systems/6.01%3A_Linear_Systems

Поэтому добавлены self-authored/model cards с локальными SVG:

- `cluster-phase-stability-visual-asymptotic-sink` - асимптотически устойчивый фокус;
- `cluster-phase-stability-visual-center-stable-not-asymptotic` - устойчивый, но не асимптотически устойчивый центр;
- `cluster-phase-stability-visual-saddle-unstable` - неустойчивое седло.

Филиппов 889 отдельно покрывает тонкий визуальный случай: притягивающее, но не устойчивое по Ляпунову равновесие.

## Теоретический блок

Добавлены только компактные карточки, где не было близкого аналога:

- `cluster-phase-stability-lyapunov-definitions`;
- `cluster-phase-stability-linear-plane-classification`;
- `cluster-phase-stability-linearization-hyperbolic`;
- `cluster-phase-stability-lyapunov-direct-method`;
- `cluster-phase-stability-first-integral-center`.

Существующие задачные аналоги оставлены и связаны: `lyapunov-linearization-example`, `oral-middle-nonlinear-system-lyapunov`, `local-du-romanko-first-integral-center`, `local-du-written-2014-51-equilibrium-linearization`, `local-du-written-2022-nonlinear-equilibria-linearization`, Lebl degenerate linearization.

## Дубли

Удалений не выполнялось. Причина: найденные близкие карточки различаются ролью в базе.

- `weak-pass-linear-system-saddle` и визуальная saddle-card: первая вычисляет решение системы, вторая проверяет определение устойчивости по рисунку.
- `waterloo-spiral-phase-portrait-isoclines` и визуальная sink-card: Waterloo добавляет изоклины и направление вращения, новая карточка только про определение асимптотической устойчивости.
- `local-du-romanko-first-integral-center` и новая lemma-card: Романко - задача с первым интегралом, новая карточка - переносимый теоретический факт.
- Нелинейные экзаменационные карточки на равновесия и линеаризацию не удалялись: они содержат разные исходные системы и служат source-verified local_du examples.

## Добавленные файлы

- Карточки: `data/problems/cluster_audit/phase_stability/*.yaml`.
- Assets: `data/assets/images/phase_stability/`.
- Связи: `data/relations/relations.d/cluster-phase-stability.yaml`.
- Batch: `data/import_batches/cluster-phase-stability.yaml`.

## Проверки

Проверки запущены в конце прохода:

```powershell
python tools\validate.py
python tools\check_links.py
python tools\audit_rules.py
python tools\check_clusters.py
python tools\build_index.py
python tools\build_viewer.py
```

Итоговый результат см. в финальном сообщении исполнителя.
