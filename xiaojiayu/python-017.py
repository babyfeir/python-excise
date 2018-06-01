# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__ = "飞飞"

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(20)

mouse = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text('搜索设置').click()
sleep(5)

driver.find_element_by_xpath('//td[@id="se-setting-3"]/select/option[3]').click()
'''
s = driver.find_element_by_id('nr')
s.find_element_by_xpath('//option[@value="50"]').click()
'''
sleep(5)

driver.quit()

