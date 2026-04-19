-- Write your query below
select c.name as country
from country c
inner join person p on c.country_code = LEFT(p.phone_number,3)
inner join calls ca on ca.caller_id = p.id or ca.callee_id = p.id
group by c.name
having avg(ca.duration) > (select avg(duration) from calls)

