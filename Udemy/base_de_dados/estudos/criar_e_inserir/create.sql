-- create database
CREATE DATABASE base_de_estudos;

-- create user
CREATE USER 'estudante1' IDENTIFIED BY 'estudante';

-- create permission
GRANT ALL PRIVILEGES ON base_de_estudos.* TO 'estudante1';

-- create table
CREATE TABLE base_de_estudos.customers(
id INT AUTO_INCREMENT PRIMARY KEY,
FirstName VARCHAR(50),
LastName VARCHAR(50),
Age INT,
Email VARCHAR(100),
Phone VARCHAR(50),
Address VARCHAR(200),
city VARCHAR(50),
PostalCode INT,
State VARCHAR(50)
)