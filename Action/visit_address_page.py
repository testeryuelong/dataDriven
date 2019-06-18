# -*-coding:utf-8 -*-
# @Author : Zhigang

from selenium import webdriver
from Util.FormatTime import *
import time
from PageObject.login_page import *
from Action.login import *

def visit_address_page(driver):
    hp=HomePage(driver)
    hp.address_book_page_link().click()
    time.sleep(3)

if __name__=="__main__":
    driver=webdriver.Chrome()
    login(driver, "yzg18730603667", "807237157@yzg")
    visit_address_page(driver)