#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"
import requests
import unittest
class TokenClass(unittest.TestCase):
	def setUp(self):
		self.heders={"Parkingwang-Client-Source":"ParkingWangAPIClientWeb",
					 "Content-Type":"application/json;charset=UTF-8"}
		self.url="http://180.97.80.42:9090"

	def getToken(self):
		data={
			"username":"6666666666",
			"password":"8144ed050cd8d053f24a1e179d7529e17c3a2ba9cfcfcd7d3bda9ec6a8156758"}
		self.r=requests.post(self.url+"/v5/login",json=data,headers=self.heders)
		return {"token":self.r.json()["data"]["token"]}
	def test_getInfo(self):
		self.getToken()
		self.r=requests.post(self.url+"/v5/infoGet",json=self.getToken(),headers=self.heders)
		print(self.r.json())

	def tearDown(self):
		pass

if __name__ == "__mian__":
	suite=unittest.TestLoader().loadTestsFromTestCase(TokenClass)
	unittest.TextTestRunner(verbosity=2).run(suite)

