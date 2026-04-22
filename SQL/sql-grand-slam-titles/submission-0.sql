-- Write your query below
with player_id_win_count
as
(select wimbledon as player_id, count(wimbledon) as grand_slams_count
from championships
group by wimbledon
union all
select fr_open as player_id, count(fr_open) as grand_slams_count
from championships
group by fr_open
union all
select us_open as player_id, count(us_open) as grand_slams_count
from championships
group by us_open
union all
select au_open as player_id, count(au_open) as grand_slams_count
from championships
group by au_open)

select p.player_id,
p.player_name,
sum(grand_slams_count) as grand_slams_count
from
players p 
inner join player_id_win_count w on p.player_id = w.player_id
group by p.player_id, p.player_name
