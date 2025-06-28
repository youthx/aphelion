from aphelion.core.opengl.functions import (
    _glCreateShader, _glDeleteProgram, _glShaderSource, _glCompileShader,
    _glGetShaderiv, _glGetShaderInfoLog, _glCreateProgram,
    _glAttachShader, _glLinkProgram, _glGetProgramiv,
    _glGetProgramInfoLog, _glDeleteShader, _glUseProgram,
)
from aphelion.core.opengl.constants import (
    GL_VERTEX_SHADER, GL_FRAGMENT_SHADER, GL_COMPILE_STATUS,
    GL_LINK_STATUS
)

class ShaderCompilationError(Exception): pass 
class ShaderLinkError(Exception): pass 

class ShaderProgram(object):
    def __init__(self, vertex_src: str, fragment_src: str):
        self.vertex_shader = self.compileShader(vertex_src, GL_VERTEX_SHADER)
        self.fragment_shader = self.compileShader(fragment_src, GL_FRAGMENT_SHADER)
        self.program = self.link(self.vertex_shader, self.fragment_shader)
        
    def compileShader(self, src: str, shader_type):
        shader = _glCreateShader(shader_type)
        _glShaderSource(shader, src)
        _glCompileShader(shader)
        
        if not _glGetShaderiv(shader, GL_COMPILE_STATUS):
            msg = _glGetShaderInfoLog(shader)
            raise ShaderCompilationError(f"Shader Compilation Error:\n{msg}")
        return shader 
    
    def link(self, vertex_shader, fragment_shader):
        program = _glCreateProgram()
        _glAttachShader(program, vertex_shader)
        _glAttachShader(program, fragment_shader)
        _glLinkProgram(program)
        
        if not _glGetProgramiv(program, GL_LINK_STATUS):
            msg = _glGetProgramInfoLog(program)
            raise ShaderLinkError(f"Program Linkage Error:\n{msg}")
        
        _glDeleteShader(vertex_shader)
        _glDeleteShader(fragment_shader)
        return program 
    
    def use(self):
        _glUseProgram(self.program)
            
    def unuse(self):
        _glUseProgram(0)
    
    def delete(self):
        _glDeleteProgram(self.program)
        
