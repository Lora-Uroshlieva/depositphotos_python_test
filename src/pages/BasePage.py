class BasePage:

    def __init__(self, driver):
        self.base_url = 'https://depositphotos.com'
        self.driver = driver

    def open_page(self, relative_url='/'):
        self.driver.get(self.base_url + relative_url)
