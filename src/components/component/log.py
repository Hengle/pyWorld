from components import Component


class Log(Component):
    def __init__(self, entity_id):
        self.entity_id = entity_id
        self.text = {}
        self.drawables = {}

    def clear(self):
        self.text.clear()
        self.drawables.clear()
        self.text["entity_id"] = self.entity_id

    def __str__(self) -> str:
        return "\n".join(self.text)
