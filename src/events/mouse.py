import pygame

mouse_pressed = (False, False, False)
mouse_held = (False, False, False)
mouse_released = (False, False, False)


def reset():
    global mouse_pressed
    global mouse_held
    global mouse_released

    mouse_pressed = (False, False, False)
    mouse_held = (False, False, False)
    mouse_released = (False, False, False)


def is_mouse_event(event):
    return event.dict.get('type') in {pygame.MOUSEMOTION,
                                      pygame.MOUSEBUTTONDOWN,
                                      pygame.MOUSEBUTTONUP,
                                      pygame.MOUSEWHEEL}


def is_mouse_up(event):
    if event.type == pygame.MOUSEBUTTONUP:
        global mouse_released
        mouse_released = True
    return mouse_released


def handle_mouse_event(event):
    pass
