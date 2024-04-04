
-- 01문제
SELECT FirstName, BirthDate, Notes
  FROM employees
 WHERE lastName = 'King';
  
  
-- 02문제
SELECT ProductName, Price
  FROM Products
 WHERE ProductName like 'C%'
   AND Price > 20
 ORDER BY Price DESC;
 
 
 -- 03문제
 SELECT CategoryID, SUM(Price), MAX(Price), MIN(Price)
   FROM Products 
  GROUP BY CategoryID;
 
 
 -- 04문제
 SELECT *, CASE
			WHEN cnt > 10 THEN '많음'
            ELSE '적음'
		   END 'check'
    FROM (
	 SELECT CategoryID,
			count(*) AS cnt
	   FROM Products
	  GROUP BY CategoryID
	) AS pc;
    
    
 -- 05문제
 SELECT country, cnt, (cnt / all_cnt) * 100 as 백분위
 FROM (
 SELECT country,
		count(*) AS cnt,
        (select count(*) from Customers) AS all_cnt
   FROM customers
  GROUP BY country
  ) AS c;
 
 
 
 
 
 
 
 
 
 
 
 