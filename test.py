import pygame
from PyCleanUI.Window import Window
from PyCleanUI.widgets.Text import Text
from PyCleanUI.widgets.Button import Button
from PyCleanUI.widgets.Input import Input
layout = [
    Text("Fill in these boxes"),
    [Text("Name: "), Input("")],
    [Text("Password: "), Input("")],
    Button("Done"),
]

window = Window("Hello world", layout)

while window.is_running():
    window.loop()
    if window.get_event() is not None:
        print(window.get_event(), window.get_values())

window.close()
