# coding=utf-8
__author__ = "jiacai"

from appium import webdriver
import random
import time


class ControlPage():

    def __init__(self, driver):
        self.driver = driver
        self.initViewsData()
        # print('---- actionControl init success ----{}'.format(self.__class__))

    def __del__(self):
        print('---- actionControl destory ----{}'.format(self.__class__))

    def initViewsData(self):
        self.buttonArr = []

    def control_hideKeyboard(self):
        try:
            self.clickButtonWithLabel('完成')  # 收起键盘
        except Exception as e:
            print('failed: 键盘收起失败， 忽略')

    def randomClickButtons(self):
        randomIndex = random.randint(0, len(self.buttonArr)-1)
        self.clickButtonWithIndex(randomIndex)

    def clickButtonWithIndex(self, index):
        label = self.buttonArr[index]
        print("current selected button label = {}, index = {}".format(label, index))
        self.clickButtonWithLabel(label)

    def clickButtonWithLabel(self, label):
        button = self.findClickControlWithText(label)
        button.click()

    def setValueForTextFiledWithRecognizedText(self, recognizedText, setValue):
        """
        根据 输入框 前的标识label， 定位输入框
        :param recognizedText:  输入框 前的标识label
        :return: 输入框
        """
        (
            self.findTextControlWithRecognizedText(recognizedText)
            .send_keys(setValue)
        )


    def setValueForSliderWithRecognizedText(self, recognizedText, setValue):
        (
            self.findSliderControlWithRecognizedText(recognizedText)
            .send_keys(setValue)
         )

    def setValueForSliderWithIndex(self, index, setValue):
        (
            self.findSliderControlWithIndex(index)
            .send_keys(setValue)
        )

    def clickOptionalControlWithRecognizedText(self, recognizedText):
        (
            self.findOptionalControlWithRecognizedText(recognizedText)
            .click()
        )

    def findClickControlWithText(self, text):
        return (self.driver
         .find_element_by_ios_predicate('label CONTAINS "{}" OR name CONTAINS "{}" OR value CONTAINS "{}" '.format(text, text, text))
         )

    def findTextControlWithRecognizedText(self, recognizedText):
        """
        根据 输入框 前的标识label， 定位输入框
        :param recognizedText:  输入框 前的标识label
        :return: 输入框
        """
        return (self.driver
         .find_element_by_xpath('//XCUIElementTypeStaticText[@label="{}"]/..//XCUIElementTypeTextField'.format(recognizedText))
         )

    def findSliderControlWithRecognizedText(self, recognizedText):
        """
        根据 slider 前的标识label， 定位滑动条
        :param recognizedText:  slider 前的标识label
        :return: slider
        """
        return (self.driver
         .find_element_by_xpath('//XCUIElementTypeStaticText[@label="{}"]/following-sibling::*[1]'.format(recognizedText))
         )

    def findSliderControlWithIndex(self, index):
        """
        根据 slider 前的标识label， 定位滑动条
        :param recognizedText:  slider 前的标识label
        :return: slider
        """
        return self.driver.find_element_by_xpath('//XCUIElementTypeCell[{}]/XCUIElementTypeSlider'.format(index))

    def findOptionalControlWithRecognizedText(self, recognizedText):
        """
        根据 optional 前的标识label， 定位选择弹窗按钮
        :param recognizedText: optionalControl 前的标识label
        :return: optionalControl
        """
        return (self.driver
         .find_element_by_xpath('//XCUIElementTypeStaticText[@label="{}"]/following-sibling::*[1]'.format(recognizedText))
         )

class DrawStyleTable:

    def __init__(self, driver):
        self.driver = driver
        self.colorTypeIndex = 1
        print('table init')

    def clickCellDeleteButtonWithIndex(self, index):
        self.findCellDeleteButtonWithIndex(index).click()

    def drawStyleChangeValueWithCellIndex(self, cellIndex, mainMax, subMax):
        self.clickCellOptionalButtonWithIndex(cellIndex)
        time.sleep(1) # 弹框后等待1s
        self.selecteDrawStyleWithColorTypeIndex(mainMax, subMax)

    def selecteDrawStyleWithColorTypeIndex(self, mainMax, subMax):
        try:
            firstVale = random.randint(1, mainMax) if self.colorTypeIndex == 1 else self.colorTypeIndex
            randomStyle = '{:0>2d}_{:0>2d}'.format(firstVale, random.randint(1, subMax))
            print('画法类型选中： ' + randomStyle)
            self.clickButtonWithLabel(randomStyle)
        except Exception as e:
            print(e)
            # 选择失败， 重新选择
            time.sleep(1)
            self.selecteDrawStyleWithColorTypeIndex(mainMax, subMax)

    def clickCellOptionalButtonWithIndex(self, index):
        self.findCellOptionalButtonWithIndex(index).click()

    def findCellOptionalButtonWithIndex(self, index):
        """
        查找 画法cell的 选项按钮
        :param index: cell的index
        :return: 选线按钮
        """
        return (self.driver.find_element_by_xpath('//XCUIElementTypeButton[@label="+ 添加一组画法"]/../XCUIElementTypeTable/XCUIElementTypeCell[{}]/XCUIElementTypeButton[1]'.format(index)))

    def findCellDeleteButtonWithIndex(self, index):
        """
        查找 画法cell的 删除按钮
        :param index: cell的index
        :return: 删除按钮
        """
        return (self.driver.find_element_by_xpath('//XCUIElementTypeButton[@label="+ 添加一组画法"]/../XCUIElementTypeTable/XCUIElementTypeCell[{}]/XCUIElementTypeButton[2]'.format(index)))





