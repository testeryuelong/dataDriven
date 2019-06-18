# -*-coding:utf-8 -*-
# @Author : Zhigang

from selenium import webdriver
from Util.Log import *
from Util.FormatTime import *
from PageObject.login_page import LoginPage
from PageObject.home_page import  *

def login(driver, userName, passWd):
    lp=LoginPage(driver)
    lp.login(userName,passWd)
    info("login successfully!")
    print (dateTimeChinese())

if __name__=="__main__":
    driver=webdriver.Chrome()
    login(driver,"yzg18730603667", "807237157@yzg")
