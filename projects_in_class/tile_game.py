from abc import abstractmethod


class Player:
    def __init__(self):  # self, energy_level=20 also counts but that is mainly if we are going to add more to the energy level.
        self.energy_level = 20
        self.__tools = []

        @property
        def energy_level(self):
            return self.__energy_level

        @energy_level.setter
        def energy_level(self, value):
            self.__energy_level = value

        @property
        def tools(self):
            return self.__tools

        def add_tools(self, tool):
            self.__tools.append(tool)

class Tile(Player):
    # you don't need to have an __init__(aka constructor)
    @property
    @abstractmethod
    def energy_loss(self):
        ...
    
    @energy_loss.setter
    @abstractmethod
    def energy_loss(self, value):
        ...

    def tools_needed():
        return False
    

class Stone(Tile):
    def __init__(self, damage=100):
        self.damage = damage
        self.energy_loss = 5

    def tools_needed(self, player):
        return True


class Water(Tile):
    def __init__(self):
        self.energy_loss = 3



class Mud(Tile):
    def __init__(self):
        self.energy_loss = 2


class Path(Tile):
    def __init__(self):
        self.energy_loss = 1
   