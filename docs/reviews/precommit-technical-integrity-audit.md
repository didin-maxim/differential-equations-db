# Pre-commit technical integrity audit

Дата: 2026-05-27.

Цель: проверить техническую целостность базы перед финальным коммитом без содержательной переработки карточек и без отката параллельных изменений.

## Команды

Запущены из корня репозитория `C:\Users\Admin\Documents\Codex\differential-equations-db`.

```powershell
python tools\validate.py
python tools\check_links.py
python tools\audit_rules.py
python tools\check_clusters.py
python tools\check_encoding.py
python tools\build_index.py
python tools\build_viewer.py
rg -n "needs_solution_completion|TODO|FIXME|MISSING|unknown|UNKNOWN" data docs tools
```

## Результаты

- `validate.py`: OK, `357 cards`, `521 relations`, `38 sources`.
- `check_links.py`: OK, ссылки согласованы.
- `audit_rules.py`: OK, `0 warnings`.
- `check_clusters.py`: OK, `32 task clusters`.
- `check_encoding.py`: OK, явных mojibake-маркеров нет.
- `build_index.py`: OK, пересобран `index/generated.json` на `357` карточек.
- `build_viewer.py`: OK, пересобран `viewer/index.html`.

## Что проверено

- JSON-compatible YAML читается валидаторами.
- Дубли `id`, неизвестные `tag`, `source_id`, `standard_ideas`, `definition_ids` не обнаружены.
- Relations не ссылаются на неизвестные карточки и используют известные типы связей.
- Cluster `representative_card_ids` ссылаются на существующие карточки.
- Битых ссылок на источники и определения в проверяемых полях не найдено.
- Явных признаков битой кириллицы валидатор кодировки не нашел.

## Замечания

- Репозиторий по-прежнему целиком выглядит как untracked в `git status`; аудит ничего не индексировал, не коммитил и не пушил.
- `rg` нашел известный содержательный маркер `needs_solution_completion` у карточки `msu-ode-2023-8-fourth-order-zero-count-review`. Это не техническая ошибка: карточка уже помечена как неполная и исключена из solved/representative-использования в связанных аудитах.
- В ходе этого аудита правки данных не потребовались.
