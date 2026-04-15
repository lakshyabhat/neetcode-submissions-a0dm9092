-- Write your query below


with friendship
as
(select user2_id as friend from
friendship where user1_id = 1
union
select user1_id as friend from friendship
where user2_id = 1)


select distinct page_id as recommended_page from likes
where user_id IN (select friend from friendship)
AND page_id not in  (select page_id from likes where user_id = 1)
