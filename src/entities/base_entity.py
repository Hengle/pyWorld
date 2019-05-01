from abc import ABC, abstractmethod


class Entity(ABC):

    @abstractmethod
    def logic(self, delta_time):
        pass


class DrawableEntity(Entity):

    @abstractmethod
    def draw(self, surface):
        pass
