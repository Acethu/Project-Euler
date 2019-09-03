import pygame
from PyCleanUI.Style import STYLE
import PyCleanUI.LayoutHandler
import PyCleanUI.EventHandler

class Window:

    """ initialisation """
    def __init__(self, title, layout):
        self.title = title
        self.layout = layout
        self.widgets = []
        self.pgInit() # -> class method
        self.loop() # -> class method | window main loop

    """ pygame initialisation stuff """
    def pgInit(self):
        self.display = pygame.display.set_mode((500, 300)) # window
        pygame.display.set_caption(self.title) # title

        pygame.font.init() # allow font usage
        self.font = pygame.font.SysFont(STYLE["font"]["type"], STYLE["font"]["size"])

        PyCleanUI.LayoutHandler.setup_render(self) # setup the layout
        self.display.fill(STYLE["background"]["color"]) # background color
        PyCleanUI.LayoutHandler.render(self) # file
        pygame.display.flip() # update window

    """ Window Loop"""
    def loop(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type in [pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]:
                    self.update(event)

    """ every event """
    def update(self, event):
        PyCleanUI.EventHandler.test_change(self, event)

    """ stuff to add later """
    def read(self):
        return pygame.event.get()

    def close(self):
        pygame.quit()
