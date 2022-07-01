from base.clock_observer import ClockObserver
from base.time_source import TimeSource
from time_source_implementation import TImeSourceImplementation


class MockTimeSource(TimeSource):
    def __init__(self):
        self.ts_imp = TImeSourceImplementation()

    def register_observer(self, observer: ClockObserver):
        self.ts_imp.register_observer(observer)

    def set_time(self, hours, minutes, seconds):
        self.ts_imp.notify(hours, minutes, seconds)

