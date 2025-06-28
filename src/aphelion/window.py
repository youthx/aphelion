import ctypes
import logging
from aphelion.core.opengl.functions import init_gl_functions
from aphelion.core.pipeline_manager import Passes, RenderingPipelineManager
from aphelion.core.sdl2.window import _SDL2Window, sdl2

# Set up logging for this module
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

class _WindowInstance(_SDL2Window):
    """
    Main window class for Aphelion, handling event processing, rendering pipeline,
    and input state tracking.
    Inherits from _SDL2Window.
    """
    def __init__(self, width=800, height=600, title="Aphelion"):
        """
        Initialize the window, rendering pipeline, and input state.
        """
        super().__init__(width, height, title)
        self._rendering_pipeline = RenderingPipelineManager()
        self._keys_down = set()              # Set of currently pressed keys
        self._mouse_buttons_down = set()     # Set of currently pressed mouse buttons
        self._mouse_pos = (0, 0)             # Current mouse position (x, y)
        self.running = True                  # Main loop control flag
        init_gl_functions()                  # Initialize OpenGL functions

    def getMouseButtonsDown(self):
        """
        Returns:
            set: Set of currently pressed mouse buttons.
        """
        return self._mouse_buttons_down

    def getMousePosition(self):
        """
        Returns:
            tuple: Current mouse position as (x, y).
        """
        return self._mouse_pos

    def setActivePipeline(self, pipeline: RenderingPipelineManager):
        """
        Set the active rendering pipeline.

        Args:
            pipeline (RenderingPipelineManager): The pipeline to set as active.

        Raises:
            TypeError: If pipeline is not a RenderingPipelineManager instance.
        """
        if not isinstance(pipeline, RenderingPipelineManager):
            raise TypeError("Expected a RenderingPipelineManager instance")
        self._rendering_pipeline = pipeline
        logger.info("Active rendering pipeline set.")

    def run(self):
        """
        Start the window's main loop and initialize the rendering pipeline.
        """
        logger.info("Initializing rendering pipeline and starting main loop...")
        self._start()
        self._rendering_pipeline.run_stage("startup")
        self._run_main_loop()

    def _run_main_loop(self):
        """
        Main event and rendering loop.
        Processes SDL2 events, updates input state, and renders frames.
        """
        event = sdl2.SDL_Event()
        while self.running:
            while self.poll_event(event):
                if event.type == sdl2.SDL_QUIT:
                    self.running = False
                    self._quit()
                elif event.type == sdl2.SDL_KEYDOWN:
                    key = event.key.keysym.sym
                    self._keys_down.add(key)
                    self._keydown(key)
                elif event.type == sdl2.SDL_KEYUP:
                    key = event.key.keysym.sym
                    self._keys_down.discard(key)
                    self._keyup(key)
                elif event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                    button = event.button.button
                    self._mouse_buttons_down.add(button)
                    self._mousedown(button, event.button.x, event.button.y)
                elif event.type == sdl2.SDL_MOUSEBUTTONUP:
                    button = event.button.button
                    self._mouse_buttons_down.discard(button)
                    self._mouseup(button, event.button.x, event.button.y)
                elif event.type == sdl2.SDL_MOUSEMOTION:
                    self._mouse_pos = (event.motion.x, event.motion.y)
                    self._mousepos(event.motion.x, event.motion.y)

            self.frame_wrapper()
            sdl2.SDL_GL_SwapWindow(self.window)

    def frame_wrapper(self):
        """
        Wrapper for per-frame logic and rendering pipeline stage.
        """
        self._rendering_pipeline.run_stage("frame")
        self._update()

    def _keydown(self, key: sdl2.SDL_Keycode):
        """
        Override to handle key down events.

        Args:
            key: SDL2 key code.
        """
        ...

    def _keyup(self, key: sdl2.SDL_Keycode):
        """
        Override to handle key up events.

        Args:
            key: SDL2 key code.
        """
        ...

    def _mousedown(self, button, x: int, y: int):
        """
        Override to handle mouse button down events.

        Args:
            button: Mouse button code.
            x (int): Mouse x position.
            y (int): Mouse y position.
        """
        ...

    def _mouseup(self, button, x: int, y: int):
        """
        Override to handle mouse button up events.

        Args:
            button: Mouse button code.
            x (int): Mouse x position.
            y (int): Mouse y position.
        """
        ...

    def _mousepos(self, x: int, y: int):
        """
        Override to handle mouse movement events.

        Args:
            x (int): Mouse x position.
            y (int): Mouse y position.
        """
        ...

    def _start(self):
        """
        Override to implement custom startup logic.
        Called once after window/context creation.
        """
        pass

    def _update(self):
        """
        Override to implement per-frame logic.
        Called every frame.
        """
        pass

    def _quit(self):
        """
        Override to implement shutdown/cleanup logic.
        Called once when exiting.
        """
        self.close()

    def close(self):
        """
        Clean up resources and close the window.
        """
        if not self.running:
            return

        self._rendering_pipeline.run_stage("cleanup")
        self.running = False

        logger.info("Closing window and cleaning up resources...")
        if self.window:
            sdl2.SDL_DestroyWindow(self.window)
            self.window = None
        sdl2.SDL_Quit()