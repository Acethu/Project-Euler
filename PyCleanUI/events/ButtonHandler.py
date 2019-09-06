import pygame
import pygame.locals

from PyCleanUI.Style import STYLE
import PyCleanUI.assets.Cursors

import PyCleanUI.widgets.Button
import PyCleanUI.widgets.Input

def handle_button(widget, event, index):
    # mouse over
    if widget.get_rect().collidepoint(pygame.mouse.get_pos()):
        PyCleanUI.assets.Cursors.set_cursor("button")

        if event.type == pygame.MOUSEBUTTONDOWN: # if down
            if event.button == 1:
                widget.set_state(state="click")
        elif event.type == pygame.MOUSEBUTTONUP: # if click
            if event.button == 1 and widget.get_state() == "click":
                widget.set_state(state="hover")
                pygame.event.post(pygame.event.Event(pygame.locals.USEREVENT,custom_type=index))
        elif widget.state == "normal": # on mouse enter
            widget.set_state(state="hover")
        widget.render()
        pygame.display.flip()
    # mouse not over
    else:
        if widget.state == "hover" or widget.state == "click": # on mouse leave
            PyCleanUI.assets.Cursors.set_cursor("normal")
            widget.set_state(state="normal")
            widget.render()
            pygame.display.flip()
