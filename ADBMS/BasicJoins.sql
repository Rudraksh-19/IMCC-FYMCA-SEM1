-- Basics of Join queries 

Drop database BasicJoin;
Create database BasicJoin;
use BasicJoin;

Create table employees (
	emp_id int primary key,
    ename varchar(50)
    );
-- drop table employees;
desc employees;

insert into employees (emp_id, ename)
values (101, 'Raghav'), 
(102, 'Rashi'),
(103, 'Rohan'),
(104, 'Rudra'),
(105, 'Ravi');

Create table projects (
	project_id int primary key,
    pname varchar(50),
    emp_id int,
    foreign key(emp_id) references employees(emp_id)
    );
drop table projects;
desc projects;

insert into projects (project_id, pname, emp_id)
values (1 , 'Project A', 101 ), 
(2 , 'Project b', 102 ), 
(3 , 'Project c', 101 ), 
(4 , 'Project d', 103 );

select * from projects;

insert into Projects values (5, 'Project E', 103);
insert into Projects values (8, 'Project F', null);
insert into employees values (106, 'Sanjay');
insert into employees values (107, 'Sakshi');

/* Inner Join 
Only matching record will be displayed 
from employees table and projects table 
*/

select * from employees Join projects On employees.emp_id = projects.emp_id;  -- (inner) join ==> join {by default}

/* fetch the employee name and the project name, 
they belong to */

select e.ename, p.pname from employees e inner join projects p on e.emp_id = p.emp_id;

select e.ename, p.pname from employees e right join projects p on e.emp_id = p.emp_id;

select e.ename, p.pname from projects p right join employees e on e.emp_id = p.emp_id;


select e.emp_id, e.ename, p.pname from employees e left join projects p on e.emp_id = p.emp_id;

insert into projects values (7, 'Project G', 105);
insert into projects (project_id, pname) values (9, 'Project H');


/* Full outer join using Union 
It display all matching and non-matching data from both tables 
*/

select * from employees 
left join projects
on employees.emp_id = projects.emp_id 
Union
select * from employees
right join projects 
on employees.emp_id = projects.emp_id;

/* Display employee names who has been assigned any project */

select employees.ename, projects.pname from employees
left join projects on employees.emp_id = projects.emp_id
where projects.emp_id is not null;

/* Display employee names who has NOT been assigned any project */
select employees.ename, projects.pname from employees
left join projects on employees.emp_id = projects.emp_id
where projects.emp_id is null;

-- Projects who has not been assigned to any employee
select employees.ename, projects.pname from employees
right join projects on employees.emp_id = projects.emp_id
where projects.emp_id is null;


