-- Write your query below


select product_name,product_id,order_id, order_date
from
(select product_name,p.product_id,order_id, order_date,
DENSE_RANK() OVER (PARTITION BY o.product_id ORDER BY order_date desc) as rnk
from orders o
inner join products p on o.product_id = p.product_id) a
where rnk = 1
order by 1,2,3