import ctypes
from ctypes import wintypes

# Basic Windows handle types as aliases for wintypes handles.
# Some may be missing depending on Python version, so fallback to HANDLE.
HWND = wintypes.HWND
HINSTANCE = wintypes.HANDLE
HDC = wintypes.HANDLE
HGLRC = wintypes.HANDLE
HRGN = wintypes.HANDLE

try:
    HICON = wintypes.HICON
except AttributeError:
    HICON = wintypes.HANDLE

try:
    HCURSOR = wintypes.HCURSOR
except AttributeError:
    HCURSOR = wintypes.HANDLE

try:
    HBRUSH = wintypes.HBRUSH
except AttributeError:
    HBRUSH = wintypes.HANDLE

HMODULE = wintypes.HANDLE

# Integer types
DWORD = wintypes.DWORD
UINT = wintypes.UINT
WORD = wintypes.WORD
BYTE = wintypes.BYTE
LONG = wintypes.LONG
BOOL = wintypes.BOOL

# WPARAM, LPARAM, LRESULT depend on pointer size (32 or 64 bit)
if ctypes.sizeof(ctypes.c_void_p) == 8:
    WPARAM = ctypes.c_ulonglong  # 64-bit unsigned
    LPARAM = ctypes.c_longlong   # 64-bit signed
    LRESULT = ctypes.c_longlong
else:
    WPARAM = ctypes.c_ulong      # 32-bit unsigned
    LPARAM = ctypes.c_long       # 32-bit signed
    LRESULT = ctypes.c_long

# Window procedure callback type
WNDPROCTYPE = ctypes.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)
wintypes.WNDPROC = WNDPROCTYPE  # attach for convenience

# WNDCLASS structure (for RegisterClass/Ex)
class WNDCLASS(ctypes.Structure):
    _fields_ = [
        ("style", wintypes.UINT),
        ("lpfnWndProc", wintypes.WNDPROC),
        ("cbClsExtra", ctypes.c_int),
        ("cbWndExtra", ctypes.c_int),
        ("hInstance", HINSTANCE),
        ("hIcon", HICON),
        ("hCursor", HCURSOR),
        ("hbrBackground", HBRUSH),
        ("lpszMenuName", wintypes.LPCWSTR),
        ("lpszClassName", wintypes.LPCWSTR),
    ]

# MSG structure for message retrieval loop
class MSG(ctypes.Structure):
    _fields_ = [
        ("hwnd", HWND),
        ("message", UINT),
        ("wParam", WPARAM),
        ("lParam", LPARAM),
        ("time", DWORD),
        ("pt", wintypes.POINT),
    ]
