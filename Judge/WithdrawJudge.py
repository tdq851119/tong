# -*- coding:utf-8 -*-
# DATE 2018-08-21
# AUTHER = tongzz
#
class judgewithdraw():
    def __init__(self,driver):
        self.driver = driver
    def withdraw1(self,title):
        title = str(title)
        judgepasswdmanagetitle = self.driver.current_activity
        print "#################### 获取到提现成功页面activity == %s  ####################"% judgepasswdmanagetitle
        if title == '充值成功':
            status = "success"
            print u"#################### 检查点校验通过,提现成功  ####################"
        else:
            status = "failed"
            print u"#################### 检查点校验通过,提现失败  ####################"
        print u"#################### 检查点校验通过  ####################",status
        return status
    def withdraw2(self,title):
        title = str(title)
        page_activity = ".views.gesture.PassManagerActivity"
        judgepasswdmanagetitle = self.driver.current_activity
        print "#################### 获取到提现成功页面activity == %s  ####################"% judgepasswdmanagetitle
        if title == '密码管理':
            status = "success"
            print u"#################### 检查点校验通过,提现成功  ####################"
        else:
            status = "failed"
            print u"#################### 检查点校验通过,提现失败  ####################"
        print u"#################### 检查点校验通过  ####################",status
        return status
    def withdraw3(self,title):
        title = str(title)
        judgepasswdmanagetitle = self.driver.current_activity
        print "#################### 获取到提现成功页面activity == %s  ####################"% judgepasswdmanagetitle
        if title == '密码修改成功，请重新登录':
            status = "success"
            print u"#################### 检查点校验通过,提现成功  ####################"
        else:
            status = "failed"
            print u"#################### 检查点校验通过,提现失败  ####################"
        print u"#################### 检查点校验通过  ####################",status
        return status





