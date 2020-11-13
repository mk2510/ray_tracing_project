import random
import math
import vector3
from vector3 import vec3
class perlin:

    def __init__(self):
        self.point_count = 256
        self.ranfloat = [0.0] * self.point_count
        self.ranvec = []
        for i in range(self.point_count):
            self.ranfloat[i] = random.random()
            self.ranvec.append(vector3.random(-1,1).unit_vector())
        

        self.perm_x = self.perlin_generate_perm()
        self.perm_y = self.perlin_generate_perm()
        self.perm_z = self.perlin_generate_perm()

    def perlin_generate_perm(self):
        p = []
        for i in range(self.point_count):
            p.append(i)

        self.permute(p, self.point_count)

        return p

    def permute(self, p, n):
        for i in range(n-1, -1, -1):
            target = random.randint(0, i)
            tmp = p[i]
            p[i] = p[target]
            p[target] = tmp
            
    def turb(self, p, depth = 7):
        accum = 0.0
        temp_p = p
        weight = 1.0

        for _ in range(depth):
            accum += weight*self.noise(temp_p)
            weight *= 0.5
            temp_p *= 2

        return abs(accum)

    def noise(self,p):
        u = p.x() - math.floor(p.x())
        v = p.y() - math.floor(p.y())
        w = p.z() - math.floor(p.z())

        i = int(math.floor(p.x()))
        j = int(math.floor(p.y()))
        k = int(math.floor(p.z()))
        c = [[[0,0],[0,0]],[[0,0],[0,0]]]

        for di in range(2):
            for dj in range(2):
                for dk in range(2):
                    c[di][dj][dk] = self.ranvec[self.perm_x[(i+di) & 255] ^self.perm_y[(j+dj) & 255] ^ self.perm_z[(k+dk) & 255]]

        return perlin_interp(c, u, v, w)

def trilinear_interp(c, u, v, w):
    accum = 0.0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                accum += (i*u + (1-i)*(1-u))*(j*v + (1-j)*(1-v))* (k*w + (1-k)*(1-w))*c[i][j][k]

    return accum

def perlin_interp(c, u, v, w):
    uu = u*u*(3-2*u)
    vv = v*v*(3-2*v)
    ww = w*w*(3-2*w)
    accum = 0.0

    for i in range(2):
        for j in range(2):
           for k in range(2):
                weight_v = vec3(u-i, v-j, w-k)
                accum += (i*uu + (1-i)*(1-uu)) * (j*vv + (1-j)*(1-vv)) * (k*ww + (1-k)*(1-ww))  * (c[i][j][k].dot(weight_v))
        
    return accum
    
