from color import write_color
from vector3 import vec3
from ray import ray

def ray_color(r):
    unit_direction = r.get_direction().unit_vector()
    t = 0.5 * unit_direction.y() + 1.0
    return vec3(1,1,1)*(1-t) + vec3(0.5,0.7,1.0)*t

aspect_ratio = 16.0 / 9.0
image_width = 400
image_height = int(image_width / aspect_ratio)

viewport_height = 2.0
viewport_width = aspect_ratio * viewport_height
focal_length = 1.0

origin = vec3(0, 0, 0)
horizontal = vec3(viewport_width, 0, 0)
vertical = vec3(0, viewport_height, 0)
lower_left_corner = origin - horizontal/2 - vertical/2 - vec3(0, 0, focal_length)



result_string = ""

# init image
result_string += "P3 \n" + str(image_width) + ' ' + str(image_height) + "\n255\n"


for j in range( image_height -1,0 ,-1):
    for i in range(0,image_width):
            u = i/ (image_width-1)
            v = j / (image_height-1)
            r = ray(origin, lower_left_corner + horizontal*u + vertical*v - origin)
            pixel_color = ray_color(r)
            result_string += write_color(pixel_color)

with open('image.ppm', 'w') as f:
    f.write(result_string)

f.close()