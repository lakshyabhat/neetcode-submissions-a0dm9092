-- Write your query below
select customer_number
from
(select customer_number,COUNT(order_number) from
orders group by customer_number order by 2 desc limit 1)