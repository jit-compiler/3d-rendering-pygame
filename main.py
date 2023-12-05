import pygame
from data_classes.vector_3 import Vector3
from three.camera import Camera
from three.mesh import Mesh
from three.scene import Scene

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

camera = Camera(0, 0, -90)
scene = Scene(camera)
cube = Mesh("cube", Vector3(-30, 50, 0), 30, 30, 30)
cube2 = Mesh("cube", Vector3(30, -50, 0), 20, 50, 20)
cube3 = Mesh("cube", Vector3(15, -10, -80), 10, 10, 10)
scene.add(cube)
scene.add(cube2)
scene.add(cube3)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    scene.render(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()