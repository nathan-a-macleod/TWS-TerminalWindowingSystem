# TWS-TerminalWindowingSystem
A terminal shell environment with support for a couple of other programs written in Python - should work on any Unix-based Operating System. Sort of like a terminal-desktop environment...

When you run the `main.py` file, it launches you straight into the app launcher, where you can run many apps (most of them aren't completed yet), including a terminal shell, calendar, file browser, CPU monitor, etc.

# Usage:
Prerequisites:
* Python 3
* Python `psutil` package - `pip3 install psutil`

Just run `python3 main.py` to run the program. When the program starts, you will see an app launcher screen with some apps you can use.

## Basic Controls:
* Up & down Arrow Keys: Highlight a selection.
* Left & right Arrow Keys: Focuses a different window.                       
* <ENTER>: 'Click' a selection.
* WASD: Moves the selected window.

# Contributing
I am looking for contributers to help with this project, especially with things like the applications (or anything else you would like to help with), because there are quite a few of them to do.

# Future plans

* This Wikipedia page is very helpful (Unicode Characters): https://en.wikipedia.org/wiki/Box-drawing_character

## A list of apps & how close they are to being completed:
* Clock (Completed)
* CPU Monitor (Completed)
* Terminal Shell (Mostly Completed - [things like autocomplete, etc aren't implemented yet])
* Help Page (Mostly completed)
* Default System Text Editor (Not started)
* File Manager (Not started)
* Settings (Not Started - [For changing things like default system colors, etc])

## A list of potential ideas for the future:
* Calendar
* Web Browser
* Email Client
* Development Library (Not sure how to do it yet, but maybe a python library (canvas.py or something to link up to automatically) where you can create graphical programs with the program.)

# Images:
![image1](/images/screenShot1.png)

![image2](/images/screenShot2.png)

![image3](/images/screenShot3.png)

# How to create an app
Recently, the process of creating and installing another app has become much easier. Here is how.
1. Add a new file in `src/Programs` with whatever name you want.
2. For the first line, type `from TWS.windowClass import *`
3. Next you will want to create a window. Type `newWindow = Window(y, x, height, width, windowTitle, functionName)`. The parameters are as follows:
* `y` and `x` define the position of the window.
* `height` and `width` is the size of the window.
* `windowTitle` is the title of the window that appears at the bar at the top of the window.
* `functionName` is the name of the function that you need to create in step `4`:
4. Create a function with the same name as `functionName` with the following parameters: `window`, `key`, `selectedButtonID`.
5. In this function, you can import the rest of the libraries you need for your program. For example `import psutil`, etc.
6. Inside the function, you can do the logic of the program. There are a few functions you can use:
* `window.addString(4, 2, "Hello, World!")` will add a string inside the window at (y:4, x:2) with the text `Hello, World!`
* `window.closeWindow()` will close the window. (Usually used with a button [for example, `newWindow.addMenuButton("closeButton", 0, "Close Window")`] explained later.)

You can also detect key presses. For example:
`if key == ord("f"):`
`    window.addString(5, 2, "You pressed the 'f' key")`
Will add text saying `You pressed the 'f' key` at (y:5, x:2) if the 'f' key is pressed.

You can also do something if a button is pressed. For example:
`if selectedButtonID == "myFirstButton":`
`    window.addString(6, 2, "Thanks for pressing the button!")`
Will add the string `Thanks for pressing the button!` at (y:6, x:2).
But wait! Buttons won't work unless you do the following:

Outside the function, after the line creating the window, add the following line:
`newWindow.addButton(buttonID, y, x, text)`
OR
`newWindow.addMenuButton(buttonID, y, x, text)`
The parameters are:
* `buttonID` the ID of the button. For example `myFirstButton`.
* `y`, `x`, `text` are the y and x positions of the buttons, as well as the text.