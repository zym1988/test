#!/usr/bin/env python 
#-*-coding:utf-8-*-

from UI.page.shouYe import  *
from UI.page.init import  *
import  unittest

class ShouYeTest(WebInit,ShouYe):
	def test_baidu_news(self):
		'''验证:点击新闻后的页面跳转'''
		self.clickNews()
		self.assertEqual(self.driver.current_url,u'http://news.baidu.com/')

if __name__ == '__main__':
    unittest.main(verbosity=2)