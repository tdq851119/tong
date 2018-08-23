# -*- coding:utf-8 -*-
# DATE 2018-08-21
# AUTHER = tongzz
#

import unittest
from  AppiumDriver import Driver
from Action import RechargeAction,LoginAction
from selenium.common.exceptions import NoSuchAttributeException
from Judge import RechargeJudge

class rechargeCases(unittest.TestCase):
    def setUp(self):
        self.driver=Driver().getDriver()
        self.login=LoginAction.login(self.driver)
        self.rechargesuccess = RechargeAction.Recharge(self.driver)
        self.rechargejudge = RechargeJudge.judgeRecharge(self.driver)

    def tearDown(self):
        pass
        # self.driver.close_app()
        # self.driver.quit()
    def test_recharge(self):
        try:
            self.login.appLogin()
            rechargetitle = self.rechargesuccess.rechargeDollar()
            print u'调用充值，返回充值成功页面title ',rechargetitle
            status = self.rechargejudge.Recharge(rechargetitle)
            print status
            if rechargetitle == '充值成功' :
                print u"充值成功"
        except NoSuchAttributeException:
            print u"充值失败"

if __name__ == '__main__':
    unittest.main()

