# -*-coding:utf-8 -*-
# @Author : Zhigang

import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig
from selenium import webdriver
from Action.login import *
from Action.visit_address_page import *


class AddressPage(object):

    def __init__(self,driver):
        "初始化参数，加载配置文件，将'126mail_addcontactspage'section内容读取出来"
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.login_page_items=self.parse_config_file.getItemsFromSection("126mail_addcontactspage")

    def add_contact_button(self):
        locateType,locateExpression=self.login_page_items["addcontacts_page.createcontactsbtn"].split(">")
        return getElement(self.driver,locateType,locateExpression)

    def contact_name(self):
        locateType,locateExpression=self.login_page_items["addcontacts_page.contactpersonname"].split(">")
        return getElement(self.driver,locateType,locateExpression)

    def contact_email(self):
        locateType,locateExpression=self.login_page_items["addcontacts_page.contactpersonemail"].split(">")
        return getElement(self.driver,locateType,locateExpression)

    def contact_is_star(self):
        locateType,locateExpression=self.login_page_items["addcontacts_page.starcontacts"].split(">")
        return getElement(self.driver,locateType,locateExpression)

    def contact_mobile(self):
        locateType,locateExpression=self.login_page_items["addcontacts_page.contactpersonmobile"].split(">")
        return getElement(self.driver,locateType,locateExpression)

    def contact_other_info(self):
        locateType,locateExpression=self.login_page_items["addcontacts_page.contactpersoncomment"].split(">")
        return getElement(self.driver,locateType,locateExpression)

    def contact_save_button(self):
        locateType,locateExpression=self.login_page_items["addcontacts_page.savecontactperson"].split(">")
        return getElement(self.driver,locateType,locateExpression)


if __name__=="__main__":
    driver=webdriver.Chrome()
    login(driver,"XXXX", "XXXX")
    hp=HomePage(driver)
    hp.address_book_page_link().click()
    time.sleep(2)
    ap = AddressPage(driver)
    ap.add_contact_button().click()
    time.sleep(2)
    ap.contact_name().send_keys("testyu")
    ap.contact_email().send_keys("XXXX")
    ap.contact_is_star().click()
    ap.contact_mobile().send_keys("XXXX")
    ap.contact_other_info().send_keys("自动化测试")
    ap.contact_save_button().click()
    time.sleep(2)