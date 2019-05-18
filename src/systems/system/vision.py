import colors
import maps
from components import component
from core import World
from systems import System


class Vision(System):
    def __init__(self, world: World):
        required_components = {
            component.Position,
            component.Vision
        }
        super().__init__(world, required_components)

    def update_entity(self, entity_id, entity_components: maps.ComponentMap):
        position = entity_components[component.Position]
        vision = entity_components[component.Vision]

        self._world.log_circle(entity_id,
                               "vision_radius",
                               position=position.point.as_int_tuple(),
                               color=colors.gray,
                               radius=vision.radius)

        world_entities = self._world.ec_manager.get_items([component.Position])
        for other_id, other_components in world_entities:
            if other_id == entity_id:
                continue
            other_position: component.Position = other_components[component.Position]
            distance_to = position.point.distance_to(other_position.point)
            if distance_to < vision.radius:
                vision.add(other_id)
                self._world.log_line(entity_id,
                                     f"target:{other_id}",
                                     colors.gray,
                                     position.point.as_int_tuple(),
                                     other_position.point.as_int_tuple())
            elif other_id in vision.in_range:
                vision.remove(other_id)

        self._world.log_text(entity_id, "in_range", str(vision))
