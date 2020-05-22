# coding=utf-8
__author__ = "jiacai"

from categoryPage_test import CategoryPage
from controlPage_test import DrawStyleTable
from appium import webdriver
import random
import time
from constValue import *
import public

class Eyeshadow(CategoryPage, DrawStyleTable):

    def __init__(self, driver):
        DrawStyleTable.__init__(self, driver)
        CategoryPage.__init__(self, driver)

    def initViewsData(self):
        super().initViewsData()
        self.colorTypeIndex = 2;
        lipArr = ['确定', '取消', '下一步', '眼影类型:', '添加一组画法', '删除']
        self.textArr = ['SKU:', '色号:', '1', '2', '3', '4', '5']
        self.colorType = ['单色', '双色', '三色', '四色', '五色']
        self.buttonArr = self.buttonArr + lipArr

    def clickShadowColorTypeWithIndex(self, index):
        if index > (len(self.colorType) - 1):
            return
        self.clickShadowColorTypeWithLabel(self.colorType[index])

    def clickShadowColorTypeWithLabel(self, label):
        self.findClickControlWithText(label).click()

    def normalTest(self):
        try:
            self.clickButtonWithLabel('新建')
            # category.clickButtonWithIndex(0)
            self.setValueForTextFiledWithRecognizedText('SKU:', skuID)
            self.clickButtonWithLabel('确定')
            time.sleep(3)
            self.clickOptionalControlWithRecognizedText('眼影类型:')
            time.sleep(1)
            self.clickShadowColorTypeWithIndex(self.colorTypeIndex-1) # 索引从0开始
        except Exception as e:
            print('failed: 填写数据失败')
            print(e)

        try:
            time.sleep(2)
            self.setValueForTextFiledWithRecognizedText('1', public.randomColor())
            self.setValueForTextFiledWithRecognizedText('2', public.randomColor())
        except Exception as e:
            print('failed: 多色数据失败')
            print(e)

        try:
            self.clickButtonWithLabel('添加一组画法')
            self.clickButtonWithLabel('添加一组画法')
            self.clickButtonWithLabel('添加一组画法')
            time.sleep(2)
        except Exception as e:
            print('failed: 添加画法失败')
            print(e)

        try:
            self.drawStyleChangeValueWithCellIndex(1, self.colorTypeIndex, 10)
            self.drawStyleChangeValueWithCellIndex(2, self.colorTypeIndex, 10)
            self.drawStyleChangeValueWithCellIndex(3, self.colorTypeIndex, 10)
            self.clickCellDeleteButtonWithIndex(2)  # 删除中间添加的
        except Exception as e:
            print('failed: 画法选择失败失败')
            print(e)

        try:
            self.control_hideKeyboard()
            self.clickButtonWithLabel('下一步')
            self.setValueForSliderWithIndex(1, '0.66')
            self.setValueForSliderWithIndex(2, '0.88')
            self.clickButtonWithLabel('确认')
        except Exception as e:
            print('failed: 透明度设置失败')
            print(e)

        try:
            self.clickButtonWithIndex(0)
        except Exception as e:
            print('failed: 返回主界面失败')
            print(e)