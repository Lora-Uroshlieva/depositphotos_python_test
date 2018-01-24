import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.helpers.element_helper import S
from src.helpers.DriverHolder import DriverHolder
from src.pages.HomePage import HomePage
from user import User
User = User()


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome()
        DriverHolder(webdriver.Chrome())
        cls.driver = DriverHolder.get_instance().get_driver()
        # cls.HomePage = HomePage(cls.driver)
        cls.HomePage = HomePage()
        cls.HomePage.open_page()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        DriverHolder.get_instance().get_driver().quit()

    def test_login_valid(self):
        self.HomePage.open_login_form()
        self.HomePage.login_module.log_in(User.name, User.password)
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://depositphotos.com/home.html'))
        self.assertEqual("https://depositphotos.com/home.html", self.driver.current_url)
        self.assertIn('VinsOrder', self.driver.page_source)

    def test_login_invalid_username(self):
        self.HomePage.open_login_form()
        self.HomePage.login_module.log_in('SomeUser123', User.password)
        warning_text = S('span.field-box__error').text
        self.assertIn('This login does not exist. Please try again.', warning_text)

    def test_login_invalid_password(self):
        self.HomePage.open_login_form()
        self.HomePage.login_module.log_in(User.name, '1111')
        warning_text = S('span.field-box__error').text
        self.assertIn('Incorrect password', warning_text)


if __name__ == "__main__":
    unittest.main()
