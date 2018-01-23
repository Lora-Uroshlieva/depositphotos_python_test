from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.BasePage import BasePage
from src.pages.modules.LoginModule import LoginModule
from src.pages.modules.AuthModule import AuthModule
from src.pages.modules.SearchModule import SearchModule


class HomePage(BasePage):
    _login_module_selector = "div.login-box-wrapper"
    _auth_module_selector = "div.auth-box"
    _search_module_selector = "div.search-bar"
    _sign_in_button_selector = "a.not-auth-box__btn[href*='login']"

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.login_module = LoginModule(self.driver, self._login_module_selector)
        self.auth_module = AuthModule(self.driver, self._auth_module_selector)
        self.search_module = SearchModule(self.driver, self._search_module_selector)

    def open_page(self, relative_url='/'):
        self.driver.get(self.base_url + relative_url)

    def open_login_form(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self._sign_in_button_selector))
        )
        element.click()

