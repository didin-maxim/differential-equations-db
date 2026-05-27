import json

from build_index import COURSE_TAGS, build_data
from lib import ROOT


def safe_json(data):
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


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
      <div class="result-grid" id="results"></div>
    </main>
  </div>

  <script id="db-data" type="application/json">__PAYLOAD__</script>
  <script>
    const DB = JSON.parse(document.getElementById('db-data').textContent);
    const COURSE_TAGS = __COURSE_TAGS__;
    const cards = DB.cards || [];
    const problemsById = Object.fromEntries((DB.problems || []).map(problem => [problem.id, problem]));
    const sourceById = Object.fromEntries((DB.sources || []).map(item => [item.id, item]));
    const ideaById = Object.fromEntries((DB.standard_ideas || []).map(item => [item.id, item]));
    const clusterById = Object.fromEntries((DB.task_clusters || []).map(item => [item.id, item]));

    const state = {
      q: '',
      studyMode: 'all',
      ideaScore: 'all',
      technicalScore: 'all',
      scoreRange: 'all',
      excludeOlympiad: 'all',
      assetFilter: 'all',
      source: 'all',
      author: 'all',
      cluster: 'all',
      standardIdea: 'all',
      tag: 'all',
      kind: 'all',
      course: 'all',
      publicReady: 'all',
      reviewStatus: 'all',
      difficultyMain: 'all',
      sort: 'title'
    };

    const filterKeys = [
      'studyMode', 'ideaScore', 'technicalScore', 'scoreRange', 'excludeOlympiad', 'assetFilter',
      'source', 'author', 'cluster', 'standardIdea',
      'tag', 'kind', 'course', 'publicReady', 'reviewStatus', 'difficultyMain'
    ];

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
      tag: { id: 'tag', label: 'Тег', all: 'Все теги' },
      kind: { id: 'kind', label: 'Тип', all: 'Все типы' },
      course: { id: 'course', label: 'Курс', all: 'Все уровни курса' },
      publicReady: { id: 'public-ready', label: 'Готовность', all: 'Любая готовность' },
      reviewStatus: { id: 'review-status', label: 'Статус проверки', all: 'Любой статус проверки' },
      difficultyMain: { id: 'difficulty-main', label: 'Сложность', all: 'Любая сложность' }
    };

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

    const quickModes = [
      { id: 'written_minimum', label: 'Письменный минимум' },
      { id: 'written_middle', label: 'Средний письменный' },
      { id: 'exam_middle', label: 'Средний экзамен' },
      { id: 'written_strong', label: 'Сильный письменный' },
      { id: 'theory', label: 'Теория' },
      { id: 'clusters', label: 'Кластеры' },
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

    function renderMathText(text) {
      return prettifyPlainMath(esc(text || ''));
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

    function matchesStudyMode(card, mode) {
      if (!mode || mode === 'all') return true;
      if (mode === 'no_olympiad') return !isOlympiadLike(card);
      if (mode === 'theory') {
        return ['theorem', 'lemma', 'definition', 'corollary'].includes(card.kind)
          || hasAnyTag(card, ['theory_assignment', 'standard_theory']);
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
        const selected = filters[key];
        if (!selected || selected === 'all') continue;
        if (key === 'studyMode' || key === 'excludeOlympiad') continue;
        if (!valuesFor(card, key).map(String).includes(String(selected))) return false;
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
      const selected = state[key];
      const allCount = matchingCards({ [key]: 'all' }).length;
      const options = uniqueOptions(key)
        .map(value => ({ value, label: labelFor(key, value), count: optionCount(key, value) }))
        .filter(option => option.count > 0 || option.value === selected);
      byId(config.id).innerHTML = [
        `<option value="all">${esc(config.all)} (${allCount})</option>`,
        ...options.map(option => `<option value="${esc(option.value)}">${esc(option.label)} (${option.count})</option>`)
      ].join('');
      byId(config.id).value = options.some(option => option.value === selected) ? selected : 'all';
      if (byId(config.id).value !== selected) state[key] = 'all';
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
        if (state[key] !== 'all') {
          items.push({ key, label: `${selectConfig[key].label}: ${labelFor(key, state[key])}` });
        }
      }
      byId('active-filters').innerHTML = items.map(item => `
        <button class="chip active" type="button" data-clear-filter="${esc(item.key)}">${esc(item.label)} ×</button>
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
              <button class="chip ${state[key] === row.value ? 'active' : ''}" type="button" data-set-filter="${esc(key)}" data-filter-value="${esc(row.value)}">
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
      const activeClass = state[key] === String(value) ? ' active' : '';
      return `
        <button class="chip ${esc(cls)}${activeClass}" type="button" data-set-filter="${esc(key)}" data-filter-value="${esc(value)}" title="${esc(`Показать карточки: ${text}`)}">
          <span>${esc(text)}</span>
        </button>
      `;
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

    function renderCard(card) {
      const problem = problemsById[card.id] || {};
      const proofLabel = ['theorem', 'lemma', 'corollary', 'definition'].includes(card.kind) ? 'Доказательство' : 'Решение';
      const sourceBadges = (card.source_ids || []).slice(0, 3).map(id => renderFilterChip('source', id, labelFor('source', id))).join('');
      const clusterBadges = (card.cluster_ids || []).slice(0, 2).map(id => renderFilterChip('cluster', id, labelFor('cluster', id), 'good')).join('');
      const tagBadges = (card.tags || []).slice(0, 7).map(tag => renderFilterChip('tag', tag, tag)).join('');
      const ideaBadges = (card.standard_idea_ids || []).slice(0, 3).map(id => renderFilterChip('standardIdea', id, labelFor('standardIdea', id))).join('');
      const ideasHtml = renderIdeas(problem);
      const solutionsHtml = renderSolutions(problem, proofLabel);
      return `
        <article class="card" id="card-${esc(card.id)}">
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
          <div class="meta-row">${sourceBadges}${clusterBadges}${ideaBadges}${tagBadges}</div>
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

    function renderStudyHome(items) {
      const imageCount = countBy(card => card.has_image);
      const theoryCount = countBy(card => matchesStudyMode(card, 'theory'));
      const problemCount = countBy(card => card.kind === 'problem');
      const noOlympiadCount = countBy(card => !isOlympiadLike(card));
      const quickHtml = quickModes.map(mode => {
        const active = mode.id === 'no_olympiad'
          ? state.excludeOlympiad === 'exclude'
          : state.studyMode === mode.id;
        const count = mode.id === 'no_olympiad'
          ? noOlympiadCount
          : countBy(card => matchesStudyMode(card, mode.id));
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

    function renderResults() {
      const items = sortedResults(matchingCards());
      renderStudyHome(items);
      renderSummary(items);
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

    for (const [key, config] of Object.entries(selectConfig)) {
      if (!config.id) continue;
      byId(config.id).addEventListener('change', event => {
        state[key] = event.target.value;
        render();
        scrollToResults();
      });
    }

    byId('q').addEventListener('input', event => {
      state.q = event.target.value;
      render();
    });

    byId('sort').addEventListener('change', event => {
      state.sort = event.target.value;
      render();
      scrollToResults();
    });

    byId('reset').addEventListener('click', () => {
      state.q = '';
      for (const key of filterKeys) state[key] = 'all';
      render();
      scrollToResults();
    });

    document.addEventListener('click', event => {
      const setButton = event.target.closest('[data-set-filter]');
      if (setButton) {
        const key = setButton.dataset.setFilter;
        const value = setButton.dataset.filterValue;
        state[key] = state[key] === value ? 'all' : value;
        render();
        scrollToResults();
        return;
      }
      const clearButton = event.target.closest('[data-clear-filter]');
      if (clearButton) {
        const key = clearButton.dataset.clearFilter;
        if (key === 'q') state.q = '';
        else state[key] = 'all';
        render();
        scrollToResults();
        return;
      }
      const quickButton = event.target.closest('[data-quick-mode]');
      if (quickButton) {
        const mode = quickButton.dataset.quickMode;
        if (mode === 'no_olympiad') {
          state.excludeOlympiad = state.excludeOlympiad === 'exclude' ? 'all' : 'exclude';
        } else {
          state.studyMode = state.studyMode === mode ? 'all' : mode;
          if (mode.startsWith('written_') || mode === 'exam_middle') state.excludeOlympiad = 'exclude';
          if (mode === 'written_minimum') state.sort = 'difficulty_asc';
          if (mode === 'written_middle') state.scoreRange = 'middle';
          if (mode === 'exam_middle') state.sort = 'difficulty_asc';
          if (mode === 'written_strong') state.sort = 'idea_desc';
        }
        render();
        scrollToResults();
      }
    });

    render();
    window.addEventListener('load', () => renderMathIn(document));
  </script>
</body>
</html>
"""
    return page.replace("__PAYLOAD__", payload).replace("__COURSE_TAGS__", course_tags)


def main():
    data = build_data()
    out = ROOT / "viewer" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(build_html(data), encoding="utf-8")
    print(f"OK: wrote {out}")


if __name__ == "__main__":
    main()
