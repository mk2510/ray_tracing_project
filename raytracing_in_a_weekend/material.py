from ray import ray
from vector3 import random_unit_vector, reflect, vec3

class material:
    def scatter(self,r_in, rec):
        return False, ray(vec3(0,0,0), vec3(0,0,0)), 0.0

class lambertian(material):
    def __init__(self,a):
        self.albedo = a

    def scatter(self, r_in, rec):
        scatter_direction = rec.normal + random_unit_vector()

        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        scattered = ray(rec.p, scatter_direction)
        attenuation = self.albedo
        return True, scattered, attenuation

class metal(material):
    def __init__(self,a):
        self.albedo = a
    def scatter(self, r_in, rec):
        reflected = reflect(r_in.direction.unit_vector(), rec.normal)
        scattered = ray(rec.p, reflected)
        attenuation = self.albedo
        return scattered.direction.dot(rec.normal) > 0, scattered, attenuation