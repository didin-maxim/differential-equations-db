# Viewer Definition Navigation

## Что сделано

- Добавлен фильтр `definition` в viewer: выпадающий список «Определения» / «Все определения», фасет «Определения» с количеством карточек и активные фильтры.
- Карточки показывают chip-кнопки связанных определений по `definition_ids` с подписями из `definition_labels`.
- `definition` читается из query string и синхронизируется обратно в URL при смене фильтров.
- Добавлен быстрый режим «Определения» и вход с главной страницы на `viewer/index.html?nav=definitions`.
- Поиск покрывает определения: после `build_index.py` карточки с `definition_ids` содержат `definition_labels` в `search_text`.

## Проверки

- `python tools/build_index.py` — OK.
- `python tools/build_viewer.py` — OK.
- JS syntax sanity для встроенных скриптов viewer — OK.
- Browser smoke test на `http://127.0.0.1:8777/viewer/index.html?definition=solution` — OK: фильтр восстановился, карточки и definition chips отрисовались.
- `python tools/validate.py` — OK.
- `python tools/check_links.py` — OK.
- `python tools/check_encoding.py` — OK.
- `python tools/check_clusters.py` — OK.
- `python tools/audit_rules.py --max-items 80` — OK, 7 предупреждений.

## Предупреждения аудита

- `cluster-olympiad-transformed-linear-mvt-method-guide`: `olympiad_above_exam` with exam_score tag.
- `cluster-olympiad-transformed-linear-mvt-method-guide`: method guide has no references.
- `cluster-olympiad-transformed-linear-mvt-zero-sign-exam`: `olympiad_above_exam` with exam_score tag.
- `local-du-written-2014-51-characteristics-pde`: exam_score tag with technical_score > 5.
- `local-du-written-2014-51-factorized-variable-coeff`: exam_score tag with technical_score > 5.
- `local-du-written-2014-51-lagrange-singular-curves`: exam_score tag with technical_score > 5.
- `local-du-written-2024-variational-free-endpoint`: exam_score tag with technical_score > 5.

Данные карточек и кластеров не менялись.
