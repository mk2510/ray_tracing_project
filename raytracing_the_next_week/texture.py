import math

class texture:
    def value(self,u, v, p):
        return 0

class solid_color(texture):
    
        def __init__(self, c) : 
            self.color_value = c

        def value(self, u, v, p):
            return self.color_value

class checker_texture(texture): 
        def __init__(self, _even,  _odd):
            self.even = _even
            self.odd = _odd
 

        def value(self, u,  v, p):
            sines = math.sin(10*p.x())*math.sin(10*p.y())*math.sin(10*p.z())
            if (sines < 0):
                return self.odd.value(u, v, p)
            else:
                return self.even.value(u, v, p)