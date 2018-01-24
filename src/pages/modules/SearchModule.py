from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.modules.BaseModule import BaseModule
from src.helpers.element_helper import S


class SearchModule(BaseModule):
    _input_selector = 'input[name="query"]'
    _reset_button_selector = 'a.button-reset'
    _search_by_img_selector = 'i.icon-search-by-image'
    _search_by_type_selector = 'span.search-bar-type-indicator__title'
    _submit_button_selector = 'button.search-bar__button-submit.button-search-large'

    def get_input_field(self):
        element = S(self._input_selector)
        return element

    def get_reset_button(self):
        element = S(self._reset_button_selector)
        return element

    def get_search_by_img(self):
        element = S(self._search_by_img_selector)
        return element

    def get_search_by_type(self):
        element = S(self._search_by_type_selector)
        return element

    def get_submit_button(self):
        element = S(self._submit_button_selector)
        return element

    def search_by_word(self, word):
        self.get_input_field().send_keys(word)
        self.get_submit_button().click()

    def get_images_after_search(self):
        images = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.search-box__result img')))
        return images

