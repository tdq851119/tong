# -*- coding: utf-8 -*-
import unittest
from AppiumDriver import Driver
from Action import LoginAction,inMoneyAction
from Judge import inMoneyJudge
import time
class inMoneyCases(unittest.TestCase):
    def setUp(self):
        self.driver=Driver().getDriver()
        self.login=LoginAction.login(self.driver)
        self.inmoney=inMoneyAction.inMoney(self.driver)
        self.inmoneycheck=inMoneyJudge.judgeInMoney(self.driver)

    def teatDown(self):
        #self.driver.quit()
        pass

    '''转入成功'''
    def test_1_inMoney(self):
        self.login.appLogin()
        inmoney=self.inmoney.appinmoney()
        status=self.inmoneycheck.InMoneyCheck(inmoney)
        print u"返回的活期转入的状态为："+status
        self.assertEqual(status,"success",u"活期转入失败")

    '''全部转入'''
    def test_2_inMoneyAll(self):
        self.login.appLogin()
        #self.inmoney.allIn()
        inmoney=self.inmoney.allIn()
        # print 2
        # print inmoney
        # print type(inmoney)
        status=self.inmoneycheck.InMoneyCheck(inmoney)
        print u"返回的活期转入的状态为："+status
        self.assertEqual(status,"success",u"活期转入失败")

if __name__ == '__main__':
    unittest.main()
