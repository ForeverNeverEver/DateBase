#-*- coding:utf-8 -*-
####系统入口

import os
import MySQLdb
import Student
import Teacher
import Login
import SystemManager

if __name__ == '__main__':
	conn = MySQLdb.connect(user='root',passwd = '',db = 'test')
	log = Login.Login(conn)
	if log.MainFunc():
		account = log.GetLoginAccount()
		if account[2] == 0:
			usr = SystemManager.SystemManager(conn,account[0],account[1])
			usr.MainFunc()
		elif account[2] == 1:
			usr = Teacher.Teacher(conn,account[0],account[1])
			usr.MainFunc()
		elif account[2] == 2:
			usr = Student.Student(conn,account[0],account[1])
			usr.MainFunc()
		else : 
			conn.close()
			raise Exception()
	conn.close()
	
