USE ljb8802;

CREATE TABLE Persons (
	PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

DROP TABLE Persons;

CREATE TABLE Persons (
	SEQ int NOT NULL AUTO_INCREMENT,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255),
    PRIMARY KEY(SEQ)
);

ALTER TABLE Persons
ADD Email varchar(255);

USE ljb8802;

CREATE TABLE Students (
	studentNumber int NOT NULL AUTO_INCREMENT,
    name varchar(10),
    age int,
    address varchar(200),
    PRIMARY KEY(studentNumber)
);

CREATE TABLE Grades (
	studentNumber int,
    math int,
    english int,
    science int
);



USE ljb8802;

INSERT INTO persons (LastName, FirstName, Address, City, Email)
     VALUES ('이', '진범', '인천', '인천', 'dante@fins.ai');
     
SELECT *
  FROM persons;
  
DELETE FROM persons WHERE SEQ = 10;

UPDATE persons
   SET LastName = '홍',
	   FirstName = '길동'
 WHERE SEQ = 2;


INSERT INTO students (name, age, address) VALUES ('홍길동', 30, '인천광역시');
INSERT INTO students (name, age, address) VALUES ('이연걸', 60, '서울특별시');
INSERT INTO students (name, age, address) VALUES ('이몽룡', 42, '대전광역시');
INSERT INTO students (name, age, address) VALUES ('성춘향', 27, '경기도');

SELECT *
  FROM students;

INSERT INTO grades (studentNumber, math, english, science) VALUES (1, 90, 80, 50);
INSERT INTO grades VALUES (2, 69, 76, 65);
INSERT INTO grades VALUES (3, 98, 87, 97);
INSERT INTO grades VALUES (4, 87, 67, 79);

SELECT *
  FROM grades;





---------------- 데이터조회


USE w3schools;

SELECT *
  FROM author;

SELECT DISTINCT CustomerName, Country
  FROM w3schools.customers;
  
SELECT DISTINCT Country
  FROM w3schools.customers;

SELECT *
  FROM w3schools.customers
 WHERE country = 'France';
 
SELECT *
  FROM w3schools.customers
 WHERE ContactName like 'Mar%';
 
 SELECT *
  FROM w3schools.customers
 WHERE ContactName like '%et';
 
 SELECT *
  FROM w3schools.customers
 WHERE ContactName like '%te%';

SELECT *
  FROM w3schools.customers
 WHERE Country = 'France'
   AND CustomerName like 'La%';
   

SELECT *
  FROM w3schools.customers
 WHERE (Country = 'France' OR CustomerName like 'LA%');

SELECT *
  FROM w3schools.customers
 WHERE NOT Country = 'France';
 
 SELECT *
  FROM w3schools.customers
 WHERE Country != 'France';

SELECT *
  FROM w3schools.customers
 WHERE Country IN ('France', 'Spain');
 
SELECT *
  FROM w3schools.Products
 WHERE price BETWEEN 10 AND 15;
 
SELECT *
  FROM w3schools.products
 WHERE price >= 10
   AND price <= 15;

SELECT *
  FROM w3schools.Products
 WHERE ProductID IN (
		SELECT ProductID
		  FROM w3schools.Products
		 WHERE price BETWEEN 10 AND 15
 );
 
SELECT *
  FROM w3schools.Customers 
 WHERE PostalCode IS NOT null;
 
 
SELECT *
  FROM Customers
 ORDER BY CustomerName;
 
 SELECT *
   FROM products
  ORDER BY Price DESC;
  
  SELECT *
    FROM Customers
ORDER BY Country, CustomerName DESC;

SELECT *
  FROM Customers
 WHERE Country = 'UK'
 LIMIT 3;
 
 SELECT Price,
		CASE
          WHEN Price < 30 THEN '저'
          WHEN Price >= 30 AND Price <= 50 THEN '중'
          ELSE '고'
		END AS PriceGroup
   FROM products;
   
   SELECT COUNT(*) AS cnt
     FROM Customers
    WHERE Country = 'France';
    
    SELECT AVG(Price) AS PriceAvg
      FROM Products;
      
    SELECT MAX(Price)
      FROM Products;
      
    SELECT MIN(Price)
      FROM Products;
      
	SELECT SUM(Quantity)
      FROM order_details;
	
   SELECT country, count(*) as CNT
     FROM customers
	GROUP BY country
    ORDER BY CNT;
    
SELECT country, city, count(*) as CNT
  FROM customers
 GROUP BY country, city
 ORDER BY CNT DESC;


SELECT country, count(*) as CNT
  FROM customers
 GROUP BY country
HAVING CNT > 5;


SELECT *
FROM (
	SELECT country, count(*) as CNT
	  FROM customers
	 GROUP BY country
 ) AS a
 WHERE CNT > 5; 
  
  
  SELECT country as coun,
		 (SELECT count(*) FROM customers) as ALL_CNT,
		 count(*) as CNT
    FROM customers
   GROUP BY country;
  
  
  
  SELECT *
   FROM customers
   WHERE country = 'France'
   UNION ALL
   SELECT *
   FROM customers
   WHERE country = 'UK';

     
   
   
 
 
  
 
 






















