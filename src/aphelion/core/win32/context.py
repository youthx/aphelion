import time
import ctypes
from ctypes import windll, POINTER, byref, c_int, c_void_p
from aphelion.core.win32.pfd import PIXELFORMATDESCRIPTOR

gdi32 = windll.gdi32
wgl = windll.opengl32

PFD_DRAW_TO_WINDOW = 0x00000004
PFD_SUPPORT_OPENGL = 0x00000020
PFD_DOUBLEBUFFER = 0x00000001
PFD_TYPE_RGBA = 0
PFD_MAIN_PLANE = 0

wgl.wglCreateContext.restype = c_void_p
wgl.wglCreateContext.argtypes = [c_void_p]
wgl.wglMakeCurrent.restype = c_int
wgl.wglMakeCurrent.argtypes = [c_void_p, c_void_p]
wgl.wglDeleteContext.restype = c_int
wgl.wglDeleteContext.argtypes = [c_void_p]
wgl.wglGetCurrentContext.restype = ctypes.c_void_p
    
def is_opengl_context_active() -> bool:
    return bool(wgl.wglGetCurrentContext())

def create_opengl_context(hdc):
    while is_opengl_context_active():
        wgl.wglMakeCurrent(None, None)
        wgl.wglDeleteContext(wgl.wglGetCurrentContext())
    
    pfd = PIXELFORMATDESCRIPTOR()
    pfd.nSize = ctypes.sizeof(PIXELFORMATDESCRIPTOR)
    pfd.nVersion = 1
    pfd.dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER
    pfd.iPixelType = PFD_TYPE_RGBA
    pfd.cColorBits = 32
    pfd.cDepthBits = 24
    pfd.cStencilBits = 8
    pfd.iLayerType = PFD_MAIN_PLANE

    fmt = gdi32.ChoosePixelFormat(hdc, byref(pfd))
    if not fmt or not gdi32.SetPixelFormat(hdc, fmt, byref(pfd)):
        raise ctypes.WinError()

    time.sleep(0.1)
    ctx = wgl.wglCreateContext(hdc)
    if not ctx or not wgl.wglMakeCurrent(hdc, ctx):
        if ctx:
            wgl.wglDeleteContext(ctx)
        raise RuntimeError("Failed to create or activate OpenGL context")

    return ctx

def delete_opengl_context(ctx):
    wgl.wglMakeCurrent(None, None)
    if not wgl.wglDeleteContext(ctx):
        raise ctypes.WinError()
