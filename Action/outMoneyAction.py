# -*- coding: utf-8 -*-
import time
from Elements import outMoneyElements
from appium.webdriver.webdriver import By
from selenium.common.exceptions import NoSuchElementException
class outMoney():
    def __init__(self,driver):
        self.driver=driver

    '''活期转出'''
    def appoutmoney(self):
        try:
            self.driver.find_element(By.ID,outMoneyElements.click_left).click()
            self.driver.find_element(By.ID,outMoneyElements.click_bid).click()
            #self.driver.find_element(By.ID,inMoneyElements.click_maskImg).click()
            self.driver.find_element(By.ID,outMoneyElements.click_huoqi).click()
            self.driver.find_element(By.ID,outMoneyElements.click_outMoney).click()
            self.driver.find_element(By.ID,outMoneyElements.enter_outMoneyEdit).send_keys(outMoneyElements.money)
            oumoney=self.driver.find_element(By.ID,outMoneyElements.enter_outMoneyEdit).text
            self.driver.find_element(By.ID,outMoneyElements.click_outOutBtn).click()
            self.driver.find_element(By.ID,outMoneyElements.enter_tradepassword).send_keys(outMoneyElements.tradePassword)
            self.driver.find_element(By.ID, outMoneyElements.click_btn_submit).click()
            time.sleep(3)
            print "--------------活期转出操作-找到操作元素-------------"
            return oumoney
        except NoSuchElementException:
            print "------------活期转出操作-没有找到操作元素-------------"

    '''活期全部转出'''
    def appOutAll(self):
        try:
            self.driver.find_element(By.ID,outMoneyElements.click_left).click()
            self.driver.find_element(By.ID,outMoneyElements.click_bid).click()
            self.driver.find_element(By.ID,outMoneyElements.click_huoqi).click()
            self.driver.find_element(By.ID,outMoneyElements.click_outMoney).click()
            self.driver.find_element(By.ID,outMoneyElements.click_allout).click()
            oumoney=self.driver.find_element(By.ID,outMoneyElements.enter_outMoneyEdit).text
            self.driver.find_element(By.ID,outMoneyElements.click_outOutBtn).click()
            self.driver.find_element(By.ID,outMoneyElements.enter_tradepassword).send_keys(outMoneyElements.tradePassword)
            self.driver.find_element(By.ID, outMoneyElements.click_btn_submit).click()
            print "--------------活期转出操作-找到操作元素-------------"
            return oumoney
        except NoSuchElementException:
            print "------------活期转出操作-没有找到操作元素-------------"



