import abc

from .state import RoutineState
from core.world import World


class Routine:
    def __init__(self, entity_id, world: World):
        self.entity_id = entity_id
        self._world = world
        self.state = None

    def start(self):
        self.state = RoutineState.RUNNING

    def log(self, key, value):
        self._world.log_text(self.entity_id, key, value)

    @abc.abstractmethod
    def reset(self):
        pass

    def restart(self):
        self.reset()
        self.start()

    def succeed(self):
        self.state = RoutineState.SUCCESS

    def fail(self):
        self.state = RoutineState.FAILURE

    def is_running(self):
        return self.state == RoutineState.RUNNING

    def is_success(self):
        return self.state == RoutineState.SUCCESS

    def is_failure(self):
        return self.state == RoutineState.FAILURE

    @abc.abstractmethod
    def act(self):
        pass
