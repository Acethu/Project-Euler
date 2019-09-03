import pygame
from PyCleanUI.Window import Window
from PyCleanUI.Widgets.Text import Text
from PyCleanUI.Widgets.Button import Button

layout = [
    Text("Search Folder:"),
    [Text("'C:/Desktop'"), Button("Browse")]
]

window = Window("Hello world", layout)

while window.is_running():
    window.loop()
    if not window.get_event() is None:
        print(window.get_event())


window.close()
