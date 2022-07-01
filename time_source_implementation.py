from base.clock_observer import ClockObserver


class TImeSourceImplementation:
    def __init__(self):
        self.__its_observers = list()

    def register_observer(self, observer: ClockObserver):
        self.__its_observers.append(observer)

    def notify(self, hours, minutes, seconds):
        for observer in self.__its_observers:
            observer.update(hours, minutes, seconds)