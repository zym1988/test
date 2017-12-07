#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"
# import  csv
# import  os
#
# def readcsv(value1,value2):
# 	rows = []
# 	dataCSV = open(os.path.join(os.path.dirname(os.path.dirname(__file__)),"data","test.csv"))
# 	reader = csv.reader(dataCSV)
# 	#next(reader,None)
# 	for row in reader:
# 		rows.append(row)
# 	return "".join(rows[value1][value2]).decode("gb2312")
# print readcsv(0,0)
# print readcsv(0,2)
# print readcsv(1,0)

from webUI.utils.helper import *
from webUI.page.login import *
from webUI.page.init import *
import unittest

data = DataHelper()
class BaiduCSVTest(WebInit,Login):
	def test_login_username_pwd_null(self):
		"""登录：用户名和密码为空点击后的错误提示信息"""
		self.login(data.readcsv(0,0),data.readcsv(0,1))
		divText =  self.getDivError
		#self.assertEqual(divText,data.readcsv(0,2))
		print data.readcsv(0,0)
		print data.readcsv(0,1)
		print data.readcsv(0,2)

	def test_login_pwd_null(self):
		"""登录：密码为空点击后的错误提示信息"""
		#data = DataHelper()
		self.login(data.readcsv(1,0),data.readcsv(1,1))
		divText =  self.getDivError
		#self.assertEqual(divText,data.readcsv(1,2))
		print data.readcsv(1,0)
		print data.readcsv(1,1)
		print data.readcsv(1,2)

	def test_login_yzm_null(self):
		"""登录：验证码为空点击后的错误提示信息"""
		#data = DataHelper()
		self.login(data.readcsv(2,0),data.readcsv(2,1))
		divText =  self.getDivError
		#self.assertEqual(divText,data.readcsv(2,2))
		print data.readcsv(2,0)
		print data.readcsv(2,1)
		print data.readcsv(2,2)


if __name__ == "__main__":
	unittest.main(verbosity=2)

