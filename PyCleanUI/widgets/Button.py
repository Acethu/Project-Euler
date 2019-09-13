import pygame

class Button:
    def __init__(self, text="", width=None):
        self.text = text
        self.width = width
        self.state = "normal"

    """ prerender pygame surface """
    def setup_render(self, window, position):
        self.window = window
        self.position = position

        self.pg_text = self.font.render(self.text, True, self.window.style["font"]["color"])

        if self.width == None:
            self.width = self.get_size()[0]
            
        self.pg_rect = pygame.Rect(self.position[0], self.position[1], self.get_size()[0], self.get_size()[1])


        if self.width:
            self.text_pos = (self.position[0] + self.get_size()[0]/2 - self.pg_text.get_width()/2, self.position[1] + self.window.style["padding"])
        else:
            self.text_pos = (self.position[0] + self.window.style["padding"], self.position[1] + self.window.style["padding"])

    """ render """
    def render(self):
        pygame.draw.rect(self.window.display, self.window.style["button"][self.state], self.pg_rect)
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
        if self.width:
            return (self.width, self.pg_text.get_height() + self.window.style["padding"]*2)
        return (self.pg_text.get_width() + self.window.style["padding"]*2, self.pg_text.get_height() + self.window.style["padding"]*2)
