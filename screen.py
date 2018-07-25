import time
from appium import webdriver

def screen_shot(drv, money):
     #scree_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
     filename = 'e:/pythontest/alipay/pic/%s.png' %money
     drv.get_screenshot_as_file(filename)



