from typing import Callable 
from aphelion.core.opengl import _glClearColor, _glEnable, _glClear
from aphelion.core.opengl.constants import GL_DEPTH_TEST, GL_BLEND, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT 

class Passes:
    def UseClearColor(r: float, g: float, b: float, a: float):
        return lambda: _glClearColor(r, g, b, a)

    def RunClear():
        return _glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def EnableGLDepthTest():
        return _glEnable(GL_DEPTH_TEST)
    
    def EnableGLBlend():
        return _glEnable(GL_BLEND)

    def EndStartPasses():
        return 0x000000A1
    
    def EndActivePasses():
        return 0x000000A2
    
    def OptimizeFor3dRendering():
        return Passes.EnableGLDepthTest()
    
    def EnableTransparency():
        return Passes.EnableGLBlend()
    
    def UseLatestPrerenderingPasses():
        Passes.OptimizeFor3dRendering() 
        Passes.EnableTransparency()
    
    
class RenderingPipelineManager(object):
    
    def __init__(self):
        self._active_passes = []
        self._start_passes = []
        self._active_list = self._start_passes
        
    
    def add(self, _pass: Callable):
        if callable(_pass):
            if _pass == Passes.EndStartPasses:
                self._active_list = self._active_passes
            elif _pass == Passes.EndActivePasses:
                self._active_list = self._start_passes
            else:
                self._active_list.append(_pass)
        else:
            raise TypeError("Pass must be a callable function, got {}".format(type(_pass)))
        
        return _pass 
    
    def remove(self, _pass: Callable):
        if _pass in self._active_list:
            self._active_passes.remove(_pass)
        else:
            raise ValueError("Pass not found in active passes")
    
    def clearPasses(self):
        self._active_passes.clear()
        self._start_passes.clear()
    

    def runStartPasses(self):
        if not self._start_passes:
            raise RuntimeError("No active passes available")
        
        for _pass in self._start_passes:
            try:
                _pass()
            except Exception as _:
                raise RuntimeError(f"Error running start pass: {_pass.__name__}")
        
    def runActivePasses(self):
        if not self._active_passes:
            raise RuntimeError("No active passes available")
        
        for _pass in self._active_passes:
            try:
                _pass()
            except Exception as _:
                raise RuntimeError(f"Error running active pass: {_pass.__name__}")   
            