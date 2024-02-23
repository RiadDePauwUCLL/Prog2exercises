class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("bruh moment")

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("bruh moment")
    
    def __str__(self):
        return f'Vector({self.x}, {self.y})'


vector1 = Vector(1, 2)
vector2 = Vector(3, 4)
vector3 = Vector(5, 4)



sum = vector1.add(vector3)
print(sum.y)

result = vector1 + vector2
print(result)