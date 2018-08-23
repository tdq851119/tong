# -*- coding: utf-8 -*-
import unittest
from AppiumDriver import Driver
from Action import LoginAction,outMoneyAction
from Judge import outMoneyJudge
class outMoneyCases(unittest.TestCase):
    def setUp(self):
        self.driver=Driver().getDriver()
        self.login=LoginAction.login(self.driver)
        self.outmoney=outMoneyAction.outMoney(self.driver)
        self.outmoneycheck=outMoneyJudge.judgeOutMoney(self.driver)

    def teatDown(self):
        #self.driver.quit()
        pass

    '''正常转出'''
    def test_1_outMoney(self):
        self.login.appLogin()
        outmoney=self.outmoney.appoutmoney()
        status=self.outmoneycheck.OutMoneyCheck(outmoney)
        print u"返回的活期转出的状态为：" + status
        self.assertEqual(status, "success", u"活期转出失败")

    '''全部转出'''
    def test_2_outMoneyAll(self):
        self.login.appLogin()
        outmoney=self.outmoney.appOutAll()
        status=self.outmoneycheck.OutMoneyCheck(outmoney)
        print u"返回的活期转出的状态为：" + status
        self.assertEqual(status, "success", u"活期转出失败")

if __name__ == '__main__':
    unittest.main()
