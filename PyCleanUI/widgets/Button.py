import pygame
from PyCleanUI.Style import STYLE

class Button:
    def __init__(self, text="", padx=None):
        self.text = text
        self.padx = padx
        self.state = "normal"

    """ prerender pygame surface """
    def setup_render(self, window, position):
        self.window = window
        self.position = position

        self.pg_text = self.font.render(self.text, True, STYLE["font"]["color"])
        self.pg_rect = pygame.Rect(self.position[0], self.position[1], self.get_size()[0], self.get_size()[1])

        if self.padx is not None:
            self.text_pos = (self.position[0] + self.get_size()[0]/2 - self.pg_text.get_width()/2, self.position[1] + STYLE["padding"])
        else:
            self.text_pos = (self.position[0] + STYLE["padding"], self.position[1] + STYLE["padding"])

    """ render """
    def render(self):
        pygame.draw.rect(self.window.display, STYLE["button"][self.state], self.pg_rect)
        self.window.display.blit(self.pg_text, self.text_pos)

    """ setters """
    # set font
    def set_font(self, font):
        self.font = font

    # set state -> normal / hover / click
    def set_state(self, state):
        self.state = state

    """ getters """
    # return pg_rect
    def get_rect(self):
        return self.pg_rect

    # return state -> normal / hover / click
    def get_state(self):
        return self.state

    # return widget px size
    def get_size(self):
        if self.padx is not None:
            return (self.padx + self.pg_text.get_width() + STYLE["padding"]*2, self.pg_text.get_height() + STYLE["padding"]*2)
        return (self.pg_text.get_width() + STYLE["padding"]*2, self.pg_text.get_height() + STYLE["padding"]*2)
