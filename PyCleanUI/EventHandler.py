import pygame
import pygame.locals

from PyCleanUI.Style import STYLE
import PyCleanUI.Assets.Cursors

import PyCleanUI.Widgets.Button
import PyCleanUI.Widgets.Input

""" test for visual changes to be made due to an event """
def test_change(window, event):
    index = 0
    for widget in window.widgets:
        index += 1
        """ Button """
        if type(widget) == PyCleanUI.Widgets.Button.Button: # if widget is a button
            # mouse over
            if widget.get_rect().collidepoint(pygame.mouse.get_pos()):
                PyCleanUI.Assets.Cursors.set_cursor("button")

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
                break # change found, so no need to check for other changes
            # mouse not over
            else:
                if widget.state == "hover" or widget.state == "click": # on mouse leave
                    PyCleanUI.Assets.Cursors.set_cursor("normal")
                    widget.set_state(state="normal")
                    widget.render()
                    pygame.display.flip()
                    break # change found, so no need to check for other changes
                else:
                    continue
                break
            break
        elif type(widget) == PyCleanUI.Widgets.Input.Input: # if widget is a input
            if widget.get_rect().collidepoint(pygame.mouse.get_pos()): # mouse over
                PyCleanUI.Assets.Cursors.set_cursor("input")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    widget.set_state("active")
                    widget.render()
                    pygame.display.flip()
                break
            # mouse not over
            else:
                if PyCleanUI.Assets.Cursors.get_cursor() == "input":
                    PyCleanUI.Assets.Cursors.set_cursor("normal")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    widget.set_state(state="inactive")
                    widget.render()
                    pygame.display.flip()
                continue
            break
        else:
            continue
        break



""" get source of custom event """
def get_source(window, event):
    if event != None:
        return {"name": window.widgets[event.custom_type-1].text, "index": event.custom_type}
