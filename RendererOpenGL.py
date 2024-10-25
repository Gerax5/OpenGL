import pygame
from pygame.locals import *
from gl import *
from shaders import *
from model import *

width = 960
height = 540

pygame.init()


screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.SetShaders(vertex_shader, fragment_shader)

# rend.scene.append(Buffer(triangle))
faceModel = Model("OBJ/model.obj")
faceModel.AddTexture("texture/model.bmp")
faceModel.rotation.y = 180

rend.scene.append(faceModel)

isRunning = True

while isRunning:

    deltaTime = clock.tick(60) / 1000

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            elif event.key == pygame.K_1:
                rend.FilledMode()
            elif event.key == pygame.K_2:
                rend.WireframeMode()

    if keys[K_LEFT]:
        faceModel.rotation.y -= 10 * deltaTime

    if keys[K_RIGHT]:
        faceModel.rotation.y += 10 * deltaTime


    rend.time += deltaTime

        


    # print(deltaTime)


    rend.Render()

    pygame.display.flip()

pygame.quit()