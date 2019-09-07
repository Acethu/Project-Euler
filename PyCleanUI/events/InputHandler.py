import pygame
import pygame.locals

from PyCleanUI.Style import STYLE
import PyCleanUI.assets.Cursors

import PyCleanUI.widgets.Button
import PyCleanUI.widgets.Input

def handle_input(window, widget, event):
    if widget.get_state() == "active":
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                widget.set_text(widget.get_text()[:-1]) # remove last of widget.text
                if pygame.key.get_pressed()[pygame.K_LSHIFT]:
                    widget.set_text("")
            else:
                widget.set_text(widget.get_text() + event.unicode) # add key to widget.text
            widget.render()
            pygame.display.flip()

    if widget.get_rect().collidepoint(pygame.mouse.get_pos()): # mouse over
        PyCleanUI.assets.Cursors.set_cursor("input")
        if event.type == pygame.MOUSEBUTTONDOWN and widget.get_state() == "inactive":
            for w in window.widgets:
                if type(w) == PyCleanUI.widgets.Input.Input:
                    w.set_state("inactive")
                    w.render()
            widget.set_state("active")
            widget.render()
            pygame.display.flip()
    # mouse not over
    else:
        should_change = True
        for w in window.widgets:
            if type(w) == PyCleanUI.widgets.Input.Input:
                if w.get_rect().collidepoint(pygame.mouse.get_pos()):
                    should_change = False
        if PyCleanUI.assets.Cursors.get_cursor() == "input" and should_change:
            PyCleanUI.assets.Cursors.set_cursor("normal")
        if event.type == pygame.MOUSEBUTTONDOWN:
            widget.set_state(state="inactive")
            widget.render()
            pygame.display.flip()
