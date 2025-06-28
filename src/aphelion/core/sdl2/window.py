from typing_extensions import runtime
import sdl2
import sdl2.ext


class _SDL2Window:
    def __init__(self, width=800, height=600, title="SDL2 Window"):
        if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0:
            raise RuntimeError(f"SDL_Init Error: {sdl2.SDL_GetError().decode('utf-8')}")

        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 3)
        sdl2.SDL_GL_SetAttribute(
            sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE
        )

        self.window = sdl2.SDL_CreateWindow(
            title.encode(),
            sdl2.SDL_WINDOWPOS_CENTERED,
            sdl2.SDL_WINDOWPOS_CENTERED,
            width,
            height,
            sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN,
        )
        
        if not self.window:
            raise RuntimeError(sdl2.SDL_GetError().decode('utf-8'))
        
        self.context = sdl2.SDL_GL_CreateContext(self.window)
        if not self.context:
            raise RuntimeError(sdl2.SDL_GetError().decode('utf-8'))
        
        self.running = False 
    
    def poll_event(self, event: sdl2.SDL_Event) -> sdl2.SDL_Event:
        return sdl2.SDL_PollEvent(event)
        
    def __sdlsystem(self, update_callback):
        
        while self.running:
            
            event = sdl2.SDL_Event()
            while self.poll_event(event):
                if event.type == sdl2.SDL_QUIT:
                    self.running = False 
                    self.__sdlquit()
                    
            update_callback()
            sdl2.SDL_GL_SwapWindow(self.window)
        
                    
    def __sdlquit(self):
        ...
        
    def run(self):
        running = True
        while running:
            for event in sdl2.ext.get_events():
                if event.type == sdl2.SDL_QUIT:
                    running = False
            self.window.refresh()

        sdl2.ext.quit()
