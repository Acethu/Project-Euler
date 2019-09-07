# PyCleanUI
*(version 1.0)*

PyCleanUI is a python library inspired by PySimpleUI. It is made with pygame from scratch, it is very easy to learn and to understand and has an adjustable clean style.

## Table of contents
1. [ Beginner's Tutorial ](#begin)
2. [ Core Principles ](#core)
3. [ Q&A ](#qna)

<a name="begin"></a>
## 1. Beginner's Tutorial
*(basic window)*
``` python
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
    Button("Done")
]
# window
window = Window("PyCleanUI Tutorial", layout)
# main loop
while window.is_running():
    window.update() # always update the window before getting events
    if window.get_event() is not None: # on event
        print("event:", window.get_event()) # returns the button, that has been pressed
        print("values:", window.get_values()) # returns values of the inputs

window.close() # closes the window properly
```
*(on windows)*

![alt text](https://i.pinimg.com/originals/3e/f3/04/3ef304635f521b582b6def9ae05b3e3a.png)
![alt text](https://i.pinimg.com/originals/73/03/6a/73036a5e793bca42bc894c9c4a7d749b.png)

Now everytime you press the 'Done' button, the console should log something like this:
``` python
event: {'index': 6, 'name': 'Done'}
values: [{'index': 3, 'value': 'my_name'}, {'index': 5, 'value': 'my@mail.com'}]
```
***'index'*** - describes the widgets index in the windows layout

***'name'*** - is the text of the button

***'values'*** - returns a list of dictionaries with an *'index'* and the *'value'* of an input

With this information you should now be able to create your own simple UI applications.
For now there are no more widgets than these 3 ( Text(), Button() & Input() ), but I will add more in the future.

<a name="core"></a>
## 2. Core Principles
### 1. Event

An event in PyCleanUI is e.g. when a button gets clicked.

You can get the current event with:
``` python
window.get_event()
```

If you were to print out that event, it would look somewhat like this:
```python
print(window.get_event())
>> {'index': 1, 'name': 'Testbutton'}
```

Note that *window.get_event()* can return also *None*. So to only get actual events you can do:
``` python
if window.get_event() is not None:
    # on actual event
```

### 2. Values
### 3. Widgets
### 4. Style
### 5. Layout

<a name="qna"></a>
## 3. Q&A
*(questions & answers)*

**1. Is PyCleanUI multiplatform, does it work on Mac & Linux too?**

*To be honest, I don't know. It should work fine. Just test it out and tell me.*


**2. Will PyCleanUI get updated (frequently)?**

*Right now, PyCleanUI is in a state, where I am happy with it and it fits my needs. It is in no ways finished or very well polished though. So maybe in the future I will add new widgets, etc.. If you wan't more features, tell me, or if you want, you can add them yourself.*

