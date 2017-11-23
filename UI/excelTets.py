#!/usr/bin/env python 
#-*-coding:utf-8-*-

import  xlrd
import  os


def readExcel(value1,value2):
	book=xlrd.open_workbook(os.path.join(os.path.dirname(__file__),'csvTest.xlsx'))
	sheet=book.sheet_by_index(0)
	return sheet.cell_value(value1,value2)



def readExcels():
	rows=[]
	book=xlrd.open_workbook(os.path.join(os.path.dirname(__file__),'csvTest.xlsx'))
	sheet=book.sheet_by_index(0)
	for row in range(1,sheet.nrows):
		rows.append(list(sheet.row_values(row,0,sheet.ncols)))
	return rows

from selenium import  webdriver
import  unittest
import  ddt

@ddt.ddt
class BaiduExcel(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://www.baidu.com')

	@ddt.data(*readExcels())
	@ddt.unpack
	def test_login_div_null(self,username,password,result):
		self.driver.find_element_by_link_text(u'登录').click()
		self.driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys(username)
		self.driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys(password)
		self.driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
		print self.driver.find_element_by_id('TANGRAM__PSP_10__error').text
		self.assertEqual(self.driver.find_element_by_id('TANGRAM__PSP_10__error').text,result)

	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	unittest.main(verbosity=2)








