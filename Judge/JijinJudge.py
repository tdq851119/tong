# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchElementException
import re
class judgeInMoney():
    def __init__(self,driver):
        self.driver=driver

    def jijinCheck(self):
        time.sleep(2)
        actlogin = ".views.webview.imp.WebViewActivity"
        act1 = self.driver.current_activity
        act = str(act1)
        typeact = str(type(act))
        print u"获取到当前页的activity的值是：" + act
        print u"获取到当前页的activity值的类型是：" + typeact
        if actlogin == act:
            sta = "success"
            print u"---------------------检查点校验通过--------------------"
        else:
            sta = "fail"
            print u"---------------------检查点校验未通过--------------------"
        return sta