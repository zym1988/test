#!/usr/bin/env python 
#-*-coding:utf-8-*-


from selenium import  webdriver
import  unittest
import ddt
from UI.utils.helper import *
from UI.page.login import  *
from UI.page.init import *



@ddt.ddt
class BaiduTxtTest(WebInit,Login):
	@ddt.data(*DataHelper.readExcels())
	@ddt.unpack
	def test_login_username_passwd_null(self,username,password,expected):
		'''登录：登录错误的验证'''
		self.login(username,password)
		self.assertEqual(self.getDivError,expected)

if __name__ == '__main__':
	unittest.main(verbosity=2)