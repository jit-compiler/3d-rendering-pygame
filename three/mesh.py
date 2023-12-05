from data_classes.vector_3 import Vector3
from three.geometries.cube import Cube
import math
from data_classes.vector_3 import Vector3

class Mesh:
    def __init__(self, geometry, position, size_x, size_y, size_z, texture_urls=None):
        self.geometry = geometry
        self.position = position
        self.size_x = size_x
        self.size_y = size_y
        self.size_z = size_z
        self.texture_urls = texture_urls or {}  # Dictionary to store texture URLs for each face

        # Generate vertices, edges, and faces based on the geometry type
        if self.geometry == "cube":
            vertices, edges, faces = Cube().generate_cube(size_x, size_y, size_z)
            # Offset the vertices based on the mesh position
            self.vertices = [vertex + position for vertex in vertices]
            self.edges = edges
            self.faces = faces
            self.normals = self.calculate_normals()

            # Generate default texture coordinates (you can adjust these based on your requirements)
            self.texture_coords = [
                Vector3(0, 0, 0),
                Vector3(1, 0, 0),
                Vector3(1, 1, 0),
                Vector3(0, 1, 0),
                Vector3(0, 0, 0),
                Vector3(1, 0, 0),
                Vector3(1, 1, 0),
                Vector3(0, 1, 0),
            ]
            
    def calculate_normals(self):
        normals = []
        for face in self.faces:
            v1 = self.vertices[face[1]] - self.vertices[face[0]]
            v2 = self.vertices[face[2]] - self.vertices[face[0]]
            normal = v1.cross(v2).normalize()
            normals.append(normal)
        return normals
