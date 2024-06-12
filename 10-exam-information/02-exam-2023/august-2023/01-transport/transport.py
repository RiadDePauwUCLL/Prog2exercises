import re
from abc import ABC, abstractmethod

class Passenger:
    def __init__(self, id, name, money):
        if not Passenger.is_valid_name(name):
            raise ValueError("name is invalid")
        self.id = id
        self.__name = name
        self.money = money
    
    @staticmethod
    def is_valid_name(name):
        if re.search(r"^(\w+\s)+\w+$", name):
            return True
        else:
            return False
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if not self.is_valid_name(new_name):
            raise ValueError("name is invalid")
        self.__name = new_name



class Vehicle(ABC):
    def __init__(self, license_plate, amount_of_seats):
        self.license_plate = license_plate
        self.amount_of_seats = amount_of_seats
        self.__occupants = {}

    @property
    @abstractmethod
    def maximum_occupants(self):
        pass

    @property
    def number_of_occupants(self):
        return len(self.__occupants)

    def add_passenger(self, passenger):
        self.__occupants[passenger.id] = passenger

    def remove_passenger(self, passenger):
        if passenger.id in self.__occupants:
            del self.__occupants[passenger.id]

    def remove_all_passengers(self):
        self.__occupants.clear()

    @property
    def occupant_names(self):
        return [passenger.name for passenger in self.__occupants.values()]
    

    
class Taxi(Vehicle):
    def __init__(self, license_plate, amount_of_seats):
        super().__init__(license_plate, amount_of_seats)
        self.is_available = True

    @property
    def maximum_occupants(self):
        return self.amount_of_seats

    def pickup(self, passengers, distance):
        if not self.is_available or len(passengers) > self.maximum_occupants:
            raise ValueError("Taxi is unavailable or too many passengers")
        fare = max(1 + distance, 5)
        if passengers[0].money < fare:
            raise RuntimeError("Insufficient funds for fare")
        passengers[0].money -= fare
        for passenger in passengers:
            self.add_passenger(passenger)
        self.is_available = False

    def dropoff(self):
        if not self.passengers:
            return
        self.passengers.clear()
        self.is_available = True


class Bus(Vehicle):
    def __init__(self, license_plate, amount_of_seats):
        super().__init__(license_plate, amount_of_seats)

    @property
    def maximum_occupants(self):
        return 2 * self.amount_of_seats

    def board(self, passenger):
        if self.number_of_occupants + 1 > self.maximum_occupants:
            raise RuntimeError("Bus is full")
        fare = 2
        if passenger.money < fare:
            raise RuntimeError("Insufficient funds for fare")
        passenger.money -= fare
        self.add_passenger(passenger)

    def disembark(self, passenger):
        self.remove_passenger(passenger)