from vector3 import vec3
from ray import ray

class camera:
    def __init__(self):
        aspect_ratio = 16.0 / 9.0
        viewport_height = 2.0
        viewport_width = aspect_ratio * viewport_height
        focal_length = 1.0

        self.origin = vec3(0, 0, 0)
        self.horizontal = vec3(viewport_width, 0.0, 0.0)
        self.vertical = vec3(0.0, viewport_height, 0.0)
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - vec3(0, 0, focal_length)
    

    def get_ray(self, u, v):
        return ray(self.origin, self.lower_left_corner + self.horizontal*u + self.vertical*v - self.origin)
    