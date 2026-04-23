-- Write your query below
with grp as
(select 
log_id,
log_id - ROW_NUMBER() OVER (ORDER BY log_id) as g
from logs
)

select
min(log_id) as start_id,
max(log_id) as end_id
from
grp
group by g
order by 1,2