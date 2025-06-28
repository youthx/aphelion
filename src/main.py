from Mesh import Quad
from aphelion.core.opengl.functions import _glClear
from aphelion.window import _WindowInstance
from aphelion.core.pipeline_manager import Passes, RenderingPipelineManager
from aphelion.shaders.apsl import ShaderModule, assign, gl_Position, vec2, Func, mat4, vec4 
from aphelion.shaders.shader import ShaderProgram

class App(_WindowInstance):
    def _start(self):
        pipeline = RenderingPipelineManager()
        pipeline.add_pass("frame", Passes.UseClearColor(0.5, 0.8, 1.0, 1.0))
        self.setActivePipeline(pipeline)
        fragShader = ShaderModule(
            vec2("vTex").In(),
            vec4("fragColor").Out(),
            Func.main().set(
                assign("fragColor", "vec4(1.0, 0.3, 0.2, 1.0)")
            )
        )

        vertShader = ShaderModule(
            vec2("aPos").In().with_location(0),
            vec2("aTex").In().with_location(1),
            vec2("vTex").Out(),  # lowercase here
            Func.main().set(
                assign("vTex", "aTex"),  # must match exactly
                gl_Position.set("vec4(aPos, 0.0, 1.0)")
            )
        )

        program = ShaderProgram(str(vertShader), str(fragShader))
        self.quad = Quad(program)
        
    def _update(self):
        self._rendering_pipeline.add_pass("frame", Passes.RunClear())
        self.quad.render()      
          
if __name__ == "__main__":
    app = App(640, 400)
    app.run()
    app.close()
    del app 
    