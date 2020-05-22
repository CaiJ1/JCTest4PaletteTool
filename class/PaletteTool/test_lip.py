# coding=utf-8
__author__ = "jiacai"

from categoryPage_test import CategoryPage
from appium import webdriver
import random
import time
from constValue import *

class Lip(CategoryPage):

    def initViewsData(self):
        super().initViewsData()
        lipArr = ['确定', '取消', '下一步', 'avr makeup downArrow']
        self.textArr = ['SKU:', '色号:', 'RGB:']
        self.typeOptionArr = ['哑光', '丝绒', '高光', '闪光', '瑞泽', '金属']
        self.buttonArr = self.buttonArr + lipArr

    def clickLipTypeWithIndex(self, index):
        if index > (len(self.typeOptionArr) - 1):
            return
        self.clickLipTypeWithLabel(self.typeOptionArr[index])

    def clickLipTypeWithLabel(self, label):
        self.findClickControlWithText(label).click()

    def normalTest(self):
        try:
            self.clickButtonWithLabel('新建')
            # category.clickButtonWithIndex(0)
            self.setValueForTextFiledWithRecognizedText('SKU:', skuID)
            self.clickButtonWithLabel('确定')
            time.sleep(4)
            self.setValueForTextFiledWithRecognizedText('RGB:', public.randomColor())
        except Exception as e:
            print('failed: 填写数据失败')
            print(e)

        try:
            self.clickOptionalControlWithRecognizedText('质地:')
            time.sleep(2)
            self.clickLipTypeWithIndex(2)
        except Exception as e:
            print('failed: 口红质地选择')
            print(e)

        try:
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
