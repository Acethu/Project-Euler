# imports
import tkinter.filedialog
# PyCleanUI
from PyCleanUI.Window import Window
from PyCleanUI.widgets.Text import Text # text label to display a string of text
from PyCleanUI.widgets.Button import Button # simple button with text
from PyCleanUI.widgets.Input import Input # simple input
# Style
from Style import style
# layout
layout = [
    Text("Select an Image"),
    [Text("Image File: ", width=90), Input("", width=200), Button("Browse", width=100)],
    [Button("Done", width=250), Button("Cancel", width=150)]
]
# window
window = Window("PyCleanUI Tutorial", style, layout)
# main loop
while window.is_running():
    window.update() # always update the window before getting events
    event = window.get_event()
    if event: # on event
        print("event:", window.get_event()) # returns information about the event, that has been pressed
        print("values:", window.get_values()) # returns values of the inputs
        if event["name"] == "Cancel":
            window.close() # closes window, when 'Cancel' button is pressed
        if event["name"] == "Browse":
            window.widgets[2].set_text("hi")


window.close() # always close the window properly
