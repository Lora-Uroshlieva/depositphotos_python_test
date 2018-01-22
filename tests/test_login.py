import unittest
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from src.pages.HomePage import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.HomePage = HomePage(cls.driver)

    def setUp(self):
        self.HomePage.open_page()

    def tearDown(self):
        self.driver.close()

    def test_login_valid(self):
        self.HomePage.open_page()
        self.driver.maximize_window()
        self.HomePage.open_login_form()
        self.HomePage.login_module.log_in()
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://depositphotos.com/home.html'))
        self.assertEqual("https://depositphotos.com/home.html", self.driver.current_url)


if __name__ == "__main__":
    unittest.main()
