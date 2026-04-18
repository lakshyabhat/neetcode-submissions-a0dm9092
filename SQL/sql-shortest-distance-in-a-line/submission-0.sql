-- Write your query below

select min(diff) as shortest
from
(select x -  LAG(x) OVER (ORDER BY x) as diff
from point) a