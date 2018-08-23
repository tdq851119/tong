# -*- coding: utf-8 -*-
# DATE 2018-08-21
# AUTHER = tongzz
#

import time
from selenium.common.exceptions import NoSuchAttributeException
from Elements import RechargeElements
import re
class judgeRecharge():
    def __init__(self,driver):
        self.driver = driver
    def Recharge(self,title):
        title = str(title)
        judgeRechargetitle = self.driver.current_activity
        print title,judgeRechargetitle
        print "#################### 获取到充值成功页面activity == %s  ####################"% judgeRechargetitle
        if title == '充值成功':
            status = "success"
            print u"#################### 检查点校验通过,充值成功  ####################"
        else:
            status = "failed"
            print u"#################### 检查点校验通过,充值失败  ####################"
        print u"#################### 检查点校验通过  ####################",status
        return status


