# -*- coding: utf-8 -*-
import unittest
from AppiumDriver import Driver
from Action import SuggestAction,LoginAction
from Judge import SuggestJudge
class SuggestCases(unittest.TestCase):
    def setUp(self):
        self.driver=Driver().getDriver()
        self.login=LoginAction.login(self.driver)
        self.suggest=SuggestAction.suggest(self.driver)
        self.suggestCheck=SuggestJudge.judgeSuggest(self.driver)

    def teatDown(self):
        #self.driver.quit()
        pass

    def test_1_suggestSuccess(self):
        self.login.appLogin()
        text2=self.suggest.appSuggest()
        status = self.suggestCheck.suggestCheck(text2)
        print u"返回的登录状态为:"+status
        self.assertEqual(status, u'登录成功', u'登录失败')

if __name__ == '__main__':
    unittest.main()
