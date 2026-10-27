
create database user;

use user;

create table customer(custid int,custname varchar(15),city varchar(10),product varchar(15),price int);

desc customer;

insert into customer values(1,'manas','nashik','pc',10000),
(2,'sahil','nashik','mobile',10000),
(3,'shivam','nashik','pc',10000),
(4,'manas','nashik','pen',1000),
(5,'sujal','pune','mouse',1000);

select * from customer;

select custid,custname,city from customer;

select * from customer where custid=3;

select * from customer where custid in(1,3);

create table clonetable as select * from customer;
select * from clonetable;

drop table clonetable;

select custname,product,price from customer where price>15000;
select custname,product,price from customer where price<10000;

select * from customer where city='nashik';
select * from customer order by price;
select * from customer order by price desc;
select * from customer order by price,city;
select * from customer order by city desc,price asc;


select upper(custname),lower(product) from customer where custid<3;
select upper(custname),lower(product) from customer;

alter table customer add lastname varchar(15);


set sql_safe_updates=0;

update customer set lastname='deshmukh' where custid=1;
select * from customer;


select concat(custname,' ',lastname) as fullname from customer;
select substr(custname,1,3) from customer;
select substr(custname,0,3) from customer;
select instr(custname,'a') as position from customer;
select substr(custname,1,2),instr(custname,'a') from customer;



-- Date and time function

select now();

select now() as current_datetime;

alter table customer add column date date;

update customer set date='2024-2-10' where custid = 1;
update customer set date='2024-8-10' where custid = 2;
update customer set date='2024-10-10' where custid = 3;

-- alter table customer drop column date;

select * from customer;

