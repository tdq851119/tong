# -*- coding: utf-8 -*-
import unittest
import AppiumDriver
from Action import RegisterAction
from Judge import RegisterJudge
class RegisterCases(unittest.TestCase):
    def setUp(self):
        self.driver=AppiumDriver.Driver().getDriver()
        self.register=RegisterAction.register(self.driver)
        self.registercheck=RegisterJudge.judgeRegister(self.driver)

    def tearDown(self):
        pass

    def test_1_RegisterSucces(self):
        self.register.appRegister()
        #self.registercheck.registerCheck()
        status = self.registercheck.registerCheck()
        print u"返回的注册状态为:" + status
        self.assertEqual(status, 'success', u'注册失败')

    def test_2_RegisterPassAuth(self):
        self.register.appRegisterPassAuth()
        status = self.registercheck.registerPassAuth()
        print u"返回的注册状态为:" + status
        self.assertEqual(status, 'success', u'注册失败')

if __name__ == '__main__':
    unittest.main()
