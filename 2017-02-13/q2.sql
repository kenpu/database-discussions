.mode column
.header off

--
-- list the people in Mary's circle
--
select 'Marys circle';

.header on

WITH marycircle(name) AS (
    SELECT y from friends where x = 'mary'
    UNION
    SELECT F.y
    FROM marycircle T join friends F on T.name = F.x
) SELECT * from marycircle;

select "Everyone's circle";

WITH fof(name1, name2) AS (
    SELECT x, y FROM friends
    UNION
    SELECT name1, y
    FROM fof JOIN friends on name2 = x
) SELECT * FROM fof;

select "Everyone's cirlce:";

.width 10 10 40
WITH f0 AS (
    SELECT * FROM friends
    UNION
    SELECT y, x FROM friends
), fof(name1, name2, path) AS (
    SELECT x, y, x || "-" || y FROM f0
    UNION
    SELECT name1, y, path || "-" || y
    FROM fof JOIN f0 on name2 = x
    WHERE instr(path, y) = 0 and (NOT name1 = y)
) select * from fof order by name1, name2;


