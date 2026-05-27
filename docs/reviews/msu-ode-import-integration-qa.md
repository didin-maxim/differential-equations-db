# Интеграционный QA импорта МГУ ОДУ

Дата: 2026-05-27.

## Область проверки

Проверены MSU ODE-карточки, которые были видны в рабочем дереве на момент QA:

- `data/problems/olympiad/msu_ode/` - 10 карточек старого импорта;
- `data/problems/olympiad/msu_ode_2021_2024/` - 5 карточек свежего импорта 2021/2024;
- `data/problems/olympiad/msu_ode_2025_2026/` - 7 карточек свежего импорта 2025/2026.

Всего проверено 22 карточки, 3 batch-файла и 3 relation-файла:

- `data/import_batches/msu-ode-olympiad.yaml`;
- `data/import_batches/msu-ode-2021-2024.yaml`;
- `data/import_batches/msu-ode-2025-2026.yaml`;
- `data/relations/relations.d/msu-ode-olympiad.yaml`;
- `data/relations/relations.d/msu-ode-2021-2024.yaml`;
- `data/relations/relations.d/msu-ode-2025-2026.yaml`.

## Критерии QA

- В базу должны попадать только задачи, где содержательная идея действительно относится к ОДУ/системам: существование и единственность, продолжение, матричная экспонента, фундаментальная матрица, устойчивость, фазовая плоскость, интегрирующие множители, Риккати, Вронскиан/Лиувилль, нули линейных ОДУ.
- Не включать сюжеты, где ОДУ является декоративной оболочкой, либо задача фактически про кратные интегралы, ряды, чистые интегральные неравенства, дискретную динамику/геометрию вне фокуса базы.
- Для курса использовать местные теги `standard_course_methods`, `advanced_standard_course`, `beyond_standard_course`. Олимпиадная сложность сама по себе не должна автоматически давать `beyond_standard_course`.
- Карточки с `idea_score > 10` должны быть явно отделены от обычного экзаменационного слоя; если решения нет или нужен внешний факт, карточка не должна быть публично готовой.
- Связи ставятся по переносимому механизму, а не просто по источнику или теме.
- Предложения для симуляции экзамена из олимпиад должны оставаться отдельными proposal-слоями и быть короткими, идейными, с низкой технической нагрузкой.

## Исправлено

- В `data/problems/olympiad/msu_ode_2021_2024/msu-ode-2021-2-nonextendable-blowup-coordinates.yaml` изменено `editorial.public_ready` с `true` на `false`: карточка уже имела `review_status: needs_human_review`, а заметка честно говорит, что реализацию заданной кривой как траектории непрерывного поля лучше оформить отдельной леммой.
- Пересобраны `index/generated.json` и `viewer/index.html` штатными командами после текущего состояния импортов.

## Итоги проверки

- Все 22 MSU ODE-карточки ссылаются на `src-msu-ode-olympiad`; batch-файлы ссылаются только на существующие problem id.
- В MSU relation-файлах не найдено битых `from`/`to`.
- Явных карточек не по теме базы среди импортированных MSU ODE-задач не найдено. В отчетах импортеров спорные задачи вроде MSU 2021/7, части 2023, 2024/7 и вычислительных/геометрических сюжетов оставлены вне импорта или как near-miss.
- Разметка курса выглядит согласованной: большинство задач выше обычной техники помечены `advanced_standard_course`, но не `beyond_standard_course`; это соответствует правилу, что олимпиадность не равна выходу за курс.
- Единственная MSU-карточка с `idea_score > 10` - `msu-ode-2023-8-fourth-order-zero-count-review` - остается review-only: `solutions: []`, `needs_solution_completion`, `beyond_standard_course`, `olympiad_above_exam`, `public_ready: false`.
- Предложения для симуляции экзамена по 2025/2026 лежат только в `data/exam_simulation/question_batches/msu-ode-2025-2026.yaml`, не в основном `questions.yaml`; автоматический риск-фильтр по ним не нашел проблем.

## Оставшиеся риски

- `msu-ode-2021-2-nonextendable-blowup-coordinates` теперь не публичная, но `data/exam_simulation/question_batches/msu-ode-2021-2024.yaml` все еще содержит proposal `exam-sim-proposal-msu-2021-2-self-check`. Перед переносом в основной exam simulation его нужно удалить или оставить только после закрытия human review.
- Новые импорты 2021/2024 и 2025/2026 в основном связаны через relation-файлы с существующими якорями и кластерами. Я не правил `data/task_clusters/clusters.yaml`, чтобы не мешать параллельным импортерам; при финальном проходе можно точечно решить, какие из новых карточек стоит включить в `representative_card_ids`/notes кластеров.
- `msu-ode-2023-8-fourth-order-zero-count-review` остается корректно изолированной, но математически незакрытой карточкой. Ее нельзя использовать как solved representative или источник экзаменационного вопроса, пока не будет самодостаточного доказательства леммы о нулях четвертого порядка.
- QA сделан по текущему снимку рабочего дерева. Если параллельные импортеры добавят новые MSU-файлы после этого отчета, их нужно прогнать тем же чек-листом.

## Команды проверки

Запущены успешно:

```powershell
python tools/build_index.py
python tools/build_viewer.py
python tools/validate.py
python tools/check_links.py
python tools/audit_rules.py
python tools/check_encoding.py
python tools/check_clusters.py
```

Результаты:

- `build_index.py`: OK, записан `index/generated.json`, 386 cards.
- `build_viewer.py`: OK, записан `viewer/index.html`.
- `validate.py`: OK, 386 cards, 567 relations, 41 sources.
- `check_links.py`: OK, links are consistent.
- `audit_rules.py`: OK, 0 warnings.
- `check_encoding.py`: OK, UTF-8 без очевидных mojibake-маркеров.
- `check_clusters.py`: OK, 33 task clusters.
