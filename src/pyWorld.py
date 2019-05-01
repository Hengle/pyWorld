import pygame

import engine
import world
from exceptions import QuitException

height = 800
width = 1024

if __name__ == '__main__':
    try:
        world_engine = engine.WorldEngine((width, height))
        world_engine.run()
    except QuitException as e:
        pygame.quit()
