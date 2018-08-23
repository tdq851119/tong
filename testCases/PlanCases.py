# -*- coding: utf-8 -*-
import unittest
from AppiumDriver import Driver
from Action import LoginAction,PlanAction
from Judge import PlanJudge
class PlanCases(unittest.TestCase):
    def setUp(self):
        self.driver=Driver().getDriver()
        self.login=LoginAction.login(self.driver)
        self.plan=PlanAction.plan(self.driver)
        self.plancheck=PlanJudge.judgePlan(self.driver)

    def teatDown(self):
        #self.driver.quit()
        pass

    '''加入计划成功'''
    def test_1_plan(self):
        self.login.appLogin()
        planmoney=self.plan.appPlan()
        #status=self.plancheck.planCheck(self.driver)
        status=self.plancheck.planCheck(planmoney)
        print u"返回的加入理财计划状态为："+status
        self.assertEqual(status,"success",u"加入理财计划失败")

    '''全部投入'''
    def test_2_planAll(self):
        self.login.appLogin()
        planmoney=self.plan.appPlanAll()
        status=self.plancheck.planCheck(planmoney)
        print u"返回的加入理财计划状态为："+status
        self.assertEqual(status,"success",u"加入理财计划失败")

    '''优惠券兑付'''
    def test_3_planCouponCash(self):
        self.login.appLogin()
        planmoney=self.plan.planCouponCash()
        status=self.plancheck.planCheck(planmoney)
        print u"返回的加入理财计划状态为："+status
        self.assertEqual(status,"success",u"加入理财计划失败")


if __name__ == '__main__':
    unittest.main()
