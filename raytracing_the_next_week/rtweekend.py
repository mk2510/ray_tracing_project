import math
import random as rd

infinity = float('inf') 
pi = math.pi

def random_double(min, max):
    return min + (max-min)*rd.random()

def clamp(x,min,max):
    if(x<min):
        return min
    if (x>max):
        return max
    return x

def degree_to_radians(degrees):
    return degrees * pi / 180.0