import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.helpers.element_helper import S
from src.pages.HomePage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.HomePage = HomePage(cls.driver)
        cls.HomePage.open_page()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_valid(self):
        self.HomePage.open_login_form()
        self.HomePage.login_module.log_in('VinsOrder', '123456')
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://depositphotos.com/home.html'))
        self.assertEqual("https://depositphotos.com/home.html", self.driver.current_url)
        self.assertIn('VinsOrder', self.driver.page_source)

    def test_login_invalid_username(self):
        self.HomePage.open_login_form()
        self.HomePage.login_module.log_in('VinsOrder123', '123456')
        warning_text = S(self.driver, 'span.field-box__error').text
        self.assertIn('This login does not exist. Please try again.', warning_text)

    def test_login_invalid_password(self):
        self.HomePage.open_login_form()
        self.HomePage.login_module.log_in('VinsOrder', '1111')
        warning_text = S(self.driver, 'span.field-box__error').text
        self.assertIn('Incorrect password', warning_text)


if __name__ == "__main__":
    unittest.main()
