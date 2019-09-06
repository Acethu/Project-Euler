import pygame
import pygame.locals

from PyCleanUI.Style import STYLE
import PyCleanUI.assets.Cursors

import PyCleanUI.events.ButtonHandler
import PyCleanUI.events.InputHandler

import PyCleanUI.widgets.Button
import PyCleanUI.widgets.Input

""" test for visual changes to be made due to an event """
def handle_event(window, event):
    index = 0
    for widget in window.widgets:
        index += 1
        # handle event on 'Button'
        if type(widget) == PyCleanUI.widgets.Button.Button: # if widget is a button
            PyCleanUI.events.ButtonHandler.handle_button(widget, event, index)
        # handle event on 'Input'
        elif type(widget) == PyCleanUI.widgets.Input.Input: # if widget is a input
            PyCleanUI.events.InputHandler.handle_input(window, widget, event)


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
                {"index": index, "value":widget.get_text()}
            )
    return values
