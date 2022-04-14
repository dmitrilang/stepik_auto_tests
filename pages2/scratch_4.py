from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome('/Users/d.lang/chromedriver')
    browser.get(link)

    browser.execute_script("window.scrollBy(0, 140);")
    elem = browser.find_element_by_css_selector('#input_value')
    x = elem.text
    print(x)
    xint = int(x)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    print(y)
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)
    robot = browser.find_element_by_css_selector('#robotCheckbox')
    robot.click()
    robotrule = browser.find_element_by_css_selector('#robotsRule')
    robotrule.click()
    btn = browser.find_element_by_tag_name('button')
    btn.click()


finally:
    time.sleep(3)
    browser.quit()

