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



# rend.scene.append(Buffer(triangle))
faceModel = Model("OBJ/banan.obj")
faceModel.AddTexture("texture/banan.bmp")
faceModel.translation.z = -5
faceModel.translation.y = -1
faceModel.scale.x = 2
faceModel.scale.y = 2
faceModel.scale.z = 2


rend.scene.append(faceModel)

isRunning = True

vShader = vertex_shader
fShader = fragment_shader
rend.SetShaders(vShader, fShader)

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

            #Vertex shader
            elif event.key == pygame.K_3:
                vShader = vertex_shader
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_4:
                vShader = fat_shader
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_5:
                vShader = water_shader
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_KP_1:
                vShader = wave_shader
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_KP_2:
                vShader = cut_shader
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_KP_3:
                vShader = anormal_shader
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_KP_4:
                vShader = ondulation_shader
                rend.SetShaders(vShader, fShader)
            


            #fragment_Shader
            elif event.key == pygame.K_6:
                fShader = fragment_shader
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_7:
                fShader = negative_shader
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_KP_9:
                fShader = pixel_shader
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_KP_8:
                fShader = fragment_noise
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_KP_7:
                fShader = fragment_dissolved_pattern
                rend.SetShaders(vShader, fShader)
            elif event.key == pygame.K_KP_6:
                fShader = fragment_hologram
                rend.SetShaders(vShader, fShader)


                



    if keys[K_LEFT]:
        rend.pointLight.x -= 1

    if keys[K_RIGHT]:
        rend.pointLight.x += 1

    if keys[K_UP]:
        rend.pointLight.z -= 1

    if keys[K_DOWN]:
        rend.pointLight.z += 1
    
    if keys[K_PAGEUP]:
        rend.pointLight.y += 1

    if keys[K_PAGEDOWN]:
        rend.pointLight.y -= 1

    if keys[K_a]:
        rend.camera.position.x -= 1 * deltaTime

    if keys[K_d]:
        rend.camera.position.x += 1 * deltaTime

    if keys[K_s]:
        rend.camera.position.y -= 1 * deltaTime

    if keys[K_w]:
        rend.camera.position.y += 1 * deltaTime



    rend.time += deltaTime

        


    # print(deltaTime)


    rend.Render()

    pygame.display.flip()

pygame.quit()