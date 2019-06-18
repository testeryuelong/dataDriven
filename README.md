# dataDriven
基于PO模式的数据驱动框架


Action

  # 封装操作函数
  --add_contact.py   # 添加联系人信息函数
  
  --login.py               # 登录函数
  
  --visit_address_page.py    # 访问主页函数
  

Conf

  # 配置目录
  --Logger.conf      # 日志配置文件
  
  --PageObjectRepository.ini    # 定位元素配置文件



PageObject


  # 每个业务场景对应一个类，利用不同的方法来操作不同的元素
  --addressBook.py   # 封装AddressPage类
  
  --home_page.py     # 封装HomePage类
  
  --login_page       # 封装LoginPage类
  

ProjectVar

  # 工程路径
  --var.py     # 存储工程相关的全局变量
  

TestData

  # 测试数据/测试用例
  --126邮箱联系人.xlsx   测试数据，记录测试结果
  

TestScript

  # 运行测试框架的主程序
  --runScript.py           # 主程序，操作此脚本
   
  --AutoTestLog.py     # 记录运行日志
   

Util

  # 封装常用的模块
  --Excel.py            # 操作excel模块
  
  --FormatTime.py       # 时间模块
  
  --Log.py              # 日志模块
  
  --ObjectMap.py        # 定位元素模块
  
  --ParsePageObjectRepository.py    # 解析配置文件模块
  
