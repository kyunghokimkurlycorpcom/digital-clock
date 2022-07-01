from abc import ABCMeta, abstractmethod


class TimeSource(metaclass=ABCMeta):
    @abstractmethod
    def set_driver(self, driver):
        pass
