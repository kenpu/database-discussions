with recursive T(n) as (
    values (1)
    union
    select n+1 from T where n < 10
)
select * from T;
