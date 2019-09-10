import pygame
import PyCleanUI

def handle_update(window, event):
    _handle_input_delete(window, event)
    _handle_input_cursor(window)

def _handle_input_delete(window, event):
    # very shitty code, hard to understand, sorry
    global del_time, del_rate
    if 'del_time' in globals(): # if 'del_time' exists
        del_time += 1
    else: # in case not (init), set 'del_time' to 0
        del_time = 0
        del_rate = 6 # the rate of deleting a character

    if event is not None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                del_time = 0
            else:
                event = None
        else:
            event = None
    if event is None:
        if 'del_rate' in globals():
            if del_time % del_rate == 0:
                if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_BACKSPACE))
                    if del_rate > 1:
                        del_rate -= 1
                else:
                    del_rate = 6

def _handle_input_cursor(window):
    # handles the input cursor
    global show_time
    if 'show_time' in globals(): # if 'show_time' exists
        show_time -= 1
        if show_time == -1:
            show_time = 10
    else: # in case not (init), set show_time' to 10
        show_time = 10
    if show_time == 0:
        for widget in window.widgets:
            if type(widget) == PyCleanUI.widgets.Input.Input:
                if widget.get_state() == "active":
                    widget.toggle_cursor()
