CREATE DATABASE if not exists JWGL;
USE JWGL;
create table if not exists 学生(
    学号 varchar(10) primary key ,
    姓名 varchar(5),
    性别 varchar(5),
    民族 varchar(5),
    生日 varchar(10),
    家庭住址 varchar(20),
    电话 varchar(13),
    专业代码 varchar(10),
    类别 varchar(5));
create table if not exists 教师(
    教师号 varchar(10) primary key ,
    姓名 varchar(5),
    性别 varchar(5),
    民族 varchar(5),
    生日 varchar(10),
    家庭住址 varchar(20),
    电话 varchar(13),
    职称 varchar(5),
    学历 varchar(5));
create table if not exists 课程(
    课号 varchar(10) primary key ,
    课名 varchar(10),
    总学时 integer(5),
    教学大纲 varchar(10),
    课程类型 varchar(5),
    课程简介 varchar(20));
create table if not exists 教学计划(
    计划号 varchar(10) primary key ,
    计划名称 varchar(5),
    总学时 varchar(4),
    必修学分 integer(2),
    选修学分 integer(2),
    制定日期 date,
    专业代号 varchar(10),
    学生类别 varchar(3));
create table if not exists 教室(
    教室号 varchar(10) primary key ,
    名称 varchar(5),
    教师类型 varchar(2),
    容量 integer(5));
create table if not exists 教学计划细节(
    计划号 varchar(10) primary key ,
    课号 varchar(10),
    学分 integer(5),
    课程性质 varchar(5),
    开设学期 varchar(5));
create table if not exists 课程先导关系(
    课号 varchar(10),
    先导课号 varchar(10));
create table if not exists 教学班(
    教学班号 varchar(10) primary key ,
    学年 varchar(2),
    学期 varchar(3),
    课号 varchar(10),
    限定人数 integer(2),
    教师号 varchar(10),
    教学工作数量 integer(2),
    评估成绩 integer(3));
create table if not exists 教室使用(
    教室号 varchar(10) primary key ,
    教学班号 varchar(10),
    周 varchar(5),
    节 varchar(5));
create table if not exists 选课(
    学号 varchar(10) primary key ,
    教学班号 varchar(10),
    成绩 integer(3),
    院系教学 varchar(5));
create table if not exists 专业(
    专业代号 varchar(10) primary key ,
    名称 varchar(5))
