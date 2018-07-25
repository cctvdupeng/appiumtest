#coding=utf-8
from appium import webdriver
import time
import screen
import numpy as np


start = time.time()

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'NCE-TL10'
desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
desired_caps['noReset'] = True
#desired_caps['autoLaunch'] = 'false'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print('正在打开APP...')

print('收钱')
#driver.implicitly_wait(10)

try:   
     driver.find_element_by_id('com.alipay.android.phone.openplatform:id/collect_layout').click()
     for i in np.arange(4.5, 4.6, 0.01):
          driver.find_element_by_name('设置金额').click()
          driver.find_element_by_id('com.alipay.mobile.ui:id/content').send_keys(str(i))
          driver.find_element_by_name('确定').click()
          driver.implicitly_wait(3)
          payee_ = driver.find_element_by_id('com.alipay.mobile.payee:id/payee_QRCodeImageView')
          screen.screen_shot(driver, i)
          driver.find_element_by_name('清除金额').click()
          
except Exception as err:
     print(err)
     
end = time.time()
print('运行时间：' + str(end-start) + 'S')







