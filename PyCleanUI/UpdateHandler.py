import pygame

def handle_update(window, event):
    # very shitty code, hard to understand, sorry
    global frame, del_rate
    if 'frame' in globals(): # if 'frame' exists
        frame += 1
    else: # in case not (init), set 'frame' to 0
        frame = 0
        del_rate = 5 # the rate of deleting a character

    if event is not None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                frame = 0
    else:
        if 'del_rate' in globals():
            if frame % del_rate == 0:
                if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_BACKSPACE))
                    if del_rate > 1:
                        del_rate -= 1
                else:
                    del_rate = 5
