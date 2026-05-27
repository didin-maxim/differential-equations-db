# Аудит кластера ортогональных траекторий

Дата: 2026-05-27.

## Что проверено

- В базе уже была карточка `orthogonal-trajectories-circles` про окружности `x^2+y^2=C` и прямые через начало. Это близкий базовый представитель, но не пучок окружностей через две общие точки.
- В `recover-ode-from-family` есть Waterloo-карточка про восстановление ОДУ по семейству касательных окружностей. Она методически близка, но это не задача на ортогональные траектории.
- Отдельного кластера `orthogonal-trajectories` до аудита не было.

## Добавлено

- `cluster-orthogonal-coaxal-real-base-points`: пучок окружностей через `(1,0)` и `(-1,0)`, ортогональный пучок `x^2+y^2-2bx+1=0`.
- `cluster-orthogonal-coaxal-imaginary-base-points`: пучок `x^2+y^2-2ax+1=0` без действительных общих точек, ортогональный пучок `x^2+y^2-2by-1=0`.
- `cluster-orthogonal-confocal-conics-gradient`: софокусные эллипсы и гиперболы, доказательство ортогональности через градиенты `r1+r2` и `r1-r2`.

## Источники и авторство

Надежного точного автора для этих конкретных учебных формулировок не найдено. Это классическая геометрия/фольклор задач на ортогональные траектории; формулировки и решения написаны заново для базы.

Использованы как проверочные источники:

- MathWorld, Coaxal Circles: https://mathworld.wolfram.com/CoaxalCircles.html
- MathWorld, Confocal Conics: https://mathworld.wolfram.com/ConfocalConics.html
- MathWorld, Confocal Ellipses: https://mathworld.wolfram.com/ConfocalEllipses.html
- NPTEL, Orthogonal Trajectories: https://archive.nptel.ac.in/content/storage2/courses/122104018/node67.html
- Euler Archive E390, `Considerationes de traiectoriis orthogonalibus`: https://scholarlycommons.pacific.edu/euler-works/390/

В `data/sources/sources.yaml` добавлен `src-classical-orthogonal-trajectories`.

## Дедупликация

Новые карточки не дублируют `orthogonal-trajectories-circles`: базовая задача имеет концентрические окружности и прямые, а новые окружностные карточки работают с сопряженными коаксиальными пучками. Они также не пополняют массово `recover-ode-from-family`: восстановление ОДУ используется только как шаг внутри ортогональных траекторий.

Связи записаны только в `data/relations/relations.d/cluster-orthogonal-trajectories.yaml`, batch - в `data/import_batches/cluster-orthogonal-trajectories.yaml`.
