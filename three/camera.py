from data_classes.vector_3 import Vector3

class Camera:
    def __init__(self, x, y, z):
        self.position = Vector3(x, y, z)
        self.x = x
        self.y = y
        self.z = z
        