from components import Component


class Debug(Component):
    def __init__(self):
        self.lines = {}

    def __str__(self) -> str:
        return "\n".join(self.lines)
