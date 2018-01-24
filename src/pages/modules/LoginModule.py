from src.pages.modules.BaseModule import BaseModule
from src.helpers.element_helper import S


class LoginModule(BaseModule):

    _username_input_selector = "input[name='username']"
    _password_input_selector = "input[name='password']"
    _confirm_button_selector = "button[type='submit']"
    _incorrect_data_warn_selector = 'span[class="field-box__error"]'

    def get_username_input(self):
        element = self.get_wrapper().S(self._username_input_selector)
        return element

    def get_password_input(self):
        element = self.get_wrapper().S(self._password_input_selector)
        return element

    def get_confirm_button(self):
        element = self.get_wrapper().S(self._confirm_button_selector)
        return element

    def log_in(self, username, password):
        self.get_username_input().send_keys(username)
        self.get_password_input().send_keys(password)
        self.get_confirm_button().click()

    def get_warn_incorrect_data(self):
        element = S(self._incorrect_data_warn_selector)
        return element

