from aphelion.core.opengl.functions import init_gl_functions
from aphelion.window import _WindowInstance
from aphelion.core.pipeline_manager import Passes, RenderingPipelineManager

class App(_WindowInstance):
    def on_start(self):
        
        self.RPPassManager = RenderingPipelineManager()
        self.RPPassManager.add(Passes.UseLatestPrerenderingPasses)
        self.RPPassManager.add(Passes.UseClearColor(0.5, 0.8, 1.0, 1.0))
        self.RPPassManager.add(Passes.EndStartPasses)
        
        self.RPPassManager.add(Passes.RunClear)
        self.RPPassManager.add(Passes.EndActivePasses)
        self.setActivePipeline(self.RPPassManager)
        
        
        
    def update(self):
        ...
        
    
if __name__ == "__main__":
    app = App(800, 800)
    app.run()
    app.close()
    del app 
    