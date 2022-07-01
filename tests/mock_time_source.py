from base.time_source import TimeSource
from subject import Subject


class MockTimeSource(Subject, TimeSource):
    def __init__(self):
        super().__init__()
        self.__its_seconds = None
        self.__its_minutes = None
        self.__its_hours = None

    def set_time(self, hours, minutes, seconds):
        self.__its_hours = hours
        self.__its_minutes = minutes
        self.__its_seconds = seconds
        self.notify_observers()

    def get_hours(self):
        return self.__its_hours

    def get_minutes(self):
        return self.__its_minutes

    def get_seconds(self):
        return self.__its_seconds
