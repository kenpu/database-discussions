drop index if exists idx_instructor;
create index if not exists idx_instructor ON schedule(instructor, actual);

with S as (
    select * from schedule
    where semester > '2015' and schtype = 'Lecture'
),
T(n) as (
    select count(distinct semester)
    from schedule
    where semester > '2015' and (semester like '%01' or semester like '%09')
)
select distinct instructor 
from S S1
where (select count(distinct semester) 
        from S S2
        where S2.instructor = S1.instructor and S2.actual > 100) = (select n from T);
