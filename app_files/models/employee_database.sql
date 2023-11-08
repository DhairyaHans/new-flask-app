create database employee;
use employee;

drop table login;

create table login(
sno INT Primary Key auto_increment,
username  varchar(60) unique not null,
password varchar(20) not null,
designation varchar(10) not null
);

select * from login;

insert into login values(1,'admin@abc.com','123456789','admin');
insert into login values(2,'emp@abc.com','123456789','emp');
insert into login values(3,'emp1@abc.com','000000000','emp');

create table register(
sno INT Primary Key auto_increment,
firstname varchar(60) not null,
lastname varchar(60) not null,
gender varchar(6) not null,
dob varchar(10) not null,
email varchar(60) unique not null,
ph_no varchar(12) not null,
address varchar(120) not null
);

select * from register;

insert into register values(1,'Tony','Stark','male','04/05/2023','admin@abc.com','1234567890','Stark Tower, Washington DC');