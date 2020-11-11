import math

from color import write_color
from vector3 import vec3
from ray import ray
import rtweekend
from hittable import hit_record
from hittable_list import hit_ls
from sphere import sphere

def hit_sphere(center, radius, r):
    oc = r.origin - center
    a = r.direction().length_squared()
    half_b = vec3.dot(oc,r.direction())
    c = oc.length_squared() - radius * radius
    discriminant = half_b * half_b - a*c
    if discriminant < 0:
        return -1.0
    return (-half_b - math.sqrt(discriminant)) / a

def ray_color(r, world):
    rec = hit_record(vec3(0,0,0), vec3(0,0,0), 0.0, False)
    hit_anything, rec = hit_ls(world, r, 0, rtweekend.infinity, rec)
    if hit_anything:
        return rec.normal + vec3(1,1,1) * 0.5
    unit_direction = r.get_direction().unit_vector()
    t = 0.5 * (unit_direction.y() + 1.0)
    return vec3(1,1,1)*(1-t) + vec3(0.5,0.7,1.0)*t

#Image
aspect_ratio = 16.0 / 9.0
image_width = 400
image_height = int(image_width / aspect_ratio)

#World
world = []
world.append(sphere(vec3(0,0,-1), 0.5))
world.append(sphere(vec3(0,-100.5,-1),100))

# camera
viewport_height = 2.0
viewport_width = aspect_ratio * viewport_height
focal_length = 1.0

origin = vec3(0, 0, 0)
horizontal = vec3(viewport_width, 0, 0)
vertical = vec3(0, viewport_height, 0)
lower_left_corner = origin - horizontal/2 - vertical/2 - vec3(0, 0, focal_length)



result_string = ""

# render
result_string += "P3 \n" + str(image_width) + ' ' + str(image_height) + "\n255\n"


for j in range( image_height -1,0 ,-1):
    for i in range(0,image_width):
            u = i/ (image_width-1)
            v = j / (image_height-1)
            r = ray(origin, lower_left_corner + horizontal*u + vertical*v - origin)
            pixel_color = ray_color(r, world)
            result_string += write_color(pixel_color)

with open('image.ppm', 'w') as f:
    f.write(result_string)

f.close()