#!/usr/bin/env python 
#-*-coding:utf-8-*-


from selenium import  webdriver
import  unittest
from ddt import  *

@ddt
class BaiduTest(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://www.baidu.com')

	def tearDown(self):
		self.driver.quit()

	@data(('','',u'请您输入手机/邮箱/用户名'),('username','',u'请您输入密码'))
	@unpack
	def test_login_div_null(self,username,password,result):
		self.driver.find_element_by_link_text(u'登录').click()
		self.driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys(username)
		self.driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys(password)
		self.driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
		print self.driver.find_element_by_id('TANGRAM__PSP_10__error').text
		self.assertEqual(self.driver.find_element_by_id('TANGRAM__PSP_10__error').text,result)

if __name__ == '__main__':
	unittest.main(verbosity=2)