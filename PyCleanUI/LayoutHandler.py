import pygame
import PyCleanUI

""" create pygame Renders, determine position of widgets """
def setup_render(window):
    padding = window.style["padding"]
    nx = padding
    ny = padding

    greatest_nx = 0

    for item in window.layout:
        if isinstance(item, list): # case: list of widgets
            for widget in item:
                widget.set_font(window.font)
                widget.setup_render(window, (nx, ny))
                window.widgets.append(widget)
                nx += widget.get_size()[0] + padding # width

            greatest_height = get_greatest_height(item)

            for widget in item: # allign the y position
                height = widget.get_size()[1]
                if height < greatest_height:
                    widget.setup_render(window, (widget.position[0], ny + (greatest_height-height)/2))

            if nx > greatest_nx:
                greatest_nx = nx

            nx = padding
            ny += greatest_height + padding # chose the one with the highest height

        else: # case: widget
            item.set_font(window.font)
            item.setup_render(window, (nx, ny))
            window.widgets.append(item)
            ny += item.get_size()[1] + padding # height # mind fuck stuff - please dont touch

            if item.get_size()[0] > greatest_nx:
                greatest_nx = item.get_size()[0] + padding*2

    pygame.display.set_mode((greatest_nx, ny))

""" render layout of a Window"""
def render(window):
    for widget in window.widgets:
        widget.render()


""" gets the greatest height of a list of widgets"""
def get_greatest_height(list):
    greatest_height = 0
    for widget in list:
        height = widget.get_size()[1]
        if height > greatest_height:
            greatest_height = height
    return greatest_height
