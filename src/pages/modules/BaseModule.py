from src.helpers.element_helper import S


class BaseModule:

    def __init__(self, driver, parent_element):
        self.driver = driver
        self.parent_element = parent_element

    def get_wrapper(self):
        return S(self.driver, self.parent_element)
