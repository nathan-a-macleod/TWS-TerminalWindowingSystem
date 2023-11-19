# TWS-TerminalWindowingSystem
A terminal shell environment with support for a couple of other programs written in Python - should work on any Unix-based Operating System. Sort of like a terminal-desktop environment...

When you run the `main.py` file, it launches you straight into the app launcher, where you can run many apps (most of them aren't completed yet), including a terminal shell, calendar, file browser, CPU monitor, etc.

# Usage:
Prerequisites:
* Python 3
* Python `psutil` package - `pip3 install psutil`

Just run `python3 main.py` from inside the `src/` folder to run the program. When the program starts, you will see an app launcher screen with all the installed apps.

You can also do `chmod +x main.y` from inside the `src/` folder then, run `./main.py` instead

## Controls:
* Up & Down Arrow Keys or K(Up) and J(Down): Highlight a selection.
* Left & right Arrow Keys: Focuses a different window. 
* ENTER: 'Click' a selection.
* Q, E (UpperCase), PgUp, PgDn: Scrolling vertically.
* Q, E (LowerCase) or Insert(Right) and Delete(Left): Scrolling horizontally.
* W, A, S, D (UpperCase): Move Current Window
* W, A, S, D (LowerCase): Resize Current Window
* R (UpperCase): Roll Up The Current Window (But Keep It Focused)
* R (LowerCase): Maximize Current Window
* ".": Toggle between showing & hiding the desktop.

# Contributing
I am looking for contributers to help with this project, especially with things like the applications (or anything else you would like to help with), because there are quite a few of them to do.

# Future plans

* This Wikipedia page is very helpful (Unicode Characters): https://en.wikipedia.org/wiki/Box-drawing_character

## A list of apps & how close they are to being completed:
* A way to develop custom apps (Ongoing).
* Clock (Completed)
* CPU Monitor (Completed)
* Terminal Shell (Completed)
* Help Page (Mostly completed)
* Default System Text Editor (Not started)
* File Manager (In Progress)
* Settings (In Progress - [For changing things like default system colors(Done), etc])

## A list of potential ideas for the future:
* Calendar
* Web Browser [somewhat ready, currently just runs ELinks]
* Email Client

# Images:

![screenShot1](https://github.com/RobiTheGit/TWS-TerminalWindowingSystem/assets/94720060/eb27d1e9-b1a1-4f74-8173-cff0b0b5227c)

![screenShot2](https://github.com/RobiTheGit/TWS-TerminalWindowingSystem/assets/94720060/2a0f4bf3-e8e8-41ab-b120-8e4f70500e6f)


![image3](/images/screenShot3.png)

# How to create an app
Recently, the process of creating and installing another app has become much easier. Here is how.
1. Add a new folder in `src/Programs` with any name.
2. Inside that folder, create a file called `main.py`, and another called `TWSProgram.txt`
3. Inside `TWSProgram.txt`, put the following lines of code:
```
displayname="name_of_your_program"
displaysymbol="symbol_to_be_displayed"
```
* You must format it exactly like it is shown because of how the file is detected. Remember, `displaysymbol` is a single character to be displayed in the app launcher screen.
2. Then, begin coding the app in `main.py`! An example is in `src/Programs/TWS-Example/main.py`:
If you would like more explaination than this, feel free to create an issue in the github page.
