# terminalEnv
A terminal shell environment with support for a couple of other programs written in Python - should work on any Unix-based Operating System. Sort of like a terminal-desktop environment for developers?!

When you run the `main.py` file, it launches you straight into the app launcher, where you can run many apps (most of them aren't completed yet), including a terminal shell, calendar, file browser, task monitor, etc.

When you open a program, it can only run one program at a time - right now it a stacking window manager, however it is very limited as you can only open one window at a time, and you can't switch between windows, etc.

# Usage:
Prerequisites:
* Python 3

Just run `python3 main.py` to run the program. When the program starts, you will see an app launcher screen with some options for apps you can use.

# Contributing
I am looking for contributers to help with this project, especially with things like the applications (or anything else you would like to help with), because there are quite a few of them to do.

# Future plans

* At some point soon, this wikipedia page may become helpful: https://en.wikipedia.org/wiki/Box-drawing_character

## Here is a list of planned apps, and how close they are to being completed:
* Terminal Shell (Mostly Completed - [things like autocomplete, etc aren't implemented yet])
* Default System Text Editor (Not started - [probably use the curses module])
* Software Planning Tool (Half finished)
* Games Library (Not Started - [Probably use curses for some things, and text based things for other things])
* Settings (Not Started - [Change things like default system colors, etc])

## Here is a list of potential ideas for the future:
* Calendar
* Web Browser
* Email Client
* Task Monitor
* File Browser
* Development Library (Not sure how to do it yet, but maybe a python library (canvas.py or something to link up to automatically) where you can create graphical programs with the program.)