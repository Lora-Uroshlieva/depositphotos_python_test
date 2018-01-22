import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        driver.maximize_window()
        driver.add_cookie({"name": '111', "value": '222'})
        print(driver.get_cookies())
        driver.find_element_by_tag_name('div')
    #
    # def tearDown(self):
    #     # self.driver.close()
    #      pass


if __name__ == "__main__":
    unittest.main()