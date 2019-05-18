import time

from core.world import World
from .routine import Routine


class Stand(Routine):
    def __init__(self, entity_id, world: World, stand_time=0):
        super().__init__(entity_id, world)
        self.stand_time = stand_time
        self.start_time = 0

    def set_stand_time(self, stand_time):
        self.stand_time = stand_time

    def reset(self):
        self.start_time = time.time()

    def act(self):
        cur_time = time.time()
        time_left = cur_time - self.start_time
        self.log(f"Waiting [{time_left}/{self.stand_time}]")
        if time_left >= self.stand_time:
            self.succeed()
