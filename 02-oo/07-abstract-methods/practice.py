from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @abstractmethod
    def make_sound(self):
        ...


class Cow(Animal):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def make_sound(self):
        return "moo"
    

class Cat(Animal):

    def __init__(self, name, weight, wiskers):
        self.name = name
        self.weight = weight
        self.wiskers = wiskers

    def make_sound(self):
        return "miauw"
    

class Dog(Animal):

    def __init__(self, name, weight, doggo):
        self.name = name
        self.weight = weight
        self.doggo = doggo

    def make_sound(self):
        return "woof"


cow = Cow("Yone", "200kg")
dog = Dog("tommy", "50kg", True)
cat = Cat("Richard", "14kg", True)

print(cow.make_sound())
print(cat.make_sound())
print(dog.make_sound())