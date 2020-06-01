# coding=utf-8
__author__ = "jiacai"

from appium import webdriver
import random
from public_appium import *

class mainProductPage():
    def __init__(self, driver):
        self.driver = driver

    def pushThreeDViewController(self):
        (
            self.driver
                .find_element_by_xpath('//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeCollectionView/following-sibling::*[1]/XCUIElementTypeButton[1]')
                .click()
        )





