# -*-coding:utf-8 -*-
# @Author : Zhigang

import time
import datetime


def dateTimeChinese():
    "中文日期和时间"
    return time.strftime("%Y{y}%m{m}%d{d} %H{H}%M{M}%S{S}").format(y="年",m="月",d="日",H="时",M="分",S="秒")

def dateChinese():
    "中文日期"
    return time.strftime("%Y{y}%m{m}%d{d}").format(y="年", m="月", d="日")

def timeChinese():
    "中文时间"
    return time.strftime("%H{H}%M{M}%S{S}").format(H="时",M="分",S="秒")

def dateTime():
    "数字日期和时间"
    return time.strftime("%Y-%m-%d %H:%M:%S")

def dateTimeSlash():
    "斜线数字日期和时间"
    return time.strftime("%Y/%m/%d %H:%M:%S")

def dates():
    "日期"
    return time.strftime("%Y-%m-%d")

def dateSlash():
    "斜线日期"
    return time.strftime("%Y/%m/%d")

def times():
    "时间"
    return time.strftime("%H:%M:%S")

def year():
    "年"
    return time.strftime("%Y")

def month():
    "月"
    return time.strftime("%m")

def day():
    "日"
    return time.strftime("%d")

def hour():
    "小时"
    return time.strftime("%H")

def minute():
    "分钟"
    return time.strftime("%M")

def seconds():
    "秒"
    return time.strftime("%S")

def str_to_tuple(stime):
    "字符串转化为时间元组"
    return time.strptime(stime,"%Y-%m-%d %H:%M:%S")

def intervalDate(dayNum):
    "间隔天数的日期，可增可减"
    today=datetime.date.today()
    return today+datetime.timedelta(dayNum)

if __name__=="__main__":
    print (dateTimeChinese())
    print (dateChinese())
    print (timeChinese())
    print (dateTime())
    print (dateTimeSlash())
    print (dates())
    # print (dateSlash())
    # print (times())
    # print (year())
    # print (month())
    # print (day())
    # print (hour())
    # print (minute())
    # print (seconds())
    # print (str_to_tuple("2019-02-01 11:05:25"))
    print (intervalDate(-3))