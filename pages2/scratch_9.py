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
    link = 'http://suninjuly.github.io/wait1.html'
    browser = webdriver.Chrome('/Users/d.lang/chromedriver')
   #browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд
    
    browser.get("http://suninjuly.github.io/wait2.html")
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

    button.click()
    message = browser.find_element_by_id("verify_message")

    # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    assert "successful" in message.text

finally:
    time.sleep(5)
    browser.quit()


