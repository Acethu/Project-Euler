# imports
from PyCleanUI.Window import Window
from PyCleanUI.widgets.Text import Text # text label to display a string of text
from PyCleanUI.widgets.Button import Button # simple button with text
from PyCleanUI.widgets.Input import Input # simple input
# layout
layout = [
    Text("Fill in these boxes"),
    Text("Name:"),
    Input("", width=400), # width *optional
    Text("Email:"),
    Input("", width=400),
    [Button("Done"), Button("Cancel")]
]
# window
window = Window("PyCleanUI Tutorial", layout)
# main loop
while window.is_running():
    window.update() # always update the window before getting events
    if window.get_event() is not None: # on event
        print("event:", window.get_event()) # returns information about the event, that has been pressed
        print("values:", window.get_values()) # returns values of the inputs
        window.close() # closes window, after 'Done' button is pressed

window.close() # always close the window properly
