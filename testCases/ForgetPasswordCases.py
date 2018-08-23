# -*- coding: utf-8 -*-
import unittest

from Action import ForgetPasswordAction
from AppiumDriver import Driver
from Judge import ForgetPasswordJudge


class ForgetPasswordCases(unittest.TestCase):
    def setUp(self):
        self.driver=Driver().getDriver()
        self.forgetpassword= ForgetPasswordAction.forget(self.driver)
        self.forgetpasswordcheck=ForgetPasswordJudge.ForgetPassCheck(self.driver)

    def teatDown(self):
        #self.driver.quit()
        pass

    def test_1_forgetpasswordSuccess(self):
        self.forgetpassword.appForgetPassword()
        status=self.forgetpasswordcheck.fogetPassCheck()
        print u"返回的加入理财计划状态为："+status
        self.assertEqual(status,"success",u"加入理财计划失败")

if __name__ == '__main__':
    unittest.main()
