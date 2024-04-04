 -- 01문제 특강 73p
SELECT suppliers.city
	  ,suppliers.SupplierName
      ,products.productName
      ,products.price
  FROM suppliers
 INNER JOIN Products
    ON suppliers. SupplierID = Products. SupplierID
 WHERE suppliers. City = 'Tokyo';
 

  -- 02문제 특강 73p
SELECT CategoyName, ProductName
  FROM Categories
 INNER JOIN Products
    ON Categories.CategoryID = Products.CategoryID
 WHERE Categories.CategoryName = 'SeaFood';
 
 
   -- 03문제 특강 73p
SELECT suppliers. Country,
	   Categories. CategoryName,
       count(*) as cnt,
       avg(price) as avg
  FROM suppliers, Products, Categories
 WHERE suppliers. SupplierID = Products. SupplierID 
   AND Products. SupplierID = Categories. CountryID
 GROUP BY suppliers. Country, Categories. CountryID
 ORDER BY Country, CategoryName;
 
 
    -- 04문제 특강 73p
SELECT 
avg
FROM 
INNER JOIN
ON


    -- 01문제(5) 특강 74p
SELECT supplier SupplierName,
       sum(Quantity)
avg
FROM 
INNER JOIN
ON
    
    -- 02문제(6) 특강 74p


    -- 03문제(7) 특강 74p
    