from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome('/Users/d.lang/chromedriver')
    #driver = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("@mail")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file1.txt')
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)
    #element.send_keys("/Users/d.lang/Library/Application Support/JetBrains/PyCharmCE2021.3/scratches/file.txt")
    btn = browser.find_element_by_css_selector('button')
    btn.click()

finally:
    time.sleep(4)
    browser.quit()

