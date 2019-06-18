# -*-coding:utf-8 -*-
# @Author : Zhigang

from configparser import ConfigParser
from ProjectVar.var import page_object_repository_path

class ParsePageObjectRepositoryConfig(object):

    def __init__(self):
        self.cf=ConfigParser()
        self.cf.read(page_object_repository_path)

    def getItemsFromSection(self,sectionName):
        "转换成字典类型"
        return dict(self.cf.items(sectionName))

    def getOptionsValue(self,sectionName,optionName):
        return self.cf.get(sectionName,optionName)


if __name__=="__main__":
    p=ParsePageObjectRepositoryConfig()
    print (p.getItemsFromSection("126mail_login"))
    print (p.getOptionsValue("126mail_login","login_page.username"))
