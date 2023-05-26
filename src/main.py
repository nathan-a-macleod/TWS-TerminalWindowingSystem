#!/usr/bin/python3
# Import the curses library...
import curses
import os
import random
import re
# ...and some other files
from CoreLib.Windows.windowClass import *
from CoreLib.screenCycle import *
from pathlib import Path
bgclr = Path("bgclr.txt") #Note, the color has to be one of the 7 default colors
if bgclr.exists():
    f = open("bgclr.txt", "r")
else:
    os.system("touch bgclr.txt")
    f = open("bgclr.txt", "w")
    f.write("blue")
    f.close()
    f = open("bgclr.txt", "r")  
x = f.read()
bgnd = re.sub("\n", '', x).lower()
colors = {
"blue" : curses.COLOR_BLUE,
"black" : curses.COLOR_BLACK,
"cyan" : curses.COLOR_CYAN,
"green" : curses.COLOR_GREEN,
"magenta" : curses.COLOR_MAGENTA,
"red" : curses.COLOR_RED,
"white" : curses.COLOR_WHITE,
"yellow" : curses.COLOR_YELLOW
}

blue = colors["blue"] #Can have white text
black = colors["black"] #Can have white text
cyan = colors["cyan"] #Can't have white text (readability)
green = colors["green"] #Can have white text
magenta = colors["magenta"] #Can't have white text (readability)
red = colors["red"] #Can have white text
white = colors["white"] #Can't have white text (readability)
yellow = colors["yellow"] #Can't have white text (readability)
if bgnd == "white" or bgnd == "yellow" or bgnd == "cyan" or bgnd == "magenta":
    fg = "black"
else:
    fg = "white"
# The main function
def main(stdscr):
    # Color combinations
    curses.init_pair(1, black, yellow) # For the shadows
    curses.init_pair(2, black, white) # Same, but inverted
    try:
        curses.init_pair(3, colors[fg], colors[bgnd]) # The background color
    except:
        curses.init_pair(3, white, blue) # The background color       
         
    curses.init_pair(4, white, black) # For the titles
    
    # Stdscr settings
    curses.curs_set(0)
    stdscr.bkgd(" ", curses.color_pair(3))
    stdscr.refresh()
    # The bootup screen:
    line0 = "╔═══════════════════════════════════════════════════════╗"
    line1 = "║       Welcome to TWS-TerminalWindowingSystem!         ║"
    line2 = "║To access help at any time, press '?' on your keyboard.║"
    line3 = "║           Press any key to continue...                ║"
    line4 = "╚═══════════════════════════════════════════════════════╝"
    stdscr.addstr(curses.LINES//2-4, curses.COLS//2-len(line0)//2, line0)
    stdscr.addstr(curses.LINES//2-3, curses.COLS//2-len(line1)//2, line1)
    stdscr.addstr(curses.LINES//2-2, curses.COLS//2-len(line2)//2, line2)
    stdscr.addstr(curses.LINES//2-1, curses.COLS//2-len(line3)//2, line3)
    stdscr.addstr(curses.LINES//2, curses.COLS//2-len(line4)//2, line4)    
    stdscr.getch()
    stdscr.timeout(500) # Set the timeout from now on

    # The core of the program
    scr = Screen(stdscr)
    scr.mainloop()

    # Update the screen and wait for 1 second (curses.napms())
    stdscr.refresh()
    curses.napms(1000)

curses.wrapper(main)
