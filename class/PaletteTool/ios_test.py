# python脚本语言要注意每行缩进，这是python语法特性

import time
from public_appium import *
from appium import webdriver
from controlPage_test import ControlPage
from homePage_test import HomePage
from categoryPage_test import CategoryPage
from test_lip import Lip
from test_blush import Blush
from test_eyebrow import Eyebrow
from test_eyeshadow import Eyeshadow
from test_eyeliner import Eyeliner
from test_eyelash import Eyelash
from test_foundation import Foundation

def normalTestForSevenCategory(home):
    # homePage 相关操作
    # page.randomClickButtons()
    # page.clickButtonWithLabel('口红')
    # home.clickButtonWithIndex(0)

    ### 口红测试
    home.clickButtonWithIndex(0)
    lip = Lip(driver)
    lip.normalTest()

    ### 腮红测试
    home.clickButtonWithIndex(1)
    blush = Blush(driver)
    blush.normalTest()

    ### 眉笔测试
    home.clickButtonWithIndex(2)
    eyebrow = Eyebrow(driver)
    eyebrow.normalTest()

    ### 底妆测试
    home.clickButtonWithIndex(6)
    foundation = Foundation(driver)
    foundation.normalTest()

    ### 眼影测试
    home.clickButtonWithIndex(3)
    eyeshadow = Eyeshadow(driver)
    eyeshadow.normalTest()

    ### 眼线测试
    home.clickButtonWithIndex(4)
    eyeliner = Eyeliner(driver)
    eyeliner.normalTest()

    ### 睫毛膏测试
    home.clickButtonWithIndex(5)
    eyelash = Eyelash(driver)
    eyelash.normalTest()

if __name__ == '__main__':
    mainApp = 'com.jd.ar.thailand'
    driver = lanchApp(mainApp)

    home = HomePage(driver)
    # getDevicePageSource(driver)
    # home.clickButtonWithLabel('媒体中心')
    # getDevicePageSource(driver)
    # time.sleep(3)
    # getDevicePageSource(driver)

    # ### 眼影测试
    # home.clickButtonWithIndex(3)
    # eyeshadow = Eyeshadow(driver)
    # eyeshadow.normalTest()

    for times in range(5):
        normalTestForSevenCategory(home)
        changeToOtherAppAndBack(driver, mainApp, 'com.apple.compass')


    time.sleep(3)
    getDevicePageSource(driver)


