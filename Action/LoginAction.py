# -*- coding: utf-8 -*-
import time
from Elements import LoginElements
from appium.webdriver.webdriver import By
from selenium.common.exceptions import NoSuchElementException
import others
class login():
    def __init__(self,driver):
        self.driver=driver
        self.other=others.Other(self.driver)

    #登录
    def appLogin(self):
        time.sleep(3)
        try:
            #self.driver.find_element_by_id("ib_guide_pass").click()
            self.driver.find_element(By.ID, LoginElements.click_guide_pass).click()

            #调用活动弹窗方法
            self.other.Activewindow()

            #self.driver.find_element(By.ID, LoginElements.click_maskImg).click()
            self.driver.find_element(By.ID, LoginElements.click_actionMy).click()
            self.driver.find_element(By.ID, LoginElements.click_topMy).click()
            self.driver.find_element(By.ID, LoginElements.enter_username).send_keys(LoginElements.username)
            self.driver.find_element(By.ID, LoginElements.enter_password).send_keys(LoginElements.password)
            self.driver.find_element(By.ID, LoginElements.click_login_button).click()
            print "--------------登录操作-找到操作元素-------------"
        except NoSuchElementException:
            print "------------登录操作-没有找到操作元素------------"
