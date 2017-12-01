#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"

from selenium import webdriver
import unittest

class WebInit(unittest.TestCase):
      def setUp(self):
		  self.driver = webdriver.Firefox()
		  self.driver.maximize_window()
		  self.driver.implicitly_wait(30)
		  self.driver.get("http://www.baidu.com")

      def tearDown(self):
		  self.driver.quit()