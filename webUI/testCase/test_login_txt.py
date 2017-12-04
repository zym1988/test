#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"

from webUI.utils.helper import *
from webUI.page.login import *
from webUI.page.init import *
import unittest

class BaiduTxtTest(WebInit,Login):
	def test_login_username_pwd_null(self):
		"""登录：用户名和密码为空点击后的错误提示信息"""
		self.login(readTxt()[0],readTxt()[1])
		divText =  self.getDivError
		self.assertEqual((divText).encode("utf-8"),readTxt()[2])

if __name__ == "__main__":
	unittest.main(verbosity=2)

