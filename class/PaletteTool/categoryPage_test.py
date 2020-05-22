# coding=utf-8
__author__ = "jiacai"

from controlPage_test import ControlPage
from appium import webdriver
import random

class CategoryPage(ControlPage):

    def initViewsData(self):
        """统计 页面控件"""
        super().initViewsData()
        self.buttonArr = self.buttonArr + ['avr maketuptool backIcon', '导出', 'avr maketuptool deleteIcon', 'avr maketuptool helpIcon', '新建', '编辑']
        print(self.buttonArr)




