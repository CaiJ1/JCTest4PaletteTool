# coding=utf-8
__author__ = "jiacai"

from categoryPage_test import CategoryPage
from controlPage_test import DrawStyleTable
from appium import webdriver
import random
import time
from constValue import *

class Eyelash(CategoryPage, DrawStyleTable):

    def __init__(self, driver):
        CategoryPage.__init__(self, driver)
        DrawStyleTable.__init__(self, driver)

    def initViewsData(self):
        super().initViewsData()
        lipArr = ['确定', '取消', '下一步']
        self.textArr = ['SKU:', '色号:', 'RGB值:']
        self.buttonArr = self.buttonArr + lipArr

    def normalTest(self):
        try:
            self.clickButtonWithLabel('新建')
            # category.clickButtonWithIndex(0)
            self.setValueForTextFiledWithRecognizedText('SKU:', skuID)
            self.clickButtonWithLabel('确定')
            time.sleep(3)
            self.setValueForTextFiledWithRecognizedText('RGB值:', public.randomColor())
        except Exception as e:
            print('failed: 填写数据失败')
            print(e)

        try:
            self.clickButtonWithLabel('添加一组画法')
            self.clickButtonWithLabel('添加一组画法')
            self.clickButtonWithLabel('添加一组画法')
        except Exception as e:
            print('failed: 添加画法失败')
            print(e)

        try:
            self.drawStyleChangeValueWithCellIndex(1, 3, 10)
            self.drawStyleChangeValueWithCellIndex(2, 3, 10)
            self.drawStyleChangeValueWithCellIndex(3, 3, 10)
            self.clickCellDeleteButtonWithIndex(2)  # 删除中间添加的
        except Exception as e:
            print('failed: 画法选择失败失败')
            print(e)

        try:
            self.control_hideKeyboard()
            self.clickButtonWithLabel('下一步')
            self.setValueForSliderWithIndex(1, '0.66')
            self.clickButtonWithLabel('确认')
        except Exception as e:
            print('failed: 透明度设置失败')
            print(e)

        try:
            self.clickButtonWithIndex(0)
        except Exception as e:
            print('failed: 返回主界面失败')
            print(e)