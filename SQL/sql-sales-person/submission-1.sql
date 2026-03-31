-- Write your query below
select name
from
sales_person
where sales_id NOT IN 
(select sales_id from orders o
    inner join company c on o.com_id = c.com_id 
    where name = 'CRIMSON')