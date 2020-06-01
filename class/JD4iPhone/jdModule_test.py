# coding=utf-8
__author__ = "jiacai"

import random
import time
from appium import webdriver

from public_appium import *


if __name__ == '__main__':
    mainApp = 'com.jd.jdmobileske'
    driver = lanchApp(mainApp)


    time.sleep(3)
    getDevicePageSource(driver)