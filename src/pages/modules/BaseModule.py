from src.helpers.element_helper import S
from src.helpers.DriverHolder import DriverHolder


class BaseModule:

    def __init__(self, parent_selector):
        self.driver = DriverHolder.get_instance().get_driver()
        self.parent_element = parent_selector

    def get_wrapper(self):
        return S(self.parent_element)
