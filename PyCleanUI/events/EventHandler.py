import pygame
import pygame.locals

from PyCleanUI.Style import STYLE
import PyCleanUI.assets.Cursors

import PyCleanUI.widgets.Button
import PyCleanUI.widgets.Input

""" test for visual changes to be made due to an event """
def test_change(window, event):
    index = 0
    for widget in window.widgets:
        index += 1
        # button
        if type(widget) == PyCleanUI.widgets.Button.Button: # if widget is a button
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
        # input
        elif type(widget) == PyCleanUI.widgets.Input.Input: # if widget is a input
            if widget.get_state() == "active":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        widget.set_text(widget.get_text()[:-1]) # remove last of widget.text
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
                #break
            # mouse not over
            if not widget.get_rect().collidepoint(pygame.mouse.get_pos()):
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


""" get source of custom event """
def get_source(window, event):
    if event != None:
        return {"index": event.custom_type, "name": window.widgets[event.custom_type-1].text}

""" get values """
def get_values(window):
    values = []
    index = 0

    for widget in window.widgets:
        index += 1
        if type(widget) == PyCleanUI.widgets.Input.Input:
            values.append(
                {"index": index, "values":widget.get_text()}
            )
    return values
