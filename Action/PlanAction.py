# -*- coding: utf-8 -*-
import time
from Elements import PlanElements
from appium.webdriver.webdriver import By
from selenium.common.exceptions import NoSuchElementException
import re
class plan():
    def __init__(self,driver):
        self.driver=driver
    '''正常加入'''
    def appPlan(self):
        try:
            self.driver.find_element(By.ID,PlanElements.click_left).click()
            self.driver.find_element(By.ID,PlanElements.click_bid).click()
            self.driver.find_element(By.ID,PlanElements.click_rxbplan).click()
            self.driver.find_element(By.ID,PlanElements.click_header_background).click()
            self.driver.find_element(By.ID,PlanElements.click_pay).click()
            self.driver.find_element(By.ID,PlanElements.enter_inMoneyEdit).send_keys(PlanElements.money)
            planMoney=self.driver.find_element(By.ID,PlanElements.enter_inMoneyEdit).text
            #self.driver.find_element_by_id("allInBtn").click()
            #self.driver.hide_keyboard()
            self.driver.find_element(By.ID, PlanElements.click_submitBtn).click()
            print u"----------------加入计划操作-找到操作元素---------------"
            return planMoney
        except NoSuchElementException:
            print u"----------------加入计划操作-没有找到操作元素---------------"

    '''全部投入'''
    def appPlanAll(self):
        try:
            self.driver.find_element(By.ID,PlanElements.click_left).click()
            self.driver.find_element(By.ID,PlanElements.click_bid).click()
            self.driver.find_element(By.ID,PlanElements.click_rxbplan).click()
            self.driver.find_element(By.ID,PlanElements.click_header_background).click()
            self.driver.find_element(By.ID,PlanElements.click_pay).click()
            self.driver.find_element(By.ID,PlanElements.click_planall).click()
            planMoney=self.driver.find_element(By.ID,PlanElements.enter_inMoneyEdit).text
            #self.driver.find_element_by_id("allInBtn").click()
            #self.driver.hide_keyboard()
            self.driver.find_element(By.ID, PlanElements.click_submitBtn).click()
            print u"----------------加入计划操作-找到操作元素---------------"
            return planMoney
        except NoSuchElementException:
            print u"----------------加入计划操作-没有找到操作元素---------------"

    '''优惠券兑付'''
    def planCouponCash(self):
        try:
            self.driver.find_element(By.ID, PlanElements.click_left).click()
            self.driver.find_element(By.ID, PlanElements.click_bid).click()
            self.driver.find_element(By.ID, PlanElements.click_rxbplan).click()
            self.driver.find_element(By.ID, PlanElements.click_header_background).click()
            self.driver.find_element(By.ID, PlanElements.click_pay).click()
            #选择优惠券
            self.driver.find_element(By.ID, PlanElements.click_ChooseCoupon).click()
            self.driver.find_element(By.XPATH, PlanElements.click_Coupon).click()
            self.driver.find_element(By.ID, PlanElements.click_queding).click()
            text=self.driver.find_element(By.ID, PlanElements.youhuiquan).text
            print "text:"
            print text
            #去掉文案中的逗号
            text1=text.replace("，","")
            print "text1"
            print text1
            text2=text1.replace(",","")
            print "text2"
            print text2
            #取出文案中的数字
            text3=re.findall(r"\d+\.?\d*", text2)
            print "text3"
            print text3
            self.driver.find_element(By.ID,PlanElements.enter_inMoneyEdit).send_keys(text3[1])
            planMoney = self.driver.find_element(By.ID, PlanElements.enter_inMoneyEdit).text
            # self.driver.find_element_by_id("allInBtn").click()
            # self.driver.hide_keyboard()
            self.driver.find_element(By.ID, PlanElements.click_submitBtn).click()
            print u"----------------加入计划操作-找到操作元素---------------"
            return planMoney
        except NoSuchElementException:
            print u"----------------加入计划操作-没有找到操作元素---------------"

