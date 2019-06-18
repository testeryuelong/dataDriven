# -*-coding:utf-8 -*-
# @Author : Zhigang

import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig
from selenium import webdriver
from Action.login import *

class HomePage(object):

    def __init__(self,driver):
        "初始化参数，加载配置文件，将'126mail_homepage'section内容读取出来"
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.login_page_items=self.parse_config_file.getItemsFromSection("126mail_homepage")

    def address_book_page_link(self):
        "点击通讯录"
        locateType,locateExpression=self.login_page_items["login_page.addressbook"].split(">")
        return getElement(self.driver,locateType,locateExpression)


if __name__=="__main__":
    driver=webdriver.Firefox()
    login(driver, "XXXX", "XXXX")
    hp=HomePage(driver)
    hp.address_book_page_link().click()
    time.sleep(2)
