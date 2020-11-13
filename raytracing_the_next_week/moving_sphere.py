from hittable import hittable
import math
from aabb import aabb, surrounding_box
from vector3 import vec3

class moving_sphere(hittable):
    def __init__(self, cen0, cen1, _time0, _time1, r, m):
        self.center0 = cen0
        self.center1 = cen1
        self.time0 = _time0
        self.time1 = _time1,
        self.radius = r
        self.mat_ptr = m
    
    def center(self, time):
        return self.center0 + (self.center1 - self.center0) * ((time - self.time0) / (self.time1 - self.time0))

    def hit(self,r, t_min, t_max, rec):
        oc = r.origin - self.center
        a = r.direction.length_squared()
        half_b = oc.dot(r.direction)
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
        box0 = aabb(self.center(time0) - vec3(self.radius, self.radius,self.radius), 
                            self.center(time0) + vec3(self.radius, self.radius,self.radius))
        box1 = aabb(self.center(time1) - vec3(self.radius, self.radius,self.radius), 
                            self.center(time1) + vec3(self.radius, self.radius,self.radius))
        return True, surrounding_box(box0, box1)