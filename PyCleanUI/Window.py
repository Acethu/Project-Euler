import pygame
from PyCleanUI.Style import STYLE
import PyCleanUI.LayoutHandler
import PyCleanUI.EventHandler
import PyCleanUI.assets.Cursors
import sys

class Window:

    """ initialisation """
    def __init__(self, title, layout):
        self.title = title
        self.layout = layout
        self.widgets = []
        self.running = True
        self.pgInit() # -> class method

    """ pygame initialisation stuff """
    def pgInit(self):
        pygame.init()
        self.display = pygame.display.set_mode((500, 300)) # window
        pygame.display.set_caption(self.title) # title

        pygame.font.init() # allow font usage
        self.font = pygame.font.Font(STYLE["font"]["file"], STYLE["font"]["size"])

        PyCleanUI.assets.Cursors.set_cursor("normal")

        PyCleanUI.LayoutHandler.setup_render(self) # setup the layout
        self.display.fill(STYLE["background"]["color"]) # background color
        PyCleanUI.LayoutHandler.render(self) # file
        pygame.display.flip() # update window

    """ every tick"""
    def loop(self):
        self.event = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            #elif event.type in [pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]:
                #PyCleanUI.EventHandler.test_change(self, event)
            elif event.type == pygame.USEREVENT:
                self.event = event
            PyCleanUI.EventHandler.test_change(self, event)

    def is_running(self):
        return self.running

    """ get current window event - can be NoneType Object """
    def get_event(self):
        return PyCleanUI.EventHandler.get_source(self, self.event)

    def get_values(self):
        return PyCleanUI.EventHandler.get_values(self)

    """ close the window - uninitialize pygame """
    def close(self):
        pygame.display.quit()
        pygame.quit()
        sys.exit()
