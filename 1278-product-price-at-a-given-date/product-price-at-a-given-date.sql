WITH t1 AS
(SELECT DISTINCT product_id, MAX(change_date) last_day
FROM Products
WHERE change_date<='2019-08-16'
group by product_id )

SELECT t1.product_id, p.new_price price
FROM t1
JOIN Products p
ON t1.product_id=p.product_id AND t1.last_day=p.change_date

UNION

SELECT product_id, 10 price
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM t1)