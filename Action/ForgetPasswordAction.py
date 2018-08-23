# -*- coding:utf-8 -*-
import time
from Elements import ForgetPasswordElements
from appium.webdriver.webdriver import By
from selenium.common.exceptions import NoSuchElementException
import others
class forget():
    def __init__(self,driver):
        self.driver=driver
        self.other=others.Other(self.driver)

    #忘记登录密码
    def appForgetPassword(self):
        try:
            self.driver.find_element(By.ID, ForgetPasswordElements.click_guide_pass).click()
            # self.driver.find_element_by_id("ib_guide_pass").click()

            #调用活动弹窗方法
            self.other.Activewindow()

            # self.driver.find_element(By.ID, ForgetPasswordElements.click_maskImg).click()
            self.driver.find_element(By.ID, ForgetPasswordElements.click_actionMy).click()
            self.driver.find_element(By.ID, ForgetPasswordElements.click_topMy).click()
            self.driver.find_element(By.ID, ForgetPasswordElements.click_forget).click()
            self.driver.find_element(By.ID, ForgetPasswordElements.enter_phone).send_keys(ForgetPasswordElements.phone)
            self.driver.find_element(By.ID, ForgetPasswordElements.click_getcode).click()
            self.driver.find_element(By.ID, ForgetPasswordElements.enter_codeEdit).send_keys(
                ForgetPasswordElements.code)
            self.driver.find_element(By.ID, ForgetPasswordElements.click_next).click()
            self.driver.find_element(By.ID, ForgetPasswordElements.enter_new_login).send_keys(
                ForgetPasswordElements.newpassword)
            self.driver.find_element(By.ID, ForgetPasswordElements.click_next).click()
            print u"--------------忘记登录密码操作-找到操作元素-------------"
        except NoSuchElementException:
            print u"------------忘记登录密码操作-没有找到操作元素-----------"



