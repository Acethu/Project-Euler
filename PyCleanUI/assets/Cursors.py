import pygame


# initialize cursors
def init(window):
    global normal, button, _input
    normal = pygame.cursors.compile(window.style["cursors"]["normal"], 'X', '.', 'o')

    button = pygame.cursors.compile(window.style["cursors"]["button"], 'X', '.', 'o')

    _input = pygame.cursors.compile(window.style["cursors"]["input"], 'X', '.', 'o')

# set pygame cursor by name -> self.window.style
def set_cursor(name):
    if name == "normal":
        pygame.mouse.set_cursor((24, 32), (0, 0), *normal)
    elif name == "button":
        pygame.mouse.set_cursor((24, 24), (6, 0), *button)
    elif name == "input":
        pygame.mouse.set_cursor((8, 24), (4, 12), *_input)

# returns cursor name of current pygame cursor
def get_cursor():
    if pygame.mouse.get_cursor() == ((24, 32), (0, 0), *normal):
        return "normal"
    elif pygame.mouse.get_cursor() == ((24, 24), (6, 0), *button):
        return "button"
    elif pygame.mouse.get_cursor()[2] == _input[0]:
        return "input"
