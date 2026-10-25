/* 	BEGIN	;
-- or
	START TRANSACTION; -- */
create database TCL;
use TCL;

create table orders (
		order_id INT PRIMARY KEY,
		customer_name varchar(100),
		status varchar(50)
);

desc orders;

-- start transaction;
begin;
set autocommit = 0;
insert into orders values(101, 'Geet', 'Pending');
insert into orders values(102, 'Bob', 'Pending');
update orders set customer_name = 'Raj' where order_id = 102;

truncate table orders;
select * from orders;
rollback;
commit;

insert into orders values(103, 'Om', 'Pending');
insert into orders values(104, 'Sahil', 'Pending');
savepoint sp1;
select * from orders;

update orders set status = 'Shipped' where order_id = 103;
savepoint sp2;

rollback to savepoint sp1;

delete from orders where order_id = 102;
savepoint sp3;
select * from orders;
rollback;



            