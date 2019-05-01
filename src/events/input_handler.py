import pygame

from exceptions import QuitException


def handle_event(event):
    key_dict = event.dict
    if key_dict['key'] == pygame.K_ESCAPE:
        raise QuitException
