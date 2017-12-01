#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"
from webUI.page.init import *
from webUI.page.shouye import *
import unittest

class LoginShouye(WebInit,ShouYe):
	def test_baidu_news(self):
		"""验证：点击新闻后页面跳转"""
		self.clickNews()
		self.assertEqual(self.driver.current_url,u"http://news.baidu.com/")

if __name__ == "__main__":
	unittest.main(verbosity=2)