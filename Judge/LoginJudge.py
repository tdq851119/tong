# -*- coding: utf-8 -*-
import time
class judgeLogin():
    def __init__(self,driver):
        self.driver = driver

    def loginCheck(self):
        actlogin = ".views.gesture.imp.GestureEditActivity"
        time.sleep(2)
        act1 = self.driver.current_activity
        act = str(act1)
        typeact = str(type(act))
        print u"获取到当前页的activity的值是111：" + act
        print u"获取到当前页的activity值的类型是111：" + typeact
        status=[u"登录成功",u"登录失败"]
        if actlogin == act:
            sta = status[0]
            print u"---------------------检查点校验通过--------------------"
        else:
            sta = status[1]
            print u"---------------------检查点校验未通过--------------------"
        return sta