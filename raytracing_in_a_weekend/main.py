import math
import random

from color import write_color
from vector3 import vec3, random_in_unit_sphere
from ray import ray
import rtweekend
from hittable import hit_record
from hittable_list import hit_ls
from sphere import sphere
from camera import camera

def ray_color(r, world, depth):
    rec = hit_record(vec3(0,0,0), vec3(0,0,0), 0.0, False)

    if depth <= 0:
        return vec3(0,0,0)

    hit_anything, rec = hit_ls(world, r, 0, rtweekend.infinity, rec)
    if hit_anything:
        target = rec.p + rec.normal + random_in_unit_sphere()
        return ray_color(ray(rec.p, target - rec.p), world, depth - 1) * 0.5
    unit_direction = r.get_direction().unit_vector()
    t = 0.5 * (unit_direction.y() + 1.0)
    return vec3(1,1,1)*(1-t) + vec3(0.5,0.7,1.0)*t

#Image
aspect_ratio = 16.0 / 9.0
image_width = 400
image_height = int(image_width / aspect_ratio)
samples_per_pixel = 100
max_depth = 50

#World
world = []
world.append(sphere(vec3(0,0,-1), 0.5))
world.append(sphere(vec3(0,-100.5,-1),100))

# camera
cam = camera()


# render
result_string = ""
result_string += "P3 \n" + str(image_width) + ' ' + str(image_height) + "\n255\n"


for j in range( image_height -1,0 ,-1):
    for i in range(0,image_width):
        pixel_color = vec3(0,0,0)
        for _ in range(samples_per_pixel):
            u = (i + random.random()) / (image_width-1)
            v = (j + random.random()) / (image_height-1)
            r = cam.get_ray(u, v)
            pixel_color =  pixel_color + ray_color(r, world, max_depth)

        result_string += write_color(pixel_color, samples_per_pixel)

with open('image.ppm', 'w') as f:
    f.write(result_string)

f.close()