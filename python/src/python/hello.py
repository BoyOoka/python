#ecoding:utf-8
'''
Created on 2017年9月9日

@author: gaya
'''
from selenium import webdriver

print "Hello world!"
driver = webdriver.Chrome("/Users/gaya/git/python/python/chromedriver")
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("test")
driver.find_element_by_id("su").click()
driver.quit()
