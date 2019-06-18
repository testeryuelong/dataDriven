# -*-coding:utf-8 -*-
# @Author : Zhigang

from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig
from selenium import webdriver

class LoginPage(object):

    def __init__(self,driver):
        "初始化参数，加载配置文件，将'126mail_login'section内容读取出来"
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.login_page_items=self.parse_config_file.getItemsFromSection("126mail_login")

    def frame(self):
        "定位frame元素"
        locateType,locateExpression=self.login_page_items["login_page.frame"].split(">")
        return getElement(self.driver,locateType,locateExpression)

    def username(self):
        "定位账号输入框元素"
        locateType,locateExpression=self.login_page_items["login_page.username"].split(">")
        return getElement(self.driver,locateType,locateExpression)

    def password(self):
        "定位密码输入框元素"
        locateType,locateExpression=self.login_page_items["login_page.password"].split(">")
        return getElement(self.driver,locateType,locateExpression)

    def loginButton(self):
        "定位登陆按钮元素"
        locateType,locateExpression=self.login_page_items["login_page.loginbutton"].split(">")
        return getElement(self.driver,locateType,locateExpression)

    def login(self,userName,passWd):
        "封装登陆动作,这指定了访问网址"
        self.driver.get("http:mail.126.com")
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame(self.frame())
        self.username().clear()
        self.username().send_keys(userName)
        self.password().clear()
        self.password().send_keys(passWd)
        self.loginButton().click()
        time.sleep(2)

    """下面方法是将每一步操作进一步封装"""

    def switchFrame(self):
        "切换frame操作"
        self.driver.switch_to.frame(self.frame())

    def usernameClear(self):
        "清空账号输入框内容"
        self.username().clear()

    def usernameInput(self,value):
        "在账号输入框内输入指定内容"
        self.username().send_keys(value)

    def passwordInput(self,value):
        "在密码输入框内输入指定内容"
        self.password().send_keys(value)

    def loginButtonClick(self):
        "点击登陆按钮"
        self.loginButton().click()

    def loginAdvanced(self,username,password):
        "封装登陆进化版"
        self.driver.get("http:mail.126.com")
        self.driver.implicitly_wait(5)
        self.switchFrame()
        self.usernameClear()
        self.usernameInput(username)
        self.passwordInput(password)
        self.loginButtonClick()
        time.sleep(2)

if __name__=="__main__":
    '''第二次封装后的测试代码
    driver=webdriver.Chrome()
    lp=LoginPage(driver)
    lp.login("XXXX","XXXX")'''

    "第三次封装后的测试代码"
    driver=webdriver.Chrome()
    lp=LoginPage(driver)
    lp.loginAdvanced("XXXX","XXXX")

    '''第一次未封装后的测试代码
    driver = webdriver.Chrome()
    driver.get("http:mail.126.com")
    driver.implicitly_wait(10)
    lp=LoginPage(driver)
    driver.switch_to.frame(lp.frame())
    lp.username().clear()
    lp.username().send_keys("XXXX")
    lp.password().clear()
    lp.password().send_keys("XXXX")
    lp.loginButton().click()
    time.sleep(2)
    driver.quit()'''