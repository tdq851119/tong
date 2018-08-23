# -*- coding: utf-8 -*-
import unittest

from Action import LoginAction, JijinAction
from AppiumDriver import Driver
from Judge import JijinJudge


class inMoneyCases(unittest.TestCase):
    def setUp(self):
        self.driver=Driver().getDriver()
        self.login=LoginAction.login(self.driver)
        self.jijin= JijinAction.JiJin(self.driver)
        self.jijincheck=JijinJudge.judgeInMoney(self.driver)

    def teatDown(self):
        #self.driver.quit()
        pass

    '''打开基金页面成功'''
    def test_1_openJijin(self):
        self.login.appLogin()
        self.jijin.openJijin()
        status=self.jijincheck.jijinCheck()
        print u"返回的打开基金页面的状态为："+status
        self.assertEqual(status,"success",u"基金页面打开失败")


if __name__ == '__main__':
    unittest.main()
