from base.time_source import Subject


class MockTimeSource(Subject):
    def set_time(self, hours, minutes, seconds):
        self.notify_observers(hours, minutes, seconds)
