# -*- coding:utf-8 -*-
# DATE 2018-08-21
# AUTHER = tongzz
#
from appium.webdriver.webdriver import By
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from Elements.PasswordmanageElements import *
from Elements.LoginElements import *
import others
import time
class Passwdmanage():
    def __init__(self,driver):
        self.driver = driver
        self.other = others.Other(self.driver)
        # self.driver.implicitly_wait(30)

    def passwdmanage1(self):
        try:
            self.driver.implicitly_wait(30)
            self.driver.find_element(By.ID, click_left).click()
            self.driver.find_element(By.ID, click_actionMy).click()
            self.driver.find_element(By.ID, click_setting).click()
            self.driver.find_element(By.ID, click_passwdmanage).click()
            self.driver.find_element(By.ID, click_set_trade_passwd).click()
            self.driver.find_element(By.ID, set_newtradepasswd).send_keys(tradepasswd)
            self.driver.find_element(By.ID, click_set_newtradepasswd_button).click()
            print u"设置交易密码成功！"
            time.sleep(3)
            title = self.driver.find_element(By.ID,passwdmanage_title).text
            judgepasswdmanagetitle = self.driver.current_activity
            print judgepasswdmanagetitle
            print "#################### 设置交易密码找到元素，修改成功! recharge_title = %s  ####################" % title
            return title
        except NoSuchAttributeException:
            print u"#################### 设置交易密码操作没有找到元素  ####################"

    def passwdmanage2(self):
        try:
            self.driver.implicitly_wait(30)
            self.driver.find_element(By.ID,click_left).click()
            self.driver.find_element(By.ID,click_actionMy).click()
            self.driver.find_element(By.ID,click_setting).click()
            self.driver.find_element(By.ID,click_passwdmanage).click()
            self.driver.find_element(By.ID,click_change_tradepasswd).click()
            self.driver.find_element(By.ID,change_trade_passwd_old).send_keys(tradepasswd)
            self.driver.find_element(By.ID,change_trade_passwd_new).send_keys(new_tradepasswd)
            self.driver.find_element(By.ID,change_trade_passwd_sure).send_keys(new_tradepasswd)
            self.driver.find_element(By.ID,click_passwd_button).click()
            print u"修改交易密码成功"
            time.sleep(3)
            title = self.driver.find_element(By.ID, passwdmanage_title).text
            # judgepasswdmanagetitle = self.driver.current_activity
            print "#################### 修改交易密码找到元素，修改成功! recharge_title = %s  ####################"%title
            return title
        except NoSuchAttributeException:
            print u"#################### 修改交易密码操作没有找到元素  ####################"
    def passwdmanage3(self):
        try:
            self.driver.implicitly_wait(30)
            self.driver.find_element(By.ID,click_left).click()
            self.driver.find_element(By.ID,click_actionMy).click()
            self.driver.find_element(By.ID,click_setting).click()
            self.driver.find_element(By.ID,click_passwdmanage).click()
            self.driver.find_element(By.ID,click_forget_trade_passwd).click()
            print u"点击获取验证码"
            self.driver.find_element(By.ID,forget_getcode_button).click()
            print u"点击获取验证码成功"
            self.driver.find_element(By.ID,forget_getcode).send_keys(Verification_Code)
            self.driver.find_element(By.ID,confirm_button).click()
            self.driver.find_element(By.ID,foget_trade_passwd_new).send_keys(tradepasswd)
            self.driver.find_element(By.ID,click_settradepasswd_button).click()
            print u"忘记交易密码成功"
            time.sleep(3)
            title = self.driver.find_element(By.ID, passwdmanage_title).text
            # judgepasswdmanagetitle = self.driver.current_activity
            print "#################### 忘记交易密码找到元素，修改成功! recharge_title = %s  ####################"%title
            return title
        except NoSuchAttributeException:
            print u"#################### 忘记交易密码操作没有找到元素  ####################"
    def passwdmanage4(self):
        try:
            self.driver.implicitly_wait(30)
            self.driver.find_element(By.ID,click_left).click()
            self.driver.find_element(By.ID,click_actionMy).click()
            self.driver.find_element(By.ID,click_setting).click()
            self.driver.find_element(By.ID,click_passwdmanage).click()
            self.driver.find_element(By.ID,click_passwd_change).click()
            self.driver.find_element(By.ID,passwd_old).send_keys(password)
            self.driver.find_element(By.ID,passwd_new).send_keys(new_passwd)
            self.driver.find_element(By.ID,passwd_sure).send_keys(new_passwd)
            self.driver.find_element(By.ID,click_passwd_button).click()
            time.sleep(3)
            title = self.driver.find_element(By.ID,passwd_txt).text
            print "#################### 修改登录密码找到元素，修改成功! recharge_title = %s  ####################"%title
            return title
        except NoSuchAttributeException:
            print u"#################### 修改登录密码操作没有找到元素  ####################"
#忘记登录密码
    def appForgetPassword5(self):
        try:
            self.driver.find_element(By.ID, click_guide_pass).click()
            # self.driver.find_element_by_id("ib_guide_pass").click()
            #调用活动弹窗方法
            self.other.Activewindow()
            # self.driver.find_element(By.ID, ForgetPasswordElements.click_maskImg).click()
            self.driver.find_element(By.ID, click_actionMy).click()
            self.driver.find_element(By.ID, click_topMy).click()
            self.driver.find_element(By.ID, click_forget).click()
            self.driver.find_element(By.ID, enter_phone).send_keys(phone)
            self.driver.find_element(By.ID, click_getcode).click()
            self.driver.find_element(By.ID, enter_codeEdit).send_keys(code)
            self.driver.find_element(By.ID, click_next).click()
            print u"手机号验证码成功"
            print self.driver.current_activity
            time.sleep(3)
            self.driver.find_element(By.ID, "name").send_keys(u'仝志钊')
            self.driver.find_element(By.ID, "cardId").send_keys('610125198511194330')
            # self.driver.find_element(By.ID, "name").send_keys("仝志钊")
            # self.driver.find_element(By.ID, "cardId").send_keys("610125198511194330")
            # self.driver.find_element(By.ID, name_edit).send_keys(name)
            # self.driver.find_element(By.ID, number_edit).send_keys(number)
            self.driver.find_element(By.ID, click_next).click()
            self.driver.find_element(By.ID, enter_new_login).send_keys(newpassword)
            self.driver.find_element(By.ID, click_next).click()
            print u"--------------忘记登录密码操作-找到操作元素-------------"
        except NoSuchElementException:
            print u"------------忘记登录密码操作-没有找到操作元素-----------"






