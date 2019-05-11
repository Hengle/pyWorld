import components
from behaviour import Move, Routine, Stand
from core.world import World


class Wander(Routine):
    def __init__(self, entity_id, world: World):
        super().__init__(entity_id, world)
        self.move = Move(entity_id, world)
        self.stand = Stand(entity_id, world, 5)

    def reset(self):
        pass

    def act(self):
        if self.move.is_running():
            self.move.act()
        elif self.stand.is_running():
            self.stand.act()

        if not self.move.is_running():
            self.move.target = self._world.get_random_location()
            self._world.ec_manager.create_component(
                self.entity_id,
                components.Velocity,
                (1, 1)
            )
            self.move.start()

        if self.move.is_success() and not self.stand.is_running():
            self._world.ec_manager.remove_component(
                self.entity_id,
                components.Velocity
            )
            self.stand.reset()
            self.stand.start()
