-- Write your query below
select name
from
sales_person
where sales_id NOT IN (select sales_id from orders 
    where com_id = (select com_id from company where name = 'CRIMSON'))