--
--
--

.mode column
.header on
.width 4 10 10 10

with schedule_2016 as (
    select * from schedule
    where semester like '2016%'
), weekdays(weekday) as (
    select distinct weekday from schedule_2016
), lectures(weekday, nLectures) as (
    select weekday, count(*)
    from schedule_2016
    where schtype = 'Lecture'
    group by weekday
), tutorials(weekday, nTutorials) as (
    select weekday, count(*)
    from schedule_2016
    where schtype = 'Tutorial'
    group by weekday
), labs(weekday, nLabs) as (
    select weekday, count(*)
    from schedule_2016
    where schtype = 'Laboratory'
    group by weekday
), counts as (
    select weekday, 
        CASE WHEN nLectures ISNULL THEN 0 ELSE nLectures end as lectures,
        CASE WHEN nTutorials ISNULL THEN 0 ELSE nTutorials end as tutorials,
        CASE WHEN nLabs ISNULL THEN 0 ELSE nLabs end as labs
    from weekdays left join lectures using (weekday)
        left join tutorials using (weekday)
        left join labs using (weekday)
)
select *, lectures + tutorials + labs as total
from counts
order by total desc;
