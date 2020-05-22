# python脚本语言要注意每行缩进，这是python语法特性

import time
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

def lanchApp(bundleID, appPath='', orgID=''):
    desired_caps = {'platformName': 'ios',
                    'deviceName': 'JiaC',
                    'platformVersion': '13.2.3',
                    'udid': '00008030-001555DE1A98802E',
                    'noReset': True,
                    'resetKeyboard': True,
                    'automationName': 'XCUITest',

                    'app': appPath, #'/Users/jiacai/Desktop/GJDMALL-V2.16.0-100.9354-202004261227-RELEASE-2.16.0.ipa',
                    'bundleId': bundleID, # 'com.jd.ar.thailand',
                    'xcodeOrgId': orgID, #'arvr-app@jd.com',
                    }
    # desired_caps = {'platformName': 'ios',
    #                 'deviceName': 'iPhone_bao',
    #                 'platformVersion': '12.4',
    #                 'udid': 'c08186bc599e2fcfcaba7091f48c7c06aea7c855',
    #                 'noReset': True,
    #                 'resetKeyboard': True,
    #                 'automationName': 'XCUITest',
    #
    #                 'app': appPath,  # '/Users/jiacai/Desktop/GJDMALL-V2.16.0-100.9354-202004261227-RELEASE-2.16.0.ipa',
    #                 'bundleId': bundleID,  # 'com.jd.ar.thailand',
    #                 'xcodeOrgId': orgID,  # 'arvr-app@jd.com',
    #                 }

    print('---------开始测试-------------------------')

    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                              desired_capabilities=desired_caps)
    return driver

def getDevicePageSource(driver):
    """获取当前页面信息"""
    driver_page = driver.page_source
    print(driver_page)

def getDeviceSize(driver):
    """获取设备逻辑分辨率"""
    size = driver.get_window_size()
    print(size)

def changeToOtherAppAndBack(mainStr, otherStr='com.apple.springboard'):
    """
    切换其他app 3秒后返回
    :param mainStr:  当前应用identity
    :param otherStr: 跳转应用的identity， 默认桌面APP
    :return: 无返回值
    """
    driver.activate_app(otherStr)
    time.sleep(3)
    print(driver.query_app_state(mainStr))
    driver.activate_app(mainStr)


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
        changeToOtherAppAndBack(mainApp, 'com.apple.compass')


    time.sleep(3)
    getDevicePageSource(driver)


