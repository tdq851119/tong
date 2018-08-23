# -*- coding: utf-8 -*-
import time
class ForgetPassCheck():
    def __init__(self,driver):
        self.driver=driver

    def fogetPassCheck(self):
        act1 = ".views.login.imp.LoginActivity"
        time.sleep(2)
        act2 = self.driver.current_activity
        act = str(act2)
        if act1 == act:
            sta="success"
            print u"---------------------检查点校验通过--------------------"
        else:
            sta="fail"
            print u"---------------------检查点校验未通过--------------------"
        return sta
