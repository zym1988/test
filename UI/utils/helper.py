#!/usr/bin/env python 
#-*-coding:utf-8-*-

import  os
import  csv
import  xlrd

def readlists():
	lists=[
		['','',u'请您输入手机/邮箱/用户名'],
		['admin','',u'请您输入密码'],
		['','admin',u'请您输入手机/邮箱/用户名']]
	return lists

def readTxt(index):
	with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','login.txt'),'r') as f :
		d=f.readlines()
	return d[index]

def readTxt():
	'''txt记事本的操作'''
	import  os
	with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','log.txt'),'r') as f:
		return f.read().split('\n')


class DataHelper(object):

	def readCsv(self,value1,value2):
		rows=[]
		data_file=open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','csvTest.csv'))
		reader=csv.reader(data_file)
		next(reader,None)
		for row in reader:
			rows.append(row)
		return ''.join(rows[value1][value2]).decode('gb2312')

	@staticmethod
	def readExcel(value1, value2):
		book = xlrd.open_workbook(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'csvTest.xlsx'))
		sheet = book.sheet_by_index(0)
		return sheet.cell_value(value1, value2)

	@staticmethod
	def readExcels():
		rows = []
		book = xlrd.open_workbook(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'csvTest.xlsx'))
		sheet = book.sheet_by_index(0)
		for row in range(1, sheet.nrows):
			rows.append(list(sheet.row_values(row, 0, sheet.ncols)))
		return rows





