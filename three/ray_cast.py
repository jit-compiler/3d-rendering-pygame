import pygame
from math import tan, radians
from data_classes.vector_3 import Vector3

class RayCaster:
    def __init__(self):
        pass

    def project_vertex(self, vertex, camera):
        # Apply the camera transformation to project the vertex
        projected_x = (vertex.x - camera.x) / (vertex.z - camera.z)
        projected_y = (vertex.y - camera.y) / (vertex.z - camera.z)
        return Vector3(projected_x, projected_y, 0)

    def ray_cast(self, mesh, camera, screen):
        vertices, edges = mesh.vertices, mesh.edges
        projected_vertices = []

        for vertex in vertices:
            # Project each vertex onto the screen
            projected_vertex = self.project_vertex(vertex, camera)
            projected_vertices.append(projected_vertex)

        # Scale and translate the vertices to fit the screen
        screen_width, screen_height = screen.get_width(), screen.get_height()
        scale_factor = min(screen_width, screen_height) / 2
        translated_vertices = [
            Vector3(projected.x * scale_factor + screen_width / 2, projected.y * scale_factor + screen_height / 2, 0)
            for projected in projected_vertices
        ]

        return translated_vertices, edges
