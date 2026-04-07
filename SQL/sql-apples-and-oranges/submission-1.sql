-- Write your query below

select a.sale_date, a.sold_num - o.sold_num as diff
from sales a  
    inner join sales o 
        on a.sale_date = o.sale_date
        where a.fruit = 'apples' and o.fruit = 'oranges'
        ORDER BY a.sale_date;