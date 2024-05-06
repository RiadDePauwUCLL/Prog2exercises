from datetime import date


class Calendar:
    def __init__(self):
        self.__today = date.today()

    @property
    def today(self):
        return self.__today


class CalendarStub:
    def __init__(self, today):
        self.__today = today