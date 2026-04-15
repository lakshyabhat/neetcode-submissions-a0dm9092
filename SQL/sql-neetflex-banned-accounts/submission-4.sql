-- Write your query below
select distinct l1.account_id
from 
log_info l1 
inner join log_info l2 
on l1.account_id = l2.account_id
where l1.ip_address != l2.ip_address 
    and l1.logout >= l2.login
    and l1.login <= l2.login
    and TO_CHAR(l1.login,'YYYY-MM-DD') = TO_CHAR(l2.login,'YYYY-MM-DD')
