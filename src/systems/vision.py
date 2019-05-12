import colors
import components
from core import World
from managers import mappers
from .system import System


class Vision(System):
    def __init__(self, world: World):
        required_components = {
            components.Position,
            components.Vision
        }
        super().__init__(world, required_components)

    def update_entity(self, entity_id, entity_components: mappers.ComponentMap):
        position = entity_components[components.Position]
        vision = entity_components[components.Vision]

        self._world.log_circle(entity_id,
                               "vision_radius",
                               position=position.vector_int,
                               color=colors.gray,
                               radius=vision.radius)

        world_entities = self._world.ec_manager.get_items([components.Position])
        for other_id, other_components in world_entities:
            if other_id == entity_id:
                continue
            other_position: components.Position = other_components[components.Position]
            distance_to = position.distance_to(other_position)
            if distance_to < vision.radius:
                vision.add(other_id)
                self._world.log_line(entity_id,
                                     f"target:{other_id}",
                                     colors.gray,
                                     position.vector_int,
                                     other_position.vector_int)
            elif other_id in vision.in_range:
                vision.remove(other_id)

        self._world.log_text(entity_id, "in_range", str(vision))
