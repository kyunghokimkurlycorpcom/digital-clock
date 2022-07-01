import unittest

from clock_driver import ClockDriver
from tests.mock_time_sink import MockTimeSink
from tests.mock_time_source import MockTimeSource


class TestDigitalClock(unittest.TestCase):
    def test_time_change(self):
        td_source = MockTimeSource()
        td_sink = MockTimeSink()
        sut = ClockDriver(td_source, td_sink)

        param_list = [
            (3, 4, 5),
            (7, 8, 9)
        ]

        for p1, p2, p3 in param_list:
            with self.subTest(msg=f"Expected Value - hours : {p1}, minutes: {p2}, seconds: {p3}"):
                td_source.set_time(p1, p2, p3)
                self.assertEqual(p1, td_sink.get_hours())
                self.assertEqual(p2, td_sink.get_minutes())
                self.assertEqual(p3, td_sink.get_seconds())


if __name__ == '__main__':
    unittest.main()
