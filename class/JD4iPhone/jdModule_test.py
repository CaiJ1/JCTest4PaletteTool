# coding=utf-8
__author__ = "jiacai"

import random
import time
from appium import webdriver
from networkPage_test import networkPage

from public_appium import *




if __name__ == '__main__':
    mainApp = 'com.jd.jdmobileske'
    driver = lanchApp(mainApp)

    network = networkPage(driver)
    network.selectedNetworkConfigWithIndex(0)



    time.sleep(20)
    getDevicePageSource(driver)