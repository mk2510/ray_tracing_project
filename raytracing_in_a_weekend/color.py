from rtweekend import clamp
import math

def write_color(pixel_color, samples_by_pixel):
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # Divide the color by the number of samples.
    scale = 1.0 / samples_by_pixel
    r = math.sqrt(scale * r)
    g = math.sqrt(scale * g)
    b = math.sqrt(scale*b)

    return str(int(256*clamp(r,0.0,0.999))) + ' ' + str(int(256*clamp(g,0.0,0.999))) + ' ' + str(int(256*clamp(b,0.0,0.999))) + '\n'