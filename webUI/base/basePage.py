#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"
from selenium.common.exceptions import NoSuchElementException
import time
class WebDriver(object):
	def __init__(self,driver):
		self.driver =driver

	def findElement(self,*loc):
		try:
			return self.driver.find_element(*loc)
		except NoSuchElementException as e:
			print "Error details :%s" %(e.args[0])

	def findsElement(self,*loc):
		try:
			return self.driver.find_elements(*loc)
		except NoSuchElementException as e:
			print "Error details :%s" %(e.args[0])

	def wait(self):
		time.sleep(2)