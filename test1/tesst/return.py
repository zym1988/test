#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"

def test():
	a = 11
	b = 123
	c = 13
	'''
	#第一种用一个列表来封装3个变量的值
	d=[a,b,c]
	return d
	'''

	# #第二种
	# return [a,b,c]

	# #3
	# return a,b,c

    #4
	return (a,b,c)

print(test())