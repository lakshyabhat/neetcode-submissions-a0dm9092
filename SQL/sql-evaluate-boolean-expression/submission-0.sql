-- Write your query below
select
left_operand,
operator,
right_operand,
CASE 
    WHEN operator = '>' and vl.value > vr.value THEN True
    WHEN operator = '<' and vl.value < vr.value THEN True
    WHEN operator = '=' and vl.value = vr.value THEN True
    ELSE False END as value
from expressions e
inner join variables vl on vl.name = e.left_operand
inner join variables vr on vr.name = e.right_operand
