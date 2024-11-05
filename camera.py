import glm

from math import sin, cos, radians


class Camera(object):
    def __init__(self, width, height):
        self.position = glm.vec3(0,0,0)
        self.rotation = glm.vec3(0,0,0)

        self.screenWidth = width
        self.screenHeight = height

        self.usingLookAt = False

        self.CreateProjectionMatrix(60, 0.1, 1000)

    def GetViewMatrix(self):
        identity = glm.mat4(1)

        if not self.usingLookAt:
            translateMat = glm.translate(identity, self.position)

            pitchMat = glm.rotate(identity, glm.radians(self.rotation.x), glm.vec3(1,0,0))
            yawMat = glm.rotate(identity, glm.radians(self.rotation.y), glm.vec3(0,1,0))
            rollMat = glm.rotate(identity, glm.radians(self.rotation.z), glm.vec3(0,0,1))

            rotationMat = pitchMat * yawMat * rollMat

            camMat = translateMat * rotationMat

            self.viewMatrix = glm.inverse(camMat)

        self.usingLookAt = False

        return self.viewMatrix
    
    def GetProjectionMatrix(self):
        return self.projectionMatrix
    
    def CreateProjectionMatrix(self, fov, nearPlane, farPlane):
        self.projectionMatrix = glm.perspective(glm.radians(fov),self.screenWidth/self.screenHeight, nearPlane, farPlane)

    def LookAt(self, center):
        self.usingLookAt = True
        self.viewMatrix = glm.lookAt(self.position, center, glm.vec3(0,1,0))

    def Orbit(self, center, distance, angle):
        self.position.x = center.x + sin( radians(angle) ) * distance
        self.position.z = center.z + cos( radians(angle) ) * distance
    
    def vertical(self, center, distance, angle):
        self.position.y = center.y + distance * sin(radians(angle))

        
