# coding=utf-8
__author__ = "jiacai"

from appium import webdriver
import random
from public_appium import *

class threedPage():
    def __init__(self, driver):
        self.driver = driver

    def backToLastView(self):
        backBtn = findUniqueViewWithVisibleText(self.driver, "threed titlebar back")
        backBtn.click()



