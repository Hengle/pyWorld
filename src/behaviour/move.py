from behaviour import Routine
from world import World


class Move(Routine):
    def __init__(self, entity_id, world: World):
        super().__init__(entity_id, world)

    def reset(self):
        pass

    def act(self):
        pass
