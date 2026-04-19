-- Write your query below
with caller_id_country
as
(select c.name,SUM(duration) as total_duration,COUNT(caller_id) as cnt
from calls a
left join person p on a.caller_id = id
left join country c on c.country_code = LEFT(p.phone_number,3)
group by c.name),
callee_id_country
as
(
select c.name,SUM(duration) as total_duration,COUNT(callee_id) as cnt
from calls a
left join person p on a.callee_id = id
left join country c on c.country_code = LEFT(p.phone_number,3)
group by c.name
),
combine
as
(
select name, total_duration,cnt from caller_id_country
union all
select name,total_duration,cnt from callee_id_country
),
average_call
as
(
select sum(total_duration)/SUM(cnt) as global_avg
from combine
),
avg_call
as
(select name,sum(total_duration)/sum(cnt) as avg_call_country,global_avg
from combine
cross join average_call
group by name,global_avg)


select name as country
from avg_call
where avg_call_country > global_avg