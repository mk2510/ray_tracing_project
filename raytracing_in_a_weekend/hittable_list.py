from hittable import hit_record
from vector3 import vec3

def hit_ls(ls,r,t_min, t_max, rec):
    temp_rec = hit_record(vec3(0,0,0),vec3(0,0,0), 0.0, False)
    hit_anything = False
    closest_so_far = t_max

    for l in ls:
        if l.hit(r,t_min,closest_so_far, temp_rec):
            hit_anything = True
            closest_so_far = temp_rec.t
            rec = temp_rec

    return (hit_anything, rec)        