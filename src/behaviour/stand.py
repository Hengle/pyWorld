from .routine import Routine


class Stand(Routine):
    def __init__(self, entity_id, world: World):
        super().__init__(entity_id, world)

    def reset(self):
        pass

    def act(self):
        pass
