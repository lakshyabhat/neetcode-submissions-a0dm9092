-- Write your query below

select project_id,employee_id
from
(select project_id,
p.employee_id,
DENSE_RANK() OVER (PARTITION BY project_id ORDER BY experience_years desc) as rnk
from  
project p inner join 
employee e on p.employee_id = e.employee_id and p.employee_id!=999) a
where rnk = 1

