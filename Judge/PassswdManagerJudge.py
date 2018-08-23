# -*- coding:utf-8 -*-
# DATE 2018-08-21
# AUTHER = tongzz
#

import time
from selenium.common.exceptions import NoSuchAttributeException
from Elements import RechargeElements
import re
class PasswdManageJudge():
    def __init__(self,driver):
        self.driver = driver
    def passwdmanage1(self,title):
        title = str(title)
        # active = str(active)
        passwdmanagetitle = self.driver.current_activity
        print title,passwdmanagetitle
        print "#################### 获取到设置交易密码成功页面activity == %s  ####################"% passwdmanagetitle
        if title == '密码管理':
            status = "success"
            print u"#################### 检查点校验通过,忘记交易密码成功  ####################"
        else:
            status = "failed"
            print u"#################### 检查点校验通过,忘记交易密码失败  ####################"
        print u"#################### 检查点校验通过  ####################",status
        return status
    def passwdmanage2(self,title):
        title = str(title)
        passwdmanagetitle = self.driver.current_activity
        print title,passwdmanagetitle
        print "#################### 获取到修改交易密码成功页面activity == %s  ####################"% passwdmanagetitle
        if title == '密码管理':
            status = "success"
            print u"#################### 检查点校验通过,修改交易密码成功  ####################"
        else:
            status = "failed"
            print u"#################### 检查点校验通过,修改交易密码失败  ####################"
        print u"#################### 检查点校验通过  ####################",status
        return status
    def passwdmanage3(self,title):
        title = str(title)
        passwdmanagetitle = self.driver.current_activity
        print title,passwdmanagetitle
        print "#################### 获取到忘记交易密码成功页面activity == %s  ####################"% passwdmanagetitle
        if title == '密码管理':
            status = "success"
            print u"#################### 检查点校验通过,忘记交易密码成功  ####################"
        else:
            status = "failed"
            print u"#################### 检查点校验通过,忘记交易密码失败  ####################"
        print u"#################### 检查点校验通过  ####################",status
        return status

    def passwdmanage4(self,title):
        title = str(title)
        judgepasswdmanagetitle = self.driver.current_activity
        print "#################### 获取到修改登录密码页面activity == %s  ####################" % judgepasswdmanagetitle
        if title == '密码修改成功，请重新登录':
            status = "success"
            print u"#################### 检查点校验通过,修改登录密码成功  ####################"
        else:
            status = "failed"
            print u"#################### 检查点校验通过,修改登录密码失败  ####################"
        print u"#################### 检查点校验通过  ####################",status
        return status