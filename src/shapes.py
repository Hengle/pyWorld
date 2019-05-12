from abc import ABC, abstractmethod

import pygame

import colors


class Shape(ABC):
    def __init__(self, color=colors.blue):
        self.color = color

    def update(self, **kwargs):
        pass

    @abstractmethod
    def render(self, surface: pygame.Surface):
        pass


class Line(Shape):
    def __init__(self, color=None, start_position=(0, 0), end_position=(0, 0)):
        super().__init__(color)
        self.start_position = start_position
        self.end_position = end_position

    def render(self, surface: pygame.Surface):
        Line.render_static(surface, self.color, self.start_position, self.end_position)

    @staticmethod
    def render_static(surface: pygame.Surface, color, start_position, end_position):
        pygame.draw.line(
            surface,
            color,
            start_position,
            end_position,
            2
        )


class Circle(Shape):
    def __init__(self, color=None, position=(0, 0), radius=0):
        super().__init__(color)
        self.position = position
        self.radius = radius

    def render(self, surface: pygame.Surface):
        Circle.render_static(surface, self.color, self.position, self.radius)

    @staticmethod
    def render_static(surface: pygame.Surface, color, position, radius):
        pygame.draw.circle(
            surface,
            color,
            position,
            radius,
            2
        )


class Rectangle(Shape):
    def __init__(self, color=None, position=(0, 0), size=(0, 0)):
        super().__init__(color)
        self.position = position
        self.size = size

    def render(self, surface: pygame.Surface):
        Rectangle.render_static(surface, self.color, self.position, self.size[0], self.size[1])

    @staticmethod
    def render_static(surface, color, position, width, height):
        pygame.draw.lines(
            surface,
            color,
            True,
            Rectangle.get_corners(position, width, height),
            2
        )

    @staticmethod
    def get_corners(position, width, height):
        half_width = width / 2
        x_plane_1 = position[0] - half_width
        x_plane_2 = position[0] + half_width

        half_height = height / 2
        y_plane_1 = position[1] - half_height
        y_plane_2 = position[1] + half_height
        return [
            (x_plane_1, y_plane_1),
            (x_plane_2, y_plane_1),
            (x_plane_2, y_plane_2),
            (x_plane_1, y_plane_2)
        ]
