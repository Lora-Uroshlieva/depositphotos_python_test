from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginModule:
    _username_input_selector = "form.login-box input[name='username']"
    _password_input_selector = "form.login-box input[name='password']"
    _confirm_button_selector = "form.login-box button[type='submit']"

    def __init__(self, driver, parent_element):
        self.driver = driver
        self.parent_element = parent_element

    def get_username_input(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self._username_input_selector)))
        return element

    def get_password_input(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self._password_input_selector)))
        return element

    def get_confirm_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self._confirm_button_selector)))
        return element

    def log_in(self):
        self.get_username_input().send_keys('VinsOrder')
        self.get_password_input().send_keys('123456')
        self.get_confirm_button().click()