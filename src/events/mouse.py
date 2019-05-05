import pygame

M1_BUTTON = 1

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
        pass


def is_m1_pressed() -> bool:
    return M1_BUTTON in pressed


def is_m1_held() -> bool:
    return M1_BUTTON in held
