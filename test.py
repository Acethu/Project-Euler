import pygame as pg
from PyCleanUI.Window import Window
from PyCleanUI.Widgets.Text import Text
from PyCleanUI.Widgets.Button import Button

layout = [
    Text("asdasdasd"),
    [Text("'C:/Desktop'"), Button("Browse")],
    Text("help")
]

window = Window("Hello world", layout)
window.close()
