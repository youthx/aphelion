import ctypes
from aphelion.core.win32 import opengl as _gl

# === Raw OpenGL function bindings ===


def bind(name, restype=None, argtypes=()):
    return _gl.load_function(name, restype, argtypes)

# Function pointer container to track load state


def init_gl_functions():
    global _glClearColor_core, _glClear_core, _glViewport_core, _glEnable_core, _glDisable_core
    global _glGenBuffers_core, _glBindBuffer_core, _glBufferData_core
    global _glCreateShader_core, _glShaderSource_core, _glCompileShader_core
    global _glGetShaderiv_core, _glGetShaderInfoLog_core
    global _glCreateProgram_core, _glAttachShader_core, _glLinkProgram_core
    global _glGetProgramiv_core, _glGetProgramInfoLog_core, _glUseProgram_core
    global _glGetUniformLocation_core, _glUniformMatrix4fv_core
    global _glDeleteShader_core, _glDeleteProgram_core
    global _glGenVertexArrays_core, _glBindVertexArray_core
    global _glEnableVertexAttribArray_core, _glVertexAttribPointer_core
    global _glDrawArrays_core, _glDrawElements_core

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
    _glEnableVertexAttribArray_core = bind(
        "glEnableVertexAttribArray", None, [ctypes.c_uint])
    _glVertexAttribPointer_core = bind("glVertexAttribPointer", None, [
                                       ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_ubyte, ctypes.c_int, ctypes.c_void_p])
    _glDrawArrays_core = bind("glDrawArrays", None, [
                              ctypes.c_uint, ctypes.c_int, ctypes.c_int])
    _glDrawElements_core = bind("glDrawElements", None, [
                                ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_void_p])

# === Pythonic wrapper functions ===


def _glClearColor(r, g, b, a): _glClearColor_core(
    float(r), float(g), float(b), float(a))


def _glClear(mask): _glClear_core(int(mask))
def _glViewport(x, y, w, h): _glViewport_core(int(x), int(y), int(w), int(h))
def _glEnable(cap): _glEnable_core(int(cap))
def _glDisable(cap): _glDisable_core(int(cap))
def _glGenBuffers(n): arr = (
    ctypes.c_uint * n)(); _glGenBuffers_core(n, arr); return list(arr)


def _glBindBuffer(target, buf): _glBindBuffer_core(int(target), int(buf))


def _glBufferData(target, data, usage):
    if isinstance(data, bytes):
        size, ptr = len(data), ctypes.c_char_p(data)
    elif hasattr(data, '_length_'):
        size, ptr = ctypes.sizeof(data), ctypes.byref(data)
    else:
        raise TypeError("Invalid data type")
    _glBufferData_core(int(target), size, ptr, int(usage))


def _glCreateShader(t): return _glCreateShader_core(int(t))


def _glShaderSource(shader, src):
    encoded = src.encode("utf-8")
    ptr = ctypes.c_char_p(encoded)
    length = ctypes.c_int(len(encoded))
    _glShaderSource_core(int(shader), 1, ctypes.byref(ptr),
                         ctypes.byref(length))


def _glCompileShader(shader): _glCompileShader_core(int(shader))


def _glGetShaderiv(shader, pname): val = ctypes.c_int(); _glGetShaderiv_core(
    int(shader), int(pname), ctypes.byref(val)); return val.value


def _glGetShaderInfoLog(shader):
    log_len = _glGetShaderiv(shader, 0x8B84)
    if not log_len:
        return ""
    buf = ctypes.create_string_buffer(log_len)
    _glGetShaderInfoLog_core(shader, log_len, None, buf)
    return buf.value.decode()


def _glCreateProgram(): return _glCreateProgram_core()
def _glAttachShader(prog, shader): _glAttachShader_core(int(prog), int(shader))
def _glLinkProgram(prog): _glLinkProgram_core(int(prog))


def _glGetProgramiv(prog, pname): val = ctypes.c_int(); _glGetProgramiv_core(
    int(prog), int(pname), ctypes.byref(val)); return val.value


def _glGetProgramInfoLog(prog):
    log_len = _glGetProgramiv(prog, 0x8B84)
    if not log_len:
        return ""
    buf = ctypes.create_string_buffer(log_len)
    _glGetProgramInfoLog_core(prog, log_len, None, buf)
    return buf.value.decode()


def _glUseProgram(prog): _glUseProgram_core(int(prog))


def _glGetUniformLocation(prog, name): return _glGetUniformLocation_core(
    int(prog), name.encode("utf-8"))
def _glUniformMatrix4fv(loc, count, trans, val): _glUniformMatrix4fv_core(
    int(loc), int(count), int(trans), val)


def _glDeleteShader(shader): _glDeleteShader_core(int(shader))
def _glDeleteProgram(prog): _glDeleteProgram_core(int(prog))
def _glGenVertexArrays(n): arr = (
    ctypes.c_uint * n)(); _glGenVertexArrays_core(n, arr); return list(arr)


def _glBindVertexArray(arr): _glBindVertexArray_core(int(arr))


def _glEnableVertexAttribArray(
    index): _glEnableVertexAttribArray_core(int(index))


def _glVertexAttribPointer(index, size, typ, norm, stride, ptr): _glVertexAttribPointer_core(
    int(index), int(size), int(typ), int(norm), int(stride), ptr)


def _glDrawArrays(mode, first, count): _glDrawArrays_core(
    int(mode), int(first), int(count))


def _glDrawElements(mode, count, typ, indices): _glDrawElements_core(
    int(mode), int(count), int(typ), indices)
