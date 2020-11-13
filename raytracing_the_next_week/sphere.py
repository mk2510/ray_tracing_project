import math

from vector3 import vec3
from hittable import hit_record
from hittable import hittable
from aabb import aabb

class sphere(hittable):
    def __init__(self, cen = None, r = None, m = None):
        self.center = cen
        self.radius = r
        self.mat_ptr = m
    
    def hit(self,r, t_min, t_max, rec):
        oc = r.origin - self.center
        a = r.direction.length_squared()
        half_b = vec3.dot(oc, r.direction)
        c = oc.length_squared() - self.radius * self.radius

        discriminant = half_b * half_b - a*c
        if discriminant < 0 or a == 0:
            return False

        sqrtd = math.sqrt(discriminant)
        
        # Find the nearest root that lies in the acceptable range.
        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if (root < t_min or t_max < root):
                return False

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)
        rec.mat_ptr = self.mat_ptr

        return True

    def bounding_box(self, time0, time1):
        return True, aabb(self.center - vec3(self.radius, self.radius,self.radius), 
                            self.center + vec3(self.radius, self.radius,self.radius))