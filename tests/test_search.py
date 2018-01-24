import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.helpers.element_helper import S
from src.pages.HomePage import HomePage


class SearchTest(unittest.TestCase):

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

    def test_search_by_keyword(self):
        self.HomePage.search_module.search_by_word('texture')
        images = self.HomePage.search_module.get_images_after_search()
        self.assertGreater(len(images), 0)
        # print(len(images))


if __name__ == "__main__":
    unittest.main()
