# Write your MySQL query statement below
select name as Customers from customers
where Id not in (select CustomerId from orders);
