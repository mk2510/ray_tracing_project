import random

class perlin:

    def __init__(self):
        self.point_count = 256
        self.ranfloat = [0.0] * self.point_count
        for i in range(self.point_count):
            self.ranfloat[i] = random.random()
        

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
            

    def noise(self,p):
        i = int((4*p.x())) & 255
        j = int(4*p.y()) & 255
        k = int(4*p.z()) & 255

        return self.ranfloat[int(self.perm_x[i]) ^ int(self.perm_y[j]) ^ int(self.perm_z[k])]
        
