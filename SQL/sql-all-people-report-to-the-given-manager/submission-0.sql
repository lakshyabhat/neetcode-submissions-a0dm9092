-- Write your query below
select e1.employee_id
from employees e1 
inner join employees m1 on e1.manager_id = m1.employee_id 
inner join employees m2 on m1.manager_id = m2.employee_id
inner join employees m3 on m2.manager_id = m3.employee_id
where e1.employee_id !=1 and (m1.manager_id = 1 or m2.manager_id = 1 or m3.manager_id = 1)