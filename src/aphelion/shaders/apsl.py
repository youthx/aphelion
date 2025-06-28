from typing import Self, Union


class _APSLObject:
    def emit(self, _format: str, *args):
        return _format.format(*args)


class _APSLVar(_APSLObject):
    def __init__(self, type_: str, name: str):
        self.type = type_
        self.name = name
        self.qualifier = ""
        self.location: int | None = None

    def In(self):
        self.qualifier = "in"
        return self

    def Out(self):
        self.qualifier = "out"
        return self

    def Uniform(self):
        self.qualifier = "uniform"
        return self

    def with_location(self, location: int):
        self.location = location
        return self

    def emit(self):
        if self.location is not None:
            return f"layout(location = {self.location}) {self.qualifier} {self.type} {self.name};"
        return f"{self.qualifier} {self.type} {self.name};"

    def __str__(self):
        return self.emit()


class vec2(_APSLVar):
    def __init__(self, name: str):
        super().__init__("vec2", name)


class vec3(_APSLVar):
    def __init__(self, name: str):
        super().__init__("vec3", name)


class vec4(_APSLVar):
    def __init__(self, name: str):
        super().__init__("vec4", name)


class mat4(_APSLVar):
    def __init__(self, name: str):
        super().__init__("mat4", name)


class _APSLFunc(_APSLObject):
    def __init__(self, name: str, return_type: str):
        self.name = name
        self.return_type = return_type
        self.body: list[Union[str, _APSLObject]] = []

    @staticmethod
    def main():
        return _APSLFunc("main", "void")

    def set(self, *body):
        if len(body) == 1 and isinstance(body[0], (list, tuple)):
            self.body = list(body[0])
        else:
            self.body = list(body)
        return self

    def emit(self):
        lines = [f"\n{self.return_type} {self.name}() {{"]
        for stmt in self.body:
            if isinstance(stmt, _APSLObject):
                lines.append("    " + stmt.emit())
            else:
                lines.append("    " + str(stmt))
        lines.append("}")
        return "\n".join(lines)

    def __str__(self):
        return self.emit()


class gl_Position:
    @staticmethod
    def set(value: str):
        return f"gl_Position = {value};"


def assign(lhs: Union[str, _APSLObject], rhs: Union[str, _APSLObject]) -> str:
    return f"{lhs} = {rhs};"


def declare(var: _APSLVar, value: str) -> str:
    return f"{var.type} {var.name} = {value};"


class PassThroughComment(_APSLObject):
    def __init__(self, text: str):
        self.text = text

    def emit(self):
        return f"// {self.text}"


class ShaderModule:
    def __init__(self, *items):
        self.headers = ["#version 330 core"]
        self.variables = []
        self.functions = []
        self.extra_lines = []

        for item in items:
            if isinstance(item, _APSLVar):
                self.variables.append(item)
            elif isinstance(item, _APSLFunc):
                self.functions.append(item)
            elif isinstance(item, str):
                self.extra_lines.append(item)
            else:
                raise TypeError(f"Unsupported item in shader module: {type(item)}")

    def __str__(self):
        out = self.headers[:]
        out += [str(var) for var in self.variables]
        out += self.extra_lines
        out += [str(func) for func in self.functions]
        return "\n".join(out)


Func = _APSLFunc
Var = _APSLVar