-- Write your query below
select employee_id, count(employee_id) OVER (PARTITION BY team_id) as team_size
from employee