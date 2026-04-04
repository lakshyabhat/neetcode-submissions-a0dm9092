-- Write your query below
select
name as warehouse_name,
sum(width*length*height*units) as volume
from
warehouse w 
    inner join products p on w.product_id = p.product_id
    group by name