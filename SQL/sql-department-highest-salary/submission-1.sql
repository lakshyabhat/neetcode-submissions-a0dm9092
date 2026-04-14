-- Write your query below
select department, employee, salary
from
(select d.name as department, e.name as employee, salary, DENSE_RANK() OVER (PARTITION BY d.name ORDER BY salary desc) as rnk
from 
employee e 
inner join department d on e.department_id = d.id) a
where rnk = 1
order by 2