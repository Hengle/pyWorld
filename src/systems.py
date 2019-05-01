import abc
from collections import Set
from typing import Dict

import pygame

import colors
import components
from world import World


class System(abc.ABC):
    required_components: Set = set()

    def __init__(self, world: World, required_components: Set = None):
        self.world = world
        if not required_components:
            required_components = set()
        self.required_components = required_components

    def update(self):
        for entity_id in self.world.get_entities():
            entity_components = self.world.get_entity_components(entity_id)
            if self.is_applicable(entity_components):
                self.update_entity(entity_id, entity_components)

    @abc.abstractmethod
    def update_entity(self, entity_id, entity_components):
        pass

    def is_applicable(self, entity_components: Dict):
        x = [k in entity_components for k in self.required_components]
        return all(x)


class SystemManager:
    def __init__(self, world: World):
        self.world = world

        self.systems = {
            God(world),
            Movement(world),
            Render(world)
        }

    def update(self):
        for system in self.systems:
            system.update()


class God(System):
    def update_entity(self, entity_id, entity_components):
        position: components.Position = entity_components[components.Position]
        position.set_position(pygame.mouse.get_pos())


class Movement(System):
    def update_entity(self, entity_id, entity_components):
        pass


class Render(System):

    def __init__(self, world: World):
        required_components = {
            components.Render
        }
        super().__init__(world, required_components)

    def update_entity(self, entity_id, entity_components):
        render_component: components.Render = entity_components[components.Render]
        position_component: components.Position = entity_components[components.Position]

        pygame.draw.circle(self.world.surface, colors.red,
                           position_component.position,
                           render_component.radius,
                           render_component.width)
