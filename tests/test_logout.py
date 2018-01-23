import unittest
from selenium import webdriver
from src.pages.HomePage import HomePage
from src.helpers.element_helper import S


class LogOut(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.HomePage = HomePage(cls.driver)

    def setUp(self):
        self.HomePage.open_page()
        self.driver.maximize_window()
        self.HomePage.open_login_form()
        self.HomePage.login_module.log_in('VinsOrder', '123456')

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.close()

    def test_logout(self):
        self.HomePage.auth_module.log_out()
        self.assertEqual("https://depositphotos.com/home.html", self.driver.current_url)
        sign_in_button_text = S(self.driver, 'a._btn-sign-in').text
        self.assertEqual('Sign In', sign_in_button_text)
        self.assertNotIn('VinsOrder', self.driver.page_source)


if __name__ == "__main__":
    unittest.main()
