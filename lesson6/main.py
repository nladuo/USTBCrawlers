#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

exe_path = "/Users/kalen/Programfiles/phantomjs-2.1.1-macosx/bin/phantomjs"
driver = webdriver.PhantomJS(executable_path=exe_path)

driver.get("http://vps.kalen25115.cn:3000/")

time.sleep(1)
print driver.page_source

driver.quit()





