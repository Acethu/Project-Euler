# PyCleanUI
#### version 1.0

PyCleanUI is a python library inspired by [ PySimpleGUI ](https://github.com/PySimpleGUI/PySimpleGUI). PyCleanUI windows are non-native and custom, made with the python library [ pygame](https://pygame.org), so to use PyCleanUI you need pygame installed on your system. It is very easy to learn and to understand and has an adjustable clean style.

## Table of contents
### 1. [ Tutorial ](#1-tutorial)
 - [ Basic Window ](#basic-window)
### 2. [ Core Principles ](#2-core-principles)
 - [ Events & Values ](#1-events--values)
 - [ Widgets ](#2-widgets)
 - [ Style ](#3-style)
 - [ Layout ](#4-layout)
### 3. [ Q&A ](#3-qa)
 - [ 1. Is PyCleanUI multiplatform, does it work on Mac & Linux too? ](#q1)
 - [ 2. Will PyCleanUI get updated (frequently)? ](#q2)
 - [ 3. Is there a way to make resizeable windows in PyCleanUI? ](#q3)

## 1. Tutorial
#### Basic Window
``` python
# imports
# PyCleanUI
from PyCleanUI.Window import Window
from PyCleanUI.widgets.Text import Text # text label to display a string of text
from PyCleanUI.widgets.Button import Button # simple button with text
from PyCleanUI.widgets.Input import Input # simple input
# Style
from Style import style
# layout
layout = [
    Text("Fill in these boxes"),
    Text("Name:"),
    Input("", width=400), # width *optional
    Text("Email:"),
    Input("", width=400),
    [Button("Done", width=240), Button("Cancel", width=150)]
]
# window
window = Window("PyCleanUI Tutorial", style, layout)
# main loop
while window.is_running():
    window.update() # always update the window before getting events
    if window.get_event() is not None: # on event
        print("event:", window.get_event()) # returns information about the event, that has been pressed
        print("values:", window.get_values()) # returns values of the inputs
        if window.get_event()["name"] == "Cancel":
            window.close() # closes window, when 'Cancel' button is pressed

window.close() # always close the window properly
```
*(on windows)*

![alt text](https://i.pinimg.com/originals/3e/f3/04/3ef304635f521b582b6def9ae05b3e3a.png)
![alt text](https://i.pinimg.com/originals/73/03/6a/73036a5e793bca42bc894c9c4a7d749b.png)

Now, when you press the 'Done' Button, the Window should close and the console should log something like this:
``` python
event: {'index': 6, 'name': 'Done'}
values: [{'index': 3, 'value': 'my_name'}, {'index': 5, 'value': 'my@mail.com'}]
```

***'index'*** - describes the Widgets index in the Windows Layout

***'name'*** - is the name (text) of the Button

***'values'*** - returns a list of dictionaries with an *'index'* and the *'value'* of an Input

With this information you should now be able to create your own simple UI applications.

You can find a copy of the [ basic_window.py ](basic_window.py) file in this repository.

## 2. Core Principles
### 1. Events & Values
#### 1.1 Events
An event in PyCleanUI is e.g. when a Button gets clicked.

You can get the current Event with:
``` python
window.get_event()
```

If you were to print out that Event, it would look somewhat like this:
```python
print(window.get_event())
>>> {'index': 1, 'name': 'Testbutton'}
```

Note that *window.get_event()* can return also *None*. So to only get actual Events you can do:
``` python
if window.get_event() is not None:
    # on actual event
```

#### 1.2 Values
A value in PyCleanUI is e.g. the Value (text) of an input.

You can get a list of all Values of a Window with:
``` python
window.get_values()
```

*window.get_values()* would return something like this, if you were to print it out:
```python
print(window.get_values())
>>> [{'index': 1, 'value': 'my_name'}, {'index': 2, 'value': 'my@mail.com'}]
```

***'index'*** - describes the Inputs index in the Windows layout

***'value'*** - is the *'value'* (text) of an input

A good way to get the *'values'* of your Window, is to make a 'Submit' or 'Done' Button:
```python
if window.get_event() is not None:
    if window.get_event()['name'] == 'Submit' # or 'Done'
        values = window.get_values()
```

### 2. Widgets
Widgets in PyCleanUI are the elements on screen that you can interact with and see.
#### 2.1 Text
The Text Widget displays a string (text) onto the Window.

Parameters:

- text (*string*)
#### 2.2 Button
The Button Widget is an interactable Widget, that you can click on. It can also display text.

Parameters:

- text (*string*)
- padx (*int*) # extra width (in px)
#### 2.3 Input
The Input Widget is an interactable Widget, that you input text.

Parameters:

- text (*string*) # text on start
- width (*int*) # width (in px)
### 3. Style
The Style in PyCleanUI determines the look of the Window, the Layout and the Widgets.

To see all the different options or to change the Style, you can take a look at the *Style.py* file, which you can find [here](PyCleanUI/Style.py).
### 4. Layout
With a Layout you can decide how the Widgets in your Window are packed.

A Layout in PyCleanUI is a list with the Widgets inside:
```python
layout = [
    Text("My Text"),
    Button("Done")
]
```

You can also pack Widgets horizontally like this:
```python
layout = [
    [Text("My Text"), Input()],
    Button("Done")
]
```

After creating a Layout, you also have to apply it to your Window:
```python
window = Window("Name", layout)
```

## 3. Q&A
*(questions & answers)*

<a name="q1"></a>
### 1. Is PyCleanUI multiplatform, does it work on Mac & Linux too?

*To be honest, I don't know. It should work fine. Just test it out and tell me.*

<a name="q2"></a>
### 2. Will PyCleanUI get updated (frequently)?

*Right now, PyCleanUI is in a state, where I am happy with it and it fits my needs. It is in no ways finished or very well polished though. So maybe in the future I will add new widgets, etc.. If you wan't more features, tell me, or if you want, you can add them yourself.*

<a name="q3"></a>
### 3. Is there a way to make resizeable windows in PyCleanUI?

*Sadly, there isn't, and I'm not going to implement that, because it would be way to hard to implement resizable widgets.*
