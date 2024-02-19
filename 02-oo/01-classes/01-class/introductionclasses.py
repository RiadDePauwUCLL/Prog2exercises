class Person:

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f'{self.name}, {self.age} yo, {self.height} cm, {self.weight} kg'

p1 = Person("Serhat", 27, 182, 100)

print(p1)




class Dog:
    def __init__(self, breed, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.breed = breed
        self.age = age

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, value):
            if value < 0:
                raise ValueError("Age cannot be negative")
            self.__age = value


d1 = Dog("English bulldog", 10)
d2 = Dog("German Shepard", 15)
print(d1.age)

print(d1.breed)
print(d2.breed)