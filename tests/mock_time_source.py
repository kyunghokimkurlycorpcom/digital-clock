from base.time_source import TimeSource


class MockTimeSource(TimeSource):
    def __init__(self):
        self.__its_driver = None

    def set_driver(self, driver):
        self.__its_driver = driver

    def set_time(self, hours, minutes, seconds):
        self.__its_driver.update(hours, minutes, seconds)
