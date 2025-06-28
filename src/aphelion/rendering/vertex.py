
from dataclasses import dataclass, field
from typing import Tuple


@dataclass
class V2D:
    """Represents a 2D vertex."""
    
    x: float
    y: float
    
    u: float = field(default_factory=float, init=False)
    v: float = field(default_factory=float, init=False)
    
    color4: Tuple[float, float, float, float]  = field(default_factory=tuple, init=False)
    
    def setUV(self, u: float, v: float):
        self.u = u 
        self.v = v
    
    def setColor4(self, color: Tuple[float, float, float, float]):
        self.color4 = color 

    def position(self) -> Tuple[float, float]:
        return self.x, self.y 

    @staticmethod 
    @property
    def Zero() -> "V2D":
        return V2D(0, 0)



        