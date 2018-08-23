# -*- coding: utf-8 -*-
import time
from Elements import JijinElements
from appium.webdriver.webdriver import By
from selenium.common.exceptions import NoSuchElementException
import others
class JiJin():
    def __init__(self,driver):
        self.driver=driver

    def openJijin(self):
        try:
            self.driver.find_element(By.ID, JijinElements.click_left).click()
            self.driver.find_element(By.ID, JijinElements.click_bid).click()
            self.driver.find_element(By.ID, JijinElements.click_jijin).click()
            self.driver.find_element(By.ID, JijinElements.click_shengou).click()
            print u"--------------基金打开操作-找到操作元素-------------"
        except NoSuchElementException:
            print u"------------基金打开操作-没有找到操作元素-----------"

