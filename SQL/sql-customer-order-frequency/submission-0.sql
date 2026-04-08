-- Write your query below


select customer_id, name
from
(select c.customer_id, 
name,
SUM(CASE WHEN TO_CHAR(order_date,'YYYY-MM') = '2020-06' THEN quantity*price ELSE 0 END) as spend_june,
SUM(CASE WHEN TO_CHAR(order_date,'YYYY-MM') = '2020-07' THEN quantity*price ELSE 0 END) as spend_july
from orders o 
    inner join product p on o.product_id = p.product_id
    inner join customers c on o.customer_id = c.customer_id
    group by c.customer_id)
    where spend_june >= 100 and spend_july >= 100

