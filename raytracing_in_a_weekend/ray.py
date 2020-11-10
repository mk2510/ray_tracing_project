from vector3 import vec3

class ray:
    def __init__(self, _origin, _direction):
        self.origin = _origin
        self.direction = _direction

    def get_origin(self):
        return self.origin

    def get_direction(self):
        return self.direction
    
    def at(self, t):
        return self.origin + dir * t

    