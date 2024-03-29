# -*-coding:utf-8 -*-
# @Author : Zhigang

import logging.config
from ProjectVar.var import *

#读取日志的配置文件
logging.config.fileConfig(project_path+"\\Conf\\Logger.conf")
#选择一个日志格式
logger=logging.getLogger("example02")

def error(message):
    "打印debug级别的信息"
    logger.error(message)

def info(message):
    "打印info级别的信息"
    logger.info(message)

def warning(message):
    "打印warnning级别的信息"
    logger.warning(message)

if __name__=="__main__":
    print ("conf file path:",project_path+"\\Conf\\Logger.conf")
    info("hi")
    error("world")
    warning("gloryroad")