from selenium import webdriver
import math
import time
try:
    #link = 'http://suninjuly.github.io/math.html'
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome('/Users/d.lang/chromedriver')
    browser.get(link)
    x_element = browser.find_element_by_css_selector('#treasure')
    valuexatr = x_element.get_attribute('valuex')
    x = valuexatr
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)
    robot = browser.find_element_by_css_selector('#robotCheckbox')
    robot.click()
    robotrule = browser.find_element_by_css_selector('#robotsRule')
    robotrule.click()
    btn = browser.find_element_by_tag_name('button')
    btn.click()
finally:
    time.sleep(10)
    browser.quit()

