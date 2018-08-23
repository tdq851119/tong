# -*- coding:utf-8 -*-
# DATE 2018-08-21
# AUTHER = tongzz
#
import unittest
from  AppiumDriver import Driver
from Action import PasswordManageAction,LoginAction,ForgetPasswordAction
from selenium.common.exceptions import NoSuchAttributeException
from Judge import PassswdManagerJudge
from Database import TradePasswd
import time
class Withdraw(unittest.TestCase):
    def setUp(self):
        self.driver=Driver().getDriver()
        self.login=LoginAction.login(self.driver)
        self.passwdmanageaction = PasswordManageAction.Passwdmanage(self.driver)
        self.passwdmanagejudge = PassswdManagerJudge.PasswdManageJudge(self.driver)
        self.forgetpasswd = ForgetPasswordAction.forget(self.driver)
        self.tradepasswd = TradePasswd.Tradepasswd()

    def tearDown(self):
        pass
    # @unittest.skip(u"强制跳过设置交易密码")
    def test_1passwdmanage1(self):
        try:
            self.login.appLogin()
            passwdmanagetitle = self.passwdmanageaction.passwdmanage1()
            status = self.passwdmanagejudge.passwdmanage1(passwdmanagetitle)
            print status
            if status == "success":
                print u"设置交易密码成功！"
            else:
                print u"设置交易密码失败！"
        except NoSuchAttributeException:
            print u"修改登录密码失败！"

    # @unittest.skip(u"强制跳过设置交易密码")
    def test_2passwdmanage2(self):
        try:
            self.login.appLogin()
            passwdmanagetitle = self.passwdmanageaction.passwdmanage2()
            status = self.passwdmanagejudge.passwdmanage2(passwdmanagetitle)
            print status
            if status == "success":
                print u"修改交易密码成功！"
            else:
                print u"修改交易密码失败！"
        except NoSuchAttributeException:
            print u"修改交易密码失败！"
    # @unittest.skip(u"强制跳过设置交易密码")
    def test_3passwdmanage3(self):
        try:
            self.login.appLogin()
            passwdmanagetitle = self.passwdmanageaction.passwdmanage3()
            status = self.passwdmanagejudge.passwdmanage3(passwdmanagetitle)
            print status
            if status == "success":
                print u"忘记交易密码成功！"
            else:
                print u"忘记交易密码失败！"
        except NoSuchAttributeException:
            print u"忘记交易密码失败！"

    # @unittest.skip(u"强制跳过设置交易密码")
    def test_4passwdmanage4(self):
        try:
            self.login.appLogin()
            passwdmanagetitle = self.passwdmanageaction.passwdmanage4()
            status = self.passwdmanagejudge.passwdmanage4(passwdmanagetitle)
            print status
            if status == "success":
                print u"修改登录密码成功！"
            else:
                print u"修改登录密码失败！"
        except NoSuchAttributeException:
            print u"修改登录密码失败！"
    def test_5forgetpasswd(self):
        try:
            self.passwdmanageaction.appForgetPassword5()
            print u"忘记登陆密码操作恢复登陆密码成功！"
        except NoSuchAttributeException:
            print u"初始化登陆密码失败"
    @unittest.skip(u"强制跳过设置交易密码")
    def test_6tradepasswds(self):
        try:
            returnmessage = self.tradepasswd.tradePasswd()
            time.sleep(5)
            print returnmessage
            print u"恢复交易密码初始化成功!"
        except NoSuchAttributeException:
            print u"恢复交易密码初始化失败!"
if __name__ == '__main__':
    unittest.main()
