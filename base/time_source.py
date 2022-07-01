from abc import ABCMeta, abstractmethod

from base.clock_observer import ClockObserver


class TimeSource(metaclass=ABCMeta):
    @abstractmethod
    def register_observer(self, observer: ClockObserver):
        pass
