# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.baidu.com/')