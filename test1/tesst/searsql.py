#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"
import pymysql
#连接db
conn = pymysql.connect(host="localhost",
					   user="root",
					   passwd="",
					   db="zym",
					   charset="utf8")
#得到一个可以执行sql语句的光标对象
cursor=conn.cursor()
#修改数据的sql语句
# sql ="select * from student where SNAME=%s"
# SNAME="李四"

sql1 ="select * from student  "
try:
	# cursor.execute(sql,"王五")
	cursor.execute(sql1)
	conn.commit()
	# 获取单条查询数据
	# ret = cursor.fetchone()
	# 获取多条查询数据
	ret = cursor.fetchall()
	print(ret)
except Exception as e:
	conn.rollback()
cursor.close()
conn.close()
