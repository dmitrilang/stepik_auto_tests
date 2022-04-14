import unittest
import time
from selenium import webdriver


class TestAbs(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        #link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome('/Users/d.lang/chromedriver')
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_tag_name("input[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_tag_name("input[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_tag_name("input[placeholder='Input your email']")
        input3.send_keys("@mail")
        input4 = browser.find_element_by_tag_name("input[placeholder='Input your phone:']")
        input4.send_keys("899999")
        input5 = browser.find_element_by_tag_name("input[placeholder='Input your address:']")
        input5.send_keys("Msc")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test1fail")
        #assert "Congratulations! You have successfully registered!" == welcome_text

    def test_registration2(self):
        #link = "http://suninjuly.github.io/registration1.html"
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome('/Users/d.lang/chromedriver')
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_tag_name("input[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_tag_name("input[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_tag_name("input[placeholder='Input your email']")
        input3.send_keys("@mail")
        input4 = browser.find_element_by_tag_name("input[placeholder='Input your phone:']")
        input4.send_keys("899999")
        input5 = browser.find_element_by_tag_name("input[placeholder='Input your address:']")
        input5.send_keys("Msc")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test2fail")


if __name__ == "__main__":
    unittest.main()

