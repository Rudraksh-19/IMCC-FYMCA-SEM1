-- Filtering data from table
-- where, select distinct, and, or, not, in, between, like, limit, is null

drop database organization;

create database organization;

use organization;

create table employee (Emp_id int not null primary key,
first_name varchar(15), last_name varchar(15),
Gender char, role varchar(15), Dept varchar(15), Manager_id varchar(10)
);

insert into employee values (1, 'Rudra', 'Bhumkar', 'M', 'Team Leader', 'Retail', 'M11');
insert into employee values (2, 'Vedant', 'Pawar', 'M', 'Team Leader', 'Finance', 'M12');
insert into employee values (3, 'Dipak', 'Deshmukh', 'M', 'Manager', 'Retail', 'M13');
insert into employee values (4, 'Manoj', 'Kulkarni', 'M', 'Manager', 'HR', 'M14');
insert into employee values (5, 'Harshad', 'Kale', 'M', 'President', 'HR', 'M15');
insert into employee values (6, 'Parmeshwar', 'Bhumre', 'M', 'President', 'Finance', 'M16');

select * from employee;

-- distince keyword -> distince clause in the select stmt is used to eliminate duplicate rows from the result 

select distinct Dept from employee order by Dept;

select distinct role from employee order by role;

-- and operatior -> it is logical op which combines 2 or more boolean expressions and returns 1, 0 or null.
-- AND op is used with WHERE clause

select * from employee where role='President' and dept='Retail';

select * from employee where role ='President' and dept = 'HR';

-- OR Operator -> or op is the logical op that combines two Boolean expressions and return 1
-- (true) if either of the expression is true
-- The OR Operator is used for the filtering the data with WHERE clause

select * from employee where role = 'Manager' or dept = 'Team Leader';

-- IN Operator -> IN Operator is used to determine if a value matcher any other value in a list
-- if the value epuals any value in the list (val1,val2,val3,...) it returns 1 (true) otherwise returns 0 (false)

select * from employee where role in ('President','Manager');

select * from employee where role in ('TM','CEO');

/* NOT IN Operator -> is formed by combining the NOT and IN operator
it is used to determine if a value does not match any of the values in a list */

select * from employee where role not in ('President','Manager');

/* BETWEEN Operator -> logical op that determines whether a valuse velongs in a range.
it returns null, if the value, low, or high (Out of range) is NULL */

alter table employee add column Experience int;

update employee set experience=8 where emp_id=1;
update employee set experience=5 where emp_id=2;
update employee set experience=8 where emp_id=3;
update employee set experience=6 where emp_id=4;
update employee set experience=2 where emp_id=5;
update employee set experience=10 where emp_id=6;

select * from employee;

select * from employee where Experience between 6 and 10;

select * from employee where Experience = 5 or experience = 10;

/* Like Operator -> logical op that determines whether or not a string contains a specified pattern */

select * from employee where last_name like 'P%';

select * from employee where last_name like 'M%';

select * from employee where first_name like 'P%';

/* LIMIT Operator -> limit clause in the SELECT
stmt is used to limit the no. of rows returned */

select * from Employee;

select * from employee order by experience limit 5;

/* IS NULL -> it determines whether or not a value is NULL.
the exp returns true 1, if the value is NULL
or returns false 0 */

insert into employee values (7, 'Asha','Joshi','F','President','HR', ' ' , null);

insert into employee (emp_id, first_name, last_name, Gender, Role, Dept) values (8, 'Vedika','Dahale','F','Team Leader','Finance');

select * from employee where manager_id is null;

select * from employee where experience is null;

/* IS NOT NULL Operator -> 

*/
select * from employee where experience is not null;

select count(*) from employee;

select count(emp_id) from employee where dept = 'Finance';

select count(Experience) from employee;
select max(Experience) from employee;
select min(Experience) from employee;
select sum(Experience) from employee;
select avg(Experience) as emp_exr from employee;

select * from employee;




