#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"
import os
import xlrd
import  csv
import xml.dom.minidom

# def base_dir(self,fileName,path="data"):
# 	"""
# 	@:param fileName:要读取的文件名称
# 	@:param  data:存储的文件目录
# 	"""
# 	return  os.path.join(os.path.dirname(os.path.dirname(__file__)),path,fileName)

def readlists():
	lists =[
		["","",u"请您输入手机/邮箱/用户名"],
		["admin","",u"请您输入密码"],
		["admin","admin",u"请您输入验证码"]]
	return  lists

def readTxt():
	"""对记事本txt的操作"""
	with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),"data","log.txt"),"r") as f:
		return f.read().split("\n")#字符串转换为列表用split

def readExcel(value1,value2):
	"""数据存储到excel的读取方法"""
	book = xlrd.open_workbook(os.path.join(os.path.dirname(os.path.dirname(__file__)),"data","test.xlsx"))
	sheet = book.sheet_by_index(0)
	return sheet.cell_value(value1,value2)

def readExcels():
	rows =[]#定义列表
	book = xlrd.open_workbook(os.path.join(os.path.dirname(os.path.dirname(__file__)),"data","test.xlsx"))
	sheet = book.sheet_by_index(0)
	for row in range(1,sheet.nrows):
	    rows.append(list(sheet.row_values(row,0,sheet.ncols)))
	return rows

def getXmlData(value):
	dom = xml.dom.minidom.parse(os.path.join(os.path.dirname(os.path.dirname(__file__)),"data","test.xml"))
	db = dom.documentElement
	name = db.getElementsByTagName(value)
	nameValue = name[0]
	return nameValue.firstChild.data

def getXmlUser(parent,child):
	dom = xml.dom.minidom.parse(os.path.join(os.path.dirname(os.path.dirname(__file__)),"data","test.xml"))
	db = dom.documentElement
	itemlist = db.getElementsByTagName(parent)
	item = itemlist[0]
	return item.getAttribute(child)

class DataHelper(object):
	def readcsv(self,value1,value2):
		"""将数据存储到csv中读取"""
		rows = []
		dataCSV = open(os.path.join(os.path.dirname(os.path.dirname(__file__)),"data","test1.csv"))
		reader = csv.reader(dataCSV)
		next(reader,None)
		for row in reader:
			rows.append(row)
		return "".join(rows[value1][value2]).decode("gb2312")
	# print readcsv(0,0)
	# print readcsv(0,1)
	# print readcsv(0,2)






