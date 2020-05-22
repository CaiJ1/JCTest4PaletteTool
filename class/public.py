# coding=utf-8
__author__ = "jiacai"

from appium import webdriver
import random

def randomColorInt():
    return random.randint(0, 15)

def randomColor():
    """
    返回 16进制 色值
    :return: 16进制色值 例：ff5500
    """
    color = ''
    for i in range(6):
        color = color + '{:x}'.format(randomColorInt())
    print(color)
    return color


