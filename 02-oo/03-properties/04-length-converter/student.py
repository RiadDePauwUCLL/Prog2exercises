class LengthConverter:
    def __init__(self):
        self.__meter = 0
        self.__feet = 0
        self.__inch = 0

    @property
    def meter(self):
        return self.__meter
    
    @property
    def feet(self):
        return self.__feet
    
    @property
    def inch(self):
        return self.__inch
    
    @meter.setter
    def meter(self, value):
        if self.__feet:
            self.__feet /= 3.281
            return self.__feet

        elif self.__inch:
            self.__inch *= 39.37
            return self.__inch

        else:
            self.__meter = value

    @feet.setter
    def feet(self, value):
        if self.__meter:
            self.__meter *= 3.281
            return self.__meter

        elif self.__inch:
            self.__inch /= 12
            return self.__inch

        else:
            self.__feet = value

    @inch.setter
    def inch(self, value):
        if self.__feet:
            self.__feet *= 12
            return self.__feet

        elif self.__meter:
            self.__meter *= 39.37
            return self.__meter

        else:
            self.__inch = value

        