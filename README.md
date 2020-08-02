# TWS-TerminalWindowingSystem
A terminal shell environment with support for a couple of other programs written in Python - should work on any Unix-based Operating System. Sort of like a terminal-desktop environment...

When you run the `main.py` file, it launches you straight into the app launcher, where you can run many apps (most of them aren't completed yet), including a terminal shell, calendar, file browser, CPU monitor, etc.

# Usage:
Prerequisites:
* Python 3
* Python `psutil` package - `pip3 install psutil`

Just run `python3 main.py` inside the `src/` folder to run the program. When the program starts, you will see an app launcher screen with all the installed apps.

## Basic Controls:
* Up & down Arrow Keys: Highlight a selection.
* Left & right Arrow Keys: Focuses a different window.                    
* ENTER: 'Click' a selection.
* WASD (UpperCase): Moves the selected window.
* Q, E (UpperCase): Scrolling.

# Contributing
I am looking for contributers to help with this project, especially with things like the applications (or anything else you would like to help with), because there are quite a few of them to do.

# Future plans

* This Wikipedia page is very helpful (Unicode Characters): https://en.wikipedia.org/wiki/Box-drawing_character

## A list of apps & how close they are to being completed:
* A way to develop custom apps (Ongoing).
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

# Images:
![image1](/images/screenShot1.png)

![image2](/images/screenShot2.png)

![image3](/images/screenShot3.png)

# How to create an app
Recently, the process of creating and installing another app has become much easier. Here is how.
1. Add a new file in `src/Programs` with whatever name you want.
2. Then, begin coding the app! An example is in `src/Programs/TWS-Example.py`:
If you would like more explaination than this, feel free to create an issue in the github page.
