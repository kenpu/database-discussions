.header on
.mode column
.width 30 10

with T(n) as (
    select count(distinct semester)
    from schedule
    where semester > '2015' and (semester like '%01' or semester like '%09')
)
select instructor, count(distinct semester) as s
from schedule
where semester > '2015' and actual > 100
group by instructor
having s = (select n from T);
