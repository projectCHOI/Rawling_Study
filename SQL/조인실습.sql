
SELECT Customers.CustomerID,
	   CustomerName,
	   OrderDate
  FROM Customers
 INNER JOIN Orders
    ON Customers.CustomerID = Orders.CustomerID
 ORDER BY Customers.CustomerID;
    
SELECT Customers.CustomerID,
	   CustomerName,
	   OrderDate
  FROM Customers, Orders
 WHERE Customers.CustomerID = Orders.CustomerID;
 
 SELECT Customers.CustomerID, Orders.CustomerID
   FROM Customers
   LEFT JOIN Orders
     ON Customers.CustomerID = Orders.CustomerID;
  
  SELECT Customers.CustomerID, Orders.CustomerID
   FROM Customers
   RIGHT JOIN Orders
     ON Customers.CustomerID = Orders.CustomerID;
     
 