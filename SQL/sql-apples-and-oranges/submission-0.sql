-- Write your query below
with sales_apples as
(select * from sales where fruit = 'apples'),
sales_oranges as
(select * from sales where fruit = 'oranges')


select a.sale_date, a.sold_num - o.sold_num as diff
from sales_apples a  
    inner join sales_oranges o on a.sale_date = o.sale_date