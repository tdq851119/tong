# -*- coding: utf-8 -*-
import unittest
from AppiumDriver import Driver
from Action.LoginAction import login
from Judge import LoginJudge
class LoginCases(unittest.TestCase):
    def setUp(self):
        #self.start=Driver()
        self.driver=Driver().getDriver()
        self.login=login(self.driver)
        self.logincheck=LoginJudge.judgeLogin(self.driver)

    def tearDown(self):
        #self.driver.quit()
        pass

    def test_1_loginSuccess(self):
        print self.driver
        self.login.appLogin()
        #self.loginCheck.loginCheck(self.driver)
        status=self.logincheck.loginCheck()
        print u"返回的登录状态为:"+status
        self.assertEqual(status, u'登录成功', u'登录失败')

if __name__ == '__main__':
    unittest.main()
