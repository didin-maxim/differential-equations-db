# Homepage Navigation And AI Credit

Дата: 2026-05-27.

## Что смотрел в соседних базах

- `C:\Users\Admin\Documents\Codex\graph-db\viewer\index.html`: отдельный режим главной страницы через `#home`, рабочие кнопки перехода к задачам/определениям/идеям/комментариям, компактная заметка о роли ИИ в создании и классификации материалов.
- `C:\Users\Admin\Documents\Codex\incomplete-info-db\viewer\index.html`: рабочая главная с кнопками, которые выставляют реальные фильтры и режимы (`Все задачи`, `Кластеры`, фрагменты, интерактивы, отдельные кластеры), плюс сдержанный стиль без маркетингового лендинга.

Для базы дифференциальных уравнений выбран гибрид: отдельный корневой `index.html` как рабочая главная и параметры `viewer/index.html?nav=...`, которые переводят существующий viewer в нужный режим без поломки просмотра карточек.

## Что изменено

- `tools/build_viewer.py`
  - добавлена генерация отдельной корневой главной страницы `index.html`;
  - добавлены навигационные ссылки на `viewer/index.html?nav=cards|clusters|exam|theory|problems|sources|difficulty`;
  - viewer научен читать параметр `nav` и выставлять реальные состояния фильтров/режимов;
  - в быстрые режимы viewer добавлены `Задачи`, `Источники и авторы`, `Сложности и метки`;
  - для источников/авторов и сложностей/меток добавлены рабочие панели с chips, которые выставляют те же фильтры, что и левая панель;
  - поведение reveal-блоков карточек не менялось.
- `index.html`
  - пересоздан штатно через `python tools/build_viewer.py`;
  - теперь это отдельная главная страница, а не редирект;
  - добавлена формулировка: база создана при активном участии ИИ; промптил, отбирал материалы и содержательно направлял работу М. Дидин.
- `viewer/index.html`
  - пересоздан штатно через `python tools/build_viewer.py`.
- `index/generated.json`
  - пересоздан штатно через `python tools/build_index.py`.
- `docs/reviews/homepage-navigation-ai-credit.md`
  - этот отчёт.

## Как проверял

Команды:

```powershell
python tools\build_index.py
python tools\build_viewer.py
python tools\validate.py
python tools\check_links.py
python tools\check_encoding.py
node -e "const fs=require('fs'), vm=require('vm'); const html=fs.readFileSync('viewer/index.html','utf8'); const scripts=[...html.matchAll(/<script(?![^>]*application\/json)[^>]*>([\s\S]*?)<\/script>/g)].map(m=>m[1]); scripts.forEach((s,i)=>new vm.Script(s,{filename:'viewer-script-'+i+'.js'})); const home=fs.readFileSync('index.html','utf8'); if(!home.includes('База создана при активном участии ИИ')) throw new Error('AI credit missing'); console.log('JS syntax OK; scripts:', scripts.length);"
```

Результаты:

- `build_index.py`: `OK`, 386 карточек.
- `build_viewer.py`: `OK`, записаны `viewer/index.html` и `index.html`.
- `validate.py`: `OK`, 386 карточек, 579 связей, 41 источник.
- `check_links.py`: `OK`.
- `check_encoding.py`: `OK`.
- JS sanity check: `JS syntax OK; scripts: 3`.

Браузерная проверка на `http://127.0.0.1:8772/`:

- главная открывается с заголовком `База по дифференциальным уравнениям`, семь навигационных ссылок ведут на `viewer/index.html?nav=...`, AI-credit присутствует;
- клик по `Кластеры` открыл `viewer/index.html?nav=clusters`, активный фильтр стал `Режим: Кластеры`, раскрытых `details` было `0`;
- клик по кластерному chip `Существование, единственность и продолжение решений` выставил `cluster=existence-uniqueness-continuation` и сузил выдачу до 40 карточек;
- `nav=exam` показал активную экзаменационную панель, после клика `Начать симуляцию` появился экзаменационный вопрос, список карточек остался скрытым, раскрытых `details` было `0`;
- `nav=theory` дал режим `Теория` и 63 карточки;
- `nav=problems` дал режим `Задачи` и 323 карточки;
- `nav=sources` показал панель источников/авторов с 12 source-chips и 4 author-chips;
- `nav=difficulty` показал панель сложностей/меток с 5 score-chips и 16 tag-chips;
- поиск проверен запросами `Коши`, `линейная`, `матрица`, `Штурм`, `Пикара`; выдача сужалась, например `Коши` дал 90 карточек, `линейная` - 41.

Исходное состояние подсказок и решений сохранено: во всех проверенных режимах до ручного раскрытия `details[open]` было `0`.
