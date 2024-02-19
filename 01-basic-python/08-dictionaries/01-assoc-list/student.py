class AssocList:
    def __init__(self):
        self.__items = []

    def __setitem__(self, key, value):
        for i, pair in enumerate(self.__items):
            if pair[0] == key:
                self.__items[i] = [key, value]
        else:
            self.__items.append([key, value])
    
    def __str__(self):
        return str(self.__items)



grand = AssocList()
grand['cat']= 'chat'
grand['monkey']= 'singe'

print(grand)