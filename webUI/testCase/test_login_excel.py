#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"

from webUI.utils.helper import *
from webUI.page.login import *
from webUI.page.init import *
import unittest


class BaiduEXCELTest(WebInit,Login):
	def test_login_username_pwd_null(self):
		"""登录：用户名和密码为空，点击登录的错误提示信息"""
		self.login(readExcel(1,0),readExcel(1,1))
		self.assertEqual(self.getDivError,readExcel(1,2))

if __name__ == "__main__":
	unittest.main(verbosity=2)