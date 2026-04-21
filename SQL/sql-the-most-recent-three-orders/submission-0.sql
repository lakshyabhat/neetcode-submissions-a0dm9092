-- Write your query below

select customer_name,
customer_id,
order_id,
order_date
from
(select distinct name as customer_name, 
order_date,
c.customer_id,
order_id,
DENSE_RANK() OVER (PARTITION BY o.customer_id ORDER BY order_date desc) as rnk
from
orders o 
    inner join customers c on c.customer_id = o.customer_id) a
where rnk <= 3
order by 1,2,4 desc
