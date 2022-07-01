from base.time_sink import TimeSink


class MockTimeSink(TimeSink):
    def __init__(self):
        self.__its_hours = None
        self.__its_minutes = None
        self.__its_seconds = None

    def get_hours(self):
        return self.__its_hours

    def get_minutes(self):
        return self.__its_minutes

    def get_seconds(self):
        return self.__its_seconds

    def set_time(self, hours, minutes, seconds):
        self.__its_hours = hours
        self.__its_minutes = minutes
        self.__its_seconds = seconds
