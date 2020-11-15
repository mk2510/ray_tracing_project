from hittable import hittable
from vector3 import vec3
from aabb import aabb

class xy_rect(hittable):

    def __init__(self, _x0, _x1, _y0, _y1, _k,mat):
        self.x0 = _x0
        self.x1 = _x1
        self.y0 = _y0
        self.y1 = _y1
        self.k = _k
        self.mat = mat

    def bounding_box(self,time0, time1):
        output_box = aabb(vec3(self.x0,self.y0, self.k-0.0001), vec3(self.x1, self.y1, self.k+0.0001))
        return True, output_box
        
    def hit(self,r, t_min, t_max, rec):
        t = (self.k-r.origin.z()) / r.direction.z()
        if (t < t_min or t > t_max):
            return False
        x = r.origin.x() + t*r.direction.x()
        y = r.origin.y() + t*r.direction.y()
        if (x < self.x0 or x > self.x1 or y < self.y0 or y > self.y1):
            return False
        rec.u = (x-self.x0)/(self.x1-self.x0)
        rec.v = (y-self.y0)/(self.y1-self.y0)
        rec.t = t
        outward_normal = vec3(0, 0, 1)
        rec.set_face_normal(r, outward_normal)
        rec.mat_ptr = self.mat
        rec.p = r.at(t)
        return True

class xz_rect(hittable):

    def __init__(self, _x0, _x1, _z0, _z1, _k,mat):
        self.x0 = _x0
        self.x1 = _x1
        self.z0 = _z0
        self.z1 = _z1
        self.k = _k
        self.mat = mat

    def bounding_box(self,time0, time1):
        output_box = aabb(vec3(self.x0, self.k-0.0001, self.z0), vec3(self.x1, self.k+0.0001,self.z1))
        return True, output_box
        
    def hit(self,r, t_min, t_max, rec):
        t = (self.k-r.origin.y()) / r.direction.y()
        if (t < t_min or t > t_max):
            return False
        x = r.origin.x() + t*r.direction.x()
        z = r.origin.z() + t*r.direction.z()
        if (x < self.x0 or x > self.x1 or z < self.z0 or z > self.z1):
            return False
        rec.u = (x-self.x0)/(self.x1-self.x0)
        rec.v = (z-self.z0)/(self.z1-self.z0)
        rec.t = t
        outward_normal = vec3(0, 1, 0)
        rec.set_face_normal(r, outward_normal)
        rec.mat_ptr = self.mat
        rec.p = r.at(t)
        return True

class yz_rect(hittable):

    def __init__(self, _y0, _y1, _z0, _z1, _k,mat):
        self.y0 = _y0
        self.y1 = _y1
        self.z0 = _z0
        self.z1 = _z1
        self.k = _k
        self.mat = mat

    def bounding_box(self,time0, time1):
        output_box = aabb(vec3(self.k-0.0001, self.y0,self.z0 ), vec3( self.k+0.0001, self.y1, self.z1))
        return True, output_box
        
    def hit(self,r, t_min, t_max, rec):
        t = (self.k-r.origin.x()) / r.direction.x()
        if (t < t_min or t > t_max):
            return False
        y = r.origin.y() + t*r.direction.y()
        z = r.origin.z() + t*r.direction.z()

        if (z < self.z0 or z > self.z1 or y < self.y0 or y > self.y1):
            return False
        rec.u = (y-self.y0)/(self.y1-self.y0)
        rec.v = (z-self.z0)/(self.z1-self.z0)
        rec.t = t
        outward_normal = vec3(1, 0, 0)
        rec.set_face_normal(r, outward_normal)
        rec.mat_ptr = self.mat
        rec.p = r.at(t)
        return True
