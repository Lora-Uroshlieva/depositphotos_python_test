from src.pages.modules.BaseModule import BaseModule
from src.helpers.element_helper import S


class AuthModule(BaseModule):
    _user_menu_selector = 'div[class="user-box _user-box"]'
    _cart_selector = 'a[class*="user-bar-item shopping-cart-box"]'
    _active_plans_selector = 'a[class*="plans-box _products"]'
    _logout_button_selector = 'a[class="user-menu__logout _user-logout"]'

    def get_user_menu(self):
        element = S(self.driver, self._user_menu_selector)
        return element

    def get_cart(self):
        element = S(self.driver, self._cart_selector)
        return element

    def get_active_plans(self):
        element = S(self.driver, self._active_plans_selector)
        return element

    def open_user_menu(self):
        self.get_user_menu().click()

    def log_out(self):
        self.open_user_menu()
        self.get_logout_button().click()

    def get_logout_button(self):
        element = S(self.driver, self._logout_button_selector)
        return element

