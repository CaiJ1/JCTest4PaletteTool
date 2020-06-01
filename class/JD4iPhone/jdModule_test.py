# coding=utf-8
__author__ = "jiacai"

import random
import time
from appium import webdriver

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


if __name__ == '__main__':
