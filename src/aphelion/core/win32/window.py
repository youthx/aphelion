import time
import ctypes
from ctypes import windll, wintypes
from aphelion.core.win32.types import WNDPROCTYPE, WNDCLASS, WPARAM, LPARAM, LRESULT, HWND, UINT, HCURSOR
from aphelion.core.win32.context import create_opengl_context, delete_opengl_context

user32, kernel32, gdi32 = windll.user32, windll.kernel32, windll.gdi32

user32.DefWindowProcW.restype = LRESULT
user32.DefWindowProcW.argtypes = [HWND, UINT, WPARAM, LPARAM]
user32.DestroyWindow.argtypes = [HWND]
user32.ReleaseDC.argtypes = [HWND, wintypes.HDC]
user32.ShowWindow.argtypes = [HWND, ctypes.c_int]
user32.PeekMessageW.argtypes = [ctypes.POINTER(wintypes.MSG), HWND, UINT, UINT, UINT]
user32.TranslateMessage.argtypes = [ctypes.POINTER(wintypes.MSG)]
user32.DispatchMessageW.argtypes = [ctypes.POINTER(wintypes.MSG)]

WS_OVERLAPPEDWINDOW = 0x00CF0000
IDC_ARROW, SW_SHOW = 32512, 1
PM_REMOVE, WM_CLOSE, CS_OWNDC = 0x0001, 0x0010, 0x0020


def create_opengl_context_with_retry(hdc, retries=5, delay=0.2):
    last_error = ""
    for i in range(retries):
        try:
            if i: time.sleep(delay)
            ctx = create_opengl_context(hdc)
            print("[INFO] OpenGL context created.")
            return ctx
        except RuntimeError as e:
            last_error = str(e)
            print(f"[WARN] Retry {i}: {last_error}")
            if "wglCreateContext failed" in last_error or "SetPixelFormat failed" in last_error:
                continue
            raise
    raise RuntimeError(f"Failed after {retries} retries: {last_error}")


class _Win32Window:
    _class_registered = False
    _hwnd_instance_map = {}

    def __init__(self, width=800, height=600, title="Aphelion", class_name="AphelionWindowInstance"):
        
        self.hInstance = kernel32.GetModuleHandleW(None)
        self.class_name = class_name
        self.hwnd = self.hdc = self.hglrc = None
        self.exit_requested = False

        if not _Win32Window._class_registered:
            wc = WNDCLASS()
            wc.style, wc.lpfnWndProc = CS_OWNDC, _Win32Window._static_wnd_proc
            wc.hInstance = self.hInstance
            wc.hCursor = user32.LoadCursorW(None, IDC_ARROW)
            wc.lpszClassName = self.class_name
            if not user32.RegisterClassW(ctypes.byref(wc)):
                raise ctypes.WinError()
            _Win32Window._class_registered = True

        self.hwnd = user32.CreateWindowExW(
            0, self.class_name, title, WS_OVERLAPPEDWINDOW,
            100, 100, width, height,
            None, None, self.hInstance, None
        )
        if not self.hwnd:
            raise ctypes.WinError()

        _Win32Window._hwnd_instance_map[self.hwnd] = self

        self.hdc = user32.GetDC(self.hwnd)
        if not self.hdc:
            user32.DestroyWindow(self.hwnd)
            del _Win32Window._hwnd_instance_map[self.hwnd]
            raise ctypes.WinError()

        ctypes.set_last_error(0)

        try:
            self.hglrc = create_opengl_context_with_retry(self.hdc)
        except Exception as e:
            print(f"[ERROR] OpenGL context failed: {e}")
            self._cleanup()
            raise

        user32.ShowWindow(self.hwnd, SW_SHOW)
        user32.UpdateWindow(self.hwnd)
        time.sleep(0.1)

    @staticmethod
    @WNDPROCTYPE
    def _static_wnd_proc(hwnd, msg, wParam, lParam):
        inst = _Win32Window._hwnd_instance_map.get(hwnd)
        return inst._wnd_proc(hwnd, msg, WPARAM(wParam), LPARAM(lParam)) if inst else user32.DefWindowProcW(hwnd, msg, wParam, lParam)

    def _wnd_proc(self, hwnd, msg, wParam, lParam):
        if msg == WM_CLOSE:
            self.exit_requested = True
            user32.PostQuitMessage(0)
            return 0
        return user32.DefWindowProcW(hwnd, msg, wParam, lParam)

    def poll_events(self):
        msg = wintypes.MSG()
        while user32.PeekMessageW(ctypes.byref(msg), None, 0, 0, PM_REMOVE):
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))

    def swap_buffers(self):
        if not gdi32.SwapBuffers(self.hdc):
            raise ctypes.WinError()

    def close(self):
        self._cleanup()

    def _cleanup(self):
        if self.hglrc:
            try: delete_opengl_context(self.hglrc)
            except Exception as e: print(f"[WARN] Failed to delete GL ctx: {e}")
            self.hglrc = None

        if self.hdc and self.hwnd:
            try: user32.ReleaseDC(self.hwnd, self.hdc)
            except Exception as e: print(f"[WARN] Failed to release DC: {e}")
            self.hdc = None

        if self.hwnd:
            try: user32.DestroyWindow(self.hwnd)
            except Exception as e: print(f"[WARN] Failed to destroy window: {e}")
            _Win32Window._hwnd_instance_map.pop(self.hwnd, None)
            self.hwnd = None

    def __del__(self):
        try:
            if self.hglrc:
                delete_opengl_context(self.hglrc)
                self.hglrc = None
        except: pass

        try:
            if self.hdc and self.hwnd:
                user32.ReleaseDC(self.hwnd, self.hdc)
                self.hdc = None
        except: pass

        try:
            if self.hwnd:
                user32.DestroyWindow(self.hwnd)
                _Win32Window._hwnd_instance_map.pop(self.hwnd, None)
                self.hwnd = None
        except: pass
