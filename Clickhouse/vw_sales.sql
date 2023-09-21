create view vw_sales 
as
with timest as (
select id,
toDateTime64(LEFT(REPLACE(REPLACE(created_at,'T', ' '), 'Z',''),23), 3,'America/New_York')  - INTERVAL 4 HOUR as created_date
from `default`.sales
)
select s.*, t.created_date, toDateTime64(now(), 3,'America/New_York') as dt
from `default`.sales s
inner join timest t on s.id = t.id