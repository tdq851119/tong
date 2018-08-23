# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
import time
class Other():
    def __init__(self,driver):
        self.driver = driver

    '''活动弹窗处理'''
    def Activewindow(self):
        # time.sleep(5)
        try:
            if self.driver.find_element_by_id("iv_ad_photo"):
                # time.sleep(2)
                self.driver.find_element_by_id("iv_delete").click()
            else:
                pass
        except NoSuchElementException:
            pass

    '''升级弹窗处理-没做完'''
    def UpgradeWindow(self,driver):
        # time.sleep(5)
        if self.driver.find_element_by_id("iv_ad_photo"):
            # time.sleep(2)
            self.driver.find_element_by_id("iv_delete").click()
        else:
            pass
