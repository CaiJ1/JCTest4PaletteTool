# coding=utf-8
__author__ = "jiacai"

from categoryPage_test import CategoryPage
from appium import webdriver
import random
import time
from constValue import *

class Foundation(CategoryPage):

    def initViewsData(self):
        super().initViewsData()
        lipArr = ['确定', '取消', '下一步']
        self.textArr = ['SKU:', '色号:', 'RGB:']
        self.typeOptionArr = ['哑光', '丝绒', '高光', '闪光', '瑞泽', '金属']
        self.buttonArr = self.buttonArr + lipArr

    def normalTest(self):
        try:
            self.clickButtonWithLabel('新建')
            # category.clickButtonWithIndex(0)
            self.setValueForTextFiledWithRecognizedText('SKU:', skuID)
            self.clickButtonWithLabel('确定')
            time.sleep(3)
            self.setValueForTextFiledWithRecognizedText('RGB:', public.randomColor())
        except Exception as e:
            print('failed: 填写数据失败')
            print(e)

        try:
            self.control_hideKeyboard()
            self.clickButtonWithLabel('下一步')
            self.setValueForSliderWithRecognizedText('不透明度', '0.98')
            self.clickButtonWithLabel('确认')
        except Exception as e:
            print('failed: 透明度设置失败')
            print(e)

        try:
            self.clickButtonWithIndex(0)
        except Exception as e:
            print('failed: 返回主界面失败')
            print(e)