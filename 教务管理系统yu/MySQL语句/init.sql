Create Table AllMessage(
	Id int primary key auto_increment,
	MsgLevel  tinyint not null,
	SenderNo	varchar(5) not null,
	SenderName	varchar(20),
	SendTime	datetime,
	Title tinytext not null,
	Content  text,
	statu char(4) not null
);
Create Table StudentInfo(
	Id int primary key auto_increment,
	Name varchar(20) not null,
	Gender varchar(5) not null,
	StudentNo varchar(12) not null unique,
	Birth date,
	Academy	varchar(20) not null,
	TeacherNo varchar(5),
	Major varchar(20) not null,
	Grade varchar(4)
);

Create Table DefaultPassword(
	Id int primary key auto_increment,
	AccountLevel tinyint  not null,
	Password varchar(12)
);
Create Table LoginAccount(
	id int primary key auto_increment,
	Account varchar(12) not null,
	Password varchar(12),
	AccountLevel tinyint
);
Create Table PositionList(
	Id int primary key auto_increment,
	PositionNo tinyint not null,
	PositionName varchar(20)
);
Create Table TeacherInfo(
	Id int primary key auto_increment,
	Name varchar(20) not null,
	TeacherNo varchar(5) not null unique,
	Gender varchar(5) not null,
	Birth  date,
	PositionNo tinyint,
	Salary double
);
insert into DefaultPassword(AccountLevel,Password) values(0,'123456');
insert into DefaultPassword(AccountLevel,Password) values(1,'123456');
insert into DefaultPassword(AccountLevel,Password) values(2,'123456');

insert into PositionList(PositionNo,PositionName) Values(0,'headmaster');
insert into PositionList(PositionNo,PositionName) Values(1,'professor');
insert into PositionList(PositionNo,PositionName) Values(2,'teacher');
