class ClockDriver:
    def __init__(self, source, sink):
        source.set_driver(self)
        self.its_sink = sink

    def update(self, hours, minutes, seconds):
        self.its_sink.set_time(hours, minutes, seconds)
