from typing import Callable, List, Literal
from aphelion.core.opengl import _glClearColor, _glEnable, _glClear
from aphelion.core.opengl.constants import (
    GL_DEPTH_TEST, GL_BLEND,
    GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT
)


class RenderPass:
    def __init__(self, name: str, action: Callable[[], None]):
        self.name = name
        self.action = action

    def run(self):
        self.action()


class Passes:
    @staticmethod
    def UseClearColor(r: float, g: float, b: float, a: float) -> RenderPass:
        return RenderPass("UseClearColor", lambda: _glClearColor(r, g, b, a))

    @staticmethod
    def RunClear() -> RenderPass:
        return RenderPass("RunClear", lambda: _glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT))

    @staticmethod
    def EnableGLDepthTest() -> RenderPass:
        return RenderPass("EnableGLDepthTest", lambda: _glEnable(GL_DEPTH_TEST))

    @staticmethod
    def EnableGLBlend() -> RenderPass:
        return RenderPass("EnableGLBlend", lambda: _glEnable(GL_BLEND))

    @staticmethod
    def Setup3DScene() -> List[RenderPass]:
        return [
            Passes.EnableGLDepthTest(),
            Passes.EnableGLBlend(),
            Passes.UseClearColor(0.1, 0.1, 0.1, 1.0)
        ]

    @staticmethod
    def DefaultFrame() -> List[RenderPass]:
        return [Passes.RunClear()]

    @staticmethod
    def Empty() -> RenderPass:
        return RenderPass("Empty", lambda: None)


class RenderingPipelineManager:
    def __init__(self):
        self._passes: dict[str, List[RenderPass]] = {
            "startup": [],
            "frame": [],
            "cleanup": []
        }

    def add_pass(self, stage: Literal["startup", "frame", "cleanup"], render_pass: RenderPass):
        self._passes[stage].append(render_pass)

    def add_passes(self, stage: Literal["startup", "frame", "cleanup"], passes: List[RenderPass]):
        self._passes[stage].extend(passes)

    def run_stage(self, stage: Literal["startup", "frame", "cleanup"]):
        for render_pass in self._passes[stage]:
            try:
                render_pass.run()
            except Exception as e:
                raise RuntimeError(f"Error running pass '{render_pass.name}': {e}")

    def clear_stage(self, stage: Literal["startup", "frame", "cleanup"]):
        self._passes[stage].clear()

    def clear_all(self):
        for stage in self._passes:
            self._passes[stage].clear()

    def get_stage(self, stage: Literal["startup", "frame", "cleanup"]) -> List[RenderPass]:
        return self._passes[stage]

    def describe(self) -> str:
        return "\n".join(
            f"{stage}: {[p.name for p in self._passes[stage]]}"
            for stage in ("startup", "frame", "cleanup")
        )
