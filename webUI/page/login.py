#!/usr/bin/env python
# coding:utf-8
__author__ = "zym"

from  webUI.base.basePage import *
from  selenium.webdriver.common.by import By

class Login(WebDriver):
    login_loc=(By.LINK_TEXT,u'登录')
    username_loc=(By.ID,'TANGRAM__PSP_10__userName')
    password_loc=(By.ID,'TANGRAM__PSP_10__password')
    loginButton_loc=(By.ID,'TANGRAM__PSP_10__submit')
    div_loc=(By.ID,'TANGRAM__PSP_10__error')

    def clickLogin(self):
		self.findElement(*self.login_loc).click()

    def typeUsername(self,username):
		self.findElement(*self.username_loc).send_keys(username)

    def typePassword(self,password):
		self.findElement(*self.password_loc).send_keys(password)

    def clickLoginButton(self):
		self.findElement(*self.loginButton_loc).click()

    def login(self,username,password):
		self.clickLogin()
		self.typeUsername(username)
		self.typePassword(password)
		self.clickLoginButton()

    @property
    def getDivError(self):
		return self.findElement(*self.div_loc).text