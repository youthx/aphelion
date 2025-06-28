# win32/pfd.py
import ctypes
from ctypes import wintypes

class PIXELFORMATDESCRIPTOR(ctypes.Structure):
    _fields_ = [
        ("nSize",        wintypes.WORD),
        ("nVersion",     wintypes.WORD),
        ("dwFlags",      wintypes.DWORD),
        ("iPixelType",   ctypes.c_byte),
        ("cColorBits",   ctypes.c_byte),
        ("cRedBits",     ctypes.c_byte),
        ("cRedShift",    ctypes.c_byte),
        ("cGreenBits",   ctypes.c_byte),
        ("cGreenShift",  ctypes.c_byte),
        ("cBlueBits",    ctypes.c_byte),
        ("cBlueShift",   ctypes.c_byte),
        ("cAlphaBits",   ctypes.c_byte),
        ("cAlphaShift",  ctypes.c_byte),
        ("cAccumBits",   ctypes.c_byte),
        ("cAccumRedBits",ctypes.c_byte),
        ("cAccumGreenBits",ctypes.c_byte),
        ("cAccumBlueBits",ctypes.c_byte),
        ("cAccumAlphaBits",ctypes.c_byte),
        ("cDepthBits",   ctypes.c_byte),
        ("cStencilBits", ctypes.c_byte),
        ("cAuxBuffers",  ctypes.c_byte),
        ("iLayerType",   ctypes.c_byte),
        ("bReserved",    ctypes.c_byte),
        ("dwLayerMask",  wintypes.DWORD),
        ("dwVisibleMask",wintypes.DWORD),
        ("dwDamageMask", wintypes.DWORD),
    ]
