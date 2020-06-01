# coding=utf-8
__author__ = "jiacai"

import random
import time
from appium import webdriver
from networkPage_test import networkPage
from mainProductPage_test import mainProductPage
from threedPage_test import threedPage

from public_appium import *




if __name__ == '__main__':
    mainApp = 'com.jd.jdmobileske'
    driver = lanchApp(mainApp)

    network = networkPage(driver)
    network.selectedNetworkConfigWithIndex(0)

    # 手动进入商详
    time.sleep(20)
    #
    product = mainProductPage(driver)
    product.pushThreeDViewController()

    time.sleep(5)
    threed = threedPage(driver)
    threed.backToLastView()


    time.sleep(2)
    getDevicePageSource(driver)