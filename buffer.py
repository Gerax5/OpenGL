import glm

from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

from numpy import array, float32

class Buffer(object):
    def __init__(self,data):
        
        self.vertBuffer = array(data, float32)

        # Vertex Buffer Object
        self.VBO = glGenBuffers(1)

        # Vertex Array Object
        self.VAO = glGenVertexArrays(1)

    def Render(self):
        
        # Atar los buffer object a la tarjeta de video
        glBindBuffer(GL_ARRAY_BUFFER,self.VBO)
        glBindVertexArray(self.VAO)

        #Mandar la informacion de evrtices
        glBufferData(GL_ARRAY_BUFFER,                 # Buffer ID
                     self.vertBuffer.nbytes,          # Buffer size in bytes
                     self.vertBuffer,                 # Buffer data
                     GL_STATIC_DRAW)                  # Usage

        # Atributos

        # Atributo de posiciones
        glVertexAttribPointer(0,                                  # Atribute number
                              3,                                  # Size data
                              GL_FLOAT,                           # Type
                              GL_FALSE,                           # is it normalized
                              4 * 8,                              # Stride size bytes
                              ctypes.c_void_p(0))                # Offset

        glEnableVertexAttribArray(0)

        # Atributo de coordenadas de textura
        glVertexAttribPointer(1,                                  # Atribute number
                              2,                                  # Size data
                              GL_FLOAT,                           # Type
                              GL_FALSE,                           # is it normalized
                              4 * 8,                              # Stride size bytes
                              ctypes.c_void_p(4*3))                # Offset

        glEnableVertexAttribArray(1)

        # Atributo de coordenadas de normales
        glVertexAttribPointer(2,                                  # Atribute number
                              3,                                  # Size data
                              GL_FLOAT,                           # Type
                              GL_FALSE,                           # is it normalized
                              4 * 8,                              # Stride size bytes
                              ctypes.c_void_p(4*5))                # Offset

        glEnableVertexAttribArray(2)



        glDrawArrays(GL_TRIANGLES, 0,int(len(self.vertBuffer) / 8))