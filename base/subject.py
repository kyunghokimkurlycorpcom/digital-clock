from base.observer import Observer


class Subject:
    def __init__(self):
        self.__its_observers = list()

    def register_observer(self, observer: Observer):
        self.__its_observers.append(observer)

    def notify_observers(self):
        for observer in self.__its_observers:
            observer.update()
