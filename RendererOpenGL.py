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


skyboxTextureList = ["texture/skybox/clase/right.jpg",
                     "texture/skybox/clase/left.jpg",
                     "texture/skybox/clase/top.jpg",
                     "texture/skybox/clase/bottom.jpg",
                     "texture/skybox/clase/front.jpg",
                     "texture/skybox/clase/back.jpg"]

rend.CreateSkybox(skyboxTextureList, skybox_vertex_shader, skybox_fragment_shader)

# rend.scene.append(Buffer(triangle))
# faceModel = Model("OBJ/banan.obj")
# faceModel.AddTexture("texture/banan.bmp")
faceModel = Model("OBJ/model.obj")
faceModel.AddTexture("texture/model.bmp")
faceModel.rotation.y = 90
faceModel.translation.z = -10
faceModel.scale.x = 1
faceModel.scale.y = 1
faceModel.scale.z = 1


rend.scene.append(faceModel)

isRunning = True

camDistance = 5
camAngle = 0
camAngleY = 0

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
        camAngle -= 45 * deltaTime

    if keys[K_d]:
        camAngle += 45 * deltaTime
    
    if keys[K_w]:
        camDistance -= 1 * deltaTime
        camDistance = max(camDistance, 1)

    if keys[K_s]:
        camDistance += 1 * deltaTime
        camDistance = min(camDistance, 9)

    if keys[K_r]:
        camAngleY += 45 * deltaTime
        camAngleY = min(camAngleY, 10)

    if keys[K_f]:
        camAngleY -= 45 * deltaTime
        camAngleY = max(camAngleY, -10)



    rend.time += deltaTime

    rend.camera.LookAt(faceModel.translation)
    rend.camera.Orbit(faceModel.translation, camDistance, camAngle, camAngleY)

        


    # print(deltaTime)


    rend.Render()

    pygame.display.flip()

pygame.quit()