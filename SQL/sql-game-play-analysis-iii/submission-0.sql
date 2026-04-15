-- Write your query below
select player_id,event_date, SUM(games_played) OVER (PARTITION BY player_id ORDER BY event_date) as games_played_so_far
from activity