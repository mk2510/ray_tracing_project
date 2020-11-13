import math
import random

import vector3
from rtweekend import random_double
import multiprocessing
from multiprocessing import Process, Array
from ctypes import c_char_p
from moving_sphere import moving_sphere

from color import write_color
from vector3 import vec3, random_in_hemisphere
from ray import ray
import rtweekend
from hittable import hit_record
from hittable_list import hit_ls
from sphere import sphere
from camera import camera

from material import lambertian, metal, dielectric

 #image width
def multi_render(return_string, id, fromI, toI, image_height, image_width ,samples_per_pixel, cam, world, max_depth):
    for j in range( toI  , fromI -1,-1):
        for i in range(0,image_width):
            pixel_color = vec3(0,0,0)
            for _ in range(samples_per_pixel):
                u = (i + random.random()) / (image_width-1)
                v = (j + random.random()) / (image_height-1)
                r = cam.get_ray(u, v)
                pixel_color =  pixel_color + ray_color(r, world, max_depth)

            return_string[id] += write_color(pixel_color, samples_per_pixel)

def random_scene():
    world = []

    ground_material = lambertian(vec3(0.5, 0.5, 0.5))
    world.append(sphere(vec3(0,-1000,0), 1000, ground_material))

    for a in range(-11,11,1):
        for b in range(-11,11,1):
            choose_mat = random.random()
            center = vec3(a + 0.9*random.random(), 0.2, b + 0.9*random.random())

            if((center - vec3(4, 0.2, 0)).length() > 0.9):
                if (choose_mat < 0.8):
                    #diffuse
                    albedo = vector3.random().mult( vector3.random())
                    sphere_material = lambertian(albedo)
                    center2 = center + vec3(0, random_double(0,0.5), 0)
                    world.append(moving_sphere(center, center2, 0.0, 1.0, 0.2, sphere_material))
                elif (choose_mat < 0.95):
                    #metal
                    albedo = vector3.random(0.5, 1)
                    fuzz = random_double(0, 0.5)
                    sphere_material = metal(albedo, fuzz)
                    world.append(sphere(center, 0.2, sphere_material))
                else:
                    #glass
                    sphere_material = dielectric(1.5)
                    world.append(sphere(center, 0.2, sphere_material))

    material1 = dielectric(1.5)
    world.append(sphere(vec3(0, 1, 0), 1.0, material1))

    material2 = lambertian(vec3(0.4, 0.2, 0.1))
    world.append(sphere(vec3(-4, 1, 0), 1.0, material2))

    material3 = metal(vec3(0.7, 0.6, 0.5), 0.0)
    world.append(sphere(vec3(4, 1, 0), 1.0, material3))

    return world


def ray_color(r, world, depth):
    rec = hit_record(vec3(0,0,0), vec3(0,0,0), None, 0.0, False)

    if depth <= 0:
        return vec3(0,0,0)

    hit_anything, rec = hit_ls(world, r, 0.001, rtweekend.infinity, rec)
    if hit_anything:
       scat, scattered, attenuation = rec.mat_ptr.scatter(r,rec)
       if scat:
           return  ray_color(scattered, world,depth-1).mult(attenuation)
       return vec3(0,0,0)
    unit_direction = r.get_direction().unit_vector()
    t = 0.5 * (unit_direction.y() + 1.0)
    return vec3(1,1,1)*(1-t) + vec3(0.5,0.7,1.0)*t

if __name__ == '__main__':

    #Image
    aspect_ratio = 16.0 / 9.0
    image_width = 384 # optimised size for an 8-core CPU
    image_height = int(image_width / aspect_ratio)
    samples_per_pixel = 50
    max_depth = 50

    #World
    world = random_scene()

    # camera
    lookfrom = vec3(13,2,3)
    lookat = vec3(0,0,0)
    vup = vec3(0,1,0)
    dist_to_focus = 10.0
    aperture = 0.1

    cam = camera(lookfrom, lookat, vup, 20, aspect_ratio, aperture, dist_to_focus, 0.0, 1.0)


    # render
    result_string = ""
    result_string += "P3 \n" + str(image_width) + ' ' + str(image_height) + "\n255\n"


    number_of_cores = multiprocessing.cpu_count()
    process = []
    manager = multiprocessing.Manager()
    return_str = manager.dict()

    for i in range(number_of_cores):
        return_str[i] = ''
        process.append(Process(target = multi_render, args=(return_str,i,int(i*image_height/number_of_cores), int((i+1)*image_height/number_of_cores), image_height, image_width,samples_per_pixel, cam, world, max_depth),))
        process[i].start()
    
    for i in range(number_of_cores):
        process[i].join()

    for i in range(number_of_cores-1, -1, -1):
        result_string += return_str[i]


    with open('image.ppm', 'w') as f:
        f.write(result_string)

    f.close()