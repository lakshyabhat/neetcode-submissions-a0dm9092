-- Write your query below

select 
ROUND((COUNT(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE NULL END)*100.0)/count(delivery_id),2) as immediate_percentage
from delivery