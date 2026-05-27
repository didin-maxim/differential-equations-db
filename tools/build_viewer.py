import json
from html import escape as html_escape

from build_index import COURSE_TAGS, build_data
from lib import ROOT


def safe_json(data):
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def esc_html(value):
    return html_escape(str(value or ""), quote=True)


def card_kind(card):
    return card.get("kind") or ""


def has_any_tag(card, tags):
    return bool(set(card.get("tags") or []) & set(tags))


def is_theory_card(card):
    return card_kind(card) in {"theorem", "lemma", "definition", "corollary"} or has_any_tag(
        card, {"theory_assignment", "standard_theory"}
    )


def is_cluster_card(card):
    return bool(card.get("cluster_ids")) or has_any_tag(card, {"cluster_representative", "task_cluster"})


def build_home_html(data):
    cards = data.get("cards") or []
    sources = data.get("sources") or []
    definitions = data.get("definitions") or []
    clusters = data.get("task_clusters") or []
    standard_ideas = data.get("standard_ideas") or []
    relations = data.get("relations") or []
    problem_count = sum(1 for card in cards if card_kind(card) == "problem")
    theory_count = sum(1 for card in cards if is_theory_card(card))
    cluster_card_count = sum(1 for card in cards if is_cluster_card(card))
    public_ready_count = sum(1 for card in cards if card.get("public_ready"))
    tag_count = len({tag for card in cards for tag in (card.get("tags") or [])})
    cluster_task_counts = {
        cluster.get("id"): sum(
            1
            for card in cards
            if card_kind(card) == "problem" and cluster.get("id") in (card.get("cluster_ids") or [])
        )
        for cluster in clusters
    }
    cluster_links_html = "\n".join(
        f"""
        <a class="cluster-link" href="viewer/index.html?nav=clusters&cluster={esc_html(cluster.get('id'))}">
          <strong>{esc_html(cluster.get('title') or cluster.get('title_ru') or cluster.get('id'))}</strong>
          <span>{cluster_task_counts.get(cluster.get('id'), 0)} задач</span>
        </a>"""
        for cluster in sorted(clusters, key=lambda item: str(item.get("title") or item.get("id")))
    )
    hrefs = {
        "cards": "viewer/index.html?nav=cards",
        "clusters": "viewer/index.html?nav=clusters",
        "exam": "viewer/index.html?nav=exam",
        "theory": "viewer/index.html?nav=theory",
        "definitions": "viewer/index.html?nav=definitions",
        "problems": "viewer/index.html?nav=problems",
        "sources": "viewer/index.html?nav=sources",
        "difficulty": "viewer/index.html?nav=difficulty",
    }
    optional_entries = []
    if definitions:
        optional_entries.append(
            f"""
        <a class="entry compact" href="{hrefs['definitions']}">
          <span class="entry-kicker">Справочник</span>
          <strong>Определения</strong>
          <span>Термины и связанные с ними карточки.</span>
          <em>{len(definitions)} определений</em>
        </a>"""
        )
    if sources:
        optional_entries.append(
            f"""
        <a class="entry compact" href="{hrefs['sources']}">
          <span class="entry-kicker">Библиография</span>
          <strong>Источники и авторы</strong>
          <span>Учебники, листки, экзамены и привязки к авторам.</span>
          <em>{len(sources)} источников</em>
        </a>"""
        )
    optional_entries_html = "".join(optional_entries)
    page = f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>База по дифференциальным уравнениям</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f6f4ee;
      --panel: #ffffff;
      --ink: #202522;
      --muted: #65716d;
      --line: #d8d5ca;
      --accent: #176b5f;
      --accent-dark: #0f4039;
      --soft: #e7f3ef;
      --soft-2: #eef0df;
      --warn: #fff4d6;
    }}

    * {{ box-sizing: border-box; }}

    html, body {{
      max-width: 100%;
      overflow-x: clip;
    }}

    body {{
      margin: 0;
      font-family: "Segoe UI", Arial, sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.5;
    }}

    a {{ color: inherit; }}

    input, button {{ font: inherit; }}

    .page {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 24px clamp(16px, 4vw, 42px) 48px;
    }}

    header {{
      border-bottom: 1px solid var(--line);
      padding: 10px 0 24px;
    }}

    .topline {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 12px;
    }}

    .pill {{
      display: inline-flex;
      align-items: center;
      min-height: 25px;
      border-radius: 999px;
      padding: 3px 9px;
      background: #ece8dd;
      color: #303835;
      font-size: 13px;
    }}

    .layout {{
      display: grid;
      grid-template-columns: minmax(0, 1.15fr) minmax(310px, 0.85fr);
      gap: clamp(20px, 4vw, 40px);
      align-items: start;
    }}

    h1 {{
      margin: 0;
      font-size: clamp(34px, 6vw, 58px);
      line-height: 1.04;
      letter-spacing: 0;
    }}

    .lead {{
      max-width: 820px;
      margin: 12px 0 0;
      color: #42504b;
      font-size: 18px;
    }}

    .search-panel {{
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      padding: 16px;
      box-shadow: 0 10px 30px rgba(32, 37, 34, 0.06);
    }}

    .search-panel h2 {{
      margin: 0 0 10px;
      font-size: 20px;
      line-height: 1.2;
      letter-spacing: 0;
    }}

    .search-form {{
      display: grid;
      gap: 10px;
    }}

    .search-row {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 8px;
    }}

    .search-row input {{
      min-width: 0;
      min-height: 44px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--ink);
      padding: 9px 11px;
    }}

    .button, .action {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 40px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--ink);
      padding: 8px 12px;
      text-decoration: none;
      cursor: pointer;
    }}

    .button.primary, .action.primary {{
      background: var(--accent-dark);
      border-color: var(--accent-dark);
      color: #fff;
    }}

    .hint {{
      margin: 0;
      color: var(--muted);
      font-size: 13px;
    }}

    .actions, .quick-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 9px;
      margin-top: 18px;
    }}

    .quick-links {{
      margin-top: 12px;
    }}

    .quick-links a {{
      border-bottom: 1px solid rgba(23, 107, 95, 0.45);
      color: var(--accent-dark);
      font-size: 13px;
      text-decoration: none;
    }}

    .entry-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
      margin-top: 18px;
    }}

    .entry {{
      display: flex;
      flex-direction: column;
      min-height: 180px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      padding: 16px;
      text-decoration: none;
      transition: border-color 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease;
    }}

    .entry:hover {{
      border-color: #9acfc4;
      box-shadow: 0 10px 24px rgba(32, 37, 34, 0.08);
      transform: translateY(-1px);
    }}

    .entry.primary {{
      background: var(--soft);
      border-color: #b9d9d1;
    }}

    .entry.compact {{
      min-height: 145px;
      background: #fbfaf7;
    }}

    .entry-kicker {{
      color: var(--accent-dark);
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
    }}

    .entry strong {{
      display: block;
      margin-top: 8px;
      font-size: 22px;
      line-height: 1.15;
    }}

    .entry span:not(.entry-kicker) {{
      margin-top: 9px;
      color: var(--muted);
      font-size: 14px;
    }}

    .entry em {{
      margin-top: auto;
      color: #3b4945;
      font-size: 13px;
      font-style: normal;
      font-weight: 650;
    }}

    .stats {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 10px;
      margin-top: 18px;
    }}

    .stat {{
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfaf7;
      padding: 12px;
    }}

    .stat strong {{
      display: block;
      font-size: 24px;
      line-height: 1.1;
    }}

    .stat span {{
      color: var(--muted);
      font-size: 13px;
    }}

    .band {{
      padding-top: 26px;
    }}

    h2 {{
      margin: 0 0 10px;
      font-size: 20px;
      line-height: 1.2;
      letter-spacing: 0;
    }}

    .note {{
      max-width: 930px;
      border-left: 4px solid #d5a021;
      border-radius: 0 8px 8px 0;
      background: var(--warn);
      color: #51431f;
      padding: 12px 14px;
      margin: 0;
    }}

    .section-head {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 10px;
    }}

    .section-head h2 {{
      margin: 0;
    }}

    .section-head a {{
      color: var(--accent-dark);
      font-size: 14px;
      font-weight: 650;
      text-decoration: none;
    }}

    .cluster-links {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 8px;
    }}

    .cluster-link {{
      display: flex;
      justify-content: space-between;
      gap: 10px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fff;
      padding: 10px 11px;
      text-decoration: none;
      min-height: 56px;
    }}

    .cluster-link:hover {{
      border-color: #9acfc4;
      background: var(--soft);
    }}

    .cluster-link strong {{
      font-size: 14px;
      line-height: 1.25;
    }}

    .cluster-link span {{
      flex: 0 0 auto;
      color: var(--muted);
      font-size: 12px;
      white-space: nowrap;
    }}

    @media (max-width: 900px) {{
      .layout {{ grid-template-columns: 1fr; }}
      .entry-grid {{ grid-template-columns: 1fr 1fr; }}
      .stats {{ grid-template-columns: 1fr 1fr; }}
      .lead {{ font-size: 16px; }}
    }}

    @media (max-width: 480px) {{
      .page {{ padding: 16px 12px 34px; }}
      .entry-grid, .stats, .search-row {{ grid-template-columns: 1fr; }}
      .action {{ width: 100%; justify-content: center; }}
      .button {{ width: 100%; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <header>
      <div class="layout">
        <div>
          <div class="topline">
            <span class="pill">{len(cards)} карточек</span>
            <span class="pill">{problem_count} задач</span>
            <span class="pill">{len(clusters)} кластеров</span>
            {f'<span class="pill">{len(definitions)} определений</span>' if definitions else ''}
            {f'<span class="pill">{len(sources)} источников</span>' if sources else ''}
          </div>
          <h1>База по дифференциальным уравнениям</h1>
          <p class="lead">Навигационная стартовая страница для поиска по базе, перехода к режимам просмотра, кластерам задач, определениям, источникам и симуляции устного экзамена.</p>
          <div class="actions" aria-label="Основная навигация">
            <a class="action primary" href="{hrefs['cards']}">Открыть режим просмотра</a>
            <a class="action" href="{hrefs['clusters']}">Кластеры</a>
            <a class="action" href="{hrefs['exam']}">Симуляция экзамена</a>
          </div>
        </div>
        <aside class="search-panel" aria-label="Поиск по базе">
          <h2>Найти в базе</h2>
          <form class="search-form" action="viewer/index.html" method="get">
            <input type="hidden" name="nav" value="search">
            <div class="search-row">
              <input name="q" type="search" autocomplete="off" placeholder="Например: Риккати, устойчивость, Лаплас">
              <button class="button primary" type="submit">Искать</button>
            </div>
            <p class="hint">Поиск откроется во viewer вместе с фильтрами, сортировкой и карточками результатов.</p>
          </form>
          <div class="quick-links" aria-label="Быстрые ссылки поиска">
            <a href="viewer/index.html?nav=search&q=Риккати">Риккати</a>
            <a href="viewer/index.html?nav=search&q=устойчивость">устойчивость</a>
            <a href="viewer/index.html?nav=search&q=Лаплас">Лаплас</a>
          </div>
        </aside>
      </div>
    </header>

    <section class="band">
      <div class="section-head">
        <h2>Входы в базу</h2>
        <a href="{hrefs['cards']}">Все фильтры</a>
      </div>
      <div class="entry-grid">
        <a class="entry primary" href="{hrefs['cards']}">
          <span class="entry-kicker">Поиск и просмотр</span>
          <strong>Viewer базы</strong>
          <span>Полный список с поиском, фильтрами, сортировкой, идеями и решениями.</span>
          <em>{len(cards)} карточек</em>
        </a>
        <a class="entry" href="{hrefs['clusters']}">
          <span class="entry-kicker">Методы</span>
          <strong>Кластеры задач</strong>
          <span>Группы похожих приемов, маршруты и стандартные идеи.</span>
          <em>{len(clusters)} кластеров</em>
        </a>
        <a class="entry" href="{hrefs['exam']}">
          <span class="entry-kicker">Тренировка</span>
          <strong>Симуляция экзамена</strong>
          <span>Адаптивные вопросы без показа списка карточек во время ответа.</span>
          <em>режим проверки</em>
        </a>
        <a class="entry compact" href="{hrefs['problems']}">
          <span class="entry-kicker">Практика</span>
          <strong>Задачи</strong>
          <span>Фильтр по задачам без теоретических карточек.</span>
          <em>{problem_count} задач</em>
        </a>
        <a class="entry compact" href="{hrefs['theory']}">
          <span class="entry-kicker">Теория</span>
          <strong>Теоретические карточки</strong>
          <span>Теоремы, леммы, следствия и определения.</span>
          <em>{theory_count} карточек</em>
        </a>
        <a class="entry compact" href="{hrefs['difficulty']}">
          <span class="entry-kicker">Отбор</span>
          <strong>Сложности и метки</strong>
          <span>Уровни, теги, курс и готовность к публикации.</span>
          <em>{tag_count} меток</em>
        </a>{optional_entries_html}
      </div>
    </section>

    <section class="band">
      <div class="section-head">
        <h2>Все кластеры</h2>
        <a href="{hrefs['clusters']}">Открыть каталог</a>
      </div>
      <div class="cluster-links" aria-label="Главные страницы кластеров">
        {cluster_links_html}
      </div>
    </section>

    <section class="band">
      <h2>Сводка</h2>
      <div class="stats" aria-label="Сводка базы">
        <div class="stat"><strong>{len(cards)}</strong><span>карточек всего</span></div>
        <div class="stat"><strong>{public_ready_count}</strong><span>готово к публикации</span></div>
        <div class="stat"><strong>{cluster_card_count}</strong><span>карточек в кластерах</span></div>
        <div class="stat"><strong>{len(relations)}</strong><span>связей</span></div>
        <div class="stat"><strong>{len(definitions)}</strong><span>определений</span></div>
        <div class="stat"><strong>{len(standard_ideas)}</strong><span>стандартных идей</span></div>
        <div class="stat"><strong>{len(sources)}</strong><span>источников</span></div>
        <div class="stat"><strong>{tag_count}</strong><span>меток</span></div>
      </div>
    </section>

    <section class="band">
      <h2>Роль ИИ</h2>
      <p class="note">База создана при активном участии ИИ: он помогал извлекать, нормализовать и связывать карточки, готовить черновики решений и пометки. Промптил, отбирал материалы и содержательно направлял работу М. Дидин.</p>
    </section>
  </div>
</body>
</html>
"""
    return page


def build_html(data):
    payload = safe_json(data)
    course_tags = safe_json(COURSE_TAGS)
    page = """<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>База по дифференциальным уравнениям</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js"></script>
  <style>
    :root {
      color-scheme: light;
      --bg: #f5f4ef;
      --panel: #ffffff;
      --sidebar: #fbfaf7;
      --ink: #202522;
      --muted: #65716d;
      --line: #d8d5ca;
      --accent: #176b5f;
      --accent-dark: #0f4039;
      --soft: #e7f3ef;
      --warn: #fff4d6;
      --bad: #ffe5e0;
      --good: #e4f5e7;
    }

    * { box-sizing: border-box; }

    html, body {
      max-width: 100%;
      overflow-x: clip;
    }

    body {
      margin: 0;
      font-family: "Segoe UI", Arial, sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.45;
    }

    button, input, select { font: inherit; }

    .shell {
      display: grid;
      grid-template-columns: minmax(320px, 390px) minmax(0, 1fr);
      min-height: 100vh;
    }

    aside {
      position: sticky;
      top: 0;
      height: 100vh;
      overflow: auto;
      background: var(--sidebar);
      border-right: 1px solid var(--line);
      padding: 16px;
    }

    main {
      min-width: 0;
      padding: 18px clamp(16px, 3vw, 34px) 48px;
    }

    h1 {
      margin: 0;
      font-size: 22px;
      line-height: 1.15;
      letter-spacing: 0;
    }

    h2 {
      margin: 0 0 8px;
      font-size: 19px;
      line-height: 1.2;
      letter-spacing: 0;
    }

    h3 {
      margin: 18px 0 8px;
      font-size: 14px;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: .04em;
    }

    .db-meta {
      margin-top: 6px;
      color: var(--muted);
      font-size: 13px;
    }

    .filters {
      display: grid;
      gap: 9px;
      margin-top: 14px;
    }

    .filter-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }

    label {
      display: grid;
      gap: 4px;
      color: var(--muted);
      font-size: 12px;
    }

    input, select {
      width: 100%;
      min-height: 36px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--ink);
      padding: 7px 9px;
    }

    select[multiple] {
      min-height: 82px;
      padding: 4px;
    }

    select[multiple] option {
      padding: 3px 5px;
    }

    .toolbar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 14px;
    }

    .summary {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }

    .button {
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--ink);
      min-height: 36px;
      padding: 7px 10px;
      cursor: pointer;
    }

    .button.primary {
      background: var(--accent-dark);
      border-color: var(--accent-dark);
      color: #fff;
    }

    .pill, .chip {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      min-height: 24px;
      max-width: 100%;
      border-radius: 999px;
      padding: 3px 8px;
      background: #ece8dd;
      color: #303835;
      font-size: 12px;
      line-height: 1.25;
      text-decoration: none;
      overflow-wrap: anywhere;
      word-break: break-word;
    }

    .pill.good { background: var(--good); }
    .pill.warn { background: var(--warn); }
    .pill.bad { background: var(--bad); }
    .pill.code { font-family: Consolas, "Cascadia Mono", monospace; }

    .chip {
      border: 1px solid var(--line);
      background: #fff;
      cursor: pointer;
      text-align: left;
      white-space: normal;
    }

    .pill > span, .chip > span {
      min-width: 0;
      overflow-wrap: anywhere;
    }

    .chip.active {
      background: var(--soft);
      border-color: #9acfc4;
      color: var(--accent-dark);
      font-weight: 650;
    }

    .chip.good {
      background: var(--good);
    }

    .chip-count {
      color: var(--muted);
      font-variant-numeric: tabular-nums;
    }

    .facet-panel {
      border-top: 1px solid var(--line);
      padding-top: 10px;
      margin-top: 12px;
    }

    .facet-title {
      color: var(--muted);
      font-size: 12px;
      margin-bottom: 7px;
      display: flex;
      justify-content: space-between;
      gap: 8px;
    }

    .chip-row {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }

    .active-filters {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 10px;
    }

    .active-filters:empty {
      display: none;
    }

    .top-active-filters {
      margin: 0 0 12px;
    }

    .study-home {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 14px;
      overflow-wrap: anywhere;
    }

    .study-home h2 {
      margin-bottom: 6px;
    }

    .study-lead {
      margin: 0 0 12px;
      color: var(--muted);
      max-width: 78ch;
    }

    .quick-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 10px;
    }

    .quick-button {
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--ink);
      min-height: 36px;
      max-width: 100%;
      padding: 7px 10px;
      cursor: pointer;
      overflow-wrap: anywhere;
    }

    .quick-button.active {
      background: var(--soft);
      border-color: #9acfc4;
      color: var(--accent-dark);
      font-weight: 650;
    }

    .home-directory {
      border-top: 1px solid var(--line);
      margin-top: 14px;
      padding-top: 12px;
    }

    .home-directory h3 {
      margin-top: 0;
    }

    .home-directory-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
    }

    .home-note {
      margin: 10px 0 0;
      color: var(--muted);
      font-size: 13px;
      max-width: 86ch;
    }

    .cluster-dashboard {
      border-top: 1px solid var(--line);
      margin-top: 14px;
      padding-top: 12px;
      display: grid;
      gap: 12px;
    }

    .cluster-focus {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfaf7;
      padding: 12px;
      display: grid;
      gap: 10px;
    }

    .cluster-focus h3,
    .cluster-directory h3,
    .cluster-filter-block h3 {
      margin: 0 0 7px;
    }

    .cluster-filter-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 10px;
    }

    .cluster-task-list {
      display: grid;
      gap: 7px;
    }

    .cluster-task-wrap {
      display: grid;
      gap: 4px;
      align-content: start;
    }

    .cluster-task-list.prominent {
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    }

    .cluster-task {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--ink);
      padding: 8px 9px;
      text-align: left;
      cursor: pointer;
      min-height: 58px;
    }

    .cluster-task:hover {
      border-color: #9acfc4;
      background: var(--soft);
    }

    .cluster-task-title {
      display: block;
      font-weight: 650;
    }

    .cluster-task-meta {
      display: block;
      margin-top: 4px;
      color: var(--muted);
      font-size: 12px;
    }

    .cluster-back-link {
      color: var(--accent-dark);
      font-size: 12px;
      font-weight: 650;
      text-decoration: none;
    }

    .cluster-back-link:hover {
      text-decoration: underline;
    }

    .task-link {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--ink);
      padding: 9px 10px;
      text-align: left;
      cursor: pointer;
      min-height: 58px;
    }

    .task-link:hover {
      border-color: #9acfc4;
      background: var(--soft);
    }

    .task-link-title {
      display: block;
      font-weight: 650;
    }

    .task-link-meta {
      display: block;
      margin-top: 4px;
      color: var(--muted);
      font-size: 12px;
    }

    .cluster-directory-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 8px;
    }

    .cluster-card {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fff;
      padding: 10px;
      display: grid;
      gap: 8px;
    }

    .cluster-card-title {
      font-weight: 700;
    }

    .cluster-guide-strip {
      display: grid;
      gap: 7px;
    }

    .cluster-guide-strip details,
    .method-guide-compact details {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fff;
      padding: 8px 10px;
    }

    .home-stats {
      display: grid;
      grid-template-columns: repeat(4, minmax(120px, 1fr));
      gap: 8px;
      margin-top: 12px;
    }

    .home-stat {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfaf7;
      padding: 10px;
    }

    .home-stat strong {
      display: block;
      font-size: 20px;
      line-height: 1.1;
    }

    .home-stat span {
      color: var(--muted);
      font-size: 12px;
    }

    .exam-panel {
      display: none;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 14px;
      overflow-wrap: anywhere;
    }

    .exam-panel.active {
      display: block;
    }

    .exam-controls {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: end;
      margin-top: 12px;
    }

    .exam-controls label {
      min-width: 180px;
    }

    .exam-status {
      display: grid;
      grid-template-columns: repeat(4, minmax(120px, 1fr));
      gap: 8px;
      margin-top: 12px;
    }

    .exam-question {
      border-top: 1px solid var(--line);
      margin-top: 12px;
      padding-top: 12px;
    }

    .exam-answer-area {
      display: grid;
      gap: 8px;
      margin-top: 10px;
      max-width: 760px;
    }

    .exam-choice-row {
      display: grid;
      gap: 7px;
    }

    .exam-choice {
      justify-content: flex-start;
      text-align: left;
      white-space: normal;
    }

    .exam-choice.selected {
      background: var(--soft);
      border-color: #9acfc4;
      color: var(--accent-dark);
      font-weight: 650;
    }

    .exam-feedback {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfaf7;
      padding: 10px;
      margin-top: 10px;
    }

    .exam-feedback.good {
      background: var(--good);
    }

    .exam-feedback.bad {
      background: var(--bad);
    }

    .exam-source-link {
      margin-top: 8px;
    }

    .result-grid {
      display: grid;
      gap: 11px;
      min-width: 0;
    }

    .card {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      overflow-wrap: anywhere;
    }

    .card.clickable-card {
      cursor: pointer;
      transition: border-color .15s ease, box-shadow .15s ease;
    }

    .card.clickable-card:hover {
      border-color: #9acfc4;
      box-shadow: 0 6px 18px rgba(15, 64, 57, .08);
    }

    .card-head {
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: flex-start;
    }

    .card-title {
      min-width: 0;
      max-width: 100%;
    }

    .meta-row {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 8px;
    }

    .single-card-nav {
      display: grid;
      gap: 10px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfaf7;
      padding: 12px;
      margin-bottom: 12px;
    }

    .single-card-nav h2 {
      margin: 0;
      font-size: 17px;
    }

    .single-card-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }

    .related-card-list {
      display: grid;
      gap: 7px;
    }

    .related-card-link {
      display: grid;
      gap: 3px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--ink);
      padding: 8px 9px;
      text-decoration: none;
    }

    .related-card-link:hover {
      border-color: #9acfc4;
      background: var(--soft);
    }

    .related-card-title {
      font-weight: 650;
    }

    .related-card-meta {
      color: var(--muted);
      font-size: 12px;
    }

    .method-route {
      border-top: 1px solid var(--line);
      margin-top: 12px;
      padding-top: 10px;
    }

    .method-route h3 {
      margin: 0 0 8px;
      font-size: 15px;
    }

    .route-columns {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 8px;
    }

    .route-column {
      min-width: 0;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 8px;
      background: #fbfaf6;
    }

    .route-column h4 {
      margin: 0 0 6px;
      font-size: 13px;
    }

    .route-task-list {
      display: grid;
      gap: 6px;
    }

    .route-task {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--text);
      padding: 7px 8px;
      text-align: left;
      cursor: pointer;
    }

    .route-task:hover {
      border-color: #9acfc4;
      background: var(--soft);
    }

    .route-task-title {
      display: block;
      font-weight: 650;
      overflow-wrap: anywhere;
    }

    .route-task-meta {
      display: block;
      margin-top: 3px;
      color: var(--muted);
      font-size: 12px;
    }

    .statement {
      margin: 10px 0 0;
      color: #2f3935;
      white-space: pre-wrap;
      max-width: 100%;
      overflow-wrap: anywhere;
      word-break: break-word;
    }

    .tex-content {
      max-width: 100%;
      min-width: 0;
      overflow-wrap: anywhere;
    }

    .tex-content .katex-display {
      overflow-x: auto;
      overflow-y: hidden;
      padding: 2px 0;
    }

    .tex-content .katex {
      max-width: 100%;
      font-size: 1.03em;
    }

    .tex-fallback {
      display: inline-block;
      max-width: 100%;
      overflow-x: auto;
      vertical-align: baseline;
      font-family: Cambria Math, "Times New Roman", serif;
      font-size: 1.04em;
      background: #fbfaf7;
      border: 1px solid #e5e0d2;
      border-radius: 4px;
      padding: 0 4px;
    }

    .tex-fallback.display {
      display: block;
      margin: 8px 0;
      padding: 6px 8px;
    }

    .reveal {
      border-top: 1px solid var(--line);
      margin-top: 12px;
      padding-top: 8px;
    }

    .reveal > summary {
      display: inline-flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 7px;
      list-style: none;
      border: 1px solid #9acfc4;
      border-radius: 6px;
      background: var(--soft);
      color: var(--accent-dark);
      min-height: 34px;
      max-width: 100%;
      padding: 6px 10px;
      cursor: pointer;
      font-weight: 650;
      white-space: normal;
    }

    .reveal > summary::-webkit-details-marker { display: none; }
    .reveal[open] .show-label { display: none; }
    .reveal:not([open]) .hide-label { display: none; }

    .asset-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(220px, 100%), 1fr));
      gap: 10px;
      margin-top: 12px;
    }

    .asset-card {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfaf7;
      padding: 8px;
    }

    .asset-card img {
      display: block;
      width: 100%;
      max-height: 280px;
      object-fit: contain;
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 6px;
    }

    .asset-caption {
      margin-top: 6px;
      color: var(--muted);
      font-size: 12px;
      overflow-wrap: anywhere;
    }

    .block {
      white-space: pre-wrap;
      overflow-wrap: anywhere;
      word-break: break-word;
      margin: 8px 0 0;
    }

    .empty {
      color: var(--muted);
      font-style: italic;
      padding: 18px;
      border: 1px dashed var(--line);
      border-radius: 8px;
      background: #fff;
      overflow-wrap: anywhere;
    }

    .muted { color: var(--muted); }
    .compact { font-size: 13px; }

    body.single-card-route .shell {
      display: block;
      min-height: 100vh;
    }

    body.single-card-route aside {
      display: none;
    }

    body.single-card-route main {
      width: min(1120px, 100%);
      margin: 0 auto;
    }

    @media (max-width: 860px) {
      .shell { grid-template-columns: 1fr; }
      aside {
        position: static;
        height: auto;
        border-right: 0;
        border-bottom: 1px solid var(--line);
      }
      .filter-grid { grid-template-columns: 1fr; }
      .card-head { display: block; }
      .home-stats { grid-template-columns: 1fr 1fr; }
      .home-directory-grid { grid-template-columns: 1fr; }
      .cluster-filter-grid { grid-template-columns: 1fr; }
      .route-columns { grid-template-columns: 1fr; }
      .exam-status { grid-template-columns: 1fr 1fr; }
      .toolbar { display: block; }
      .toolbar label { margin-top: 10px; }
    }

    @media (max-width: 480px) {
      aside { padding: 12px; }
      main { padding: 12px 12px 36px; }
      h1 { font-size: 20px; }
      h2 { font-size: 17px; }
      .study-home, .card { padding: 12px; }
      .home-stats { grid-template-columns: 1fr; }
      .exam-panel { padding: 12px; }
      .exam-status { grid-template-columns: 1fr; }
      .exam-controls { display: grid; }
      .asset-grid { grid-template-columns: minmax(0, 1fr); }
      .pill, .chip, .quick-button { font-size: 11px; }
    }
  </style>
</head>
<body>
  <div class="shell">
    <aside>
      <h1>Дифференциальные уравнения</h1>
      <div class="db-meta" id="db-meta"></div>

      <div class="filters">
        <label>Поиск
          <input id="q" type="search" placeholder="текст, id, метод, источник">
        </label>

        <div class="filter-grid">
          <label>Идейная сложность
            <select id="idea-score"></select>
          </label>
          <label>Техническая сложность
            <select id="technical-score"></select>
          </label>
        </div>

        <div class="filter-grid">
          <label>Уровень по баллам
            <select id="score-range"></select>
          </label>
          <label>Олимпиадность
            <select id="exclude-olympiad"></select>
          </label>
        </div>

        <label>Материалы
          <select id="asset-filter"></select>
        </label>

        <label>Источник
          <select id="source"></select>
        </label>
        <label>Автор / создатель
          <select id="author"></select>
        </label>
        <label>Кластер
          <select id="cluster"></select>
        </label>
        <label>Стандартная идея
          <select id="standard-idea"></select>
        </label>
        <label>Определения
          <select id="definition"></select>
        </label>
        <label>Тег
          <select id="tag"></select>
        </label>

        <div class="filter-grid">
          <label>Тип
            <select id="kind"></select>
          </label>
          <label>Курс
            <select id="course"></select>
          </label>
        </div>

        <div class="filter-grid">
          <label>Готовность
            <select id="public-ready"></select>
          </label>
          <label>Статус проверки
            <select id="review-status"></select>
          </label>
        </div>

        <label>Сложность
          <select id="difficulty-main"></select>
        </label>

        <button class="button primary" id="reset" type="button">Сбросить фильтры</button>
      </div>

      <div class="active-filters" id="active-filters"></div>
      <div id="facets"></div>
    </aside>

    <main>
      <div class="toolbar">
        <div class="summary" id="summary"></div>
        <label class="compact">Сортировка
          <select id="sort">
            <option value="title">Название</option>
            <option value="difficulty_asc">Идея и техника ↑</option>
            <option value="idea_asc">Идейная сложность ↑</option>
            <option value="idea_desc">Идейная сложность ↓</option>
            <option value="technical_asc">Техническая сложность ↑</option>
            <option value="technical_desc">Техническая сложность ↓</option>
            <option value="kind">Тип</option>
          </select>
        </label>
      </div>
      <div class="active-filters top-active-filters" id="top-active-filters"></div>
      <section class="study-home" id="study-home"></section>
      <section class="exam-panel" id="exam-panel"></section>
      <div class="result-grid" id="results"></div>
    </main>
  </div>

  <script id="db-data" type="application/json">__PAYLOAD__</script>
  <script>
    const DB = JSON.parse(document.getElementById('db-data').textContent);
    const COURSE_TAGS = __COURSE_TAGS__;
    const cards = DB.cards || [];
    const cardsById = Object.fromEntries(cards.map(card => [card.id, card]));
    const problemsById = Object.fromEntries((DB.problems || []).map(problem => [problem.id, problem]));
    const sourceById = Object.fromEntries((DB.sources || []).map(item => [item.id, item]));
    const ideaById = Object.fromEntries((DB.standard_ideas || []).map(item => [item.id, item]));
    const clusterById = Object.fromEntries((DB.task_clusters || []).map(item => [item.id, item]));
    const definitionById = Object.fromEntries((DB.definitions || []).map(item => [item.id, item]));
    const definitionLabelById = Object.fromEntries((DB.definitions || []).map(item => [item.id, item.title || item.id]));
    for (const card of cards) {
      (card.definition_ids || []).forEach((id, index) => {
        if (!definitionLabelById[id] && (card.definition_labels || [])[index]) {
          definitionLabelById[id] = card.definition_labels[index];
        }
      });
    }

    const state = {
      view: 'home',
      activeCluster: '',
      activeCard: '',
      q: '',
      studyMode: 'all',
      ideaScore: 'all',
      technicalScore: 'all',
      scoreRange: 'all',
      excludeOlympiad: 'all',
      assetFilter: 'all',
      source: [],
      author: 'all',
      cluster: [],
      standardIdea: [],
      definition: 'all',
      tag: 'all',
      kind: 'all',
      course: 'all',
      publicReady: 'all',
      reviewStatus: 'all',
      difficultyMain: [],
      sort: 'title'
    };

    const navigation = {
      focus: '',
      cardId: ''
    };

    const examOverlay = DB.exam_simulation || {};
    const examQuestionOverlays = examOverlay.question_overlays || examOverlay.cards || [];
    const examCardOverlay = Object.fromEntries(examQuestionOverlays.map(item => [item.card_id || item.id, item]));
    const examMajorTopics = examOverlay.major_topics || [];
    const examTopicLabels = Object.fromEntries(examMajorTopics.map(item => [item.id, item.title || item.id]));
    const examState = {
      active: false,
      finished: false,
      failed: false,
      startLevel: 5,
      currentLevel: 5,
      selectedChoice: null,
      selectedChoices: [],
      current: null,
      history: [],
      usedIds: [],
      topicHistory: []
    };

    const filterKeys = [
      'studyMode', 'ideaScore', 'technicalScore', 'scoreRange', 'excludeOlympiad', 'assetFilter',
      'source', 'author', 'cluster', 'standardIdea', 'definition',
      'tag', 'kind', 'course', 'publicReady', 'reviewStatus', 'difficultyMain'
    ];

    const multiFilterKeys = new Set([
      'ideaScore', 'technicalScore', 'scoreRange', 'assetFilter',
      'source', 'author', 'cluster', 'standardIdea', 'definition',
      'tag', 'kind', 'course', 'publicReady', 'reviewStatus', 'difficultyMain'
    ]);

    const selectConfig = {
      studyMode: { label: 'Режим', all: 'Все карточки' },
      ideaScore: { id: 'idea-score', label: 'Идейная сложность', all: 'Любая идейная сложность' },
      technicalScore: { id: 'technical-score', label: 'Техническая сложность', all: 'Любая техническая сложность' },
      scoreRange: {
        id: 'score-range',
        label: 'Уровень по баллам',
        all: 'Любой уровень по баллам',
        values: ['easy', 'middle', 'exam_middle', 'strong', 'excellent']
      },
      excludeOlympiad: {
        id: 'exclude-olympiad',
        label: 'Олимпиадность',
        all: 'С олимпиадными',
        values: ['exclude']
      },
      assetFilter: {
        id: 'asset-filter',
        label: 'Материалы',
        all: 'Все карточки',
        values: ['has_image', 'no_image']
      },
      source: { id: 'source', label: 'Источник', all: 'Все источники' },
      author: { id: 'author', label: 'Автор', all: 'Все авторы' },
      cluster: { id: 'cluster', label: 'Кластер', all: 'Все кластеры' },
      standardIdea: { id: 'standard-idea', label: 'Идея', all: 'Все идеи' },
      definition: { id: 'definition', label: 'Определения', all: 'Все определения' },
      tag: { id: 'tag', label: 'Тег', all: 'Все теги' },
      kind: { id: 'kind', label: 'Тип', all: 'Все типы' },
      course: { id: 'course', label: 'Курс', all: 'Все уровни курса' },
      publicReady: { id: 'public-ready', label: 'Готовность', all: 'Любая готовность' },
      reviewStatus: { id: 'review-status', label: 'Статус проверки', all: 'Любой статус проверки' },
      difficultyMain: { id: 'difficulty-main', label: 'Сложность', all: 'Любая сложность' }
    };

    for (const key of multiFilterKeys) {
      if (selectConfig[key]) selectConfig[key].multi = true;
    }

    const kindLabels = {
      problem: 'задача',
      theorem: 'теорема',
      lemma: 'лемма',
      definition: 'определение',
      corollary: 'следствие'
    };

    const courseLabels = {
      standard_course_methods: 'методы стандартного курса',
      advanced_standard_course: 'продвинутый стандартный курс',
      beyond_standard_course: 'за пределами стандартного курса',
      uncategorized: 'уровень курса не указан'
    };

    const publicReadyLabels = {
      true: 'готово к публикации',
      false: 'требует проверки'
    };

    const reviewStatusLabels = {
      ai_checked: 'проверено агентом',
      needs_human_review: 'нужна ручная проверка',
      source_verified: 'источник проверен',
      draft: 'черновик',
      seed_links: 'заготовка связей'
    };

    const difficultyLabels = Object.fromEntries((DB.taxonomy?.difficulty || []).map(item => [item.id, item.title || item.id]));
    const fragmentLabels = Object.fromEntries((DB.taxonomy?.fragments || []).map(item => [item.id, item.title || item.id]));
    const relationTypeLabels = Object.fromEntries((DB.taxonomy?.relation_types || []).map(item => [item.id, item.title || item.id]));

    const quickModes = [
      { id: 'problems', label: 'Задачи' },
      { id: 'written_minimum', label: 'Письменный минимум' },
      { id: 'written_middle', label: 'Средний письменный' },
      { id: 'exam_middle', label: 'Средний экзамен' },
      { id: 'exam_simulation', label: 'Симуляция экзамена' },
      { id: 'written_strong', label: 'Сильный письменный' },
      { id: 'theory', label: 'Теория' },
      { id: 'definitions', label: 'Определения' },
      { id: 'clusters', label: 'Кластеры' },
      { id: 'sources_authors', label: 'Источники и авторы' },
      { id: 'difficulty_tags', label: 'Сложности и метки' },
      { id: 'no_olympiad', label: 'Без олимпиадных' }
    ];

    const rangeLabels = {
      easy: 'простые: идея/техника ≤ 4',
      middle: 'средние: идея 5-7, техника ≤ 6',
      exam_middle: 'экзамен 5-7: идея 5-7, техника 3-7',
      strong: 'сильные: идея 7-8',
      excellent: 'отлично: идея ≥ 8'
    };

    const assetLabels = {
      has_image: 'с рисунками',
      no_image: 'без рисунков'
    };

    function byId(id) {
      return document.getElementById(id);
    }

    function esc(value) {
      return String(value ?? '').replace(/[&<>"']/g, char => ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      })[char]);
    }

    function prettifyPlainMath(html) {
      return String(html)
        .replace(/-&gt;/g, '→')
        .replace(/&lt;=/g, '≤')
        .replace(/&gt;=/g, '≥')
        .replace(/(?<!\\\\)\\bpi\\b/g, 'π')
        .replace(/(?<!\\\\)\\binfty\\b/g, '∞')
        .replace(/\\+∞/g, '+∞')
        .replace(/-∞/g, '-∞');
    }

    function autoDelimitPlainMath(text) {
      const value = String(text ?? '');
      if (/\\\\\\(|\\\\\\[|\\$/.test(value)) return value;
      const patterns = [
        /(?:d\\/dt\\s*)?(?:det\\()?\\w*\\(?e\\^\\{[^{}]{1,50}\\}\\)?[\\w()^{}+\\-*/ ]*(?:=\\s*[\\w()^{}+\\-*/ ]*e\\^\\{[^{}]{1,50}\\}[\\w()^{}+\\-*/ ]*)+/g,
        /\\b[A-Za-z][A-Za-z0-9]*'{1,2}\\s*=\\s*[A-Za-z0-9_{}()[\\]'^+\\-*/. ]{1,36}/g,
        /\\b[A-Za-z][A-Za-z0-9]*\\([^)]{1,24}\\)\\s*=\\s*[A-Za-z0-9_{}()[\\]'^+\\-*/. ]{1,36}/g,
        /\\b[A-Za-z]_\\{[^{}]{1,40}\\}\\s*=\\s*[A-Za-z0-9_{}()[\\]'^+\\-*/. ]{1,50}/g,
        /\\b(?:int|sum|prod)_[A-Za-z0-9{}()'\\\\^+\\-]+(?:\\^[A-Za-z0-9{}()'\\\\^+\\-]+)?/g,
        /\\b[A-Za-z][A-Za-z0-9]*_\\{[^{}]{1,40}\\}(?:\\^[A-Za-z0-9{}()+\\-]+)?/g,
        /\\b(?:e|E)\\^\\{[^{}]{1,50}\\}/g,
        /\\b[A-Za-z][A-Za-z0-9]*\\^\\{[^{}]{1,40}\\}/g,
        /\\b(?:C\\^1|R\\^n|M\\^n|t\\^k)\\b/g,
        /\\b[A-Za-z]\\^[A-Za-z0-9{}()+\\-]+/g
      ];
      const ranges = [];
      for (const pattern of patterns) {
        for (const match of value.matchAll(pattern)) {
          const raw = match[0];
          const trimmedStart = raw.search(/\\S/);
          const trimmedEnd = raw.search(/\\s*$/);
          const start = match.index + Math.max(trimmedStart, 0);
          const end = match.index + (trimmedEnd >= 0 ? trimmedEnd : raw.length);
          const candidate = value.slice(start, end);
          if (candidate.length < 2 || /[А-Яа-яЁё]/.test(candidate)) continue;
          if (!/[=_^']|\\b(?:int|sum|prod)\\b/.test(candidate)) continue;
          if (ranges.some(range => start < range.end && end > range.start)) continue;
          ranges.push({ start, end });
          if (ranges.length >= 80) break;
        }
        if (ranges.length >= 80) break;
      }
      ranges.sort((a, b) => a.start - b.start || b.end - a.end);
      let out = '';
      let pos = 0;
      for (const range of ranges) {
        if (range.start < pos) continue;
        out += value.slice(pos, range.start);
        out += `\\\\(${value.slice(range.start, range.end)}\\\\)`;
        pos = range.end;
      }
      return out + value.slice(pos);
    }

    function renderMathText(text) {
      return prettifyPlainMath(esc(autoDelimitPlainMath(text || '')));
    }

    function fallbackFormulaText(text) {
      return String(text || '')
        .replace(/\\\\frac\\{([^{}]+)\\}\\{([^{}]+)\\}/g, '($1)/($2)')
        .replace(/\\\\left|\\\\right/g, '')
        .replace(/\\\\cdot/g, '·')
        .replace(/\\\\times/g, '×')
        .replace(/\\\\leq?|\\\\le/g, '≤')
        .replace(/\\\\geq?|\\\\ge/g, '≥')
        .replace(/\\\\to/g, '→')
        .replace(/\\\\infty/g, '∞')
        .replace(/\\\\pi/g, 'π')
        .replace(/\\\\lambda/g, 'λ')
        .replace(/\\\\mu/g, 'μ')
        .replace(/\\\\alpha/g, 'α')
        .replace(/\\\\beta/g, 'β')
        .replace(/\\\\gamma/g, 'γ')
        .replace(/\\\\Delta/g, 'Δ')
        .replace(/\\\\Phi/g, 'Φ')
        .replace(/\\\\sin/g, 'sin')
        .replace(/\\\\cos/g, 'cos')
        .replace(/\\\\exp/g, 'exp')
        .replace(/\\\\ln/g, 'ln')
        .replace(/\\\\int/g, '∫')
        .replace(/\\\\sum/g, '∑')
        .replace(/[{}]/g, '');
    }

    function splitDelimitedMath(text) {
      const delimiters = [
        { left: '$$', right: '$$', display: true },
        { left: '\\\\[', right: '\\\\]', display: true },
        { left: '\\\\(', right: '\\\\)', display: false },
        { left: '$', right: '$', display: false }
      ];
      const parts = [];
      let pos = 0;
      while (pos < text.length) {
        let best = null;
        for (const delimiter of delimiters) {
          const start = text.indexOf(delimiter.left, pos);
          if (start >= 0 && (!best || start < best.start)) best = { ...delimiter, start };
        }
        if (!best) {
          parts.push({ text: text.slice(pos), formula: false });
          break;
        }
        if (best.start > pos) parts.push({ text: text.slice(pos, best.start), formula: false });
        const contentStart = best.start + best.left.length;
        const end = text.indexOf(best.right, contentStart);
        if (end < 0) {
          parts.push({ text: text.slice(best.start), formula: false });
          break;
        }
        parts.push({ text: text.slice(contentStart, end), formula: true, display: best.display });
        pos = end + best.right.length;
      }
      return parts;
    }

    function renderFallbackMath(target = document) {
      const root = target.body || target;
      const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
        acceptNode(node) {
          const parent = node.parentElement;
          if (!parent || parent.closest('script, style, .katex, .tex-fallback')) return NodeFilter.FILTER_REJECT;
          return /\\$|\\\\\\(|\\\\\\[/.test(node.nodeValue || '') ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
        }
      });
      const nodes = [];
      while (walker.nextNode()) nodes.push(walker.currentNode);
      for (const node of nodes) {
        const parts = splitDelimitedMath(node.nodeValue || '');
        if (!parts.some(part => part.formula)) continue;
        const fragment = document.createDocumentFragment();
        for (const part of parts) {
          if (!part.formula) {
            fragment.appendChild(document.createTextNode(part.text));
            continue;
          }
          const span = document.createElement('span');
          span.className = `tex-fallback${part.display ? ' display' : ''}`;
          span.textContent = fallbackFormulaText(part.text);
          fragment.appendChild(span);
        }
        node.parentNode.replaceChild(fragment, node);
      }
    }

    function renderMathIn(target = document) {
      if (typeof renderMathInElement === 'function') {
        renderMathInElement(target.body || target, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '\\\\[', right: '\\\\]', display: true },
            { left: '\\\\(', right: '\\\\)', display: false },
            { left: '$', right: '$', display: false }
          ],
          throwOnError: false,
          strict: 'ignore',
          trust: false
        });
        return;
      }
      if (document.readyState === 'complete') renderFallbackMath(target);
    }

    function normalize(value) {
      return String(value ?? '').toLocaleLowerCase('ru');
    }

    function countText(count, one, few, many) {
      const n = Math.abs(Number(count) || 0);
      const mod10 = n % 10;
      const mod100 = n % 100;
      if (mod10 === 1 && mod100 !== 11) return `${count} ${one}`;
      if (mod10 >= 2 && mod10 <= 4 && (mod100 < 12 || mod100 > 14)) return `${count} ${few}`;
      return `${count} ${many}`;
    }

    function labelFor(key, value) {
      if (value == null || value === '') return 'без значения';
      if (key === 'source') {
        const source = sourceById[value] || {};
        return source.short_name || source.short_title || source.title || value;
      }
      if (key === 'standardIdea') return ideaById[value]?.title || value;
      if (key === 'definition') return definitionLabelById[value] || definitionById[value]?.title || value;
      if (key === 'cluster') return clusterById[value]?.title || clusterById[value]?.title_ru || value;
      if (key === 'course') return courseLabels[value] || value;
      if (key === 'publicReady') return publicReadyLabels[value] || value;
      if (key === 'reviewStatus') return reviewStatusLabels[value] || value;
      if (key === 'difficultyMain') return difficultyLabels[value] || value;
      if (key === 'kind') return kindLabels[value] || value;
      if (key === 'studyMode') return quickModes.find(mode => mode.id === value)?.label || value;
      if (key === 'scoreRange') return rangeLabels[value] || value;
      if (key === 'excludeOlympiad') return value === 'exclude' ? 'без олимпиадных' : String(value);
      if (key === 'assetFilter') return assetLabels[value] || value;
      if (key === 'ideaScore' || key === 'technicalScore') return String(value);
      return String(value);
    }

    function valuesFor(card, key) {
      if (key === 'studyMode') return [];
      if (key === 'source') return card.source_ids || [];
      if (key === 'author') return card.authors || [];
      if (key === 'cluster') return card.cluster_ids || [];
      if (key === 'standardIdea') return card.standard_idea_ids || [];
      if (key === 'definition') return card.definition_ids || [];
      if (key === 'tag') return card.tags || [];
      if (key === 'kind') return [card.kind].filter(Boolean);
      if (key === 'course') return [card.course_bucket || 'uncategorized'];
      if (key === 'publicReady') return [String(Boolean(card.public_ready))];
      if (key === 'reviewStatus') return [card.review_status].filter(Boolean);
      if (key === 'difficultyMain') return [card.difficulty_main].filter(Boolean);
      if (key === 'ideaScore') return [card.idea_score].filter(value => value != null).map(String);
      if (key === 'technicalScore') return [card.technical_score].filter(value => value != null).map(String);
      if (key === 'assetFilter') return [card.has_image ? 'has_image' : 'no_image'];
      if (key === 'scoreRange') return scoreRangeValues(card);
      if (key === 'excludeOlympiad') return ['exclude'];
      return [];
    }

    function isMultiFilter(key) {
      return multiFilterKeys.has(key);
    }

    function normalizeSelection(key, value) {
      if (!isMultiFilter(key)) {
        const raw = Array.isArray(value) ? value.find(item => item && item !== 'all') : value;
        return raw && raw !== 'all' ? String(raw) : 'all';
      }
      const rawValues = Array.isArray(value) ? value : [value];
      const values = [];
      for (const item of rawValues) {
        const text = String(item ?? '').trim();
        if (!text || text === 'all' || values.includes(text)) continue;
        values.push(text);
      }
      return values.length ? values : 'all';
    }

    function selectedValues(key, filters = state) {
      const value = filters[key];
      if (Array.isArray(value)) return value.map(String).filter(item => item && item !== 'all');
      if (value && value !== 'all') return String(value).split('||').map(item => item.trim()).filter(item => item && item !== 'all');
      return [];
    }

    function selectionHas(key, value, filters = state) {
      return selectedValues(key, filters).includes(String(value));
    }

    function setSelection(key, values) {
      if (!(key in state)) return;
      state[key] = normalizeSelection(key, values);
    }

    function toggleSelection(key, value) {
      setFilterSelection(key, value, true);
    }

    function hasSelectedValue(key, value, filters = state) {
      return selectedValues(key, filters).includes(String(value));
    }

    function setFilterSelection(key, value, toggle = false) {
      if (!(key in state)) return;
      if (!isMultiFilter(key)) {
        const next = normalizeSelection(key, value);
        state[key] = toggle && state[key] === next ? 'all' : next;
        return;
      }
      if (!toggle) {
        state[key] = normalizeSelection(key, value);
        return;
      }
      const values = selectedValues(key);
      const toggled = Array.isArray(value) ? value : [value];
      for (const item of toggled) {
        const text = String(item ?? '').trim();
        if (!text || text === 'all') continue;
        const index = values.indexOf(text);
        if (index >= 0) values.splice(index, 1);
        else values.push(text);
      }
      state[key] = values.length ? values : 'all';
    }

    function clearFilterSelection(key, value = '') {
      if (key === 'q') {
        state.q = '';
        return;
      }
      if (!(key in state)) return;
      if (!value || !isMultiFilter(key)) {
        state[key] = 'all';
        return;
      }
      const values = selectedValues(key).filter(item => item !== String(value));
      state[key] = values.length ? values : 'all';
    }

    function resetSearchContext() {
      state.q = '';
      for (const key of filterKeys) state[key] = 'all';
      state.sort = 'title';
      navigation.focus = '';
      navigation.cardId = '';
    }

    function tagsOf(card) {
      return new Set(card.tags || []);
    }

    function scoreRangeValues(card) {
      const idea = Number(card.idea_score);
      const tech = Number(card.technical_score);
      const values = [];
      if (Number.isFinite(idea) && Number.isFinite(tech)) {
        if (idea <= 4 && tech <= 4) values.push('easy');
        if (idea >= 5 && idea <= 7 && tech <= 6) values.push('middle');
        if (idea >= 5 && idea <= 7 && tech >= 3 && tech <= 7) values.push('exam_middle');
        if (idea >= 7 && idea <= 8) values.push('strong');
        if (idea >= 8) values.push('excellent');
      }
      return values;
    }

    function isOlympiadLike(card) {
      const tags = tagsOf(card);
      return tags.has('olympiad_style')
        || tags.has('olympiad_above_exam')
        || tags.has('beyond_standard_course')
        || String(card.course_bucket) === 'beyond_standard_course'
        || normalize(card.path).includes('/olympiad/');
    }

    function hasAnyTag(card, names) {
      const tags = tagsOf(card);
      return names.some(name => tags.has(name));
    }

    function inScoreBand(card, minIdea, maxIdea, maxTech = Infinity) {
      const idea = Number(card.idea_score);
      const tech = Number(card.technical_score);
      return Number.isFinite(idea)
        && idea >= minIdea
        && idea <= maxIdea
        && (!Number.isFinite(tech) || tech <= maxTech);
    }

    function inScoreBox(card, minIdea, maxIdea, minTech, maxTech) {
      const idea = Number(card.idea_score);
      const tech = Number(card.technical_score);
      return Number.isFinite(idea)
        && Number.isFinite(tech)
        && idea >= minIdea
        && idea <= maxIdea
        && tech >= minTech
        && tech <= maxTech;
    }

    function hasIdeasAndSolutions(card) {
      const problem = problemsById[card.id] || {};
      return (problem.solutions || []).length > 0
        && ((problem.ideas || []).length > 0 || (card.standard_idea_ids || []).length > 0);
    }

    const builtInExamInteractions = {
      'resit-pass-3-separable-exponential-growth': {
        type: 'numeric',
        prompt: 'Контроль ответа: для решения этой задачи Коши найдите y(1) / e^{1/2}.',
        answers: ['2', '2.0'],
        success: 'Верно: y=2e^{x^2/2}, поэтому y(1)/e^{1/2}=2.',
        failure: 'Проверьте разделение переменных и начальное условие: константа должна быть равна 2.'
      },
      'weak-pass-linear-method-choice': {
        type: 'numeric',
        prompt: 'Контроль ответа: для найденного решения введите значение y(ln 2).',
        answers: ['1/4', '0.25', '0,25'],
        success: 'Да: y=e^{-x}-e^{-2x}, значит y(ln 2)=1/2-1/4=1/4.',
        failure: 'Типичный промах здесь - пытаться разделить переменные вместо линейного множителя e^{2x}.'
      },
      'resit-pass-3-diagonal-linear-system': {
        type: 'numeric',
        prompt: 'Контроль ответа: чему равно y(1)e^2?',
        answers: ['3', '3.0'],
        success: 'Верно: вторая координата равна 3e^{-2t}.',
        failure: 'Диагональная система решается покоординатно; во второй координате показатель -2t.'
      },
      'dirichlet-eigenvalues-interval': {
        type: 'formula',
        prompt: 'Введите общий вид положительных собственных значений через натуральное n.',
        answers: ['n^2', 'n2', 'n**2', 'n²'],
        success: 'Да: λ=n^2, n=1,2,...',
        failure: 'Условие y(π)=0 требует sin(μπ)=0, поэтому μ должен быть натуральным.'
      },
      'autonomous-phase-line-stability': {
        type: 'multiple_choice',
        prompt: 'Какие равновесия асимптотически устойчивы?',
        choices: [
          { id: 'a', text: '0 и 2', correct: true },
          { id: 'b', text: 'только 1', correct: false },
          { id: 'c', text: '0, 1 и 2', correct: false },
          { id: 'd', text: 'только 0', correct: false }
        ],
        success: 'Верно: стрелки фазовой прямой направлены к 0 и к 2, а от 1.',
        failure: 'Нужно расставить знаки y(1-y)(y-2) на четырех промежутках.'
      }
    };

    function examCardType(card) {
      const overlay = examCardOverlay[card.id] || {};
      if (overlay.answer_mode === 'formula_slots') return 'formula';
      if (overlay.answer_mode === 'formula') return 'formula';
      if (overlay.answer_mode) return overlay.answer_mode;
      if (overlay.type) return overlay.type;
      if (builtInExamInteractions[card.id]) return builtInExamInteractions[card.id].type;
      if (['theorem', 'lemma', 'corollary', 'definition'].includes(card.kind)) return 'self_check';
      if (Number(card.technical_score) <= 3 && (card.standard_idea_ids || []).length) return 'multiple_choice';
      return 'self_check';
    }

    function isExamCandidate(card) {
      if (!card || !card.public_ready) return false;
      if (!['problem', 'theorem', 'lemma', 'corollary', 'definition'].includes(card.kind)) return false;
      if (hasAnyTag(card, ['needs_solution_completion', 'olympiad_above_exam'])) return false;
      const overlay = examCardOverlay[card.id] || {};
      const explicitlyExam = overlay.id || hasAnyTag(card, ['oral_exam', 'model_exam_task', 'theoretical_exam_task']);
      if (isOlympiadLike(card) && !explicitlyExam) return false;
      const idea = Number(card.idea_score);
      const tech = Number(card.technical_score);
      if (!Number.isFinite(idea)) return false;
      if (card.kind === 'problem' && Number.isFinite(tech) && tech > 5) return false;
      if (String(card.course_bucket) === 'beyond_standard_course') return false;
      return hasIdeasAndSolutions(card) || ['theorem', 'lemma', 'corollary', 'definition'].includes(card.kind);
    }

    function examTopic(card) {
      const overlay = examCardOverlay[card.id] || {};
      if (overlay.topic) return overlay.topic;
      const clusters = new Set(card.cluster_ids || []);
      const matched = examMajorTopics.find(topic => {
        if ((topic.fragments || []).includes(card.fragment)) return true;
        return (topic.cluster_ids || []).some(clusterId => clusters.has(clusterId));
      });
      return matched?.id || card.fragment || (card.cluster_ids || [])[0] || 'misc';
    }

    function examTopicLabel(topic) {
      return examTopicLabels[topic] || fragmentLabels[topic] || topic;
    }

    function examInteraction(card) {
      const overlay = examCardOverlay[card.id] || {};
      const builtIn = builtInExamInteractions[card.id] || {};
      const autoCheck = overlay.auto_check || {};
      const selfCheck = overlay.self_check || {};
      const overlayType = overlay.answer_mode === 'formula_slots' ? 'formula' : overlay.answer_mode;
      const overlayChoices = autoCheck.options
        ? autoCheck.options.map(option => ({
          id: option.id,
          text: option.text,
          correct: (autoCheck.correct_options || []).includes(option.id)
        }))
        : null;
      const overlayAnswers = [
        ...(autoCheck.accepted_text || []),
        ...(autoCheck.accepted_latex || []),
        autoCheck.value
      ].filter(value => value != null).map(String);
      const merged = {
        ...builtIn,
        ...overlay,
        type: overlayType || overlay.type || builtIn.type,
        prompt: overlay.prompt_override || overlay.prompt || selfCheck.task || builtIn.prompt,
        hasOverlayPrompt: Boolean(overlay.prompt_override || overlay.prompt || selfCheck.task),
        criteria: selfCheck.criteria || overlay.criteria || builtIn.criteria || [],
        choices: overlayChoices || overlay.choices || builtIn.choices,
        answers: overlayAnswers.length ? overlayAnswers : (overlay.answers || builtIn.answers),
        numericValue: autoCheck.type === 'numeric' && autoCheck.value != null ? Number(autoCheck.value) : null,
        tolerance: autoCheck.tolerance != null ? Number(autoCheck.tolerance) : null,
        multiple: Boolean(autoCheck.multiple || overlay.multiple),
        success: overlay.success || builtIn.success,
        failure: overlay.failure || builtIn.failure
      };
      const type = merged.type || examCardType(card);
      if (type === 'multiple_choice' && !merged.choices) {
        const correct = (card.standard_idea_ids || [])[0];
        const correctText = correct ? labelFor('standardIdea', correct) : fragmentLabels[card.fragment] || 'основной метод карточки';
        const pool = [
          'разделение переменных',
          'интегрирующий множитель',
          'формула Лиувилля',
          'теорема существования и единственности',
          'фазовая прямая',
          'матричная экспонента',
          'сравнение Штурма',
          'характеристики уравнения первого порядка'
        ].filter(item => normalize(item) !== normalize(correctText));
        return {
          type,
          prompt: merged.prompt || 'Какой основной метод или план решения здесь наиболее естественен?',
          choices: [
            { id: 'correct', text: correctText, correct: true },
            ...pool.slice(0, 3).map((text, index) => ({ id: `d${index}`, text, correct: false }))
          ],
          success: merged.success || 'Да, это главный ход решения.',
          failure: merged.failure || 'Сравните формулировку с идеями карточки: правильный ответ должен быть переносимым методом, а не случайной техникой.',
          multiple: false
        };
      }
      if (type === 'numeric' || type === 'formula') {
        return {
          type,
          prompt: merged.prompt || 'Введите короткий ответ.',
          answers: merged.answers || [],
          numericValue: merged.numericValue,
          tolerance: merged.tolerance,
          success: merged.success || 'Ответ принят.',
          failure: merged.failure || 'Ответ не совпал с эталоном. Проверьте вычисление или раскройте решение для самопроверки.'
        };
      }
      return {
        type: 'self_check',
        prompt: merged.prompt || 'Расскажите решение вслух, затем честно отметьте, получилось ли без подсказки.',
        criteria: merged.criteria || [],
        success: merged.success || 'Отлично: засчитывайте вопрос только если смогли восстановить ключевую идею и довести рассуждение.',
        failure: merged.failure || 'Это нормальная точка диагностики: раскройте идеи, восстановите каркас решения и получите более простой соседний вопрос.'
      };
    }

    function parseSimpleNumber(value) {
      const text = normalizedAnswer(value).replace(',', '.');
      if (/^[+-]?\\d+(\\.\\d+)?$/.test(text)) return Number(text);
      const fraction = text.match(/^([+-]?\\d+(?:\\.\\d+)?)\\/([+-]?\\d+(?:\\.\\d+)?)$/);
      if (fraction && Number(fraction[2]) !== 0) return Number(fraction[1]) / Number(fraction[2]);
      return NaN;
    }

    function shuffledExamChoices(choices) {
      const out = [...(choices || [])];
      for (let i = out.length - 1; i > 0; i -= 1) {
        const j = Math.floor(Math.random() * (i + 1));
        [out[i], out[j]] = [out[j], out[i]];
      }
      return out;
    }

    function normalizedAnswer(value) {
      return normalize(value)
        .replace(/,/g, '.')
        .replace(/\\s+/g, '')
        .replace(/[{}()]/g, '')
        .replace(/\\\\cdot/g, '*')
        .replace(/²/g, '^2')
        .replace(/\\*\\*/g, '^');
    }

    function checkExamAnswer(interaction, rawAnswer, selectedChoice) {
      if (interaction.type === 'multiple_choice') {
        if (interaction.multiple) {
          const selected = new Set(examState.selectedChoices || []);
          const correct = new Set((interaction.choices || []).filter(item => item.correct).map(item => item.id));
          return selected.size === correct.size && [...correct].every(id => selected.has(id));
        }
        const choice = (interaction.choices || []).find(item => item.id === selectedChoice);
        return Boolean(choice?.correct);
      }
      if (interaction.type === 'numeric' || interaction.type === 'formula') {
        const normalized = normalizedAnswer(rawAnswer);
        if (interaction.type === 'numeric' && interaction.numericValue != null) {
          const parsed = parseSimpleNumber(rawAnswer);
          const tolerance = Number.isFinite(interaction.tolerance) ? interaction.tolerance : 1e-9;
          if (Number.isFinite(parsed) && Math.abs(parsed - interaction.numericValue) <= tolerance) return true;
        }
        return (interaction.answers || []).some(answer => normalizedAnswer(answer) === normalized);
      }
      return null;
    }

    function examEstimate() {
      const n = examState.history.length;
      if (!n) return { low: examState.currentLevel - 1, high: examState.currentLevel + 1, text: 'пока нет ответов' };
      const weighted = examState.history.reduce((sum, item) => sum + item.level + (item.correct ? 0.45 : -0.85), 0) / n;
      const center = Math.max(3, Math.min(10, Math.round((weighted + examState.currentLevel) / 2)));
      const noise = n >= 5 ? 1 : n >= 4 ? 2 : 3;
      return {
        low: Math.max(2, center - noise),
        high: Math.min(10, center + noise),
        text: `${Math.max(2, center - noise)}-${Math.min(10, center + noise)}`
      };
    }

    function shouldFinishExam() {
      const n = examState.history.length;
      if (examState.failed) return true;
      const minQuestions = Number(examOverlay.min_questions || 4);
      const maxQuestions = Number(examOverlay.max_questions || 5);
      if (n < minQuestions) return false;
      if (n >= maxQuestions) return true;
      const lastTwo = examState.history.slice(-2);
      const correctCount = examState.history.filter(item => item.correct).length;
      if (examState.currentLevel >= 9 && correctCount >= 3) return true;
      if (examState.currentLevel <= 3 || correctCount <= 1) return true;
      return lastTwo.length === 2 && lastTwo.every(item => item.correct === lastTwo[0].correct);
    }

    function selectExamCard() {
      const target = examState.currentLevel;
      const used = new Set(examState.usedIds);
      const recentTopics = new Set(examState.topicHistory.slice(-3));
      const candidates = cards
        .filter(isExamCandidate)
        .filter(card => !used.has(card.id))
        .map(card => {
          const overlay = examCardOverlay[card.id] || {};
          const idea = Number(overlay.target_score || card.idea_score) || target;
          const tech = Number(card.technical_score) || 3;
          const topic = examTopic(card);
          const type = examCardType(card);
          const typeCounts = examState.history.reduce((acc, item) => {
            acc[item.type] = (acc[item.type] || 0) + 1;
            return acc;
          }, {});
          const desiredTypes = ['self_check', 'multiple_choice', 'numeric', 'formula'];
          const typeBonus = desiredTypes.includes(type) ? -0.8 * (2 - Math.min(typeCounts[type] || 0, 2)) : 0;
          const topicPenalty = recentTopics.has(topic) ? 2.5 : 0;
          const technicalPenalty = tech > 4 ? 1.5 : 0;
          const proofBonus = ['theorem', 'lemma'].includes(card.kind) && !typeCounts.self_check ? -0.6 : 0;
          const overlayBonus = overlay.id ? -1 : 0;
          return {
            card,
            score: Math.abs(idea - target) * 1.8 + topicPenalty + technicalPenalty + typeBonus + proofBonus + overlayBonus + Math.random() * 0.3
          };
        })
        .sort((a, b) => a.score - b.score);
      return candidates[0]?.card || cards.filter(isExamCandidate).sort((a, b) => (Number(a.idea_score) || 99) - (Number(b.idea_score) || 99))[0];
    }

    function startExam(level) {
      examState.active = true;
      examState.finished = false;
      examState.failed = false;
      examState.startLevel = level;
      examState.currentLevel = level;
      examState.selectedChoice = null;
      examState.selectedChoices = [];
      examState.current = null;
      examState.history = [];
      examState.usedIds = [];
      examState.topicHistory = [];
      nextExamQuestion();
    }

    function nextExamQuestion() {
      if (shouldFinishExam()) {
        examState.finished = true;
        examState.current = null;
        render();
        return;
      }
      const card = selectExamCard();
      if (!card) {
        examState.finished = true;
        examState.current = null;
        render();
        return;
      }
      const interaction = examInteraction(card);
      if (interaction.type === 'multiple_choice') {
        interaction.choices = shuffledExamChoices(interaction.choices);
      }
      examState.current = {
        card,
        interaction,
        answered: false,
        correct: null,
        rawAnswer: '',
        feedback: ''
      };
      examState.selectedChoice = null;
      examState.selectedChoices = [];
      examState.usedIds.push(card.id);
      examState.topicHistory.push(examTopic(card));
      render();
    }

    function submitExamAnswer(value = null) {
      const current = examState.current;
      if (!current || current.answered) return;
      const interaction = current.interaction;
      const rawAnswer = value ?? byId('exam-answer-input')?.value ?? '';
      const checked = checkExamAnswer(interaction, rawAnswer, examState.selectedChoice);
      const correct = checked === null ? Boolean(value) : checked;
      current.answered = true;
      current.correct = correct;
      current.rawAnswer = rawAnswer;
      current.feedback = correct ? interaction.success : interaction.failure;
      examState.history.push({
        id: current.card.id,
        title: current.card.title,
        topic: examTopic(current.card),
        type: interaction.type,
        level: examState.currentLevel,
        correct
      });
      const failureLevel = Number(examOverlay.failure_level || 2);
      examState.currentLevel = correct ? Math.min(10, examState.currentLevel + 1) : examState.currentLevel - 1;
      if (examState.currentLevel <= failureLevel) {
        examState.failed = true;
        examState.finished = true;
      }
      render();
    }

    function matchesStudyMode(card, mode) {
      if (!mode || mode === 'all') return true;
      if (mode === 'no_olympiad') return !isOlympiadLike(card);
      if (mode === 'problems') return card.kind === 'problem';
      if (mode === 'sources_authors' || mode === 'difficulty_tags') return true;
      if (mode === 'theory') {
        return ['theorem', 'lemma', 'definition', 'corollary'].includes(card.kind)
          || hasAnyTag(card, ['theory_assignment', 'standard_theory']);
      }
      if (mode === 'definitions') {
        return (card.definition_ids || []).length > 0 || card.kind === 'definition';
      }
      if (mode === 'clusters') {
        return (card.cluster_ids || []).length > 0
          || hasAnyTag(card, ['cluster_representative', 'task_cluster']);
      }
      if (mode === 'written_minimum') {
        return !isOlympiadLike(card)
          && (hasAnyTag(card, ['written_exam', 'resit_exam', 'weak_student_check', 'exam_score_3', 'exam_score_4', 'low_technical'])
            || normalize(card.id).includes('basic-mipt'))
          && (inScoreBand(card, 0, 5, 5) || hasAnyTag(card, ['exam_score_3', 'exam_score_4']));
      }
      if (mode === 'written_middle') {
        return !isOlympiadLike(card)
          && (hasAnyTag(card, ['written_exam', 'middle_student_check', 'model_exam_task', 'exam_score_5', 'exam_score_6', 'exam_score_7'])
            || (card.source_ids || []).includes('src-local-du-written-exams'))
          && (inScoreBand(card, 4, 7, 6) || hasAnyTag(card, ['exam_score_5', 'exam_score_6', 'exam_score_7']));
      }
      if (mode === 'exam_middle') {
        return card.kind === 'problem'
          && !isOlympiadLike(card)
          && inScoreBox(card, 5, 7, 3, 7)
          && hasIdeasAndSolutions(card);
      }
      if (mode === 'exam_simulation') {
        return isExamCandidate(card);
      }
      if (mode === 'written_strong') {
        return !hasAnyTag(card, ['olympiad_above_exam', 'beyond_standard_course', 'needs_solution_completion'])
          && (hasAnyTag(card, ['written_exam', 'strong_student_check', 'excellent_check', 'mipt_excellent_level', 'exam_score_7', 'exam_score_8', 'exam_score_9', 'exam_score_10'])
            || (card.source_ids || []).includes('src-local-du-written-exams'))
          && (inScoreBand(card, 6, 10, 7) || hasAnyTag(card, ['exam_score_7', 'exam_score_8', 'exam_score_9', 'exam_score_10']));
      }
      return true;
    }

    function cardMatches(card, overrides = {}) {
      const filters = { ...state, ...overrides };
      const query = normalize(filters.q).trim();
      if (query) {
        const haystack = normalize(card.search_text);
        const tokens = query.split(/\\s+/).filter(Boolean);
        if (!tokens.every(token => haystack.includes(token))) return false;
      }
      if (!matchesStudyMode(card, filters.studyMode)) return false;
      if (filters.excludeOlympiad === 'exclude' && isOlympiadLike(card)) return false;
      for (const key of filterKeys) {
        const selected = selectedValues(key, filters);
        if (!selected.length) continue;
        if (key === 'studyMode' || key === 'excludeOlympiad') continue;
        const values = valuesFor(card, key).map(String);
        if (!selected.some(value => values.includes(String(value)))) return false;
      }
      return true;
    }

    function matchingCards(overrides = {}) {
      return cards.filter(card => cardMatches(card, overrides));
    }

    function optionCount(key, value) {
      return matchingCards({ [key]: String(value) }).length;
    }

    function uniqueOptions(key) {
      const config = selectConfig[key] || {};
      if (config.values) return config.values;
      const values = new Set();
      for (const card of cards) {
        for (const value of valuesFor(card, key)) values.add(String(value));
      }
      return [...values].sort((a, b) => labelFor(key, a).localeCompare(labelFor(key, b), 'ru', { numeric: true }));
    }

    function renderSelect(key) {
      const config = selectConfig[key];
      if (!config?.id) return;
      const selected = selectedValues(key);
      const isMulti = isMultiFilter(key);
      const allCount = matchingCards({ [key]: 'all' }).length;
      const options = uniqueOptions(key)
        .map(value => ({ value, label: labelFor(key, value), count: optionCount(key, value) }))
        .filter(option => option.count > 0 || selected.includes(option.value));
      const control = byId(config.id);
      control.multiple = isMulti;
      if (isMulti) control.size = Math.min(6, Math.max(2, options.length + 1));
      else control.removeAttribute('size');
      control.innerHTML = [
        `<option value="all">${esc(config.all)} (${allCount})</option>`,
        ...options.map(option => `<option value="${esc(option.value)}">${esc(option.label)} (${option.count})</option>`)
      ].join('');
      const available = new Set(options.map(option => option.value));
      const validSelected = selected.filter(value => available.has(value));
      if (isMulti) {
        for (const option of control.options) option.selected = validSelected.includes(option.value);
        if (!validSelected.length) control.options[0].selected = true;
      } else {
        control.value = validSelected[0] || 'all';
      }
      state[key] = normalizeSelection(key, validSelected);
    }

    function renderFilters() {
      for (const key of filterKeys) renderSelect(key);
      byId('q').value = state.q;
      byId('sort').value = state.sort;
    }

    function renderActiveFilters() {
      const items = [];
      if (state.q.trim()) items.push({ key: 'q', label: `поиск: ${state.q.trim()}` });
      for (const key of filterKeys) {
        for (const value of selectedValues(key)) {
          items.push({ key, value, label: `${selectConfig[key].label}: ${labelFor(key, value)}` });
        }
      }
      byId('active-filters').innerHTML = items.map(item => `
        <button class="chip active" type="button" data-clear-filter="${esc(item.key)}" data-clear-value="${esc(item.value || '')}">${esc(item.label)} ×</button>
      `).join('');
      byId('top-active-filters').innerHTML = byId('active-filters').innerHTML;
    }

    function facetCounts(key) {
      const counts = {};
      for (const card of matchingCards({ [key]: 'all' })) {
        for (const value of valuesFor(card, key)) {
          const normalized = String(value);
          counts[normalized] = (counts[normalized] || 0) + 1;
        }
      }
      return Object.entries(counts)
        .map(([value, count]) => ({ value, count, label: labelFor(key, value) }))
        .sort((a, b) => b.count - a.count || a.label.localeCompare(b.label, 'ru', { numeric: true }));
    }

    function renderFacet(key, title, limit = 12) {
      const rows = facetCounts(key).slice(0, limit);
      if (!rows.length) return '';
      return `
        <div class="facet-panel">
          <div class="facet-title"><span>${esc(title)}</span><span>${rows.length}</span></div>
          <div class="chip-row">
            ${rows.map(row => `
              <button class="chip ${selectionHas(key, row.value) ? 'active' : ''}" type="button" data-set-filter="${esc(key)}" data-filter-value="${esc(row.value)}">
                <span>${esc(row.label)}</span><span class="chip-count">${row.count}</span>
              </button>
            `).join('')}
          </div>
        </div>
      `;
    }

    function renderFacets() {
      byId('facets').innerHTML = [
        renderFacet('kind', 'Типы'),
        renderFacet('scoreRange', 'Уровни по баллам'),
        renderFacet('assetFilter', 'Материалы'),
        renderFacet('ideaScore', 'Идейная сложность'),
        renderFacet('technicalScore', 'Техническая сложность'),
        renderFacet('difficultyMain', 'Сложность'),
        renderFacet('cluster', 'Кластеры', 10),
        renderFacet('definition', 'Определения', 18),
        renderFacet('source', 'Источники', 10),
        renderFacet('standardIdea', 'Стандартные идеи', 10),
        renderFacet('tag', 'Теги', 16)
      ].join('');
    }

    function statusPill(card) {
      if (card.public_ready) return '<span class="pill good">готово к публикации</span>';
      return '<span class="pill warn">требует проверки</span>';
    }

    function renderPill(text, cls = '') {
      if (!text) return '';
      return `<span class="pill ${esc(cls)}">${esc(text)}</span>`;
    }

    function renderFilterChip(key, value, text, cls = '') {
      if (!text || value == null || value === '') return '';
      const activeClass = selectionHas(key, value) ? ' active' : '';
      return `
        <button class="chip ${esc(cls)}${activeClass}" type="button" data-set-filter="${esc(key)}" data-filter-value="${esc(value)}" data-filter-scope="card" title="${esc(`Показать карточки: ${text}`)}">
          <span>${esc(text)}</span>
        </button>
      `;
    }

    function renderClusterLink(clusterId, cls = 'good') {
      const title = labelFor('cluster', clusterId);
      return `
        <button class="chip ${esc(cls)}" type="button" data-open-cluster="${esc(clusterId)}" title="${esc(`Открыть кластер: ${title}`)}">
          <span>${esc(title)}</span>
        </button>
      `;
    }

    function renderCardLink(card, cls = '') {
      return `
        <button class="task-link ${esc(cls)}" type="button" data-open-card="${esc(card.id)}">
          <span class="task-link-title tex-content">${renderMathText(card.title)}</span>
          <span class="task-link-meta">${esc(kindLabels[card.kind] || card.kind || 'карточка')} · идея ${esc(card.idea_score ?? '-')} · техника ${esc(card.technical_score ?? '-')}</span>
        </button>
      `;
    }

    function currentRouteCard() {
      return navigation.cardId ? cardsById[navigation.cardId] || null : null;
    }

    function searchRouteHref() {
      const params = new URLSearchParams(window.location.search || '');
      params.delete('card');
      params.delete('id');
      if (![...params.keys()].length) params.set('nav', 'cards');
      return `${window.location.pathname}?${params.toString()}${window.location.hash || ''}`;
    }

    function cardRouteHref(cardId) {
      const params = new URLSearchParams();
      params.set('card', cardId);
      return `${window.location.pathname}?${params.toString()}`;
    }

    function clusterRouteHref(clusterId) {
      const params = new URLSearchParams();
      params.set('nav', 'clusters');
      params.set('cluster', clusterId);
      return `${window.location.pathname}?${params.toString()}`;
    }

    function linkedCardIdFromHash() {
      const raw = decodeURIComponent((window.location.hash || '').replace(/^#/, ''));
      if (!raw) return '';
      return raw.startsWith('card-') ? raw.slice(5) : raw;
    }

    function isolateCardContext(cardId) {
      if (!cardsById[cardId]) return false;
      clearAllFilters();
      navigation.cardId = cardId;
      state.q = cardId;
      state.sort = 'title';
      return true;
    }

    function isolateClusterContext(clusterId) {
      if (!clusterById[clusterId]) return false;
      clearAllFilters();
      activateQuickMode('clusters');
      setSelection('cluster', [clusterId]);
      navigation.focus = 'cluster';
      return true;
    }

    function relatedCardsFor(card) {
      const seen = new Set();
      const related = [];
      for (const relation of DB.relations || []) {
        const from = relation.from;
        const to = relation.to;
        if (from !== card.id && to !== card.id) continue;
        const otherId = from === card.id ? to : from;
        if (seen.has(otherId)) continue;
        const other = cardsById[otherId];
        if (!other) continue;
        seen.add(otherId);
        const relationText = from === card.id ? relation.forward_text : relation.backward_text;
        related.push({
          card: other,
          type: relationTypeLabels[relation.type] || relation.type || 'связь',
          text: relationText || ''
        });
      }
      if (related.length) return related.slice(0, 8);

      const clusterIds = new Set(card.cluster_ids || []);
      if (!clusterIds.size) return [];
      return cards
        .filter(item => item.id !== card.id && (item.cluster_ids || []).some(clusterId => clusterIds.has(clusterId)))
        .sort(routeSort)
        .slice(0, 8)
        .map(item => ({ card: item, type: 'тот же кластер', text: '' }));
    }

    function openCardRoute(cardId) {
      if (!isolateCardContext(cardId)) return;
      if (window.history?.pushState) {
        window.history.pushState(null, '', cardRouteHref(cardId));
      }
      render();
      requestAnimationFrame(() => window.scrollTo({ top: 0, behavior: 'smooth' }));
    }

    function openClusterRoute(clusterId) {
      if (!isolateClusterContext(clusterId)) return;
      if (window.history?.pushState) {
        window.history.pushState(null, '', clusterRouteHref(clusterId));
      }
      render();
      scrollToNavigationTarget();
    }

    function cardDefinitionLabel(card, id, index) {
      return (card.definition_labels || [])[index] || labelFor('definition', id);
    }

    function renderText(text) {
      return `<div class="block tex-content">${renderMathText(text || '')}</div>`;
    }

    function renderReveal(kind, title, html, emptyHtml = '') {
      const content = html || emptyHtml;
      return `
        <details class="reveal" data-reveal-kind="${esc(kind)}">
          <summary>
            <span class="show-label">Показать ${esc(title.toLocaleLowerCase('ru'))}</span>
            <span class="hide-label">Скрыть</span>
          </summary>
          ${content}
        </details>
      `;
    }

    function renderIdeas(problem) {
      const ideas = problem.ideas || [];
      if (!ideas.length) return '';
      return ideas.map(idea => `
        <div class="block tex-content"><strong>${renderMathText(idea.title || idea.id || 'Идея')}</strong><br>${renderMathText(idea.text || '')}</div>
      `).join('');
    }

    function renderSolutions(problem, label) {
      const solutions = problem.solutions || [];
      if (!solutions.length) return '';
      return solutions.map(solution => `
        <div class="block tex-content"><strong>${renderMathText(solution.title || solution.id || label)}</strong><br>${renderMathText(solution.text || '')}</div>
      `).join('');
    }

    function assetUrl(path) {
      const text = String(path || '');
      if (/^(https?:|data:|file:)/i.test(text)) return text;
      if (text.startsWith('../') || text.startsWith('./')) return text;
      if (text.startsWith('data/')) return `../${text}`;
      return text;
    }

    function renderAssets(problem, card) {
      const assets = card.assets || problem.assets || [];
      if (!assets.length) return '';
      return `
        <div class="asset-grid">
          ${assets.map(asset => {
            const path = asset.path || '';
            const url = assetUrl(path);
            const title = asset.title || asset.caption || asset.role || asset.id || 'asset';
            const isImage = asset.type === 'image' || /\\.(svg|png|jpe?g|gif|webp)$/i.test(path.split('?')[0]);
            if (isImage) {
              return `
                <figure class="asset-card">
                  <a href="${esc(url)}" target="_blank" rel="noreferrer">
                    <img src="${esc(url)}" alt="${esc(asset.alt || title)}" loading="lazy">
                  </a>
                  <figcaption class="asset-caption">${esc(title)} · ${esc(path)}</figcaption>
                </figure>
              `;
            }
            return `<div class="asset-card"><a href="${esc(url)}" target="_blank" rel="noreferrer">${esc(title)}</a><div class="asset-caption">${esc(path)}</div></div>`;
          }).join('')}
        </div>
      `;
    }

    function isMethodGuideCard(card) {
      return hasAnyTag(card, ['method_guide']);
    }

    function scoreValue(value, fallback = 99) {
      const score = Number(value);
      return Number.isFinite(score) ? score : fallback;
    }

    function routeSort(a, b) {
      return scoreValue(a.idea_score) - scoreValue(b.idea_score)
        || scoreValue(a.technical_score) - scoreValue(b.technical_score)
        || a.title.localeCompare(b.title, 'ru', { numeric: true });
    }

    function representativeCandidatesForGuide(card) {
      if (!isMethodGuideCard(card)) return [];
      const clusterIds = new Set(card.cluster_ids || []);
      if (!clusterIds.size) return [];
      const representativeIds = [];
      for (const clusterId of clusterIds) {
        for (const id of clusterById[clusterId]?.representative_card_ids || []) representativeIds.push(id);
      }
      const seen = new Set();
      const fromRepresentatives = representativeIds
        .map(id => cardsById[id])
        .filter(Boolean);
      const fromCluster = cards.filter(item =>
        (item.cluster_ids || []).some(clusterId => clusterIds.has(clusterId))
      );
      return [...fromRepresentatives, ...fromCluster]
        .filter(item => {
          if (!item || item.id === card.id || seen.has(item.id)) return false;
          seen.add(item.id);
          if (item.kind !== 'problem') return false;
          if (isMethodGuideCard(item)) return false;
          if (item.public_ready === false) return false;
          return Number.isFinite(Number(item.idea_score)) || Number.isFinite(Number(item.technical_score));
        })
        .sort(routeSort);
    }

    function routeBucket(card) {
      const idea = scoreValue(card.idea_score, 0);
      const tech = scoreValue(card.technical_score, 0);
      if (tech > 5 || idea >= 8) return 'hard';
      if (idea <= 5 && tech <= 5) return 'start';
      return 'middle';
    }

    function renderRouteTask(card) {
      return `
        <button class="route-task" type="button" data-route-card-id="${esc(card.id)}" title="${esc(`Открыть карточку ${card.id}`)}">
          <span class="route-task-title tex-content">${renderMathText(card.title)}</span>
          <span class="route-task-meta">идея ${esc(card.idea_score ?? '-')} · техника ${esc(card.technical_score ?? '-')}</span>
        </button>
      `;
    }

    function renderMethodGuideRoute(card) {
      const candidates = representativeCandidatesForGuide(card);
      if (!candidates.length) return '';
      const groups = {
        start: candidates.filter(item => routeBucket(item) === 'start').slice(0, 3),
        middle: candidates.filter(item => routeBucket(item) === 'middle').slice(0, 3),
        hard: candidates.filter(item => routeBucket(item) === 'hard').slice(0, 3)
      };
      if (!groups.start.length && !groups.middle.length && !groups.hard.length) return '';
      const column = (title, items) => `
        <div class="route-column">
          <h4>${esc(title)}</h4>
          <div class="route-task-list">
            ${items.length ? items.map(renderRouteTask).join('') : '<div class="empty">Нет подходящих карточек.</div>'}
          </div>
        </div>
      `;
      return `
        <section class="method-route" aria-label="Учебный маршрут кластера">
          <h3>После методического блока</h3>
          <div class="route-columns">
            ${column('Начать', groups.start)}
            ${column('Средний уровень', groups.middle)}
            ${column('Сложнее', groups.hard)}
          </div>
        </section>
      `;
    }

    function renderCompactMethodGuideCard(card, options = {}) {
      const clusterBadges = (card.cluster_ids || []).slice(0, 3).map(id => renderClusterLink(id)).join('');
      const clickableAttrs = options.single ? '' : ` data-open-card-id="${esc(card.id)}"`;
      const clickableClass = options.single ? '' : ' clickable-card';
      return `
        <article class="card method-guide-compact${clickableClass}" id="card-${esc(card.id)}"${clickableAttrs}>
          <div class="card-head">
            <div class="card-title">
              <h2 class="tex-content">${renderMathText(card.title)}</h2>
              <div class="meta-row">
                ${renderPill(card.id, 'code')}
                ${renderPill('методический блок')}
                ${clusterBadges}
              </div>
            </div>
          </div>
          ${renderMethodGuideRoute(card)}
          <details>
            <summary>Показать методический текст</summary>
            <div class="block tex-content">${renderMathText(card.statement || '')}</div>
          </details>
        </article>
      `;
    }

    function renderCard(card, options = {}) {
      if (state.studyMode === 'clusters' && isMethodGuideCard(card)) {
        return renderCompactMethodGuideCard(card, options);
      }
      const problem = problemsById[card.id] || {};
      const proofLabel = ['theorem', 'lemma', 'corollary', 'definition'].includes(card.kind) ? 'Доказательство' : 'Решение';
      const sourceBadges = (card.source_ids || []).slice(0, 3).map(id => renderFilterChip('source', id, labelFor('source', id))).join('');
      const clusterBadges = (card.cluster_ids || []).slice(0, 2).map(id => renderClusterLink(id)).join('');
      const tagBadges = (card.tags || []).slice(0, 7).map(tag => renderFilterChip('tag', tag, tag)).join('');
      const ideaBadges = (card.standard_idea_ids || []).slice(0, 3).map(id => renderFilterChip('standardIdea', id, labelFor('standardIdea', id))).join('');
      const definitionBadges = (card.definition_ids || []).slice(0, 5).map((id, index) => renderFilterChip('definition', id, cardDefinitionLabel(card, id, index))).join('');
      const ideasHtml = renderIdeas(problem);
      const solutionsHtml = renderSolutions(problem, proofLabel);
      const methodRouteHtml = renderMethodGuideRoute(card);
      const clickableAttrs = options.single ? '' : ` data-open-card-id="${esc(card.id)}"`;
      const clickableClass = options.single ? '' : ' clickable-card';
      return `
        <article class="card${clickableClass}" id="card-${esc(card.id)}"${clickableAttrs}>
          <div class="card-head">
            <div class="card-title">
              <h2 class="tex-content">${renderMathText(card.title)}</h2>
              <div class="meta-row">
                ${renderPill(card.id, 'code')}
                ${renderPill(kindLabels[card.kind] || card.kind)}
                ${renderPill(fragmentLabels[card.fragment] || card.fragment)}
                ${renderPill(difficultyLabels[card.difficulty_main] || card.difficulty_main)}
                ${renderPill(`идея ${card.idea_score ?? '-'}`)}
                ${renderPill(`техника ${card.technical_score ?? '-'}`)}
                ${renderPill(courseLabels[card.course_bucket] || card.course_bucket)}
                ${statusPill(card)}
                ${renderPill(reviewStatusLabels[card.review_status] || card.review_status, card.review_status === 'needs_human_review' ? 'warn' : '')}
              </div>
            </div>
          </div>
          <p class="statement tex-content">${renderMathText(card.statement)}</p>
          ${renderAssets(problem, card)}
          <div class="meta-row">${sourceBadges}${clusterBadges}${ideaBadges}${definitionBadges}${tagBadges}</div>
          ${methodRouteHtml}
          ${renderReveal('ideas', 'Идеи', ideasHtml, '<div class="empty">Идеи не указаны.</div>')}
          ${renderReveal('solution', proofLabel, solutionsHtml, `<div class="empty">${proofLabel} пока не добавлено.</div>`)}
        </article>
      `;
    }

    function sortedResults(items) {
      const out = [...items];
      if (state.sort === 'idea_asc') {
        out.sort((a, b) => (Number(a.idea_score) || 99) - (Number(b.idea_score) || 99) || a.title.localeCompare(b.title, 'ru'));
      } else if (state.sort === 'difficulty_asc') {
        out.sort((a, b) =>
          (Number(a.idea_score) || 99) - (Number(b.idea_score) || 99)
          || (Number(a.technical_score) || 99) - (Number(b.technical_score) || 99)
          || a.title.localeCompare(b.title, 'ru')
        );
      } else if (state.sort === 'idea_desc') {
        out.sort((a, b) => (Number(b.idea_score) || 0) - (Number(a.idea_score) || 0) || a.title.localeCompare(b.title, 'ru'));
      } else if (state.sort === 'technical_asc') {
        out.sort((a, b) => (Number(a.technical_score) || 99) - (Number(b.technical_score) || 99) || a.title.localeCompare(b.title, 'ru'));
      } else if (state.sort === 'technical_desc') {
        out.sort((a, b) => (Number(b.technical_score) || 0) - (Number(a.technical_score) || 0) || a.title.localeCompare(b.title, 'ru'));
      } else if (state.sort === 'kind') {
        out.sort((a, b) => String(a.kind).localeCompare(String(b.kind), 'ru') || a.title.localeCompare(b.title, 'ru'));
      } else {
        out.sort((a, b) => a.title.localeCompare(b.title, 'ru', { numeric: true }));
      }
      return out;
    }

    function clusterSortedResults(items) {
      const rank = card => isClusterTask(card) ? 0 : isMethodGuideCard(card) ? 2 : 1;
      return sortedResults(items).sort((a, b) => rank(a) - rank(b) || routeSort(a, b));
    }

    function renderSummary(items) {
      const kindCounts = facetCounts('kind');
      const readyCount = items.filter(card => card.public_ready).length;
      byId('summary').innerHTML = [
        renderPill(countText(items.length, 'карточка', 'карточки', 'карточек'), 'code'),
        renderPill(`${readyCount} готово к публикации`, readyCount === items.length ? 'good' : 'warn'),
        ...kindCounts.slice(0, 4).map(item => renderPill(`${item.label}: ${item.count}`))
      ].join('');
    }

    function countBy(predicate) {
      return cards.filter(predicate).length;
    }

    function quickModeCount(mode) {
      if (mode.id === 'no_olympiad') return countBy(card => !isOlympiadLike(card));
      if (mode.id === 'sources_authors') {
        const sourceCount = uniqueOptions('source').length;
        const authorCount = uniqueOptions('author').length;
        return sourceCount + authorCount;
      }
      if (mode.id === 'difficulty_tags') {
        return uniqueOptions('difficultyMain').length + uniqueOptions('tag').length;
      }
      return countBy(card => matchesStudyMode(card, mode.id));
    }

    function renderDirectoryColumn(key, title, limit = 10) {
      const rows = facetCounts(key).slice(0, limit);
      if (!rows.length) return '';
      return `
        <div>
          <h3>${esc(title)}</h3>
          <div class="chip-row">
            ${rows.map(row => `
              <button class="chip ${selectionHas(key, row.value) ? 'active' : ''}" type="button" data-set-filter="${esc(key)}" data-filter-value="${esc(row.value)}">
                <span>${esc(row.label)}</span><span class="chip-count">${row.count}</span>
              </button>
            `).join('')}
          </div>
        </div>
      `;
    }

    function isClusterTask(card) {
      return card.kind === 'problem' && !isMethodGuideCard(card);
    }

    function clusterCards(clusterId, overrides = {}) {
      return sortedResults(matchingCards({ ...overrides, cluster: clusterId }));
    }

    function clusterTaskCards(clusterId, overrides = {}) {
      return clusterCards(clusterId, overrides).filter(isClusterTask);
    }

    function renderClusterTask(card) {
      const clusterId = (card.cluster_ids || []).find(id => selectionHas('cluster', id)) || (card.cluster_ids || [])[0] || '';
      const clusterLink = clusterId ? `
        <a class="cluster-back-link" href="${esc(clusterRouteHref(clusterId))}">К странице кластера</a>
      ` : '';
      return `
        <div class="cluster-task-wrap">
          <button class="cluster-task" type="button" data-open-card="${esc(card.id)}" title="${esc(`Открыть карточку ${card.id}`)}">
            <span class="cluster-task-title tex-content">${renderMathText(card.title)}</span>
            <span class="cluster-task-meta">${esc(card.id)} · идея ${esc(card.idea_score ?? '-')} · техника ${esc(card.technical_score ?? '-')} · ${esc(labelFor('difficultyMain', card.difficulty_main))}</span>
          </button>
          ${clusterLink}
        </div>
      `;
    }

    function renderClusterFilterBlock(key, title, limit = 14) {
      const rows = facetCounts(key).slice(0, limit);
      if (!rows.length) return '';
      return `
        <div class="cluster-filter-block">
          <h3>${esc(title)}</h3>
          <div class="chip-row">
            ${rows.map(row => `
              <button class="chip ${selectionHas(key, row.value) ? 'active' : ''}" type="button" data-set-filter="${esc(key)}" data-filter-value="${esc(row.value)}">
                <span>${esc(row.label)}</span><span class="chip-count">${row.count}</span>
              </button>
            `).join('')}
          </div>
        </div>
      `;
    }

    function renderClusterGuides(items) {
      const guides = items.filter(isMethodGuideCard);
      if (!guides.length) return '';
      return `
        <div class="cluster-guide-strip">
          <h3>Теоретический блок</h3>
          ${guides.map(card => `
            <details>
              <summary class="tex-content">${renderMathText(card.title)}</summary>
              <div class="quick-actions">
                ${(card.cluster_ids || []).map(id => `<a class="cluster-back-link" href="${esc(clusterRouteHref(id))}">К странице кластера: ${esc(labelFor('cluster', id))}</a>`).join('')}
              </div>
              <div class="block tex-content">${renderMathText(card.statement || '')}</div>
              ${renderMethodGuideRoute(card)}
            </details>
          `).join('')}
        </div>
      `;
    }

    function clusterSearchText(cluster) {
      return normalize([
        cluster.id,
        cluster.title,
        cluster.title_ru,
        cluster.goal,
        ...(cluster.duplicate_signals || []),
        ...(cluster.canonical_solution_plan || []),
        ...(cluster.allowed_variants || []).map(item => `${item.id || ''} ${item.description || ''} ${item.use_when || ''}`)
      ].join(' '));
    }

    function clusterMatchesQuery(cluster) {
      const query = normalize(state.q).trim();
      if (!query) return true;
      const haystack = clusterSearchText(cluster);
      return query.split(/\\s+/).filter(Boolean).every(token => haystack.includes(token));
    }

    function renderClusterFocus(items) {
      const selectedClusters = selectedValues('cluster');
      const selectedTitles = selectedClusters.map(id => labelFor('cluster', id));
      const tasks = items.filter(isClusterTask).sort(routeSort);
      const heading = selectedTitles.length ? selectedTitles.join(' + ') : 'Поиск и выбор кластера';
      const taskBlock = selectedClusters.length ? `
          ${renderClusterGuides(items)}
          <div>
            <h3>Список задач</h3>
            <div class="cluster-task-list prominent">
              ${tasks.length ? tasks.slice(0, 48).map(renderClusterTask).join('') : '<div class="empty">В выбранных кластерах задач не найдено. Ослабьте фильтры выше.</div>'}
            </div>
          </div>
      ` : `
          <div class="empty">Выберите кластер из каталога ниже. До выбора кластера задачи и методические карточки не выводятся общим списком.</div>
      `;
      return `
        <div class="cluster-focus" id="clusters-directory">
          <div>
            <h3>${esc(heading)}</h3>
            <p class="home-note">В режиме кластеров строка поиска ищет кластеры по названию и описанию. Задачи показываются только после открытия конкретного кластера; методические блоки отделены от списка задач.</p>
          </div>
          <div class="cluster-filter-grid">
            ${renderClusterFilterBlock('cluster', 'Темы / кластеры', 12)}
            ${renderClusterFilterBlock('standardIdea', 'Идеи', 12)}
            ${renderClusterFilterBlock('difficultyMain', 'Сложности', 8)}
            ${renderClusterFilterBlock('source', 'Источники', 12)}
          </div>
          ${taskBlock}
        </div>
      `;
    }

    function renderClusterCard(cluster) {
      const items = clusterCards(cluster.id);
      const tasks = items.filter(isClusterTask);
      const guides = items.filter(isMethodGuideCard);
      return `
        <div class="cluster-card">
          <div>
            <div class="cluster-card-title">${esc(cluster.title || cluster.title_ru || cluster.id)}</div>
            <div class="meta-row">
              ${renderPill(countText(tasks.length, 'задача', 'задачи', 'задач'), 'code')}
              ${guides.length ? renderPill(`${guides.length} методический блок`) : ''}
              ${cluster.status ? renderPill(cluster.status) : ''}
            </div>
          </div>
          <div class="cluster-task-list">
            ${tasks.slice(0, 3).map(renderClusterTask).join('') || '<div class="empty">Пока нет задач в текущей выборке.</div>'}
          </div>
          <div class="quick-actions">
            <button class="button primary" type="button" data-open-cluster="${esc(cluster.id)}">Открыть кластер</button>
          </div>
        </div>
      `;
    }

    function renderClusterDirectory(items) {
      const clusters = (DB.task_clusters || [])
        .map(cluster => ({ cluster, count: clusterTaskCards(cluster.id).length }))
        .filter(item => clusterMatchesQuery(item.cluster))
        .filter(item => item.count > 0 || selectionHas('cluster', item.cluster.id))
        .sort((a, b) => b.count - a.count || labelFor('cluster', a.cluster.id).localeCompare(labelFor('cluster', b.cluster.id), 'ru', { numeric: true }));
      return `
        <div class="cluster-dashboard">
          ${renderClusterFocus(items)}
          <div class="cluster-directory">
            <h3>Каталог кластеров</h3>
            <div class="cluster-directory-grid">
              ${clusters.slice(0, 18).map(item => renderClusterCard(item.cluster)).join('') || '<div class="empty">Кластеры не найдены.</div>'}
            </div>
          </div>
        </div>
      `;
    }

    function renderStudyDirectory() {
      if (state.studyMode === 'clusters') return renderClusterDirectory(matchingCards());
      if (state.studyMode === 'sources_authors') {
        return `
          <div class="home-directory" id="sources-authors-directory">
            <div class="home-directory-grid">
              ${renderDirectoryColumn('source', 'Источники', 12)}
              ${renderDirectoryColumn('author', 'Авторы и создатели', 12)}
            </div>
            <p class="home-note">Кнопки здесь выставляют те же фильтры, что и выпадающие списки «Источник» и «Автор» в левой панели.</p>
          </div>
        `;
      }
      if (state.studyMode === 'difficulty_tags') {
        return `
          <div class="home-directory" id="difficulty-tags-directory">
            <div class="home-directory-grid">
              ${renderDirectoryColumn('scoreRange', 'Уровни по баллам', 8)}
              ${renderDirectoryColumn('difficultyMain', 'Сложность', 8)}
              ${renderDirectoryColumn('tag', 'Метки', 16)}
              ${renderDirectoryColumn('course', 'Уровень курса', 8)}
            </div>
            <p class="home-note">Кнопки выставляют реальные фильтры сложности, курса и тегов; результаты ниже пересчитываются сразу.</p>
          </div>
        `;
      }
      if (state.studyMode === 'definitions') {
        return `
          <div class="home-directory" id="definitions-directory">
            <div class="home-directory-grid">
              ${renderDirectoryColumn('definition', 'Определения', 24)}
            </div>
            <p class="home-note">Кнопки выставляют фильтр «Определения»; в выборку попадают и методические блоки, и обычные задачи, связанные с выбранным определением.</p>
          </div>
        `;
      }
      return '';
    }

    function renderStudyHome(items) {
      const imageCount = countBy(card => card.has_image);
      const theoryCount = countBy(card => matchesStudyMode(card, 'theory'));
      const problemCount = countBy(card => card.kind === 'problem');
      const quickHtml = quickModes.map(mode => {
        const active = mode.id === 'no_olympiad'
          ? state.excludeOlympiad === 'exclude'
          : state.studyMode === mode.id;
        const count = quickModeCount(mode);
        return `
          <button class="quick-button ${active ? 'active' : ''}" type="button" data-quick-mode="${esc(mode.id)}">
            ${esc(mode.label)} <span class="chip-count">${count}</span>
          </button>
        `;
      }).join('');
      byId('study-home').innerHTML = `
        <h2>Подготовка по дифференциальным уравнениям</h2>
        <p class="study-lead">Письменные маршруты, теория, кластеры и карточки с рисунками в одном учебном списке.</p>
        <div class="quick-actions">${quickHtml}</div>
        ${renderStudyDirectory()}
        <div class="home-stats">
          <div class="home-stat"><strong>${cards.length}</strong><span>карточек всего</span></div>
          <div class="home-stat"><strong>${problemCount}</strong><span>задачи</span></div>
          <div class="home-stat"><strong>${(DB.task_clusters || []).length}</strong><span>кластера</span></div>
          <div class="home-stat"><strong>${items.length}</strong><span>в текущей выборке</span></div>
          <div class="home-stat"><strong>${theoryCount}</strong><span>теория и леммы</span></div>
          <div class="home-stat"><strong>${imageCount}</strong><span>с рисунками</span></div>
        </div>
      `;
    }

    function hasActiveSearchContext() {
      if (state.q.trim()) return true;
      if (state.studyMode !== 'all') return true;
      if (state.excludeOlympiad !== 'all') return true;
      return filterKeys.some(key => key !== 'studyMode' && key !== 'excludeOlympiad' && selectedValues(key).length);
    }

    function renderViewerLanding() {
      const landingClusters = (DB.task_clusters || [])
        .map(cluster => ({ cluster, count: clusterTaskCards(cluster.id, { studyMode: 'clusters' }).length }))
        .filter(item => item.count > 0)
        .sort((a, b) => b.count - a.count || labelFor('cluster', a.cluster.id).localeCompare(labelFor('cluster', b.cluster.id), 'ru', { numeric: true }))
      byId('results').innerHTML = `
        <section class="home-directory" aria-label="Навигация по базе">
          <div class="home-directory-grid">
            <div>
              <h3>Начать с маршрута</h3>
              <div class="quick-actions">
                <button class="quick-button" type="button" data-quick-mode="clusters">Кластеры <span class="chip-count">${(DB.task_clusters || []).length}</span></button>
                <button class="quick-button" type="button" data-quick-mode="exam_simulation">Симуляция экзамена</button>
                <button class="quick-button" type="button" data-quick-mode="written_minimum">Письменный минимум</button>
                <button class="quick-button" type="button" data-quick-mode="exam_middle">Средний экзамен</button>
                <button class="quick-button" type="button" data-quick-mode="theory">Теория</button>
                <button class="quick-button" type="button" data-quick-mode="definitions">Определения</button>
              </div>
            </div>
            <div>
              <h3>Все кластеры</h3>
              <div class="chip-row">
                ${landingClusters.map(item => `
                  <button class="chip" type="button" data-open-cluster="${esc(item.cluster.id)}">
                    <span>${esc(labelFor('cluster', item.cluster.id))}</span><span class="chip-count">${item.count}</span>
                  </button>
                `).join('')}
              </div>
            </div>
          </div>
          <p class="home-note">Карточки задач появляются после выбора маршрута, кластера, фильтра или поискового запроса. Стартовая страница не является выдачей всех задач.</p>
        </section>
      `;
    }

    function renderExamStatus() {
      const estimate = examEstimate();
      const answered = examState.history.length;
      const correct = examState.history.filter(item => item.correct).length;
      const topics = new Set(examState.history.map(item => item.topic)).size;
      const maxQuestions = Number(examOverlay.max_questions || 5);
      return `
        <div class="exam-status">
          <div class="home-stat"><strong>${examState.currentLevel}</strong><span>текущий уровень</span></div>
          <div class="home-stat"><strong>${estimate.text}</strong><span>текущий разброс баллов</span></div>
          <div class="home-stat"><strong>${answered}/${maxQuestions}</strong><span>ответов дано</span></div>
          <div class="home-stat"><strong>${correct}</strong><span>ответов зачтено</span></div>
          <div class="home-stat"><strong>${topics}</strong><span>тем затронуто</span></div>
          <div class="home-stat"><strong>${Math.max(0, maxQuestions - answered)}</strong><span>вопросов максимум осталось</span></div>
        </div>
      `;
    }

    function renderExamAnswerControls(current) {
      const interaction = current.interaction;
      if (interaction.type === 'multiple_choice') {
        return `
          <div class="exam-choice-row">
            ${interaction.multiple ? '<div class="muted compact">Можно выбрать несколько вариантов.</div>' : ''}
            ${(interaction.choices || []).map(choice => `
              <button class="button exam-choice ${(interaction.multiple ? examState.selectedChoices.includes(choice.id) : examState.selectedChoice === choice.id) ? 'selected' : ''}" type="button" data-exam-choice="${esc(choice.id)}">
                ${renderMathText(choice.text)}
              </button>
            `).join('')}
            <button class="button primary" type="button" data-exam-submit="choice">Ответить</button>
          </div>
        `;
      }
      if (interaction.type === 'numeric' || interaction.type === 'formula') {
        return `
          <label>${interaction.type === 'numeric' ? 'Численный ответ' : 'Формула'}
            <input id="exam-answer-input" type="text" autocomplete="off" placeholder="Введите короткий ответ">
          </label>
          <button class="button primary" type="button" data-exam-submit="input">Ответить</button>
        `;
      }
      return `
        <div class="muted compact">Подсказки и критерии скрыты в режиме симуляции. Оцените ответ честно; после завершения можно открыть исходную карточку из обычного viewer.</div>
        <div class="quick-actions">
          <button class="button primary" type="button" data-exam-self="correct">Получилось без подсказки</button>
          <button class="button" type="button" data-exam-self="wrong">Не получилось / нужна подсказка</button>
        </div>
      `;
    }

    function renderExamCurrent() {
      const current = examState.current;
      if (!current) return '';
      const card = current.card;
      const problem = problemsById[card.id] || {};
      const interaction = current.interaction;
      const proofLabel = ['theorem', 'lemma', 'corollary', 'definition'].includes(card.kind) ? 'Доказательство' : 'Решение';
      const questionNumber = current.answered ? examState.history.length : examState.history.length + 1;
      const feedbackClass = current.correct ? 'good' : 'bad';
      const title = interaction.hasOverlayPrompt ? 'Экзаменационный вопрос' : (current.answered ? card.title : 'Экзаменационный вопрос');
      const statement = interaction.hasOverlayPrompt ? interaction.prompt : card.statement;
      const instruction = interaction.hasOverlayPrompt ? '' : interaction.prompt;
      const answeredControls = current.answered ? `
        <div class="exam-feedback ${feedbackClass}">
          <strong>${current.correct ? 'Зачтено.' : 'Не зачтено.'}</strong>
          <div class="tex-content">${renderMathText(current.feedback)}</div>
          <div class="exam-source-link">
            <button class="button primary" type="button" data-exam-next>${examState.finished || shouldFinishExam() ? 'Показать итог' : 'Следующий вопрос'}</button>
          </div>
        </div>
      ` : `<div class="exam-answer-area">${renderExamAnswerControls(current)}</div>`;
      return `
        <div class="exam-question">
          <div class="meta-row">
            ${renderPill(`вопрос ${questionNumber}`)}
            ${renderPill(`уровень ${examState.currentLevel}`)}
            ${renderPill(examTopicLabel(examTopic(card)))}
            ${renderPill(interaction.type === 'self_check' ? 'самопроверка' : interaction.type === 'multiple_choice' ? 'тест' : interaction.type === 'numeric' ? 'число' : 'формула')}
            ${renderPill(`идея ${card.idea_score ?? '-'}`)}
            ${renderPill(`техника ${card.technical_score ?? '-'}`)}
          </div>
          <h2 class="tex-content">${renderMathText(title)}</h2>
          <p class="statement tex-content">${renderMathText(statement)}</p>
          ${instruction ? `<div class="block tex-content"><strong>${renderMathText(instruction)}</strong></div>` : ''}
          ${answeredControls}
        </div>
      `;
    }

    function renderExamFinished() {
      const estimate = examEstimate();
      const correct = examState.history.filter(item => item.correct).length;
      const rows = examState.history.map((item, index) => `
        <div class="meta-row">
          ${renderPill(`${index + 1}`)}
          ${renderPill(item.correct ? 'зачтено' : 'не зачтено', item.correct ? 'good' : 'bad')}
          ${renderPill(`уровень ${item.level}`)}
          ${renderPill(examTopicLabel(item.topic))}
          ${renderPill(item.type === 'self_check' ? 'самопроверка' : item.type === 'multiple_choice' ? 'тест' : item.type === 'numeric' ? 'число' : 'формула')}
          ${renderPill(item.title)}
        </div>
      `).join('');
      return `
        <div class="exam-question">
          <h2>${examState.failed ? 'Симуляция завершилась провалом' : 'Симуляция завершена'}</h2>
          <p class="study-lead">${examState.failed
            ? 'Уровень опустился до 2. Это сигнал вернуться к простым задачам и повторить базовые определения.'
            : `Оценочный диапазон: ${estimate.low}-${estimate.high}. Зачтено ${correct} из ${examState.history.length}.`}</p>
          ${rows}
          <div class="quick-actions">
            <button class="button primary" type="button" data-exam-restart>Начать заново</button>
            <button class="button" type="button" data-quick-mode="exam_simulation">Выйти из симуляции</button>
          </div>
        </div>
      `;
    }

    function renderExamPanel() {
      const panel = byId('exam-panel');
      if (state.studyMode !== 'exam_simulation') {
        panel.classList.remove('active');
        panel.innerHTML = '';
        return;
      }
      panel.classList.add('active');
      const levels = examOverlay.start_levels || Array.from({ length: 8 }, (_, index) => index + 3);
      const intro = `
        <h2>Симуляция устного экзамена</h2>
        <p class="study-lead">Выберите стартовый уровень. После правильного ответа уровень растет, после ошибки падает; при уровне 2 симуляция заканчивается провалом. Обычно хватает четырех вопросов, пятый задается, если результат еще шумный.</p>
        <div class="exam-controls">
          <label>Начальный уровень
            <select id="exam-start-level">
              ${levels.map(level => `<option value="${level}" ${level === examState.startLevel ? 'selected' : ''}>${level}</option>`).join('')}
            </select>
          </label>
          <button class="button primary" type="button" data-exam-start>${examState.active ? 'Перезапустить симуляцию' : 'Начать симуляцию'}</button>
        </div>
      `;
      panel.innerHTML = `
        ${intro}
        ${examState.active ? renderExamStatus() : ''}
        ${examState.finished ? renderExamFinished() : renderExamCurrent()}
      `;
      renderMathIn(panel);
    }

    function renderSingleCardRoute(card) {
      byId('study-home').innerHTML = '';
      byId('exam-panel').classList.remove('active');
      byId('exam-panel').innerHTML = '';
      byId('summary').innerHTML = [
        renderPill('отдельная карточка', 'code'),
        renderPill(card.id, 'code')
      ].join('');

      const clusterLinks = (card.cluster_ids || []).map(clusterId => `
        <a class="cluster-back-link" href="${esc(clusterRouteHref(clusterId))}">
          <span>К странице кластера: ${esc(labelFor('cluster', clusterId))}</span>
        </a>
      `).join('');
      const relatedLinks = relatedCardsFor(card).map(item => `
        <a class="related-card-link" href="${esc(cardRouteHref(item.card.id))}">
          <span class="related-card-title tex-content">${renderMathText(item.card.title)}</span>
          <span class="related-card-meta">${esc(item.type)} · идея ${esc(item.card.idea_score ?? '-')} · техника ${esc(item.card.technical_score ?? '-')}</span>
          ${item.text ? `<span class="related-card-meta">${renderMathText(item.text)}</span>` : ''}
        </a>
      `).join('');

      byId('results').innerHTML = `
        <section class="single-card-nav" aria-label="Навигация карточки">
          <div class="single-card-actions">
            <a class="button primary" href="${esc(searchRouteHref())}">Назад к поиску</a>
            ${clusterLinks || '<span class="muted compact">Кластеры не указаны.</span>'}
          </div>
          <div>
            <h2>Связанные карточки</h2>
            <div class="related-card-list">
              ${relatedLinks || '<div class="empty">Связанные карточки не найдены.</div>'}
            </div>
          </div>
        </section>
        ${renderCard(card, { single: true })}
      `;
      renderMathIn(byId('results'));
    }

    function renderMissingCardRoute() {
      byId('study-home').innerHTML = '';
      byId('exam-panel').classList.remove('active');
      byId('exam-panel').innerHTML = '';
      byId('summary').innerHTML = renderPill('карточка не найдена', 'bad');
      byId('results').innerHTML = `
        <section class="single-card-nav" aria-label="Навигация карточки">
          <div class="single-card-actions">
            <a class="button primary" href="${esc(searchRouteHref())}">Назад к поиску</a>
          </div>
          <div class="empty">Карточка ${esc(navigation.cardId)} не найдена в текущем индексе.</div>
        </section>
      `;
    }

    function renderResults() {
      if (navigation.cardId) {
        const card = currentRouteCard();
        if (card) renderSingleCardRoute(card);
        else renderMissingCardRoute();
        return;
      }
      const rawItems = matchingCards();
      const items = state.studyMode === 'clusters' ? clusterSortedResults(rawItems) : sortedResults(rawItems);
      renderStudyHome(items);
      renderExamPanel();
      renderSummary(items);
      if (state.studyMode === 'exam_simulation') {
        byId('results').innerHTML = '<div class="empty">Во время симуляции список карточек скрыт, чтобы не подсказывать решение текущего вопроса.</div>';
        return;
      }
      if (state.studyMode === 'clusters') {
        byId('summary').innerHTML = [
          renderPill('навигация по кластерам', 'code'),
          renderPill(countText((DB.task_clusters || []).filter(clusterMatchesQuery).length, 'кластер найден', 'кластера найдено', 'кластеров найдено')),
          ...selectedValues('cluster').map(id => renderPill(labelFor('cluster', id), 'good'))
        ].join('');
        byId('results').innerHTML = '';
        return;
      }
      if (!hasActiveSearchContext()) {
        byId('summary').innerHTML = [
          renderPill('главная навигация', 'code'),
          renderPill(countText(cards.length, 'карточка', 'карточки', 'карточек')),
          renderPill(countText((DB.task_clusters || []).length, 'кластер', 'кластера', 'кластеров'))
        ].join('');
        renderViewerLanding();
        return;
      }
      byId('results').innerHTML = items.length
        ? items.map(renderCard).join('')
        : '<div class="empty">Ничего не найдено. Ослабьте фильтры или сбросьте их.</div>';
      renderMathIn(byId('results'));
    }

    function render() {
      const meta = DB.meta || {};
      const problemCount = meta.problem_count ?? countBy(card => card.kind === 'problem');
      const relationCount = (DB.relations || []).length;
      const clusterCount = (DB.task_clusters || []).length;
      byId('db-meta').textContent = [
        countText(cards.length, 'карточка', 'карточки', 'карточек'),
        countText(problemCount, 'задача', 'задачи', 'задач'),
        countText(relationCount, 'связь', 'связи', 'связей'),
        countText(clusterCount, 'кластер', 'кластера', 'кластеров')
      ].join(', ');
      document.body.classList.toggle('single-card-route', Boolean(navigation.cardId));
      renderFilters();
      renderActiveFilters();
      renderFacets();
      renderResults();
    }

    function scrollToResults() {
      const target = byId('results');
      if (!target) return;
      requestAnimationFrame(() => target.scrollIntoView({ block: 'start', behavior: 'smooth' }));
    }

    function scrollToNavigationTarget() {
      const panelId = state.studyMode === 'sources_authors'
        ? 'sources-authors-directory'
        : state.studyMode === 'difficulty_tags'
          ? 'difficulty-tags-directory'
          : state.studyMode === 'definitions'
            ? 'definitions-directory'
            : state.studyMode === 'exam_simulation'
              ? 'exam-panel'
              : state.studyMode === 'clusters'
                ? 'clusters-directory'
                : 'results';
      const target = byId(panelId) || byId('results');
      if (!target) return;
      requestAnimationFrame(() => target.scrollIntoView({ block: 'start', behavior: 'smooth' }));
    }

    function clearAllFilters() {
      state.q = '';
      for (const key of filterKeys) state[key] = 'all';
      state.sort = 'title';
      navigation.focus = '';
      navigation.cardId = '';
    }

    function activateQuickMode(mode, toggle = false) {
      if (mode === 'no_olympiad') {
        state.excludeOlympiad = toggle && state.excludeOlympiad === 'exclude' ? 'all' : 'exclude';
        return;
      }
      state.studyMode = toggle && state.studyMode === mode ? 'all' : mode;
      if (state.studyMode === 'all') return;
      if (mode.startsWith('written_') || mode === 'exam_middle') state.excludeOlympiad = 'exclude';
      if (mode === 'exam_simulation') state.excludeOlympiad = 'exclude';
      if (mode === 'written_minimum') state.sort = 'difficulty_asc';
      if (mode === 'written_middle') state.scoreRange = 'middle';
      if (mode === 'exam_middle') state.sort = 'difficulty_asc';
      if (mode === 'exam_simulation') state.sort = 'difficulty_asc';
      if (mode === 'written_strong') state.sort = 'idea_desc';
    }

    function applyInitialNavigation() {
      const params = new URLSearchParams(window.location.search || '');
      const nav = (params.get('nav') || params.get('mode') || '').toLowerCase();
      if (nav) clearAllFilters();
      if (nav === 'cards' || nav === 'search') {
        navigation.focus = 'q';
      } else if (nav === 'clusters') {
        activateQuickMode('clusters');
        navigation.focus = 'cluster';
      } else if (nav === 'exam' || nav === 'exam_simulation') {
        activateQuickMode('exam_simulation');
        navigation.focus = 'exam';
      } else if (nav === 'theory') {
        activateQuickMode('theory');
      } else if (nav === 'definitions' || nav === 'definition') {
        activateQuickMode('definitions');
        navigation.focus = 'definition';
      } else if (nav === 'problems' || nav === 'tasks') {
        activateQuickMode('problems');
      } else if (nav === 'sources' || nav === 'authors') {
        activateQuickMode('sources_authors');
        navigation.focus = 'source';
      } else if (nav === 'difficulty' || nav === 'tags') {
        activateQuickMode('difficulty_tags');
        navigation.focus = 'tag';
      } else if (quickModes.some(mode => mode.id === nav)) {
        activateQuickMode(nav);
      }
      const query = params.get('q');
      if (query != null) state.q = query;
      for (const key of filterKeys) {
        const paramKey = key === 'studyMode' ? 'mode' : key;
        const values = params.getAll(paramKey)
          .flatMap(value => String(value).split('||'))
          .flatMap(value => String(value).split(','))
          .map(value => value.trim())
          .filter(Boolean);
        if (!values.length) continue;
        if (isMultiFilter(key)) state[key] = normalizeSelection(key, values);
        else state[key] = values[values.length - 1];
      }
      const sort = params.get('sort');
      if (sort) state.sort = sort;
      const linkedCardId = params.get('card') || params.get('id') || linkedCardIdFromHash();
      if (linkedCardId && isolateCardContext(linkedCardId) && window.history?.replaceState) {
        window.history.replaceState(null, '', cardRouteHref(linkedCardId));
      }
    }

    function syncQueryParams() {
      if (!window.history?.replaceState) return;
      const params = new URLSearchParams();
      if (navigation.cardId) params.set('card', navigation.cardId);
      if (state.q.trim()) params.set('q', state.q.trim());
      for (const key of filterKeys) {
        const values = selectedValues(key);
        if (!values.length) continue;
        const paramKey = key === 'studyMode' ? 'mode' : key;
        if (isMultiFilter(key)) {
          for (const value of values) params.append(paramKey, value);
        } else {
          params.set(paramKey, values[0]);
        }
      }
      if (state.sort && state.sort !== 'title') params.set('sort', state.sort);
      const query = params.toString();
      const nextUrl = `${window.location.pathname}${query ? `?${query}` : ''}${window.location.hash || ''}`;
      window.history.replaceState(null, '', nextUrl);
    }

    function focusInitialNavigationControl() {
      if (!navigation.focus) return;
      const controlIdByFocus = {
        q: 'q',
        source: 'source',
        cluster: 'cluster',
        definition: 'definition',
        tag: 'tag'
      };
      const control = byId(controlIdByFocus[navigation.focus]);
      if (control) requestAnimationFrame(() => control.focus({ preventScroll: true }));
    }

    for (const [key, config] of Object.entries(selectConfig)) {
      if (!config.id) continue;
      byId(config.id).addEventListener('change', event => {
        navigation.cardId = '';
        const value = isMultiFilter(key)
          ? [...event.target.selectedOptions].map(option => option.value).filter(value => value !== 'all')
          : event.target.value;
        setFilterSelection(key, value);
        render();
        syncQueryParams();
        scrollToResults();
      });
    }

    byId('q').addEventListener('input', event => {
      navigation.cardId = '';
      state.q = event.target.value;
      render();
      syncQueryParams();
    });

    byId('sort').addEventListener('change', event => {
      navigation.cardId = '';
      state.sort = event.target.value;
      render();
      syncQueryParams();
      scrollToResults();
    });

    byId('reset').addEventListener('click', () => {
      clearAllFilters();
      render();
      syncQueryParams();
      scrollToResults();
    });

    document.addEventListener('click', event => {
      const directCardButton = event.target.closest('[data-open-card], [data-route-card-id]');
      if (directCardButton) {
        openCardRoute(directCardButton.dataset.openCard || directCardButton.dataset.routeCardId || '');
        return;
      }
      const clusterButton = event.target.closest('[data-open-cluster]');
      if (clusterButton) {
        openClusterRoute(clusterButton.dataset.openCluster || '');
        return;
      }
      const cardArticle = event.target.closest('[data-open-card-id]');
      if (cardArticle && !event.target.closest('a, button, input, select, textarea, summary, details, .reveal')) {
        openCardRoute(cardArticle.dataset.openCardId || '');
        return;
      }
      const setButton = event.target.closest('[data-set-filter]');
      if (setButton) {
        navigation.cardId = '';
        const key = setButton.dataset.setFilter;
        const value = setButton.dataset.filterValue;
        if (setButton.dataset.filterScope === 'card') {
          clearAllFilters();
          if (key === 'cluster') activateQuickMode('clusters');
          setFilterSelection(key, value);
        } else {
          setFilterSelection(key, value, true);
        }
        render();
        syncQueryParams();
        scrollToResults();
        return;
      }
      const clearButton = event.target.closest('[data-clear-filter]');
      if (clearButton) {
        navigation.cardId = '';
        const key = clearButton.dataset.clearFilter;
        clearFilterSelection(key, clearButton.dataset.clearValue || '');
        render();
        syncQueryParams();
        scrollToResults();
        return;
      }
      const quickButton = event.target.closest('[data-quick-mode]');
      if (quickButton) {
        navigation.cardId = '';
        const mode = quickButton.dataset.quickMode;
        activateQuickMode(mode, true);
        render();
        syncQueryParams();
        scrollToNavigationTarget();
        return;
      }
      const examStart = event.target.closest('[data-exam-start]');
      if (examStart) {
        startExam(Number(byId('exam-start-level')?.value || examState.startLevel || 5));
        scrollToResults();
        return;
      }
      const examRestart = event.target.closest('[data-exam-restart]');
      if (examRestart) {
        startExam(examState.startLevel);
        scrollToResults();
        return;
      }
      const examChoice = event.target.closest('[data-exam-choice]');
      if (examChoice) {
        const choice = examChoice.dataset.examChoice;
        if (examState.current?.interaction?.multiple) {
          examState.selectedChoices = examState.selectedChoices.includes(choice)
            ? examState.selectedChoices.filter(item => item !== choice)
            : [...examState.selectedChoices, choice];
        } else {
          examState.selectedChoice = choice;
        }
        renderExamPanel();
        return;
      }
      const examSubmit = event.target.closest('[data-exam-submit]');
      if (examSubmit) {
        submitExamAnswer();
        scrollToResults();
        return;
      }
      const examSelf = event.target.closest('[data-exam-self]');
      if (examSelf) {
        submitExamAnswer(examSelf.dataset.examSelf === 'correct');
        scrollToResults();
        return;
      }
      const examNext = event.target.closest('[data-exam-next]');
      if (examNext) {
        nextExamQuestion();
        scrollToResults();
      }
    });

    window.addEventListener('popstate', () => {
      clearAllFilters();
      applyInitialNavigation();
      render();
      if (navigation.cardId) requestAnimationFrame(() => window.scrollTo({ top: 0, behavior: 'smooth' }));
      else if (navigation.focus) scrollToNavigationTarget();
    });

    applyInitialNavigation();
    render();
    focusInitialNavigationControl();
    if (navigation.cardId) requestAnimationFrame(() => window.scrollTo({ top: 0, behavior: 'smooth' }));
    else if (navigation.focus) scrollToNavigationTarget();
    window.addEventListener('hashchange', () => {
      if (!isolateCardContext(linkedCardIdFromHash())) return;
      if (window.history?.replaceState) window.history.replaceState(null, '', cardRouteHref(navigation.cardId));
      render();
      requestAnimationFrame(() => window.scrollTo({ top: 0, behavior: 'smooth' }));
    });
    window.addEventListener('load', () => renderMathIn(document));
  </script>
</body>
</html>
"""
    return page.replace("__PAYLOAD__", payload).replace("__COURSE_TAGS__", course_tags)


def main():
    data = build_data()
    viewer_out = ROOT / "viewer" / "index.html"
    viewer_out.parent.mkdir(exist_ok=True)
    viewer_out.write_text(build_html(data), encoding="utf-8")
    print(f"OK: wrote {viewer_out}")

    home_out = ROOT / "index.html"
    home_out.write_text(build_home_html(data), encoding="utf-8")
    print(f"OK: wrote {home_out}")


if __name__ == "__main__":
    main()
