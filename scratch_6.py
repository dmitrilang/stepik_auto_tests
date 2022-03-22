from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
import os

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome('/Users/d.lang/chromedriver')
    #driver = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element_by_css_selector('button')
    btn.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_css_selector('#input_value')
    valuexatr = x_element.text
    x = int(valuexatr)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)
    btn2 = browser.find_element_by_class_name('btn-primary')
    btn2.click()
finally:
    time.sleep(5)
    browser.quit()

