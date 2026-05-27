# Теоретико-методический блок: implicit-ode-discriminant

Дата: 2026-05-27.

## Что добавлено

- Создана теоретическая карточка `cluster-implicit-ode-discriminant-method-guide` в `data/problems/cluster_audit/implicit_ode_discriminant/`.
- Карточка добавлена в representatives кластера `implicit-ode-discriminant` и в batch `cluster-implicit-ode-discriminant`.
- Подключены `definition_ids` без дублирования определений: `initial_value_problem`, `cauchy_problem`, `integral_curve`, `general_solution`, `particular_solution`, `singular_solution`, `discriminant_curve`, `direction_field`, `solution`.
- Уточнены `definition_ids` у representative-карточек: `local-du-written-2022-implicit-discriminant`, `local-du-written-2020-clairaut-shifted-envelope`, `local-du-written-2014-51-lagrange-singular-curves`, `clairaut-envelope`, `cluster-implicit-branch-switch-square-root`, `cluster-implicit-discriminant-not-solution`.
- Добавлены два открытых источника в `data/sources/sources.yaml`: `src-libretexts-herman-first-order` и `src-brown-dobrush-singular-solutions`.

## Какие методы покрыты

- Переход от `F(x,y,p)=0` к регулярным ветвям `p=f_i(x,y)` при `F_p != 0`.
- Поиск дискриминантного множества через `F=0`, `F_p=0` и проекция на плоскость `(x,y)`.
- Проверка, является ли дискриминантная кривая решением: график `y=phi(x)`, вычисление `phi'(x)` и подстановка в исходное уравнение.
- Разделение ролей: дискриминант, особое решение, огибающая, граница поля направлений и место переключения ветвей.
- Уравнения Клеро и Лагранжа как учебные якоря: `p=y'`, дифференцирование, ветвь `p=const`, параметризация через `p`, огибающие.
- Ветвление задачи Коши: подсчет допустимых наклонов, регулярные ветви, потеря единственности на дискриминанте.

## Связи

Добавлены relations от методического блока к ключевым representatives:

- `local-du-written-2022-implicit-discriminant`
- `cluster-implicit-branch-switch-square-root`
- `cluster-implicit-discriminant-not-solution`
- `local-du-written-2020-clairaut-shifted-envelope`
- `local-du-written-2014-51-lagrange-singular-curves`

Соседние содержательные связи добавлены только как границы метода:

- `cluster-existence-implicit-ivp-local` -> `cluster-implicit-ode-discriminant-method-guide`: регулярная неявная IVP против дискриминантного случая `F_p=0`.
- `cluster-recover-translated-parabolas-envelope` -> `cluster-implicit-ode-discriminant-method-guide`: огибающая из заданного семейства против анализа уже заданного `F(x,y,p)=0`.
- `linear-first-order-formula` -> `cluster-implicit-ode-discriminant-method-guide`: нормальная форма с одной правой частью против выбора ветвей.

## Источники

В карточке использованы 6 источников в принятом формате:

- локальная программа `src-local-du-8-program-or-exam`;
- локальные письменные экзамены `src-local-du-written-exams`;
- Романко `src-romanko-problem-book`;
- Филиппов `src-filippov-problem-book`;
- LibreTexts/Herman `src-libretexts-herman-first-order`;
- Brown/Dobrushkin `src-brown-dobrush-singular-solutions`.

## Оставшиеся пробелы

- Нет отдельного компактного representative на cusp/caustic-дискриминант с новой геометрией; добавлять стоит только при действительно новом механизме.
- Нет отдельной карточки с полной классификацией impasse points; для базового курса это сейчас избыточно.
- Варианты Клеро/Лагранжа с другими коэффициентами по-прежнему не добавлять: кластер уже имеет дедупликационные якоря и методический блок.
