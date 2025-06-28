import ctypes
import logging
from ctypes import windll, wintypes
from aphelion.core.win32.window import _Win32Window
from aphelion.core.win32.context import delete_opengl_context
from aphelion.core.opengl.functions import init_gl_functions
from aphelion.core.pipeline_manager import Passes, RenderingPipelineManager

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

class _WindowInstance(_Win32Window):
    def __init__(self, width=800, height=600, title="Aphelion"):
        super().__init__(width, height, title, f"{title}_AphelionInstance")
        self._width = width
        self._height = height
        self._title = title
        self._running = False
        self._rendering_pipeline = RenderingPipelineManager()
        

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def setActivePipeline(self, pipeline: RenderingPipelineManager):
        if not isinstance(pipeline, RenderingPipelineManager):
            raise TypeError("Expected a RenderingPipelineManager instance")
        self._rendering_pipeline = pipeline
        logger.info("Active rendering pipeline set.")
        
    
    def set_title(self, title: str):
        if not self.hwnd:
            raise RuntimeError("Cannot set title: invalid HWND")
        if not windll.user32.SetWindowTextW(self.hwnd, ctypes.c_wchar_p(title)):
            raise ctypes.WinError()
        self._title = title
        logger.info(f"Window title changed to: {title}")

    def run(self):
        try:
            self._start_lifecycle()
            logger.info("Entering main loop...")
            while not self.exit_requested and self._running:
                self.poll_events()
                self._frame_wrapper()
                self.swap_buffers()
        except Exception as e:
            logger.error("Exception in main loop", exc_info=True)
        finally:
            self._shutdown()
        return 0

    def _start_lifecycle(self):
        init_gl_functions()
        
        self._running = True
        logger.info("Window startup complete.")
        self.on_start()
        self._rendering_pipeline.add(lambda: 0)
        self._rendering_pipeline.runStartPasses()

    def _frame_wrapper(self):
        self._rendering_pipeline.runActivePasses()
        try:
            self.update()
        except TypeError:
            self.update(None)

    def on_start(self):
        """
        Hook called once after initialization. Override to run startup code.
        """
        pass

    def update(self):
        """
        Hook called every frame. Override to implement render/update logic.
        """
        pass

    def close(self):
        self._running = False
        self.exit_requested = True
        self._shutdown()
       
    def _shutdown(self):
        try:
            if self.hglrc:
                windll.opengl32.wglMakeCurrent(None, None)
                delete_opengl_context(self.hglrc)
                self.hglrc = None
        except Exception as e:
            logger.warning(f"Error deleting OpenGL context: {e}")

        try:
            if self.hdc and self.hwnd:
                windll.user32.ReleaseDC(self.hwnd, self.hdc)
                self.hdc = None
        except Exception as e:
            logger.warning(f"Error releasing DC: {e}")

        try:
            if self.hwnd:
                windll.user32.DestroyWindow(self.hwnd)
                if self.hwnd in self._hwnd_instance_map:
                    del self._hwnd_instance_map[self.hwnd]
                self.hwnd = None
        except Exception as e:
            logger.warning(f"Error destroying window: {e}")
        logger.info("Shutting down window...")
        
        windll.user32.PostQuitMessage(0)
