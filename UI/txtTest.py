#!/usr/bin/env python
#-*-coding:utf-8-*-


import  unittest

from selenium import  webdriver

from UI.utils import helper


class BaiduTest(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://www.baidu.com')

	def tearDown(self):
		self.driver.quit()

	def test_login_div_null(self):
		self.driver.find_element_by_link_text(u'登录').click()
		self.driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys(helper.readTxt(0))
		self.driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys(helper.readTxt(0))
		self.driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
		divText=self.driver.find_element_by_id('TANGRAM__PSP_10__error').text
		divText=divText.encode('utf-8')
		print divText,type(divText)
		print helper.readTxt(3),type(helper.readTxt(3))
		self.assertTrue(helper.readTxt(3).startswith(divText))

if __name__ == '__main__':
	unittest.main(verbosity=2)