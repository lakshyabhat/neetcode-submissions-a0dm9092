-- Write your query below
select customer_id,product_id,product_name
from
(select o.customer_id,o.product_id,
product_name, 
DENSE_RANK() OVER (PARTITION BY o.customer_id ORDER BY COUNT(*) desc) as rnk from orders o
inner join products p on o.product_id = p.product_id
inner join customers c on c.customer_id = o.customer_id
group by o.customer_id,o.product_id,product_name
) a
where rnk = 1