# Write your MySQL query statement below
Select product.product_name, sales.year, sales.price from sales left join product on sales.product_id = product.product_id