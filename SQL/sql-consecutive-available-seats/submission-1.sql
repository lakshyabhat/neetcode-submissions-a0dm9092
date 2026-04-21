-- Write your query below
select a.seat_id 
    from cinema a
    left join cinema b on a.seat_id = b.seat_id - 1
    left join cinema c on a.seat_id = c.seat_id + 1
    where a.free = 1 and (b.free = 1 or c.free = 1)
    order by 1