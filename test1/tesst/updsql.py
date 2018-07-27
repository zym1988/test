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
sql ="update student SET SSEX=%s where SNMAE=%s"
SNAME="李四"
SSEX="女"
try:
	cursor.execute(sql,[SSEX,SNAME])
	conn.commit()
except Exception as e:
	conn.rollback()
cursor.close()
conn.close()