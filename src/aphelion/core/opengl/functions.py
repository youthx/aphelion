import ctypes
from aphelion.core.win32 import opengl as _gl

# === Raw OpenGL function bindings ===

def bind(name, restype=None, argtypes=()):
    """Bind a raw OpenGL function by name."""
    return _gl.load_function(name, restype, argtypes)

# === Function pointer container ===

_glClearColor_core = None
_glClear_core = None
_glViewport_core = None
_glEnable_core = None
_glDisable_core = None
_glGenBuffers_core = None
_glBindBuffer_core = None
_glBufferData_core = None
_glDeleteBuffers_core = None
_glCreateShader_core = None
_glShaderSource_core = None
_glCompileShader_core = None
_glGetShaderiv_core = None
_glGetShaderInfoLog_core = None
_glCreateProgram_core = None
_glAttachShader_core = None
_glLinkProgram_core = None
_glGetProgramiv_core = None
_glGetProgramInfoLog_core = None
_glUseProgram_core = None
_glGetUniformLocation_core = None
_glUniformMatrix4fv_core = None
_glDeleteShader_core = None
_glDeleteProgram_core = None
_glGenVertexArrays_core = None
_glBindVertexArray_core = None
_glDeleteVertexArrays_core = None
_glEnableVertexAttribArray_core = None
_glDisableVertexAttribArray_core = None
_glVertexAttribPointer_core = None
_glDrawArrays_core = None
_glDrawElements_core = None
_glActiveTexture_core = None
_glGenTextures_core = None
_glBindTexture_core = None
_glTexParameteri_core = None
_glTexImage2D_core = None
_glDeleteTextures_core = None

def init_gl_functions():
    """Load all required OpenGL function pointers."""
    global _glClearColor_core, _glClear_core, _glViewport_core, _glEnable_core, _glDisable_core
    global _glGenBuffers_core, _glBindBuffer_core, _glBufferData_core, _glDeleteBuffers_core
    global _glCreateShader_core, _glShaderSource_core, _glCompileShader_core
    global _glGetShaderiv_core, _glGetShaderInfoLog_core
    global _glCreateProgram_core, _glAttachShader_core, _glLinkProgram_core
    global _glGetProgramiv_core, _glGetProgramInfoLog_core, _glUseProgram_core
    global _glGetUniformLocation_core, _glUniformMatrix4fv_core
    global _glDeleteShader_core, _glDeleteProgram_core
    global _glGenVertexArrays_core, _glBindVertexArray_core, _glDeleteVertexArrays_core
    global _glEnableVertexAttribArray_core, _glDisableVertexAttribArray_core, _glVertexAttribPointer_core
    global _glDrawArrays_core, _glDrawElements_core
    global _glActiveTexture_core, _glGenTextures_core, _glBindTexture_core
    global _glTexParameteri_core, _glTexImage2D_core, _glDeleteTextures_core

    _glClearColor_core = bind("glClearColor", None, [ctypes.c_float]*4)
    _glClear_core = bind("glClear", None, [ctypes.c_uint])
    _glViewport_core = bind("glViewport", None, [ctypes.c_int]*4)
    _glEnable_core = bind("glEnable", None, [ctypes.c_uint])
    _glDisable_core = bind("glDisable", None, [ctypes.c_uint])
    _glGenBuffers_core = bind("glGenBuffers", None, [
        ctypes.c_int, ctypes.POINTER(ctypes.c_uint)])
    _glBindBuffer_core = bind("glBindBuffer", None, [
        ctypes.c_uint, ctypes.c_uint])
    _glBufferData_core = bind("glBufferData", None, [
        ctypes.c_uint, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_uint])
    _glDeleteBuffers_core = bind("glDeleteBuffers", None, [
        ctypes.c_int, ctypes.POINTER(ctypes.c_uint)])
    _glCreateShader_core = bind(
        "glCreateShader", ctypes.c_uint, [ctypes.c_uint])
    _glShaderSource_core = bind("glShaderSource", None, [
        ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_int)])
    _glCompileShader_core = bind("glCompileShader", None, [ctypes.c_uint])
    _glGetShaderiv_core = bind("glGetShaderiv", None, [
        ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int)])
    _glGetShaderInfoLog_core = bind("glGetShaderInfoLog", None, [
        ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p])
    _glCreateProgram_core = bind("glCreateProgram", ctypes.c_uint)
    _glAttachShader_core = bind("glAttachShader", None, [
        ctypes.c_uint, ctypes.c_uint])
    _glLinkProgram_core = bind("glLinkProgram", None, [ctypes.c_uint])
    _glGetProgramiv_core = bind("glGetProgramiv", None, [
        ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int)])
    _glGetProgramInfoLog_core = bind("glGetProgramInfoLog", None, [
        ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p])
    _glUseProgram_core = bind("glUseProgram", None, [ctypes.c_uint])
    _glGetUniformLocation_core = bind("glGetUniformLocation", ctypes.c_int, [
        ctypes.c_uint, ctypes.c_char_p])
    _glUniformMatrix4fv_core = bind("glUniformMatrix4fv", None, [
        ctypes.c_int, ctypes.c_int, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_float)])
    _glDeleteShader_core = bind("glDeleteShader", None, [ctypes.c_uint])
    _glDeleteProgram_core = bind("glDeleteProgram", None, [ctypes.c_uint])
    _glGenVertexArrays_core = bind("glGenVertexArrays", None, [
        ctypes.c_int, ctypes.POINTER(ctypes.c_uint)])
    _glBindVertexArray_core = bind("glBindVertexArray", None, [ctypes.c_uint])
    _glDeleteVertexArrays_core = bind("glDeleteVertexArrays", None, [
        ctypes.c_int, ctypes.POINTER(ctypes.c_uint)])
    _glEnableVertexAttribArray_core = bind(
        "glEnableVertexAttribArray", None, [ctypes.c_uint])
    _glDisableVertexAttribArray_core = bind(
        "glDisableVertexAttribArray", None, [ctypes.c_uint])
    _glVertexAttribPointer_core = bind("glVertexAttribPointer", None, [
        ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_ubyte, ctypes.c_int, ctypes.c_void_p])
    _glDrawArrays_core = bind("glDrawArrays", None, [
        ctypes.c_uint, ctypes.c_int, ctypes.c_int])
    _glDrawElements_core = bind("glDrawElements", None, [
        ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_void_p])
    _glActiveTexture_core = bind("glActiveTexture", None, [ctypes.c_uint])
    _glGenTextures_core = bind("glGenTextures", None, [
        ctypes.c_int, ctypes.POINTER(ctypes.c_uint)])
    _glBindTexture_core = bind("glBindTexture", None, [
        ctypes.c_uint, ctypes.c_uint])
    _glTexParameteri_core = bind("glTexParameteri", None, [
        ctypes.c_uint, ctypes.c_uint, ctypes.c_int])
    _glTexImage2D_core = bind("glTexImage2D", None, [
        ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
        ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p])
    _glDeleteTextures_core = bind("glDeleteTextures", None, [
        ctypes.c_int, ctypes.POINTER(ctypes.c_uint)])

# === Pythonic wrapper functions ===

def _glClearColor(r, g, b, a):
    """Set the clear color."""
    if _glClearColor_core is None:
        raise RuntimeError("OpenGL function glClearColor not loaded")
    _glClearColor_core(float(r), float(g), float(b), float(a))

def _glClear(mask):
    """Clear buffers to preset values."""
    if _glClear_core is None:
        raise RuntimeError("OpenGL function glClear not loaded")
    _glClear_core(int(mask))

def _glViewport(x, y, w, h):
    """Set the viewport."""
    if _glViewport_core is None:
        raise RuntimeError("OpenGL function glViewport not loaded")
    _glViewport_core(int(x), int(y), int(w), int(h))

def _glEnable(cap):
    """Enable server-side GL capability."""
    if _glEnable_core is None:
        raise RuntimeError("OpenGL function glEnable not loaded")
    _glEnable_core(int(cap))

def _glDisable(cap):
    """Disable server-side GL capability."""
    if _glDisable_core is None:
        raise RuntimeError("OpenGL function glDisable not loaded")
    _glDisable_core(int(cap))

def _glGenBuffers(n):
    """Generate buffer object names."""
    if _glGenBuffers_core is None:
        raise RuntimeError("OpenGL function glGenBuffers not loaded")
    arr = (ctypes.c_uint * n)()
    _glGenBuffers_core(n, arr)
    return list(arr)

def _glBindBuffer(target, buf):
    """Bind a named buffer object."""
    if _glBindBuffer_core is None:
        raise RuntimeError("OpenGL function glBindBuffer not loaded")
    _glBindBuffer_core(int(target), int(buf))

def _glBufferData(target, data, usage):
    """Create and initialize a buffer object's data store."""
    if _glBufferData_core is None:
        raise RuntimeError("OpenGL function glBufferData not loaded")
    if isinstance(data, bytes):
        size = len(data)
        ptr = ctypes.c_char_p(data)
    elif hasattr(data, '_length_') or hasattr(data, 'contents'):
        size = ctypes.sizeof(data)
        ptr = ctypes.byref(data)
    else:
        raise TypeError("Invalid data type '{}' for buffer data".format(str(type(data))))
    _glBufferData_core(int(target), size, ptr, int(usage))

def _glDeleteBuffers(buffers):
    """Delete named buffer objects.
    Args:
        buffers (int or list[int]): Buffer name(s) to delete.
    """
    if _glDeleteBuffers_core is None:
        raise RuntimeError("OpenGL function glDeleteBuffers not loaded")
    if isinstance(buffers, int):
        arr = (ctypes.c_uint * 1)(buffers)
        _glDeleteBuffers_core(1, arr)
    elif isinstance(buffers, (list, tuple)):
        arr = (ctypes.c_uint * len(buffers))(*buffers)
        _glDeleteBuffers_core(len(buffers), arr)
    else:
        raise TypeError("buffers must be int or list/tuple of ints")

def _glCreateShader(t):
    """Create a shader object."""
    if _glCreateShader_core is None:
        raise RuntimeError("OpenGL function glCreateShader not loaded")
    return _glCreateShader_core(int(t))

def _glShaderSource(shader, src):
    """Replace the source code in a shader object."""
    if _glShaderSource_core is None:
        raise RuntimeError("OpenGL function glShaderSource not loaded")
    encoded = src.encode("utf-8")
    ptr = ctypes.c_char_p(encoded)
    length = ctypes.c_int(len(encoded))
    ptrs = ctypes.cast(ctypes.pointer(ptr), ctypes.POINTER(ctypes.c_char_p))
    lengths = ctypes.pointer(length)
    _glShaderSource_core(int(shader), 1, ptrs, lengths)

def _glCompileShader(shader):
    """Compile a shader object."""
    if _glCompileShader_core is None:
        raise RuntimeError("OpenGL function glCompileShader not loaded")
    _glCompileShader_core(int(shader))

def _glGetShaderiv(shader, pname):
    """Return a parameter from a shader object."""
    if _glGetShaderiv_core is None:
        raise RuntimeError("OpenGL function glGetShaderiv not loaded")
    val = ctypes.c_int()
    _glGetShaderiv_core(int(shader), int(pname), ctypes.byref(val))
    return val.value

def _glGetShaderInfoLog(shader):
    """Return the information log for a shader object."""
    if _glGetShaderInfoLog_core is None:
        raise RuntimeError("OpenGL function glGetShaderInfoLog not loaded")
    log_len = _glGetShaderiv(shader, 0x8B84)  # GL_INFO_LOG_LENGTH
    if not log_len:
        return ""
    buf = ctypes.create_string_buffer(log_len)
    _glGetShaderInfoLog_core(int(shader), log_len, None, buf)
    return buf.value.decode("utf-8", errors="replace")

def _glCreateProgram():
    """Create a program object."""
    if _glCreateProgram_core is None:
        raise RuntimeError("OpenGL function glCreateProgram not loaded")
    return _glCreateProgram_core()

def _glAttachShader(prog, shader):
    """Attach a shader object to a program object."""
    if _glAttachShader_core is None:
        raise RuntimeError("OpenGL function glAttachShader not loaded")
    _glAttachShader_core(int(prog), int(shader))

def _glLinkProgram(prog):
    """Link a program object."""
    if _glLinkProgram_core is None:
        raise RuntimeError("OpenGL function glLinkProgram not loaded")
    _glLinkProgram_core(int(prog))

def _glGetProgramiv(prog, pname):
    """Return a parameter from a program object."""
    if _glGetProgramiv_core is None:
        raise RuntimeError("OpenGL function glGetProgramiv not loaded")
    val = ctypes.c_int()
    _glGetProgramiv_core(int(prog), int(pname), ctypes.byref(val))
    return val.value

def _glGetProgramInfoLog(prog):
    """Return the information log for a program object."""
    if _glGetProgramInfoLog_core is None:
        raise RuntimeError("OpenGL function glGetProgramInfoLog not loaded")
    log_len = _glGetProgramiv(prog, 0x8B84)  # GL_INFO_LOG_LENGTH
    if not log_len:
        return ""
    buf = ctypes.create_string_buffer(log_len)
    _glGetProgramInfoLog_core(int(prog), log_len, None, buf)
    return buf.value.decode("utf-8", errors="replace")

def _glUseProgram(prog):
    """Install a program object as part of current rendering state."""
    if _glUseProgram_core is None:
        raise RuntimeError("OpenGL function glUseProgram not loaded")
    _glUseProgram_core(int(prog))

def _glGetUniformLocation(prog, name):
    """Return the location of a uniform variable."""
    if _glGetUniformLocation_core is None:
        raise RuntimeError("OpenGL function glGetUniformLocation not loaded")
    return _glGetUniformLocation_core(int(prog), name.encode("utf-8"))

def _glUniformMatrix4fv(loc, count, trans, val):
    """Specify the value of a uniform matrix variable."""
    if _glUniformMatrix4fv_core is None:
        raise RuntimeError("OpenGL function glUniformMatrix4fv not loaded")
    _glUniformMatrix4fv_core(int(loc), int(count), int(trans), val)

def _glDeleteShader(shader):
    """Delete a shader object."""
    if _glDeleteShader_core is None:
        raise RuntimeError("OpenGL function glDeleteShader not loaded")
    _glDeleteShader_core(int(shader))

def _glDeleteProgram(prog):
    """Delete a program object."""
    if _glDeleteProgram_core is None:
        raise RuntimeError("OpenGL function glDeleteProgram not loaded")
    _glDeleteProgram_core(int(prog))

def _glGenVertexArrays(n):
    """Generate vertex array object names."""
    if _glGenVertexArrays_core is None:
        raise RuntimeError("OpenGL function glGenVertexArrays not loaded")
    arr = (ctypes.c_ulong * n)()
    _glGenVertexArrays_core(n, arr)
    return arr

def _glBindVertexArray(arr):
    """Bind a vertex array object."""
    if _glBindVertexArray_core is None:
        raise RuntimeError("OpenGL function glBindVertexArray not loaded")
    #print(str(_glBindVertexArray_core.argtypes) + " " + str(type(arr)))
    _glBindVertexArray_core(arr)
    

def _glDeleteVertexArrays(arrays):
    """Delete vertex array objects.
    Args:
        arrays (int or list[int]): Vertex array name(s) to delete.
    """
    if _glDeleteVertexArrays_core is None:
        raise RuntimeError("OpenGL function glDeleteVertexArrays not loaded")
    if isinstance(arrays, int):
        arr = (ctypes.c_uint * 1)(arrays)
        _glDeleteVertexArrays_core(1, arr)
    elif isinstance(arrays, (list, tuple)):
        arr = (ctypes.c_uint * len(arrays))(*arrays)
        _glDeleteVertexArrays_core(len(arrays), arr)
    else:
        raise TypeError("arrays must be int or list/tuple of ints")

def _glEnableVertexAttribArray(index):
    """Enable a generic vertex attribute array."""
    if _glEnableVertexAttribArray_core is None:
        raise RuntimeError("OpenGL function glEnableVertexAttribArray not loaded")
    _glEnableVertexAttribArray_core(int(index))

def _glDisableVertexAttribArray(index):
    """Disable a generic vertex attribute array."""
    if _glDisableVertexAttribArray_core is None:
        raise RuntimeError("OpenGL function glDisableVertexAttribArray not loaded")
    _glDisableVertexAttribArray_core(int(index))

def _glVertexAttribPointer(index, size, typ, norm, stride, ptr):
    """Define an array of generic vertex attribute data."""
    if _glVertexAttribPointer_core is None:
        raise RuntimeError("OpenGL function glVertexAttribPointer not loaded")
    _glVertexAttribPointer_core(int(index), int(size), int(typ), int(norm), int(stride), ptr)

def _glDrawArrays(mode, first, count):
    """Render primitives from array data."""
    if _glDrawArrays_core is None:
        raise RuntimeError("OpenGL function glDrawArrays not loaded")
    _glDrawArrays_core(int(mode), int(first), int(count))

def _glDrawElements(mode, count, typ, indices):
    """Render primitives from array data with indices."""
    if _glDrawElements_core is None:
        raise RuntimeError("OpenGL function glDrawElements not loaded")
    _glDrawElements_core(int(mode), int(count), int(typ), indices)

def _glActiveTexture(texture):
    """Select active texture unit."""
    if _glActiveTexture_core is None:
        raise RuntimeError("OpenGL function glActiveTexture not loaded")
    _glActiveTexture_core(int(texture))

def _glGenTextures(n):
    """Generate texture object names."""
    if _glGenTextures_core is None:
        raise RuntimeError("OpenGL function glGenTextures not loaded")
    arr = (ctypes.c_uint * n)()
    _glGenTextures_core(n, arr)
    return list(arr)

def _glBindTexture(target, texture):
    """Bind a named texture to a texturing target."""
    if _glBindTexture_core is None:
        raise RuntimeError("OpenGL function glBindTexture not loaded")
    _glBindTexture_core(int(target), int(texture))

def _glTexParameteri(target, pname, param):
    """Set texture parameter."""
    if _glTexParameteri_core is None:
        raise RuntimeError("OpenGL function glTexParameteri not loaded")
    _glTexParameteri_core(int(target), int(pname), int(param))

def _glTexImage2D(target, level, internalformat, width, height, border, format, type_, pixels):
    """Specify a two-dimensional texture image."""
    if _glTexImage2D_core is None:
        raise RuntimeError("OpenGL function glTexImage2D not loaded")
    _glTexImage2D_core(
        int(target), int(level), int(internalformat), int(width), int(height),
        int(border), int(format), int(type_), pixels)

def _glDeleteTextures(textures):
    """Delete named textures.
    Args:
        textures (int or list[int]): Texture name(s) to delete.
    """
    if _glDeleteTextures_core is None:
        raise RuntimeError("OpenGL function glDeleteTextures not loaded")
    if isinstance(textures, int):
        arr = (ctypes.c_uint * 1)(textures)
        _glDeleteTextures_core(1, arr)
    elif isinstance(textures, (list, tuple)):
        arr = (ctypes.c_uint * len(textures))(*textures)
        _glDeleteTextures_core(len(textures), arr)
    else:
        raise TypeError("textures must be int or list/tuple of ints")
