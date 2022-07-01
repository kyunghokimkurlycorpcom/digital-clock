from abc import ABCMeta, abstractmethod


class TimeSink(metaclass=ABCMeta):
    @abstractmethod
    def set_time(self, hours, minutes, seconds):
        pass
