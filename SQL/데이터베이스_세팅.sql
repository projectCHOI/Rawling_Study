-- 데이터베이스 생성
CREATE DATABASE yr2772 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 계정생성
CREATE USER 'hiiu2'@'%' IDENTIFIED BY 'hiiu2';

-- 계정확인
USE MYSQL;
SELECT user, host
  FROM user;
  
-- 권한                  
GRANT ALL PRIVILEGES ON ljb8802.* TO '각자계정'@'%';
