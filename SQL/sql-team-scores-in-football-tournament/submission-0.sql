-- Write your query below
with match_score as 
(select host_team,guest_team,
SUM(CASE WHEN host_goals > guest_goals THEN 3
WHEN host_goals < guest_goals THEN 0
ELSE 1 END) AS host_points,
SUM(CASE WHEN host_goals < guest_goals THEN 3
WHEN host_goals > guest_goals THEN 0
ELSE 1 END) AS guest_points
from matches group by host_team,guest_team
),
host_points as 
(select team_id,  team_name, SUM(host_points) as num_points
from 
teams t left join
match_score m on t.team_id = m.host_team
group by team_id,team_name),
guest_points as
(select team_id,  team_name, SUM(guest_points) as num_points
from 
teams t left join
match_score m on t.team_id = m.guest_team
group by team_id,team_name),
union_points as
(select team_id,team_name,num_points from host_points
UNION ALL
select team_id,team_name,num_points from guest_points
)

select team_id,team_name,COALESCE(SUM(num_points),0) as num_points
from union_points group by team_id,team_name order by num_points desc, team_id
