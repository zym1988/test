#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"
from  webUI.base.basePage import *
from  selenium.webdriver.common.by import By

class ShouYe(WebDriver):
	xinwen_loc = (By.LINK_TEXT,u"新闻")

	def clickNews(self):
		self.findElement(*self.xinwen_loc).click()

