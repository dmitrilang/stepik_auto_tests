from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome('/Users/d.lang/chromedriver')
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element(By.ID, "book")
    book.click()

    x_element = browser.find_element_by_css_selector('#input_value')
    valuexatr = x_element.text
    x = int(valuexatr)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)

    btn2 = browser.find_element(By.ID, "solve")
    btn2.click()

finally:
    time.sleep(20)
    browser.quit()

