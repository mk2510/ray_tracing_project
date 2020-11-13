import rtweekend
from vector3 import vec3

class aabb:
    def __init__(self, a, b):
        self.minimum = a
        self.maximum = b

    def hit(self, r, t_min, t_max):
        for a in range(3):
            t0 = min((self.minimum[a] - r.origin[a]) / r.direction[a],
                            (self.maximum[a] - r.origin[a]) / r.direction[a])
            t1 = max((self.minimum[a] - r.origin[a]) / r.direction[a],
                            (self.maximum[a] - r.origin[a]) / r.direction[a])
            t_min = max(t0, t_min)
            t_max = min(t1, t_max)
            if (t_max <= t_min):
                return False
    
        return True

def surrounding_box(box0, box1):
    small = vec3(min(box0.minimum.x(), box1.minimum.x()),
                 min(box0.minimum.y(), box1.minimum.y()),
                 min(box0.minimum.z(), box1.minimum.z()))
    big = vec3(max(box0.maximum.x(), box1.maximum.x()),
                 max(box0.maximum.y(), box1.maximum.y()),
                 max(box0.maximum.z(), box1.maximum.z()))
    
    return aabb(small, big)