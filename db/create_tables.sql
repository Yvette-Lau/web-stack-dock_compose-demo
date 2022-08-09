DROP DATABASE IF EXISTS employee;

CREATE TABLE employee (
  empid INT NOT NULL,
  empname varchar(100) NOT NULL,
  email varchar(100) NOT NULL,
  PRIMARY KEY (empid)
);