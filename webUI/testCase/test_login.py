#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"

from webUI.page.init import *
from webUI.page.login import *
import unittest
import ddt

# class LoginTest(WebInit,Login):
#
# 	def test_login_div_null(self):
# 		"""验证：用户名和密码为空的情况下，点击登录按钮的提示信息 """
# 		self.login("","")
# 		self.assertEqual((self.getDivError).encode("utf-8"),"请您输入手机/邮箱/用户名")
# 		print self.getDivError,type(self.getDivError)
#
# 	def test_login_div_pwdnull(self):
# 		"""验证：密码为空的情况下，点击登录按钮的提示信息"""
# 		self.login("admin","")
# 		self.assertEqual(self.getDivError,u"请您输入密码")
#
# 	def test_login_div_yzmnull(self):
# 		"""验证：验证码为空的情况下，点击登录按钮的提示信息"""
# 		self.login("admin","admin")
# 		self.assertEqual(self.getDivError,u"请您输入验证码")
#
# if __name__ == "__main__":
# 	unittest.main(verbosity=2)
"""引入ddt后的代码"""

# @ddt.ddt
# class LoginTest(WebInit,Login):
#      @ddt.data(("","",u"请您输入手机/邮箱/用户名"),("admin","",u"请您输入密码"),("admin","admin",u"请您输入验证码"))
#      @ddt.unpack
#      def test_login_div_null(self,username,password,expected):
#  		"""验证：对登录input表单的验证"""
#  		self.login(username,password)
#  		self.assertEqual(self.getDivError,expected)

"""ddt使用的数据放到列表中"""
from webUI.utils.helper import *
@ddt.ddt
class LoginTest(WebInit,Login):
     @ddt.data()
     @ddt.unpack
     def test_login_div_null(self,username,password,expected):
 		"""验证：对登录input表单的验证"""
 		self.login(username,password)
 		self.assertEqual(self.getDivError,expected)

if __name__ == "__main__":
     	unittest.main(verbosity=2)



