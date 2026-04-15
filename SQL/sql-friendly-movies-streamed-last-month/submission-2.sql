-- Write your query below
select distinct title
from content where kids_content = 'Y'
and content_id IN (select content_id from tv_program where TO_CHAR(program_date::DATE,'YYYY-MM') = '2020-06')
and content_type = 'Movies'