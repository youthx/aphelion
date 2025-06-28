import ctypes

_opengl32 = ctypes.windll.opengl32
_wglGetProcAddress = _opengl32.wglGetProcAddress
_wglGetProcAddress.restype = ctypes.c_void_p
_wglGetProcAddress.argtypes = [ctypes.c_char_p]

def _get_proc_address(name: str) -> int | None:
    addr = _wglGetProcAddress(name.encode("ascii"))
    if addr and addr > 0x10000:
        return addr
    try:
        return ctypes.cast(getattr(_opengl32, name), ctypes.c_void_p).value
    except AttributeError:
        return None

def load_function(name: str, restype=ctypes.c_void_p, argtypes=()):
    addr = _get_proc_address(name)
    if not addr:
        raise RuntimeError(f"OpenGL function '{name}' not found.")
    func = ctypes.CFUNCTYPE(restype, *argtypes)(addr)
    func.restype, func.argtypes = restype, argtypes
    return func
