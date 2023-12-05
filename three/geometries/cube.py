from data_classes.vector_3 import Vector3

class Cube:
    def __init__(self) -> None:
        pass

    def generate_cube(self, size_x, size_y, size_z):
        half_size_x = size_x / 2
        half_size_y = size_y / 2
        half_size_z = size_z / 2

        vertices = [
            Vector3(-half_size_x, -half_size_y, -half_size_z),
            Vector3(half_size_x, -half_size_y, -half_size_z),
            Vector3(half_size_x, half_size_y, -half_size_z),
            Vector3(-half_size_x, half_size_y, -half_size_z),
            Vector3(-half_size_x, -half_size_y, half_size_z),
            Vector3(half_size_x, -half_size_y, half_size_z),
            Vector3(half_size_x, half_size_y, half_size_z),
            Vector3(-half_size_x, half_size_y, half_size_z)
        ]

        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

        # Define faces using vertex indices
        faces = [
           (0, 1, 3, 2), # Front face
           (4, 5, 7, 6), # Back face
           (0, 1, 5, 4), # Bottom face
           (2, 3, 7, 6), # Top face
           (0, 3, 7, 4), # Left face
           (1, 2, 6, 5)  # Right face
       ]

        return vertices, edges, faces
