# aphelion/core/opengl/__init__.py

from .functions import(   # List public API functions here if you want explicit control
    _glClearColor, _glClear, _glViewport, _glEnable, _glDisable,
    _glGenBuffers, _glBindBuffer, _glBufferData, _glCreateShader,
    _glShaderSource, _glCompileShader, _glGetShaderiv, _glGetShaderInfoLog,
    _glCreateProgram, _glAttachShader, _glLinkProgram, _glGetProgramiv,
    _glGetProgramInfoLog, _glUseProgram, _glGetUniformLocation,
    _glUniformMatrix4fv, _glDeleteShader, _glDeleteProgram,
    _glGenVertexArrays, _glBindVertexArray, _glEnableVertexAttribArray,
    _glVertexAttribPointer, _glDrawArrays, _glDrawElements,
)

__all__ = [
    # List public API functions here if you want explicit control
    _glClearColor, _glClear, _glViewport, _glEnable, _glDisable,
    _glGenBuffers, _glBindBuffer, _glBufferData, _glCreateShader,
    _glShaderSource, _glCompileShader, _glGetShaderiv, _glGetShaderInfoLog,
    _glCreateProgram, _glAttachShader, _glLinkProgram, _glGetProgramiv,
    _glGetProgramInfoLog, _glUseProgram, _glGetUniformLocation,
    _glUniformMatrix4fv, _glDeleteShader, _glDeleteProgram,
    _glGenVertexArrays, _glBindVertexArray, _glEnableVertexAttribArray,
    _glVertexAttribPointer, _glDrawArrays, _glDrawElements,
]
