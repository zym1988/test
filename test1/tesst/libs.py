#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"
# import http.client
# def getBaidu():
# 	http_client=http.client.HTTPConnection("www.baidu.com",80,timeout=20)
# 	http_client.request("GET","/")
# 	r=http_client.getresponse()
# 	print(r.status)
# 	print(r.read())
#
# getBaidu()

import urllib
from urllib import request,parse
# def get_baidu():
# 	r=urllib.request.urlopen("http://www.baidu.com")
# 	print(r.getcode())
# 	print(r.status)
# 	print(r.headers)
# get_baidu()

# def post_cun():
# 	params=urllib.parse.urlencode({"cityId":"438"}).encode(encoding='UTF8')
# 	r=urllib.request.urlopen("http://m.cyw.com/index.php?m=api&c=cookie&a=setcity",params)
# 	print(r.read())
# 	print(r.getcode())
# post_cun()

import json
# print(json.__all__)
dict1={"name":"zym","age":22,"addr":"xian"}
print(type(dict1))
print(dict1)
#对dict1进行序列化的处理
str1=json.dumps(dict1)
print(type(str1))
print(str1)
#对str1进行反序列化的处理
dict2=json.loads(str1)
print(type(dict2))
print(dict2)

import requests
r=requests.get("http://wthrcdn.etouch.cn/weather_mini?city=西安")
print(r.text),(type(r.text))
#对数据进行反序列化的操作
dic=json.loads(r.text)
print(type(r.text))
print(r.json())
print(type(r.json()))


list1=["selenium","appium","android","ios"]
#把list1先序列化，再写入一个文件中
print(json.dump(list1,open("d:/log.log","w")))
print("文件内容为:")
r=open("d:/log.log","r+")
print(r.read())