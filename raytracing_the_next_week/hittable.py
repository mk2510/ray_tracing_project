from dataclasses import dataclass

from material import material
from vector3 import vec3

@dataclass
class hit_record:
    p : vec3
    normal: vec3
    mat_ptr : material 
    t: float
    front_face : bool

    def set_face_normal(self,r, outward_normal):
        self.front_face = vec3.dot(r.direction, outward_normal) < 0
        self.normal = outward_normal if self.front_face else outward_normal * -1


class hittable:
    def hit(self,r, t_min, t_max, rec):
        return 0
    def bounding_box(self, time0, time1):
        return  True, None