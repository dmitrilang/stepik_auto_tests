from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
import os

try:
    link = 'http://suninjuly.github.io/wait1.html'
    browser = webdriver.Chrome('/Users/d.lang/chromedriver')
    browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.get(link)
    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    time.sleep(5)
    browser.quit()


