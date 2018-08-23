# -*- coding: utf-8 -*-
import unittest
from AppiumDriver import Driver
from Action import LoginAction,ToubiaoAction
from Judge import ToubiaoJudge
class toubiaoCases(unittest.TestCase):
    def setUp(self):
        self.driver=Driver().getDriver()
        self.login=LoginAction.login(self.driver)
        self.toubiao=ToubiaoAction.toubiao(self.driver)
        self.toubiaocheck=ToubiaoJudge.judgeToubiao(self.driver)

    def teatDown(self):
        #self.driver.quit()
        pass

    '''正常投标'''
    def test_1_ToubiaoSuccess(self):
        self.login.appLogin()
        self.toubiao.appToubiao()
        status=self.toubiaocheck.ToubiaoCheck()
        print u"返回的投标状态为："+status
        self.assertEqual(status,"success",u"投标失败")
        self.driver.find_element_by_id("blueBtn").click()

    '''全部投入'''
    def test_2_ToubiaoSuccessAll(self):
        self.login.appLogin()
        self.toubiao.appToubiao()
        status=self.toubiaocheck.ToubiaoCheck()
        print u"返回的投标状态为："+status
        self.assertEqual(status,"success",u"投标失败")
        self.driver.find_element_by_id("blueBtn").click()

    '''优惠券兑付'''
    def test_3_toubiaoCouponCash(self):
        self.login.appLogin()
        self.toubiao.appToubiaoCouponCash()
        status=self.toubiaocheck.ToubiaoCheck()
        print u"返回的投标状态为："+status
        self.assertEqual(status,"success",u"投标失败")
        self.driver.find_element_by_id("blueBtn").click()

    '''分享标'''
    def test_4_Share(self):
        self.login.appLogin()
        self.toubiao.appToubiaoShare()
        status=self.toubiaocheck.ToubiaoShare()
        print u"返回的投标状态为："+status
        self.assertEqual(status,"success",u"投标失败")

if __name__ == '__main__':
    unittest.main()
