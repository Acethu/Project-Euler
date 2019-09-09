import pygame
from PyCleanUI.Style import STYLE
import PyCleanUI.LayoutHandler
import PyCleanUI.events.EventHandler
import PyCleanUI.assets.Cursors
import sys

class Window:

    """ initialisation """
    def __init__(self, title, layout):
        self.title = title
        self.layout = layout
        self.widgets = []
        self.frame = 0
        self.fps = 30
        self.running = True
        self.pgInit() # -> class method

    """ pygame initialisation stuff """
    def pgInit(self):
        pygame.init()
        self.display = pygame.display.set_mode((500, 300)) # window
        # window settings
        pygame.display.set_caption(self.title) # title

        self.clock = pygame.time.Clock()

        pygame.font.init() # allow font usage
        self.font = pygame.font.Font(STYLE["font"]["file"], STYLE["font"]["size"])

        PyCleanUI.assets.Cursors.set_cursor("normal")

        PyCleanUI.LayoutHandler.setup_render(self) # setup the layout
        self.display.fill(STYLE["background"]["color"]) # background color
        PyCleanUI.LayoutHandler.render(self) # file
        pygame.display.flip() # update window

    """ every tick"""
    def update(self):
        self.frame += 1
        self.custom_event = None
        # check for pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.USEREVENT:
                self.custom_event = event

            PyCleanUI.events.EventHandler.handle_event(self, event)

        self.clock.tick(self.fps) #fps

    def is_running(self):
        return self.running

    """ get current window event - can be NoneType Object """
    def get_event(self):
        return PyCleanUI.events.EventHandler.get_source(self, self.custom_event)

    def get_values(self):
        return PyCleanUI.events.EventHandler.get_values(self)

    """ close the window - uninitialize pygame """
    def close(self):
        self.is_running = False
        pygame.display.quit()
        pygame.quit()
        sys.exit()
