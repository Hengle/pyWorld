import abc
from collections import Set
from typing import Dict

import pygame

import colors
import components
from world import World


class System(abc.ABC):
    def __init__(self, world: World, required_components: Set):
        self.world = world
        if not required_components:
            required_components = set()
        self.required_components: Set = required_components

    def update(self):
        for entity_id in self.world.entity_manager.get_entities():
            entity_components = self.world.component_manager.get_entity_components(entity_id)
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

        self.systems: Set[System] = {
            God(world),
            Movement(world),
            Render(world)
        }

    def update(self):
        for system in self.systems:
            system.update()


class God(System):

    def __init__(self, world: World):
        required = {
            components.God
        }
        super().__init__(world, required)
        self.m1_clicked = False

    def should_create_entity(self):
        return self.m1_clicked

    def update_entity(self, entity_id, entity_components):
        god_position: components.Position = entity_components[components.Position]
        god_position.set_position(pygame.mouse.get_pos())

        if self.should_create_entity():
            bot_entity = self.world.entity_manager.create_entity()
            self.world.component_manager.add_component(bot_entity, components.AI, max_velocity=(3, 3))
            self.world.component_manager.add_component(bot_entity, components.Position, position=pygame.mouse.get_pos())
            self.world.component_manager.add_component(bot_entity, components.Velocity)
            self.world.component_manager.add_component(bot_entity, components.Render, radius=10, width=1)


class Movement(System):
    def __init__(self, world: World):
        required = {
            components.Position,
            components.Velocity
        }
        super().__init__(world, required)

    def update_entity(self, entity_id, entity_components):
        pass


class Render(System):
    def __init__(self, world: World):
        required = {
            components.Render,
            components.Position
        }
        super().__init__(world, required)

    def update_entity(self, entity_id, entity_components):
        render_component: components.Render = entity_components[components.Render]
        position_component: components.Position = entity_components[components.Position]

        pygame.draw.circle(self.world.surface, colors.red,
                           position_component.position,
                           render_component.radius,
                           render_component.width)
