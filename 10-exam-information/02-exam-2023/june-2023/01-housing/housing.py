import re
from abc import ABC, abstractmethod

class Person:
    def __init__(self, id, name, is_a_student: bool):
        if not Person.is_valid_name(name):
            raise ValueError("name is invalid")
        self.id = id
        self.__name = name
        self.is_a_student = is_a_student

    @staticmethod
    def is_valid_name(name):
        if re.search(r"^(\w+\s)+\w+$", name):
            return True
        else:
            return False
        
    # @staticmethod
    # def is_valid_name(name):
    #     return bool(re.search(r'\w+\s+\w+', name))

    @property
    def name(self):
        return self.__name
    
    @name.getter
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if not self.is_valid_name(new_name):
            raise ValueError("name is invalid")
        self.__name = new_name



class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = {}

    @property
    def number_of_occupants(self):
        return len(self.__occupants)
    
    @property
    def maximum_occupants(self):
        return min(self.area // 20, self.number_of_rooms * 2)

    def register_resident(self, person):
        if person.id in self.__occupants:
            return
        if self.number_of_occupants >= self.maximum_occupants:
            raise RuntimeError("Not enough room for another person")
        self.__occupants[person.id] = person

    def unregister_resident(self, id):
        if id in self.__occupants:
            del self.__occupants[id]

    @property
    def resident_names(self):
        return [person.name for person in self.__occupants.values()]
    
    @abstractmethod
    def calculate_value(self):
        pass



class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity

    def calculate_value(self):
        return (25000 * self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity)



class StudentKot(Residence):
    def __init__(self, address, area):
        super().__init__(address, area, 1)

    def register_resident(self, person):
        if not person.is_a_student:
            raise RuntimeError("Cannot register a non-student to a StudentKot.")
        super().register_resident(person)
    
    def calculate_value(self):
        return 150000 + (750 * self.area)
    


# create some people
aimee = Person("12.34.56-789.01","Aimee Backiel",False)
bastian = Person("01.02.03-040.05", "Bastian Li Backiel", True)

# create some residences
my_villa = Villa("Roeselbergdal 44, 3012 Wilsele", 151, 4, 1)
my_kot = StudentKot("Kortestraat 6, 3000 Leuven",20)

# check the values of the properties
print(my_villa.calculate_value())  # 427100
print(my_kot.calculate_value())  # 165000

# move the people into a residence
my_villa.register_resident(aimee)
my_villa.register_resident(bastian)

# check the residents of the villa
print(my_villa.resident_names)  # ["Aimee Backiel","Bastian Li Backiel"]

# Someday, sadly Bastian will grow up and move into his student kot
my_villa.unregister_resident(bastian.id)
my_kot.register_resident(bastian)

# check the residents again
print(my_villa.resident_names)
print(my_kot.resident_names)

# With all her free time, Aimee can expand the garage to make space for all her hobbies
my_villa.garage_capacity = 3
print(f'New value of Aimee\'s villa:', my_villa.calculate_value())