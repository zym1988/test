#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"

from webUI.page.login import *
from webUI.page.init import *
from webUI.utils.helper import*
import unittest


class XmlTest(WebInit,Login):
	def test_xml_001(self):
		"""验证：用户名和密码为空的情况下返回的错误提示信息"""
		self.login("","")
		self.assertEqual(self.getDivError,getXmlData("nullText"))

	def test_xml_002(self):
		"""验证：密码为空的情况下返回的错误提示信息"""
		self.login("admin","")
		self.assertEqual(self.getDivError,getXmlData("pwdNull"))

	def test_xml_003(self):
		"""验证：验证码为空的情况下返回的错误提示信息"""
		self.login("admin","admin")
		self.assertEqual(self.getDivError,getXmlData("codeNull"))

if __name__ == "__main__":
	unittest.main(verbosity=2)

