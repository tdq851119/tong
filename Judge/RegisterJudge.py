# -*- coding: utf-8 -*-
import time
import randomNo
class judgeRegister():
    def __init__(self,driver):
        self.driver=driver
    '''校验注册功能'''
    def registerCheck(self):
        self.randomPhone=randomNo.Random()
        actregister = ".views.gesture.imp.GestureEditActivity"
        time.sleep(2)
        register1 = self.driver.current_activity
        register = str(register1)
        if  actregister==register:
            sta="success"
            print u"---------------------检查点校验通过--------------------"
            return sta
        else:
            sta="fail"
            print u"---------------------检查点校验未通过--------------------"
            return sta

    '''校验注册跳过实名'''
    def registerPassAuth(self):
        self.randomPhone=randomNo.Random()
        actregister = ".views.home.imp.HomeActivity"
        time.sleep(2)
        register1 = self.driver.current_activity
        register = str(register1)
        if  actregister==register:
            sta="success"
            print u"---------------------检查点校验通过--------------------"
            return sta
        else:
            sta="fail"
            print u"---------------------检查点校验未通过--------------------"
            return sta

