-- Write your query below
select seller_name from seller
where 
seller_id NOT IN 
(select 
    seller_id 
        from orders where TO_CHAR(sale_date,'yyyy') = '2020')
order by seller_name