-- Write your query below
select
id,
CASE WHEN p_id is NULL then 'Root'
WHEN id IN (SELECT p_id from tree) THEN 'Inner'
ELSE 'Leaf' END AS type
from
tree