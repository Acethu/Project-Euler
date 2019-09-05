import pygame
import pygame.locals
import PyCleanUI
from PyCleanUI.Style import STYLE
import PyCleanUI.Cursors

""" test for visual changes to be made due to an event """
def test_change(window, event):
    index = 0
    for widget in window.widgets:
        index += 1
        """ Button """
        if type(widget) == PyCleanUI.Widgets.Button.Button: # if widget is a button
            # mouse over
            if widget.get_rect().collidepoint(pygame.mouse.get_pos()):
                PyCleanUI.Cursors.set_cursor("button")

                if event.type == pygame.MOUSEBUTTONDOWN: # if down
                    if event.button == 1:
                        widget.set_state(state="click")
                elif event.type == pygame.MOUSEBUTTONUP: # if click
                    if event.button == 1:
                        widget.set_state(state="hover")
                        pygame.event.post(pygame.event.Event(pygame.locals.USEREVENT,custom_type=index))
                elif widget.state == "normal": # on mouse enter
                    widget.set_state(state="hover")
                widget.render()
                pygame.display.flip()
                break # change found, so no need to check for other changes
            # mouse not over
            else:
                PyCleanUI.Cursors.set_cursor("normal")
                if widget.state == "hover" or widget.state == "click": # on mouse leave
                    widget.set_state(state="normal")
                    widget.render()
                    pygame.display.flip()
                    break # change found, so no need to check for other changes
                else:
                    continue
                break
            break
        else:
            continue
        break


""" get source of custom event """
def get_source(window, event):
    if event != None:
        return {"name": window.widgets[event.custom_type-1].text, "index": event.custom_type}

""" """
def has_event(event):
    if event == None:
        return False
    return True
