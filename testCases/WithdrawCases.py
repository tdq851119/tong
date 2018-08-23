# -*- coding:utf-8 -*-
# DATE 2018-08-21
# AUTHER = tongzz
#
import unittest
from  AppiumDriver import Driver
from Action import WithdrawAction,LoginAction
from selenium.common.exceptions import NoSuchAttributeException
from Judge import WithdrawJudge

class Withdraw(unittest.TestCase):
    def setUp(self):
        self.driver=Driver().getDriver()
        self.login=LoginAction.login(self.driver)
        self.withdrawsuccess = WithdrawAction.withdraw(self.driver)
        self.withdrawjudge = WithdrawJudge.judgewithdraw(self.driver)

    def tearDown(self):
        pass
    def test_withdraw(self):
        try:
            self.login.appLogin()
            withdrawtitle = self.withdrawsuccess.appwithdraw()
            status = self.withdrawjudge.withdraw(withdrawtitle)
            print status
            if status == "success":
                print u"提现成功！"
            else:
                print u"提现操作失败！"
        except NoSuchAttributeException:
            print u"提现失败！"
if __name__ == '__main__':
    unittest.main()



