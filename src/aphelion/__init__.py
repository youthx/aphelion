import ctypes
from ctypes import wintypes, windll, byref
import sys

user32 = windll.user32
gdi32 = windll.gdi32
opengl32 = windll.opengl32
kernel32 = windll.kernel32

# Define WNDPROC type
WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)

# Constants
CS_OWNDC = 0x0020
WS_OVERLAPPEDWINDOW = 0x00CF0000
CW_USEDEFAULT = 0x80000000
PFD_DRAW_TO_WINDOW = 0x00000004
PFD_SUPPORT_OPENGL = 0x00000020
PFD_DOUBLEBUFFER = 0x00000001
PFD_TYPE_RGBA = 0
PFD_MAIN_PLANE = 0

WM_DESTROY = 2
WM_CLOSE = 0x0010

# Define PIXELFORMATDESCRIPTOR structure
class PIXELFORMATDESCRIPTOR(ctypes.Structure):
    _fields_ = [
        ('nSize', wintypes.WORD),
        ('nVersion', wintypes.WORD),
        ('dwFlags', wintypes.DWORD),
        ('iPixelType', ctypes.c_byte),
        ('cColorBits', ctypes.c_byte),
        ('cRedBits', ctypes.c_byte),
        ('cRedShift', ctypes.c_byte),
        ('cGreenBits', ctypes.c_byte),
        ('cGreenShift', ctypes.c_byte),
        ('cBlueBits', ctypes.c_byte),
        ('cBlueShift', ctypes.c_byte),
        ('cAlphaBits', ctypes.c_byte),
        ('cAlphaShift', ctypes.c_byte),
        ('cAccumBits', ctypes.c_byte),
        ('cAccumRedBits', ctypes.c_byte),
        ('cAccumGreenBits', ctypes.c_byte),
        ('cAccumBlueBits', ctypes.c_byte),
        ('cAccumAlphaBits', ctypes.c_byte),
        ('cDepthBits', ctypes.c_byte),
        ('cStencilBits', ctypes.c_byte),
        ('cAuxBuffers', ctypes.c_byte),
        ('iLayerType', ctypes.c_byte),
        ('bReserved', ctypes.c_byte),
        ('dwLayerMask', wintypes.DWORD),
        ('dwVisibleMask', wintypes.DWORD),
        ('dwDamageMask', wintypes.DWORD),
    ]

# Define WNDCLASS structure
class WNDCLASS(ctypes.Structure):
    _fields_ = [
        ("style", wintypes.UINT),
        ("lpfnWndProc", WNDPROC),
        ("cbClsExtra", ctypes.c_int),
        ("cbWndExtra", ctypes.c_int),
        ("hInstance", wintypes.HINSTANCE),
        ("hIcon", wintypes.HANDLE),
        ("hCursor", wintypes.HANDLE),
        ("hbrBackground", wintypes.HANDLE),
        ("lpszMenuName", wintypes.LPCWSTR),
        ("lpszClassName", wintypes.LPCWSTR),
    ]

@WNDPROC
def wndproc(hwnd, msg, wparam, lparam):
    if msg == WM_CLOSE or msg == WM_DESTROY:
        user32.PostQuitMessage(0)
        return 0
    return user32.DefWindowProcW(hwnd, msg, ctypes.c_ulonglong(wparam), ctypes.c_longlong(lparam))

def main():
    hInstance = kernel32.GetModuleHandleW(None)
    className = "MyOpenGLWindowClass"

    # Prepare resource IDs for icon and cursor (must be c_void_p)
    IDI_APPLICATION = ctypes.c_void_p(32512)
    IDC_ARROW = ctypes.c_void_p(32512)

    # Register window class
    wndClass = WNDCLASS()
    wndClass.style = CS_OWNDC
    wndClass.lpfnWndProc = wndproc
    wndClass.cbClsExtra = 0
    wndClass.cbWndExtra = 0
    wndClass.hInstance = hInstance
    wndClass.hIcon = user32.LoadIconW(None, IDI_APPLICATION)
    wndClass.hCursor = user32.LoadCursorW(None, IDC_ARROW)
    wndClass.hbrBackground = 0
    wndClass.lpszMenuName = None
    wndClass.lpszClassName = ctypes.c_wchar_p(className)

    if not user32.RegisterClassW(byref(wndClass)):
        print("Failed to register window class")
        sys.exit(1)

    # Create window
    hwnd = user32.CreateWindowExW(
        0,
        ctypes.c_wchar_p(className),
        "OpenGL Context Test",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        640,
        480,
        None,
        None,
        hInstance,
        None
    )
    if not hwnd:
        print("Failed to create window")
        sys.exit(1)

    user32.ShowWindow(hwnd, 1)
    user32.UpdateWindow(hwnd)

    # Get device context
    hdc = user32.GetDC(hwnd)
    if not hdc:
        print("Failed to get device context")
        sys.exit(1)

    # Setup pixel format descriptor
    pfd = PIXELFORMATDESCRIPTOR()
    pfd.nSize = ctypes.sizeof(PIXELFORMATDESCRIPTOR)
    pfd.nVersion = 1
    pfd.dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER
    pfd.iPixelType = PFD_TYPE_RGBA
    pfd.cColorBits = 32
    pfd.cDepthBits = 24
    pfd.cStencilBits = 8
    pfd.iLayerType = PFD_MAIN_PLANE

    # Choose pixel format
    pixelFormat = gdi32.ChoosePixelFormat(hdc, byref(pfd))
    if pixelFormat == 0:
        print("ChoosePixelFormat failed")
        sys.exit(1)

    # Set pixel format
    if not gdi32.SetPixelFormat(hdc, pixelFormat, byref(pfd)):
        print("SetPixelFormat failed")
        sys.exit(1)

    # Create OpenGL context
    hglrc = opengl32.wglCreateContext(hdc)
    if not hglrc:
        print("wglCreateContext failed")
        sys.exit(1)

    # Make context current
    if not opengl32.wglMakeCurrent(hdc, hglrc):
        print("wglMakeCurrent failed")
        opengl32.wglDeleteContext(hglrc)
        sys.exit(1)

    # Get OpenGL version string
    opengl32.glGetString.restype = ctypes.c_char_p
    version = opengl32.glGetString(0x1F02)  # GL_VERSION = 0x1F02
    if version:
        print("OpenGL Version:", version.decode('ascii'))
    else:
        print("Failed to get OpenGL version")

    # Simple message loop
    msg = wintypes.MSG()
    while user32.GetMessageW(byref(msg), None, 0, 0) != 0:
        user32.TranslateMessage(byref(msg))
        user32.DispatchMessageW(byref(msg))

    # Cleanup
    opengl32.wglMakeCurrent(0, 0)
    opengl32.wglDeleteContext(hglrc)
    user32.ReleaseDC(hwnd, hdc)
    user32.DestroyWindow(hwnd)
    user32.UnregisterClassW(ctypes.c_wchar_p(className), hInstance)

if __name__ == "__main__":
    main()
