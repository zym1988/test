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
#定义要执行的sql语句:添加表
# sql="""
# CREATE TABLE student1(
# SNO char(3) CHARACTER SET latin1 NOT NULL,
# SNAME char(8) NOT NULL,
# SSEX char(2) NOT NULL,
# SBIRTHDAY date DEFAULT NULL,
# CLASS char(5) CHARACTER SET latin1 DEFAULT NULL,
# PRIMARY KEY (SNO)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
# """
#定义要执行的sql语句:给student表插入数据
#sql2="INSERT INTO student(SNO,SNAME,SSEX,SBIRTHDAT,CLASS)VALUES (%s,%s,%s,%s,%s)"
sql2="INSERT INTO student(SNO,SNAME,SSEX,CLASS)VALUES (%s,%s,%s,%s)"
#一条数据插入
# SNO=110
# SNAME="张三"
# SSEX="女"
# SBIRTHDAT="1998-01-23"
# CLASS="95033"
#多条数据插入
# data=[(110,"张三","女","1989-02-23","95033"),
# 	  (111,"李四","男","1979-05-23","95034"),
# 	  (112,"王五","男","1969-07-14","95032"),
# 	  (113,"赵六","男","1998-01-25","95031"),
# 	  ]
data=[(110,"张三","女","95033"),
	  (111,"李四","男","95034"),
	  (112,"王五","男","95032"),
	  (113,"赵六","男","95031"),
	  ]
#删除student表中，SNAME=张三的数据
sql3="delete FROM  student WHERE SNAME=%s"
try:
	#执行一条SQL语句
	#cursor.execute(sql2,[SNO,SNAME,SSEX,CLASS])
	#执行多条插入sql语句
	# cursor.executemany(sql2,data)
	#执行删除语句
	cursor.execute(sql3,"张三")
	#提交事务
	conn.commit()
	#打印出插入的数据条数
	# print("affected rows={}".format(cursor.rowcount))
	#提交之后，获取刚插入的数据的ID
	# last_id=cursor .lastrowid
except Exception as e:
	#有异常，回滚数据
    conn.rollback()
#关闭光标对象
cursor.close()
#关闭数据库连接
conn.close()





