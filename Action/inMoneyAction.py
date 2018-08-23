# -*- coding: utf-8 -*-
import time
from Elements import inMoneyElements
from appium.webdriver.webdriver import By
from selenium.common.exceptions import NoSuchElementException
class inMoney():
    def __init__(self,driver):
        self.driver=driver

    '''活期转入'''
    def appinmoney(self):
        try:
            self.driver.find_element(By.ID, inMoneyElements.click_left).click()
            self.driver.find_element(By.ID, inMoneyElements.click_bid).click()
            # self.driver.find_element(By.ID,inMoneyElements.click_maskImg).click()
            self.driver.find_element(By.ID, inMoneyElements.click_huoqi).click()
            self.driver.find_element(By.ID, inMoneyElements.click_inMoney).click()
            # time.sleep(2)
            self.driver.find_element(By.ID, inMoneyElements.enter_inMoneyEdit).send_keys(inMoneyElements.money)
            inmo = self.driver.find_element(By.ID, inMoneyElements.enter_inMoneyEdit).text
            # self.driver.find_element_by_id("allInBtn").click()
            # self.driver.hide_keyboard()
            self.driver.find_element(By.ID, inMoneyElements.click_inOutBtn).click()
            # time.sleep(3)
            print u"--------------活期转入操作-找到操作元素-------------"
            return inmo
        except NoSuchElementException:
            print u"------------活期转入操作-没有找到操作元素-----------"

    '''活期全部转入'''
    def allIn(self):
        try:
            self.driver.find_element(By.ID, inMoneyElements.click_left).click()
            self.driver.find_element(By.ID, inMoneyElements.click_bid).click()
            self.driver.find_element(By.ID, inMoneyElements.click_huoqi).click()
            self.driver.find_element(By.ID, inMoneyElements.click_inMoney).click()
            self.driver.find_element(By.ID, inMoneyElements.click_allIn).click()
            inmo=self.driver.find_element(By.ID, inMoneyElements.enter_inMoneyEdit).text
            # self.driver.hide_keyboard()
            self.driver.find_element(By.ID, inMoneyElements.click_inOutBtn).click()
            # time.sleep(3)
            print u"--------------活期转入操作-找到操作元素-------------"
            return inmo
        except NoSuchElementException:
            print u"------------活期转入操作-没有找到操作元素-----------"