import math

class vec3:
    def __init__(self, e0,e1,e2):
        self.e=[e0,e1,e2]
    def __add__(self,other):
       return vec3 (self.e[0] + other.e[0],
        self.e[1] + other.e[1],
        self.e[2] + other.e[2])

    def __mul__(self,other):
        return vec3(self.e[0] * other,
        self.e[1] * other,
        self.e[2] * other)

    def __sub__(self,other):
        return vec3(self.e[0] - other.e[0],
        self.e[1] - other.e[1],
        self.e[2] - other.e[2])

    def __NEG__(self,other):
        return vec3(-self.e[0],-self.e[1],-self.e[2])
    
    def __truediv__(self,other):
        return vec3(self.e[0] / other,
        self.e[1] / other,
        self.e[2] / other)

    def __getitem__(self,other):
        return self.e[other]

    def x(self):
        return self.e[0]
    def y(self):
        return self.e[1]
    def z(self):
        return self.e[2]

    def length(self):
        return math.sqrt(self.length_squared())
    
    def length_squared(self):
        return self.e[0]*self.e[0] + self.e[1]*self.e[1] + self.e[2]*self.e[2]

    def dot(self,v):
        return self.e[0] * v.e[0] + self.e[1] * v.e[1] + self.e[2] * v.e[2]

    def cross(self,v):
        return vec3(self.e[1] * v.e[2] - self.e[2] * v.e[1],
                self.e[2] * v.e[0] - self.e[0] * v.e[2],
                self.e[0] * v.e[1] - self.e[1] * v.e[0])

    def unit_vector(self):
        return self / self.length()