# Аудит языкового качества

Дата: 2026-05-27.

## Что проверено

- `data/problems/**/*.yaml` с приоритетом на видимые поля карточек: `title`, `statements.*.title/text`, `ideas.*.title/text`, `solutions.*.title/text`.
- `data/task_clusters/clusters.yaml`, `data/sources/sources.yaml`, `data/standard_ideas/standard_ideas.yaml`.
- `docs/**/*.md` по маркерам кодировки и явным англоязычным служебным словам; полный литературный проход по временным отчетам не выполнялся.
- Маркеры через `rg`: mojibake-фрагменты, `TODO`, `FIXME`, `source locator`, `proof-main`, `solution key`, `Proof`, `Solution`, `Problem`, `exercise`, `theorem`, а также частые английские остатки в русских полях.
- `tools/check_encoding.py`: расширен список маркеров типичного mojibake, чтобы ловить не только символ замены U+FFFD.

## Что исправлено

- Убраны англоязычные заголовки `statements.original.title` в Waterloo-карточках; source locator в `sources.note` оставлен на английском как источник.
- В русских текстах заменены явные английские фразы: `boundary term`, `Floquet theory`, `stable manifold theorem`, `semilinear PDE`, `companion-система`, `approaching`, `blow-up`, `shooting`, `implicit IVP`, `integral from ...`, `Rolle theorem`, `boundary value` и близкие случаи.
- Несколько формульных псевдозаписей с английскими словами переведены в локальный стиль `int_a^b`, `tr`, `det`, `принадлежит`, `из K`, без изменения математического смысла.
- В `data/task_clusters/clusters.yaml` русифицированы видимые пояснения с `blow-up alternative`, `sensitivity`, `continuous dependence`, `representatives`, `implicit IVP`.
- В `tools/check_encoding.py` добавлены типичные UTF-8/Windows-1251 mojibake-маркеры через Unicode escape-последовательности, чтобы сам файл не срабатывал на собственный список.

## Оставлено без правки

- Английские названия источников, `locator`, `note` источников и названия курсов/книг: это допустимые source locator и библиографические данные.
- Служебные id, tags и relation ids вроде `proof-main`, `semilinear_pde`, `floquet_determinant`: это не учебный текст карточки.
- Стандартная формульная латиница: `lambda`, `theta`, `Phi`, `int`, `exp`, `tr`, `det`, `Ker`, `R^n` и похожая математическая запись.
- Временные отчеты в `docs/reviews`: исправлялись только по явным маркерам, без полного стилистического редактирования.

## Human review

- Математически сомнительные формулировки специально не переписывались. В рамках языкового прохода отдельных мест, требующих немедленного математического изменения, не выявлено.
- При следующем содержательном аудите стоит отдельно решить, насколько viewer должен показывать служебные id решений (`proof-main`) и внутренние difficulty-теги (`advanced_standard_course`): сейчас они оставлены как метаданные.
