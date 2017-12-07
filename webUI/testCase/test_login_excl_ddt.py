#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"

from webUI.utils.helper import *
from webUI.page.login import *
from webUI.page.init import *
import unittest
import ddt

@ddt.ddt
class TestBaiExcel(WebInit,Login):
	@ddt.data(*readExcels())
	@ddt.unpack
	def test_login_username_pwd_null(self,username,password,expected):
		"""登录：登录错误的验证信息"""
		self.login(username,password)
		self.assertEqual(self.getDivError,expected)

if __name__ == "__main__":
	unittest.main(verbosity=2)

