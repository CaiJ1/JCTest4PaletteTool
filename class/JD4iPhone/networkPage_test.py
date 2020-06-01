# coding=utf-8
__author__ = "jiacai"

from appium import webdriver
import random

class networkPage():
    def __init__(self, driver):
        self.driver = driver
        self.cellLabel = ["正式环境", "预发布环境", "自定义环境"]

    def selectedNetworkConfigWithIndex(self, selectedIndex):
        (self.driver
                .find_element_by_xpath(
            '//XCUIElementTypeStaticText[@label="{}"]/../following-sibling::*[1]'.format(self.cellLabel[selectedIndex]))
            .click()
                )



