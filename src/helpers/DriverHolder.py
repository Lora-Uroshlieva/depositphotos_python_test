class DriverHolder:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if DriverHolder.__instance is None:
            DriverHolder()
        return DriverHolder.__instance

    def __init__(self, driver):
        """ Virtually private constructor. """
        if DriverHolder.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DriverHolder.__instance = self
        self.driver = driver

    def get_driver(self):
        return self.driver

    def set_driver(self, driver):
        self.driver = driver
