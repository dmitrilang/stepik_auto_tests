from pages.login_page import LoginPage
from pages.locators import LoginPageLocators

def test_url_check_login_page(browser):
    link = LoginPageLocators.LOGIN_URL
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_url()       # выполняем метод страницы

def test_check_login_form(browser):
    link = LoginPageLocators.LOGIN_URL
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_form()       # выполняем метод страницы

def test_check_be_register_form(browser):
    link = LoginPageLocators.LOGIN_URL
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_register_form()       # выполняем метод страницы
