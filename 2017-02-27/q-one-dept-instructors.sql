.header on
.mode column
.width 30 5 10
with T0 as (
    select instructor, substr(code, 1, 4) as dept, count(distinct semester || code) freq
    from schedule
    where instructor not like 'X %'
    group by instructor, dept
), T1 as (
    select instructor, count(distinct dept) as n
    from T0
    group by instructor
)
select T1.instructor, T0.dept, T0.freq
from T1 join T0 using (instructor)
where T1.n = 1
order by dept;

