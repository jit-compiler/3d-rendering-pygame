from three.ray_cast import RayCaster
import pygame

class Scene:
    def __init__(self, camera):
        self.meshes = []
        self.camera = camera
        self.ray_caster = RayCaster()

    def add(self, mesh):
        self.meshes.append(mesh)
        
    def render(self, screen):
        self.raycasted_objects = []
        for mesh in self.meshes:
            result = self.ray_caster.ray_cast(mesh, self.camera, screen)
            if result:
                vertices, edges = result
                self.raycasted_objects.append([vertices, edges])

        for object_data in self.raycasted_objects:
            vertices, edges = object_data
            for edge in edges:
                start_vertex = (int(vertices[edge[0]].x), int(vertices[edge[0]].y))
                end_vertex = (int(vertices[edge[1]].x), int(vertices[edge[1]].y))
                pygame.draw.line(screen, (255, 255, 255), start_vertex, end_vertex, 2)