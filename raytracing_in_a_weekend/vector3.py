import math
from rtweekend import random_double

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

    def __NEG__(self):
        return vec3(-self.e[0],-self.e[1],-self.e[2])
    
    def __truediv__(self,other):
        return vec3(self.e[0] / other,
        self.e[1] / other,
        self.e[2] / other)

    def __getitem__(self,other):
        return self.e[other]

    def mult(self,other):
        return vec3(self.e[0] * other[0],
        self.e[1] * other[1],
        self.e[2] * other[2])

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
    
    def near_zero(self):
        s=1e-8
        return math.fabs(self.e[0]) < s and math.fabs(self.e[1]) < s and math.fabs(self.e[2]) < s 

def random(min=0.0,max=1.0):
    return vec3(random_double(min, max), random_double(min,max), random_double(min, max))
    
def random_in_unit_sphere():
    while True:
        p = random(-1,1)
        if p.length_squared() < 1:
            return p

def random_in_unit_disk():
    while True:
        p = vec3(random_double(-1,1), random_double(-1,1), 0)
        if p.length_squared() < 1:
            return p

def random_unit_vector():
    return random_in_unit_sphere().unit_vector()

def random_in_hemisphere(normal):
    in_unit_sphere = random_in_unit_sphere()
    if in_unit_sphere.dot(normal) > 0.0:
        return in_unit_sphere
    return in_unit_sphere * -1

def reflect(v, n):
    return v - n * v.dot(n) * 2

def refract(uv, n, etai_over_etat):
    neg_uv = uv * -1
    cos_theta = min(neg_uv.dot(n) , 1.0)
    r_out_perp =  (uv + n * cos_theta) * etai_over_etat
    r_out_patallel = n * (-math.sqrt(math.fabs(1.0-r_out_perp.length_squared())))
    return r_out_perp + r_out_patallel
