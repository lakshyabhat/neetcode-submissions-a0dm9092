-- Write your query below

select player_id,device_id
from
(select player_id, device_id, 
DENSE_RANK() OVER (PARTITION BY player_id ORDER BY event_date) as rnk
from
activity) player_device_rank
where rnk = 1