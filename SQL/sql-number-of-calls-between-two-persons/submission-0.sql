-- Write your query below
with calls_1 as 
(select from_id as person1, to_id as person2, count(*) as  call_count,sum(duration) as total_duration
from calls 
where from_id < to_id
group by from_id, to_id
),
calls_2 as 
(select to_id as person1,from_id as person2, count(*) as  call_count,sum(duration) as total_duration
from calls 
where from_id > to_id
group by from_id, to_id)



select person1,person2,sum(call_count) as call_count ,sum(total_duration) as total_duration
from
(select person1,person2,call_count,total_duration
from calls_1
union all
select person1,person2,call_count,total_duration
from calls_2)
group by person1,person2