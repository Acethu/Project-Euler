import pygame
from PyCleanUI.Style import STYLE


# automate this when more cursors are there, for now, i dont care

normal = pygame.cursors.compile(STYLE["cursors"]["normal"], 'X', '.', 'o')

button = pygame.cursors.compile(STYLE["cursors"]["button"], 'X', '.', 'o')

text = pygame.cursors.compile(STYLE["cursors"]["input"], 'X', '.', 'o')

def set_cursor(name):
    if name == "normal":
        pygame.mouse.set_cursor((24, 32), (0, 0), *normal)
    elif name == "button":
        pygame.mouse.set_cursor((24, 24), (6, 0), *button)
    elif name == "input":
        pygame.mouse.set_cursor((8, 24), (4, 12), *text)

def get_cursor():
        return self.name
