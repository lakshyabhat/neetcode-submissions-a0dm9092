-- Write your query below

select student_id, exam_id, score
from
(select 
student_id,
exam_id, 
score,
DENSE_RANK() OVER (PARTITION BY student_id ORDER BY score desc,exam_id) as rnk
from
exam_results) a
where rnk = 1
