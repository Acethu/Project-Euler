import pygame
from PyCleanUI.Window import Window
from PyCleanUI.Widgets.Text import Text
from PyCleanUI.Widgets.Button import Button
from PyCleanUI.Widgets.Input import Input
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
