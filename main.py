import pygame

import core
from core import engine
from exceptions import QuitException

height = 800
width = 1024

if __name__ == '__main__':
    try:
        world_engine = core.engine.WorldEngine((width, height), 60)
        world_engine.run()
    except QuitException as e:
        pygame.quit()
