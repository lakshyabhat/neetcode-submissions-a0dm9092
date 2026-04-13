-- Write your query below

select employee_id
from
(select employee_id from employees where employee_id NOT IN (select employee_id from salaries)
UNION
select employee_id from salaries where employee_id NOT IN (select employee_id from employees) ) a
order by 1