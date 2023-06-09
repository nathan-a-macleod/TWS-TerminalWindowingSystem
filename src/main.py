#!/usr/bin/python3
# Import the curses library...
import curses
# Import some other libraries
import os
import random
import re
from pathlib import Path
# ...and some other files to deal with managing windows
from CoreLib.Windows.windowClass import *
from CoreLib.screenCycle import *
from CoreLib.setcolor import SetThemeColors
def main(stdscr):
    SetThemeColors()

# Stdscr settings

    curses.curs_set(0)
    stdscr.bkgd(" ", curses.color_pair(3))
    stdscr.refresh()

# The bootup screen:

    LineDict = {
    0 : "╔═══════════════════════════════════════════════════════╗",
    1 : "║       Welcome to TWS-TerminalWindowingSystem!         ║",
    2 : "║To access help at any time, press '?' on your keyboard.║",
    3 : "║           Press any key to continue...                ║",
    4 : "╚═══════════════════════════════════════════════════════╝"
    }

# A bunch of math to figure out where to start the line at so the text is centered, no matter what, unless it is above the top or bottom of the screen
 
    scrline = int(round((((len(LineDict)/2)-1)*-1), 0))
    txtline = 0

#The Welcome Message Drawing Code

    for lines in range(len(LineDict)): #Run for as many lines there are in the welcome screen
        #(Y,X,Text)
        #Add the text of LineDict[txtline] to the screen     
        try:
            stdscr.addstr(
        curses.LINES//2+scrline, #Y
        curses.COLS//2-len(LineDict[txtline])//2,#X
        LineDict[txtline] #Text
        )
        except:
            break

        scrline += 1 # make the screen go down a line for printing the next line
        txtline += 1 # tell us to read from a different index of LineDict
#Screen refresh and set timeout
    stdscr.getch() #refresh the screen and wait for the user to hit a key
    stdscr.timeout(500) # Set the timeout from now on

# The core of the program

    scr = Screen(stdscr)
    scr.mainloop()

# Update the screen and wait for 1 second (curses.napms())

    stdscr.refresh()
    curses.napms(1000) # 1 second = 1000 milliseconds

curses.wrapper(main) #Start Curses from the Main function
