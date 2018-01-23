from src.pages.modules.BaseModule import BaseModule
from src.helpers.element_helper import S


class SearchModule(BaseModule):
    _input_selector = 'input[name="query"]'
    _reset_button_selector = 'a.button-reset'
    _search_by_img_selector = 'i.icon-search-by-image'
    _search_by_type_selector = 'span.search-bar-type-indicator__title'
    _submit_button_selector = 'button.search-bar__button-submit.button-search-large'

    def get_input_field(self):
        element = S(self.driver, self._input_selector)
        return element

    def get_reset_button(self):
        element = S(self.driver, self._reset_button_selector)
        return element

    def get_search_by_imb(self):
        element = S(self.driver, self._search_by_img_selector)
        return element

    def get_search_by_type(self):
        element = S(self.driver, self._search_by_type_selector)
        return element

    def get_submit_button(self):
        element = S(self.driver, self._submit_button_selector)
        return element

