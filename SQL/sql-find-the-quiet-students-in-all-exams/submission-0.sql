-- Write your query below


with max_min_score
as
(select exam_id,e.student_id, score, 
MAX(score) OVER (PARTITION BY exam_id) as max_score,
MIN(score) OVER (PARTITION BY exam_id) as min_score,
COUNT(exam_id) OVER (PARTITION BY e.student_id) as count_exam,
student_name
from exam e
inner join student s on e.student_id = s.student_id),
quiet_students
as 
(select student_id,student_name, count_exam,count(exam_id) as count_exam_quiet
from max_min_score 
where score < max_score and score > min_score
group by student_id,student_name,count_exam
)

select student_id,student_name
from
quiet_students
where count_exam = count_exam_quiet