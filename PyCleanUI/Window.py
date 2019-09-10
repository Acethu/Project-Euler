import pygame
import PyCleanUI.LayoutHandler
import PyCleanUI.UpdateHandler
import PyCleanUI.events.EventHandler
import PyCleanUI.assets.Cursors
import sys

class Window:

    """ initialisation """
    def __init__(self, title, style, layout):
        self.title = title
        self.style = style
        self.layout = layout
        self.widgets = []
        self.fps = 30
        self.running = True
        self.pgInit() # -> class method
        self.pycleanuiInit() # -> class method

    def pgInit(self):
        pygame.init() # init pygame
        # window
        self.display = pygame.display.set_mode((500, 300)) # window
        pygame.display.set_caption(self.title) # title
        # fps
        self.clock = pygame.time.Clock()
        # font
        pygame.font.init() # init pygame.font
        self.font = pygame.font.Font(self.style["font"]["file"], self.style["font"]["size"])

    def pycleanuiInit(self):
        # cursors
        PyCleanUI.assets.Cursors.init(self)
        PyCleanUI.assets.Cursors.set_cursor("normal")
        # setup display
        PyCleanUI.LayoutHandler.setup_render(self) # setup the layout
        self.display.fill(self.style["background"]["color"]) # background color
        PyCleanUI.LayoutHandler.render(self) # render
        pygame.display.flip() # update window

    """ every tick """
    def update(self):
        self.event = None
        self.custom_event = None
        # check for pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.USEREVENT:
                self.custom_event = event

            PyCleanUI.events.EventHandler.handle_event(self, event)
            self.event = event
        # every tick
        PyCleanUI.UpdateHandler.handle_update(self, self.event)
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
