#!/usr/bin/env python
#-*-coding:utf-8-*-

from selenium import  webdriver
import  unittest

from UI.utils.helper import *
from UI.page.login import  *
from UI.page.init import *


class BaiduCSVTest(WebInit,Login):
	def test_login_username_passwd_null(self):
		'''登录：用户名和密码为空点击后的错误提示信息'''
		data=DataHelper()
		self.login(data.readCsv(0,0),data.readCsv(0,1))
		divText=self.getDivError
		self.assertEqual(divText,data.readCsv(0,2))

if __name__ == '__main__':
	unittest.main(verbosity=2)
