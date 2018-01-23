import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def S(driver, input_selector):
    """
    :param driver:
    :param input_selector:
    :return: element or Exception if element not found
    """
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, input_selector)))
        return element
    except Exception:
        # print("element with locator %s was not found") !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print(sys.exc_info())
