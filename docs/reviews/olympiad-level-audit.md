# Аудит олимпиадного уровня выше экзамена

Дата: 2026-05-27.

Зона проверки: карточки `data/problems/**` с `difficulty.idea_score > 10`, олимпиадные карточки с `local_score > 10`, метки `olympiad_above_exam`, `olympiad_style`, `beyond_standard_course`, `advanced_standard_course`, отчеты `docs/reviews/olympiad-*.md`, `olympiad-import-queue.md`, `local-du-gap-and-dedup-report.md`, `english-import-qa.md`, а также `data/task_clusters/clusters.yaml`.

## Итог

- Явных обычных экзаменационных шаблонов с `idea_score > 10` после нормального распознавания идеи не найдено.
- Две карточки снижены с `idea_score=11` до `idea_score=10`, потому что аудит выделил для них переносимый шаблон:
  - `putnam-modern-2023-a3`: угловое сравнение; оставлена олимпиадная метка, но задача больше не считается уникальной 11+.
  - `ru-misc-nure-8-3`: логарифмическая производная для пары `y`, `y^2`; добавлено обобщение `y`, `y^m`.
- Карточка `msu-ode-2023-8-fourth-order-zero-count-review` оставлена без понижения и без удаления: это честный `needs_solution_completion` / `needs_human_review` случай. Ее не надо делать публичной или использовать как solved representative, пока не закрыта лемма о дисконъюгированности четвертого порядка.
- Добавлено 5 компактных карточек в `data/problems/cluster_audit/olympiad_level/`; это не новые архивные задачи, а theorem/lemma/standard-idea слой для повторяющихся мотивов.

## Проверенные верхние карточки

| card | решение аудита |
|---|---|
| `putnam-modern-2010-b5` | Оставлена `idea_score=12`: композиционное `f'=f(f)` с глобальным противоречием не сводится к обычной экзаменационной формуле. Связана с функционально-дифференциальным кластером как более уникальный представитель. |
| `putnam-modern-2005-b3` | Оставлена `idea_score=11`: инволюция `x -> a/x` плюс логарифмическая переменная являются переносимым, но все еще олимпиадным вышеэкзаменационным ходом. |
| `putnam-modern-1999-b4` | Оставлена `idea_score=11`: даже после выделения леммы про оценки назад задача требует склеить несколько неравенств и алгебраический финал. |
| `putnam-early-1955-a7-zero-bounds` | Оставлена `idea_score=11`: задача относится к насыщенному Sturm/zero-location блоку, но конкретный знаковый анализ нулей не является обычной экзаменационной заготовкой. |
| `msu-ode-2023-8-fourth-order-zero-count-review` | Оставлена как review-only: нет полного решения, ключевой ход зависит от внепрограммной леммы. |
| `putnam-modern-2023-a3` | Снижена до `idea_score=10`: угловая скорость вынесена в общую лемму `olympiad-level-angle-speed-comparison`. |
| `ru-misc-nure-8-3` | Снижена до `idea_score=10`: вынесено обобщение `olympiad-level-power-solution-linear-ode-criterion`. |

## Повторяющиеся мотивы

### Множитель + Ролль/MVT

Представители: `imc-1994-p3-rolle-integrating-factor`, `imc-2023-p7-boundary-linear-expression`, `imc-2025-p6-derivative-of-f-over-x`, `putnam-early-1954-i3-concurrent-tangents`.

Добавлено:

- `olympiad-level-rolle-after-homogeneous-factor`
- новый кластер `olympiad-transformed-linear-mvt`

Политика: не добавлять новые карточки, если меняется только множитель `e^{-x}`, `1/x` или другое простое решение однородного уравнения.

### Дифференциальные неравенства и барьеры

Представители: `putnam-modern-1994-b3`, `putnam-modern-1997-b2`, `putnam-modern-1999-b4`, `putnam-modern-2009-b5`, `putnam-modern-2023-a3`, `ru-misc-nure-8-2`, `ru-misc-nure-8-5`, `ru-misc-nure-8-8`.

Добавлено:

- `olympiad-level-angle-speed-comparison`
- `olympiad-level-backward-positivity-derivative-lemma`
- новый кластер `olympiad-differential-inequalities-barriers`

Политика: отделять выбор барьера от вычислительной тяжести. Если новая задача только меняет константы в `arctan`, энергии или сравнении, достаточно relation.

### Функционально-дифференциальные уравнения

Представители: `putnam-modern-2005-b3`, `putnam-modern-2010-b5`, `solve-functional-ode-composition`, `ru-misc-kfu-2019-19-3`.

Добавлено:

- `olympiad-level-involution-functional-differential`
- новый кластер `olympiad-functional-differential-equations`

Политика: Putnam 2010 B5 пока оставить как уникальный композиционный nonexistence-тип; новая общая теорема нужна только если появятся еще близкие задачи.

### Логарифмическая производная для степеней решения

Представитель: `ru-misc-nure-8-3`.

Добавлено:

- `olympiad-level-power-solution-linear-ode-criterion`

Вывод: исходная карточка не одиночная в идейном смысле; у нее есть естественное обобщение `y` и `y^m`, поэтому оценка идеи снижена до 10.

## Уникальные / спорные случаи

- `msu-ode-2023-8-fourth-order-zero-count-review`: уникальная и неполная. Оставить `public_ready=false`, `needs_solution_completion`, relation к `liouville-wronskian-formula` со статусом review. Не использовать как основание для нового saturated high-order zero-count кластера без полного доказательства.
- `putnam-modern-2010-b5`: родственная функционально-дифференциальному кластеру, но не шаблон после 3-5 решений. Связь с `olympiad-level-involution-functional-differential` сделана как contrast, а не same_method.
- `putnam-early-1975-a5-wronskian-nonlinear-transform`: родственен нелинейным преобразованиям решений линейного уравнения, но механизм Wronskian/Pinney отличается от `y^m`; добавлена contrast-связь.

## Изменения

Новые карточки:

- `data/problems/cluster_audit/olympiad_level/olympiad-level-rolle-after-homogeneous-factor.yaml`
- `data/problems/cluster_audit/olympiad_level/olympiad-level-angle-speed-comparison.yaml`
- `data/problems/cluster_audit/olympiad_level/olympiad-level-backward-positivity-derivative-lemma.yaml`
- `data/problems/cluster_audit/olympiad_level/olympiad-level-involution-functional-differential.yaml`
- `data/problems/cluster_audit/olympiad_level/olympiad-level-power-solution-linear-ode-criterion.yaml`

Новые связи:

- `data/relations/relations.d/cluster-olympiad-level.yaml`

Новый batch:

- `data/import_batches/cluster-olympiad-level.yaml`

Обновлены кластеры:

- `olympiad-transformed-linear-mvt`
- `olympiad-differential-inequalities-barriers`
- `olympiad-functional-differential-equations`

Снижены оценки:

- `putnam-modern-2023-a3`: `idea_score/local_score 11 -> 10`, `technical_score=5` оставлен.
- `ru-misc-nure-8-3`: `idea_score/local_score 11 -> 10`, `technical_score=7` оставлен.

## Проверки

```powershell
python tools\validate.py
python tools\check_links.py
python tools\audit_rules.py
python tools\check_clusters.py
python tools\build_index.py
python tools\build_viewer.py
```

Результат прогона 2026-05-27:

- `validate.py` - OK: 303 cards, 341 relations, 26 sources.
- `check_links.py` - OK.
- `audit_rules.py` - OK, 0 warnings.
- `check_clusters.py` - OK: 22 task clusters.
- `build_index.py` - OK, rebuilt `index/generated.json`.
- `build_viewer.py` - OK, rebuilt `viewer/index.html`.
- Дополнительно `check_encoding.py` - OK.
