
import ctypes
import numpy as np

from aphelion.core.opengl.constants import GL_ARRAY_BUFFER, GL_FALSE, GL_FLOAT, GL_STATIC_DRAW, GL_TRIANGLES
from aphelion.core.opengl.functions import _glBindBuffer, _glBindVertexArray, _glBufferData, _glDeleteBuffers, _glDeleteVertexArrays, _glDrawArrays, _glEnableVertexAttribArray, _glGenVertexArrays, _glGenBuffers, _glVertexAttribPointer
from aphelion.shaders.shader import ShaderProgram


class Mesh:
    def __init__(self, vertices: np.ndarray, shader: ShaderProgram, usage=GL_STATIC_DRAW):
        self.shader = shader 
        self.vertex_count = len(vertices) // 4
        self.vao = _glGenVertexArrays(1)[0]
        self.vbo = _glGenBuffers(1)[0]
        
        _glBindVertexArray(self.vao)
        _glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        _glBufferData(GL_ARRAY_BUFFER,bytes(vertices), usage)
        
        _glEnableVertexAttribArray(0)
        _glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(0))
        
        _glEnableVertexAttribArray(1)
        _glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(8))
        
        _glBindBuffer(GL_ARRAY_BUFFER, 0)
        _glBindVertexArray(0)
        
    def render(self):
        self.shader.use()
        _glBindVertexArray(self.vao)
        _glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)
        _glBindVertexArray(0)
        
    def delete(self):
        _glDeleteBuffers(1, [self.vbo])
        _glDeleteVertexArrays(1, [self.vao])
        

            
class Quad(Mesh):
    def __init__(self, shader):
        vertices = np.array([
            # x, y, u, v
            -0.5, -0.5, 0.0, 0.0,
             0.5, -0.5, 1.0, 0.0,
             0.5,  0.5, 1.0, 1.0,

             0.5,  0.5, 1.0, 1.0,
            -0.5,  0.5, 0.0, 1.0,
            -0.5, -0.5, 0.0, 0.0,
        ], dtype=np.float32)

        super().__init__(vertices, shader)
