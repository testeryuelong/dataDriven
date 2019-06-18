# -*-coding:utf-8 -*-
# @Author : Zhigang

import os

"获取工程所在的目录的绝对路径"
project_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

"测试数据excel文件的绝对路径"
test_data_excel_path=project_path+"\\TestData\\126邮箱联系人.xlsx"

"获取页面对象库文件的绝对路径"
page_object_repository_path=project_path+"\\Conf\\PageObjectRepository.ini"

if __name__=="__main__":
    print(__file__)
    # print (project_path)
    # print (os.getcwd())
    # print (os.path.realpath(__file__))
    # print (os.path.dirname(os.path.realpath(__file__)))
    # print (page_object_repository_path)