from src.helpers.DriverHolder import DriverHolder


class BasePage:

    def __init__(self):
        self.base_url = 'https://depositphotos.com'
        self.driver = DriverHolder.get_instance().get_driver()

    def open_page(self, relative_url='/'):
        self.driver.get(self.base_url + relative_url)
