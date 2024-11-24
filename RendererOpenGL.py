import pygame
from pygame.locals import *
from gl import *
from shaders import *
from model import *

width = 1020
height = 650

pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

pygame.mixer.music.load("audio/fondo.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

# C:\Users\Gerax\OneDrive\Desktop\UVGG\3-2\Graficas\Open\OpenGL\texture\skybox\mio\test\back.jpeg
skyboxTextureList = ["texture/skybox/mio/Proyecto/right.png",
                     "texture/skybox/mio/Proyecto/left.png",
                     "texture/skybox/mio/Proyecto/top.png",
                     "texture/skybox/mio/Proyecto/bottom.png",
                     "texture/skybox/mio/Proyecto/front.png",
                     "texture/skybox/mio/Proyecto/back.png"]

rend.CreateSkybox(skyboxTextureList, skybox_vertex_shader, skybox_fragment_shader)

# rend.scene.append(Buffer(triangle))
Banana = Model("OBJ/banan.obj")
Banana.AddTexture("texture/banan.bmp")
Banana.SetShaders(anormal_shader, fragment_dissolved_pattern)
# faceModel = Model("OBJ/model.obj")
# faceModel.AddTexture("texture/model.bmp")
Banana.translation.z = 1
Banana.translation.x = 1
Banana.scale.x = 1
Banana.scale.y = 1
Banana.scale.z = 1
Banana.rotation.y = -30

shrek = Model("OBJ/Shrek.obj")
shrek.AddTexture("texture/sss.bmp")
shrek.SetShaders(ondulation_shader, fragment_hologram)
shrek.scale.x = 0.2
shrek.scale.y = 0.2
shrek.scale.z = 0.2
shrek.translation.x = -3
shrek.translation.y = 0.5
shrek.translation.z = 0
shrek.rotation.z = -30
shrek.rotation.y = 60

# Eugene = Model("OBJ/sp.obj")
# Eugene.AddTexture("texture/lava_texture.bmp")
# shrek.SetShaders(vertex_shader, fragment_shader)
# Eugene.translation.z = -10
# Eugene.translation.y = 1
# Eugene.scale.x = 5
# Eugene.scale.y = 5
# Eugene.scale.z = 5

Planet = Model("OBJ/sp.obj")
Planet.AddTexture("texture/lava_texture.bmp")
Planet.SetShaders(wave_shader, fragment_hologram)
Planet.translation.z = 0
Planet.translation.x = 0.5
Planet.translation.y = -5
Planet.scale.x = 5
Planet.scale.y = 5
Planet.scale.z = 5


Eugene = Model("OBJ/Eugene.obj")
Eugene.AddTexture("texture/eugene.bmp")
Eugene.SetShaders(cut_shader, pixel_shader)
Eugene.translation.z = 0
Eugene.translation.x = 4
Eugene.rotation.z = 120
Eugene.scale.x = 0.15
Eugene.scale.y = 0.15
Eugene.scale.z = 0.15


pengu = Model("OBJ/Penguin.obj")
pengu.AddTexture("texture/Pen.bmp")
pengu.SetShaders(ondulation_shader, fragment_noise)
pengu.translation.z = 1
pengu.translation.y = 2
pengu.translation.x = 5
pengu.rotation.z = 120
pengu.scale.x = 1
pengu.scale.y = 1
pengu.scale.z = 1


rend.scene.append(Banana)
rend.scene.append(shrek)
rend.scene.append(Planet)
rend.scene.append(Eugene)
rend.scene.append(pengu)

isRunning = True

camDistance = 7
camAngle = 0

currentShow = 0
models = [Banana.translation, shrek.translation, Planet.translation, Eugene.translation, pengu.translation ]
sounds = {
    0: pygame.mixer.Sound("audio/gnome.mp3"),
    1: pygame.mixer.Sound("audio/s.mp3"),
    2: pygame.mixer.Sound("audio/wow.mp3"),
    3: pygame.mixer.Sound("audio/fast.mp3"),
    4: pygame.mixer.Sound("audio/bonitos.mp3"),
}

currentLookAT = models[currentShow]


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


            elif event.key == pygame.K_SPACE:
                currentShow += 1
                currentShow = currentShow % len(models)

                if currentShow in sounds:
                    sounds[currentShow].play()

                currentLookAT = models[currentShow]

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
        rend.camera.position.y += 1 * deltaTime
        rend.camera.position.y = min(rend.camera.position.y, 1)

    if keys[K_f]:
        rend.camera.position.y -= 1 * deltaTime
        rend.camera.position.y = max(rend.camera.position.y, -1)

    mouseButtons = pygame.mouse.get_pressed()

    if mouseButtons[0]:
        rel = pygame.mouse.get_rel()
        camAngle -= rel[0] * deltaTime * 10
        rend.camera.position.y -= rel[1] * deltaTime * 0.5
        rend.camera.position.y = max(rend.camera.position.y, -1)
        rend.camera.position.y = min(rend.camera.position.y, 1)

    if mouseButtons[1]:
        rel = pygame.mouse.get_rel()
        camDistance -= rel[1] * deltaTime * 0.8

    rend.time += deltaTime

    rend.camera.Orbit(currentLookAT, camDistance, camAngle)
    rend.camera.LookAt(currentLookAT)


    rend.Render()

    pygame.display.flip()

pygame.quit()