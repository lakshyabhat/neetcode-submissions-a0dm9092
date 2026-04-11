-- Write your query below

select transaction_id
from
(select transaction_id, day,
DENSE_RANK() OVER (PARTITION BY day::DATE order by amount desc) as rnk 
from transactions)
where rnk = 1 
order by transaction_id
