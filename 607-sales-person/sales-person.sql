SELECT name from SalesPerson 
Where sales_id NOT IN
(
SELECT sales_id from Orders where
com_id =
(
    SELECT com_id from Company where 
name='RED'));