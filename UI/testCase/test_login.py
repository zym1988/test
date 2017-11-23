#!/usr/bin/env python 
#-*-coding:utf-8-*-
import  ddt
import  sys
import os
#sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'page'))
from UI.page.init import *
from UI.page.login import *

# class LoginTest(WebInit,Login):
# 	def test_login_div_null(self):
# 		'''验证:用户名和密码为空点击登陆后的错误提示信息'''
# 		self.login('','')
# 		self.assertEqual(self.getDivError,u'请您输入手机/邮箱/用户名')
#
# 	def test_login_div_passwd_null(self):
# 		'''验证:....'''
# 		self.login('admin','')
# 		self.assertEqual(self.getDivError,u'请您输入密码')
#
# 	def test_login_div_user_null(self):
# 		'''验证:....'''
# 		self.login('','admin')
# 		self.assertEqual(self.getDivError,u'请您输入手机/邮箱/用户名')
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

'''引入DDT后的代码'''

#
# @ddt.ddt
# class LoginTest(WebInit,Login):
# 	@ddt.data(('','',u'请您输入手机/邮箱/用户名'),('admin','',u'请您输入密码'),('','admin',u'请您输入手机/邮箱/用户名'))
# 	@ddt.unpack
# 	def test_login_div_null(self,username,password,expected):
# 		'''验证:对登录input表单的验证'''
# 		self.login(username,password)
# 		self.assertEqual(self.getDivError,expected)
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
#


'''ddt使用的数据放在列表中'''
from UI.utils import  helper

@ddt.ddt
class LoginTest(WebInit,Login):
	@ddt.data(*helper.readlists())
	@ddt.unpack
	def test_login_div_null(self,username,password,expected):
		'''验证:对登录input表单的验证'''
		self.login(username,password)
		self.assertEqual(self.getDivError,expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)