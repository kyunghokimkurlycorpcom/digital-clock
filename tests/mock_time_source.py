from base.time_source import TimeSource
from base.clock_observer import ClockObserver


class MockTimeSource(TimeSource):
    def __init__(self):
        self.__its_observer = None

    def set_observer(self, observer: ClockObserver):
        self.__its_observer = observer

    def set_time(self, hours, minutes, seconds):
        self.__its_observer.update(hours, minutes, seconds)
