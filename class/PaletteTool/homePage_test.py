# coding=utf-8
__author__ = "jiacai"

from appium import webdriver
from controlPage_test import ControlPage
import random

class HomePage(ControlPage):

    # def __init__(self, driver):
    #     # actionControl.__init__(driver)
    #     self.driver = driver
    #     self.initViewsData()
    #     print('---- homePage init success ----')

    def initViewsData(self):
        """统计 页面控件"""
        super().initViewsData()
        categoryArr = ['口红', '腮红', '眉笔', '眼影', '眼线', '睫毛膏', '底妆']
        otherArr = ['技术支持']
        self.buttonArr = self.buttonArr + categoryArr + otherArr
        print(self.buttonArr)


