#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"

# #用来存储名片
# card_infos = {}
#
# def print_menu():
# 	print("="*50)
# 	print("   名片管理系统")
# 	print("1.添加一个新的名片")
# 	print("2.删除一个新的名片")
# 	print("3.修改一个新的名片")
# 	print("4.查询一个新的名片")
# 	print("5.显示所有的名片")
# 	print("6.退出系统")
# 	print("="*50)
#
# def add_card_info():
# 	new_name = input("请输入名字:")
# 	new_qq = input("请输入QQ:")
# 	new_weixin =input("请输微信:")
# 	new_addr = input("请输入新的地址:")
# 	#定义字典，用来存储一个新的名片
# 	#new_info = {}
# 	new_info["name"] = new_name
# 	new_info["qq"] = new_qq
# 	new_info["weixin"] = new_weixin
# 	new_info["addr"] = new_addr
# 	#将一个字典添加到字典中
# 	card_infos.update(new_info)
# 	print(card_infos)
#
# #1.打印功能提示
# print_menu()
#
# def sear_card():
# 	find_name=input("请输入要查询的名字:")
# 	#find_flag =0 #默认没有找到
# 	for temp in card_infos:
# 		if find_name == temp["name"]:
# 			print("%s\t%s\t%s\t%s"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
# 			find_flag=1 #表示找到了
# 	#判断是否找到了
# 	# if find_flag==0:
# 	# 	print("查无此人")
# 	else:
# 		print("查无此人")
#
# def upd_card():
# 	upd_name =input("请输入要修改的名字:")
# 	for temp in card_infos:
# 		if upd_name == temp["name"]:
# 			nnew_name = input("请输入修改后的名字:")
# 			new_info["name"]= nnew_name
# 		print(card_infos)
#
# def del_card():
# 	del_name = input("请输入要删除的名字:")
# 	for temp in card_infos:
# 		if del_name == temp["name"]:
# 			print(new_info.get("name"))#调试
# 			new_info.pop("name")
# 			#card_infos.remove("name")
# 			print(card_infos)
# 		else:
# 			print("查无此人")
#
# while True:
# 	#2.获取用户的输入
# 	num = int(input("请输入操作序号:"))
# 	#3.跟进用户的数据执行相应的功能
# 	new_info = {}
# 	if num==1:
# 		add_card_info()
# 	elif num == 2:
# 		del_card()
# 	elif num==3:
# 		upd_card()
# 	elif num==4:
# 		sear_card()
# 	elif num==5:
# 		print("姓名\tQQ\t微信\t地址")
# 		for temp in card_infos.values():
# 				print("%s\t%s\t%s\t%s"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
# 	elif num==6:
# 		break
# 	else:
# 		print("输入有误，请重新输入")
# 	print("")
#
# if __name__ == "__main__":

import  datetime
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("当前时间:"+nowTime)



