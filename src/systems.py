import abc
from collections import Set
from typing import Dict

import pygame

import colors
import components
import events
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

    def update_entity(self, entity_id, entity_components):
        position: components.Position = entity_components[components.Position]
        position.set_position(pygame.mouse.get_pos())

        if 1 in events.mouse.held:
            bot_entity = self.world.entity_manager.create_entity()
            self.world.component_manager.add_component(bot_entity, components.AI)
            self.world.component_manager.add_component(bot_entity, components.Position, position)
            self.world.component_manager.add_component(bot_entity, components.Velocity, (2, 2))
            self.world.component_manager.add_component(bot_entity, components.Render, 20, 1)
            self.world.component_manager.add_component(bot_entity, components.Acceleration, 0.1, 2)


class Movement(System):
    def __init__(self, world: World):
        required = {
            components.Position,
            components.Velocity
        }
        super().__init__(world, required)

    def update_entity(self, entity_id, entity_components):
        position: components.Position = entity_components[components.Position]
        velocity: components.Velocity = entity_components[components.Velocity]

        new_x, new_y = position[0] + velocity[0], position[1] + velocity[1]
        new_vx, new_vy = velocity[0], velocity[1]

        max_x, max_y = self.world.surface.get_size()

        if new_x > max_x:
            new_x = max_x
            new_vx = -new_vx
        elif new_x < 0:
            new_x = 0
            new_vx = -new_vx

        if new_y > max_y:
            new_y = max_y
            new_vy = -new_vy
        elif new_y < 0:
            new_y = 0
            new_vy = -new_vy

        position.set_position((new_x, new_y))
        velocity.set_velocity((new_vx, new_vy))
        pass


class Render(System):
    def __init__(self, world: World):
        required = {
            components.Render,
            components.Position
        }
        super().__init__(world, required)

    def update_entity(self, entity_id, entity_components):
        render: components.Render = entity_components[components.Render]
        position: components.Position = entity_components[components.Position]

        pygame.draw.circle(self.world.surface, colors.red,
                           position.get_as_int(),
                           render.radius,
                           render.width)
