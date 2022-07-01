from base.time_source import TimeSource
from base.clock_observer import ClockObserver


class MockTimeSource(TimeSource):
    def __init__(self):
        self.__its_observers = list()

    def register_observer(self, observer: ClockObserver):
        self.__its_observers.append(observer)

    def set_time(self, hours, minutes, seconds):
        for observer in self.__its_observers:
            observer.update(hours, minutes, seconds)
