# coding:utf-8
from selenium import webdriver
from time import sleep

import uiautomator2 as u2

# webdriver connection
options = webdriver.ChromeOptions()
options.binary_location = 'C:/Users/xxzhen/AppData/Local/Programs/bncTuningTool/bncTuningTool.exe'
dr = webdriver.Chrome('C:/Users/xxzhen/python3.10/Scripts/chromedriver.exe',
                      options=options)

def connect_phone():
    d = u2.connect()
    d(description="浏览器支持服务卡片,应用在托盘上").click()
    d(resourceId="com.huawei.browser:id/search_icon").click()
    d(resourceId="com.huawei.browser:id/url_bar").click()
    d.send_keys("www.baidu.com", clear=True)
    d(resourceId="com.huawei.browser:id/search_action").click()

    sleep(3)



