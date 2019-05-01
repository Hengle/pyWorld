import pygame

import world
from exceptions import QuitException

height = 800
width = 1024

if __name__ == '__main__':
    try:
        world_engine = world.WorldEngine((width, height))
        world_engine.run()
    except QuitException as e:
        pygame.quit()
