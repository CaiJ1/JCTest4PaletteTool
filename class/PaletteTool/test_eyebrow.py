# coding=utf-8
__author__ = "jiacai"

from categoryPage_test import CategoryPage
from appium import webdriver
import random
import time
from constValue import *

class Eyebrow(CategoryPage):

    def initViewsData(self):
        super().initViewsData()
        lipArr = ['确定', '取消', '下一步', '新增一个RGB']
        self.textArr = ['SKU:', '色号:', 'RGB1:', 'RGB2:']
        self.buttonArr = self.buttonArr + lipArr

    def normalTest(self):
        try:
            self.clickButtonWithLabel('新建')
            # category.clickButtonWithIndex(0)
            self.setValueForTextFiledWithRecognizedText('SKU:', skuID)
            self.clickButtonWithLabel('确定')
            time.sleep(3)
            self.setValueForTextFiledWithRecognizedText('RGB1:', colorStr)
        except Exception as e:
            print('failed: 填写数据失败')
            print(e)

        try:
            self.clickButtonWithLabel('新增一个RGB')
            time.sleep(3)
            self.setValueForTextFiledWithRecognizedText('RGB2:', colorStr2)
        except Exception as e:
            print('failed: 输入第二个RGB')
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