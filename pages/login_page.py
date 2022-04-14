from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        url = self.browser.current_url
        assert self.browser.current_url == LoginPageLocators.LOGIN_URL, "URL not corrected"
        # реализуйте проверку на корректный url адрес
        assert True
        print(LoginPageLocators.LOGIN_URL, "LOGIN_URL")
        print(url, "LOGIN_URL_CURRENT")


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Not present login form"
        assert True
        print("Login form OK")
        # реализуйте проверку, что есть форма логина


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Not present register form"
        # реализуйте проверку, что есть форма регистрации на странице
        assert True
        print("Register form OK")


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
