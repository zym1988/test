#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"
import unittest
import HTMLTestRunner
from selenium import webdriver
class Baidu(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Firefox()
		cls.driver.get("https://www.baidu.com")
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def test_001(self):
		self.assertEqual(self.driver.title,"百度一下，你就知道")
		print(self.driver.title)

	def test_002(self):
		self.assertEqual(self.driver.current_url,"https://www.baidu.com/")
		print(type(self.driver.current_url))
		print(type("https://www.baidu.com"))

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(Baidu)
	file_path="D:\\test1\\Report\\testReport.html"
	file_result=open(file_path,"wb")
	runner =HTMLTestRunner.HTMLTestRunner(
		stream=file_result,
		title="TestReport",
		description="测试报告详细信息"
	)
	runner.run(suite)





