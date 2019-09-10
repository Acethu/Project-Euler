import pygame

class Input:
    def __init__(self, text="", width=None):
        self.text = text
        self.width = width
        self.state = "inactive"

    """ prerender pygame surface """
    def setup_render(self, window, position):
        self.window = window
        self.position = position

        if self.width == None:
            self.width = self.window.style["input"]["width"]

        self.pg_text = self.font.render(self.text, True, self.window.style["font"]["color"])

        self.pg_rect = pygame.Rect(self.position[0], self.position[1], self.get_size()[0], self.get_size()[1])

        self.text_pos = (self.position[0] + self.window.style["padding"], self.position[1] + self.window.style["padding"])

    """ render """
    def render(self):
        pygame.draw.rect(self.window.display, self.window.style["input"][self.state], self.pg_rect)
        self.window.display.blit(self.pg_text, self.text_pos)

    """ setters """
    # set widget font
    def set_font(self, font):
        self.font = font

    # set state -> active, inactive
    def set_state(self, state):
        self.state = state

    # set text (string)
    def set_text(self, text):
        self.text = text
        if self.font.render(self.text, True, self.window.style["font"]["color"]).get_width() > self.get_size()[0] - self.window.style["padding"]*2:
            self.text = self.text[:-1]
        self.pg_text = self.font.render(self.text, True, self.window.style["font"]["color"])

    """ getters """
    # return pg_rect
    def get_rect(self):
        return self.pg_rect

    # return state -> active / inactive
    def get_state(self):
        return self.state

    # return widget pixel size
    def get_size(self):
        return (self.width + self.window.style["padding"]*2, self.font.get_height() + self.window.style["padding"]*2)

    # return text
    def get_text(self):
        return self.text
