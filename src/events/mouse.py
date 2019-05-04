import pygame

pressed = set()
held = set()


def update():
    for button in pressed:
        held.add(button)
    pressed.clear()


def is_mouse_event(event: pygame.event.Event):
    return event.type in {pygame.MOUSEMOTION,
                          pygame.MOUSEBUTTONDOWN,
                          pygame.MOUSEBUTTONUP,
                          pygame.MOUSEWHEEL}


def is_mouse_up(event: pygame.event.Event):
    if event.type == pygame.MOUSEBUTTONUP:
        global mouse_released
        mouse_released = True
    return mouse_released


def handle_event(event: pygame.event.Event):
    event_type = event.type
    if event_type == pygame.MOUSEBUTTONDOWN:
        pressed.add(event.button)
    elif event_type == pygame.MOUSEBUTTONUP:
        button = event.button
        if button in pressed:
            pressed.remove(button)
        else:
            held.remove(button)
    elif event_type == pygame.MOUSEWHEEL:
        pass
    elif event_type == pygame.MOUSEMOTION:
        buttons = event.buttons
        pass
