#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"

# sex = input("请输入性别:")
#
# if sex=="女":
#
#     color = input("你白嘛？")
#
#     money = int(input("你有钱嘛？"))
#
#     beautiful = input("你美嘛？")
#
#     if color=="白"  and money >1000000  and beautiful =="美":
#
#          print("白富美")
#     else:
#
#          print("矮矬穷")
#
# else:
#
#      high = input("你高不？")
#
#      money =int(input("你有钱没"))
#
#      shuai = input("你帅不")
#
#      if high=="高" and money>1000000  and shuai=="帅":
#
#           print("高富帅")
#      else:
#
#           print("丑")
#
# i=1
# while i<=5:
#       j =1
#       while j<=5:
#             print("*",end="")
#             j = j +1
#       print("")
#       i = i +1

# i=1
#
# while i<=5:
#
# 	 j =1
# 	 while j<=i:
#             print("*",end="")
#             j+= 1
# 	 print("")
#
# 	 i+=1


#九九乘法表

# i=1
#
# while i<=9:
#
# 	 j =1
# 	 while j<=i:
#             print("%d*%d=%d\t "%(j,i,j*i),end="")
#             j+= 1
# 	 print("")
#
# 	 i+=1




#剪刀石头布
'''
import random
game =int(input("请输入 0剪刀 1石头 2布:"))
computer=random.randint(0,2)
if(game==0 and computer==2) or (game==1 and computer==0) or (game==2 and computer==1):
	 print("恭喜你赢了比赛")
elif game==computer:
	 print("请继续猜拳")
else:
	 print("sorry")
'''
'''
i=1
num =0
while i<=100:
   if i%2==0:
	   print(i)
	   num+=1
   if num==20:
       #break
	   continue
   i+=1
'''

# name="abcdefgasdfggg"
# print(name[0])
# print(name[0:-1])
# print(name[:-1])
# print(name[::-1])
# print(name[::1])
# print(name[2:6])
# print(name[2:-1])
# print(name[2:])
# print(name[2::1])
# print(name[2:-1:2])
# print(name[0:])
# print(name[-1:0:-1])
# print(name[-1::-1])
# print(name[::-1])
# print(name[::1])
#
#
# names=["aaa","bbb","ccc"]
# print(names)
# names.append("ddd")
# print(names)
# names.insert(0,"eee")
# print(names)
# name1=["张三","李四","王五"]
#
# name2=names+name1
# print(name2)
# name1.extend(names)
# print(name1)
# name1.pop()
# print(name1)
# name1.remove("张三")
# print(name1)
# del name1[0]
# print(name1)


a=[12,20,30,23,33,9,8]
