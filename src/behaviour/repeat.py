from core.world import World
from .routine import Routine


class Repeat(Routine):
    def __init__(self, entity_id, world: World, routine, max_repeat=-1):
        super().__init__(entity_id, world)
        self.routine = routine
        self.max_repeat = max_repeat
        self.repeat_count = 0

    def start(self):
        super().start()
        self.routine.start()

    def reset(self):
        self.repeat_count = 0

    def act(self):
        if self.routine.is_failure():
            self.fail()
        elif self.routine.is_success():
            if self.repeat_count == self.max_repeat:
                self.succeed()
                return
            else:
                if self.max_repeat > 0:
                    self.repeat_count += 1
                self.restart()
        if self.routine.is_running():
            self.routine.act()
