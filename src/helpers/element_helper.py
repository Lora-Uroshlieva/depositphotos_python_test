import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.helpers.DriverHolder import DriverHolder


def S(css_selector):
    """
    :param driver:
    :param css_selector:
    :return: element or Exception if element not found
    """
    try:
        element = WebDriverWait(DriverHolder.get_instance().get_driver(), 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        element.S = S
        return element
    except Exception:
        # print("element with locator %s was not found") !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print(sys.exc_info())
