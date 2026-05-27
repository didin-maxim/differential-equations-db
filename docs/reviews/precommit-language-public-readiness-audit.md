# Pre-commit аудит языка и публичной готовности

Дата: 2026-05-27.

## Область проверки

Проверены свежие олимпиадные карточки, отчеты `docs/reviews`, заметки кластеров в `data/task_clusters/clusters.yaml`, а также кодировка UTF-8.

Использованные проверки:

- `python tools/check_encoding.py`
- `rg` по типичным маркерам mojibake и фрагментам битой кириллицы, включая латинские пары, которыми часто отображаются русские байты в неправильной кодировке, и `U+FFFD`.
- `rg` по служебным английским хвостам: `Scope`, `Candidate table`, `Import decision`, `Russian summary`, `solution idea`, `Source`, `TODO`, `FIXME`, `boundary term`, `integral from`.
- выборочный просмотр свежих олимпиадных scan/report файлов и заметок кластеров.

## Исправлено

- Русифицированы служебные заголовки и колонки в свежих олимпиадных отчетах:
  - `docs/reviews/olympiad-scan-vjimc-europe.md`;
  - `docs/reviews/olympiad-scan-international-extra.md`;
  - `docs/reviews/olympiad-scan-other-international.md`;
  - `docs/reviews/olympiad-scan-imc.md`;
  - `docs/reviews/olympiad-scan-putnam.md`.
- В `docs/reviews/olympiad-import-queue.md` исправлены несколько формул, поврежденных при генерации markdown-таблицы:
  - оценка BME 2023 P3 теперь читается как `max |f| <= (L^2/8)^n max |f^(2n)|`;
  - строка ХНУРЭ 8.8 теперь содержит полную оценку `|x(t2)-x(t1)|`;
  - строка VJIMC 2016 C2 P4 теперь содержит `int_1^infty |f'| < infty`;
  - строка Putnam 2023 A3 помечена как кандидат, требующий чистого условия, вместо обрывка формулы.
- В заметках ключевых кластеров заменены явные служебные англицизмы вроде `Cross-source аудит`, `orphan-карточки`, `representatives`, `conceptual-variant`, `saturated`, `Green-function constructions` там, где это были обычные публичные русские предложения, а не идентификаторы.
- В Putnam-обзоре заменены два хвоста `Source:` на `Источник:` и русифицирована ссылка на лемму Пуанкаре.

## Оставлено осознанно

- Английские названия соревнований, книг, курсов и источников: `VJIMC`, `SEEMOUS`, `BME Mathematical Contest`, `Problem Set`, `Problems and Solutions`, `Putnam Problems: Differential Equations`.
- Идентификаторы, теги, URL, значения `locator`, `source_id`, `cluster_id`, `status`, `representative_card_ids`.
- Английские слова внутри проверочных отчетов, где они описывают сам поисковый маркер или название поля.

## Итог

Явных маркеров битой кириллицы не найдено. Исправленные места относятся к безопасной публичной полировке и не меняют математическое содержание карточек.
