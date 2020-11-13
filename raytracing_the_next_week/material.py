from ray import ray
from vector3 import random_unit_vector, reflect, vec3, random_in_unit_sphere, refract

import random
import math

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

        scattered = ray(rec.p, scatter_direction, r_in.time)
        attenuation = self.albedo
        return True, scattered, attenuation

class metal(material):
    def __init__(self,a, _fuzz):
        self.albedo = a
        self.fuzz = _fuzz if _fuzz < 1 else 1
    def scatter(self, r_in, rec):
        reflected = reflect(r_in.direction.unit_vector(), rec.normal)
        scattered = ray(rec.p, reflected + random_in_unit_sphere() * self.fuzz, r_in.time)
        attenuation = self.albedo
        return scattered.direction.dot(rec.normal) > 0, scattered, attenuation

class dielectric(material):
  
        def __init__(self, index_of_refraction):
            self.ir = index_of_refraction

        def scatter(self,r_in, rec):
            attenuation = vec3(1.0, 1.0, 1.0)
            refraction_ratio = (1.0/self.ir) if rec.front_face else self.ir
            
            unit_direction =r_in.direction.unit_vector()
            neg_unit_direction = unit_direction * -1
            cos_theta = min(neg_unit_direction.dot(rec.normal), 1.0)
            sin_theta = math.sqrt(1.0-cos_theta*cos_theta)

            unit_direction = r_in.direction.unit_vector()
            cannot_refract = refraction_ratio * sin_theta > 1.0
            if cannot_refract or _reflectance(cos_theta, refraction_ratio) > random.random():
                direction = reflect(unit_direction, rec.normal)
            else:
                direction = refract(unit_direction, rec.normal, refraction_ratio)            

            scattered = ray(rec.p, direction, r_in.time)
            return True, scattered, attenuation

def _reflectance(cosine, ref_idx):
    r0 = (1-ref_idx) / (1+ref_idx)
    r0 *= r0
    return r0 + (1-r0) * math.pow(1-cosine, 5)