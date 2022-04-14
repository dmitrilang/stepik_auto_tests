import pytest
import time
import math

@pytest.mark.parametrize('locate', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, locate):
    link = f"https://stepik.org/lesson/{locate}/step/1"
    browser.get(link)
    vr = math.log(int(time.time()))
    browser.implicitly_wait(10)
    browser.find_element_by_class_name("show-plugin").click()
    browser.find_element_by_class_name("quiz-component").click()
    browser.find_element_by_class_name("ember-text-area").click()
    browser.find_element_by_class_name("ember-text-area").send_keys(vr)
    browser.find_element_by_class_name("submit-submission").click()
    a = browser.find_element_by_class_name("smart-hints__hint").text
    assert a == 'Correct!', a


