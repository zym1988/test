#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"

import requests
from bs4 import BeautifulSoup

r = requests.get("https://movie.douban.com/")
soup = BeautifulSoup(r.text,"html.parser")
movie_list= soup.find_all("div",class_="item")

for movie in  movie_list:
	# title=movie.find("span",class_="").text
	score=movie.find("span",class_="rating_num").text
	quote=movie.find("span",class_="inq").text
	# star=movie.find("span",class_="").text
	# comment_num=movie.find("span",class_="").text
	print(score,quote)