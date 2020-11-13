from hittable import hittable
import random
from aabb import surrounding_box

class bvh_node(hittable):
    def __init__(self,hittable_ls = None, scr_objects = None, start = 0, end = 0, time0 = 0, time1 = 0):
        self.hittable_ls = hittable_ls
        self.src_objects = scr_objects
        self.start = start
        self.end = end
        self.time0 = time0
        self.time1 = time1

        self.box = None
        self.left = None
        self.right = None

        self.objects = self.src_objects
        axis = random.randint(0,2)
        comparator = box_x_compare if (axis == 0) else  box_y_compare if axis == 1 else box_z_compare

        object_span = self.end - self.start

        if (object_span == 1):
            left = self.objects[start]
            right = self.objects[start]
        elif (object_span == 2):
            if (comparator(self.objects[start], self.objects[start+1])):
                left = self.objects[start]
                right = self.objects[start+1]
            else:
                left = self.objects[start+1]
                right = self.objects[start]
        else:
            begin = self.objects[0] 
            self.objects.sort(comparator)

            temp = []
            for o in self.objects:
                if comparator(o, begin + end) and comparator(begin+start, o):
                    temp.append(o)

            objects = temp
            mid = start + object_span/2
            left = bvh_node(objects, start, mid, time0, time1)
            right = bvh_node(objects, mid, end, time0, time1)
        
        leftbool, box_left = left.bounding_box (time0, time1)
        rightbool, box_right = right.bounding_box(time0, time1)
        if (  not leftbool or not rightbool):
            raise RuntimeError("No bounding box in bvh_node constructor.\n")

        self.box = surrounding_box(box_left, box_right)


    
    def bounding_box(self, time0, time1):
        return True, self.box

    def hit(self, r,t_min, t_max, rec):
        if not self.box.hit(r,t_min, t_max):
            return False
        
        hit_left = self.left.hit(r, t_min, t_max, rec)
        hit_right = self.right.hit(r, t_min, rec.t if hit_left else t_max, rec)

        return hit_left or hit_right

def box_compare(a, b,  axis):
    abool, box_a = a.bounding_box(0,0)
    bbool, box_b = b.bounding_box(0,0)

    if (not abool or not bbool):
        raise RuntimeError("No bounding box in bvh_node constructor.\n")

    return box_a.min().e[axis] < box_b.min().e[axis]



def box_x_compare ( a, b):
    return box_compare(a, b, 0)

def box_y_compare ( a, b):
    return box_compare(a, b, 1)

def box_z_compare ( a, b):
    return box_compare(a, b, 2)
