# coding=utf-8
__author__ = "jiacai"

from appium import webdriver
import time

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

def changeToOtherAppAndBack(driver, mainStr, otherStr='com.apple.springboard'):
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


### 定位元素方法
    def findUniqueViewWithVisibleText(driver, text):
        """
        根据可视的标签文字， 定位唯一View
        :param driver: webdriver
        :param text: 可视文字（可以是其中一部分）
        :return: 查找到的View
        """
        return driver.find_element_by_ios_predicate('label CONTAINS "{}" OR name CONTAINS "{}" OR value CONTAINS "{}" '.format(text, text, text))

    def findUniqueTextFieldWithFrontLabelText(driver, FrontLabelText):
        """
       根据输入框 前的标识label， 定位输入框 （label、textField需要同级别， 且无其它textField）
       :param driver: webdriver
       :param FrontLabelText: 输入框 前面的标识label
       :return: 查找到的 textField
       """
        return driver.find_element_by_xpath('//XCUIElementTypeStaticText[@label="{}"]/..//XCUIElementTypeTextField'.format(FrontLabelText))


