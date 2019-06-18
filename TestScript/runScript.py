# -*-coding:utf-8 -*-
# @Author : Zhigang

from selenium import webdriver
from Util.Log import *
from Util.FormatTime import *
from Util.Excel import *
import time
from Action.login import *
from Action.add_contact import  *
from Action.visit_address_page import *
from ProjectVar.var import *

def main():
    pe=ParseExcel(test_data_excel_path)
    pe.setSheetByIndex(0)  # 防止默认sheet不是要操作的sheet对象，下同
    "获取第一个sheet的所有行"
    rows=pe.get_all_rows()
    for index,row in enumerate(rows[1:]):
        if row[4].value.lower()=="y":
            username=pe.get_cell_content(index + 2,2)
            password=pe.get_cell_content(index + 2,3)
            driver=webdriver.Chrome()
            try:
                login(driver,username,password)
                visit_address_page(driver)
                sheetName=pe.get_cell_content(index+2,4)
                pe.setSheetByName(sheetName)
                data_row=pe.get_all_rows()
                for id,row in enumerate(data_row[1:]):
                    whether_execute = pe.get_cell_content(id + 2, 8)
                    # print (whether_execute)
                    if whether_execute.lower() == "y":
                        name=pe.get_cell_content(id + 2, 2)
                        email=pe.get_cell_content(id + 2, 3)
                        is_star=pe.get_cell_content(id + 2, 4)
                        mobile=pe.get_cell_content(id + 2, 5)
                        other_info=pe.get_cell_content(id + 2, 6)
                        assert_word=pe.get_cell_content(id + 2, 7)
                        try:
                            add_contact(driver, name=name, email=email, is_star=True, mobile=mobile,other_info=other_info)
                        except Exception as e:
                            pe.write_cell_content(id + 2, 10, "添加联系人失败",color=colors.RED)
                        else:
                            try:
                                assert pe.get_cell_content(id + 2, 7) in driver.page_source
                            except Exception as e:
                                pe.write_cell_content(id + 2, 10, "断言失败",color=colors.RED)
                            else:
                                pe.write_cell_content(id + 2, 10, "成功",color=colors.GREEN)
                        finally:
                            pe.write_cell_content(id + 2, 9, dateTime())
                            pe.save_excel_file()
                    else:
                        pe.write_cell_content(id + 2, 9, dateTime())
                        pe.write_cell_content(id + 2, 10, "忽略")
                        pe.save_excel_file()
            except Exception as e:
                print (e)
                pe.setSheetByName("126账号")
                pe.write_cell_content(index + 2, 6, "失败",color=colors.RED)
            else:
                pe.setSheetByName("126账号")  # 之所以要加，是因为操作的sheet不同，否则会加错sheet
                pe.write_cell_content(index + 2, 6, "成功",color=colors.GREEN)
            finally:
                pe.save_excel_file()
            driver.quit()
        else:
            pe.setSheetByName("126账号")
            # print ("this case is ignored!")
            # row[5].value="忽略"      # 往测试结果中写入
            pe.write_cell_content(index + 2, 6, "忽略")  # 调用内部写的方法写入结果
            pe.save_excel_file()     # 写入内容后保存文件

if __name__=="__main__":
    main()