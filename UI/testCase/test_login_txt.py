#!/usr/bin/env python 
#-*-coding:utf-8-*-

from selenium import  webdriver
import  unittest

from UI.utils.helper import *
from UI.page.login import  *
from UI.page.init import *


class BaiduTxtTest(WebInit,Login):
	def test_login_username_passwd_null(self):
		'''登录：用户名和密码为空点击后的错误提示信息'''
		self.login(readTxt()[0],readTxt()[1])
		divText=(self.getDivError).encode('utf-8')
		self.assertEqual(divText,readTxt()[2])

if __name__ == '__main__':
	unittest.main(verbosity=2)




