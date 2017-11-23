#!/usr/bin/env python 
#-*-coding:utf-8-*-

import  os

with open(os.path.join(os.path.dirname(__file__),'log.txt'),'r') as f:
	print f.read(),type(f.read())



