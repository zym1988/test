#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"

def get_wendu():
	wendu=22
	print("当前温度是:%d"%wendu)
	return wendu
def get_wendu1(wendu):
	wendu = wendu + 3
	print("当前温度(华氏)是:%d"%wendu)
get_wendu1(get_wendu())