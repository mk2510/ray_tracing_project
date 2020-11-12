from vector3 import vec3, random_in_unit_disk
from ray import ray
from rtweekend import degree_to_radians
import math

class camera:
    def __init__(self, lookfrom, lookat, vup, vfov, aspect_ratio, aperture, focus_dist):

        theta = degree_to_radians(vfov)
        h = math.tan(theta / 2)

        viewport_height = 2.0 * h
        viewport_width = aspect_ratio * viewport_height

        self.w = (lookfrom - lookat).unit_vector()
        self.u = vup.cross(self.w).unit_vector()
        self.v = self.w.cross(self.u)

        self.origin = lookfrom
        self.horizontal =  self.u * viewport_width * focus_dist
        self.vertical =  self.v * viewport_height * focus_dist
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - self.w * focus_dist

        self.lense_radius = aperture / 2

    def get_ray(self, s, t):
        rd = random_in_unit_disk() * self.lense_radius
        offset = self.u * rd.x()  + self.v * rd.y()

        return ray(self.origin + offset,
                   self.lower_left_corner + self.horizontal*s + self.vertical*t - self.origin - offset)
    