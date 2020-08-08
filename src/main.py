# Import the curses library...
import curses
import os
import random
# ...and some other files
from CoreLib.Windows.windowClass import *
from CoreLib.screenCycle import *

# The main function
def main(stdscr):
    # Color combinations
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK) # For the shadows
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE) # Same, but inverted
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE) # The background color
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK) # For the titles

    # Stdscr settings
    curses.curs_set(0)
    stdscr.bkgd(" ", curses.color_pair(3))
    stdscr.refresh()
    
    # The bootup screen:
    line1 = "Welcome to TWS-TerminalWindowingSystem!"
    line2 = "To access help at any time, press '?' on your keyboard."
    line3 = "Press any key to continue..."
    stdscr.addstr(curses.LINES//2-3, curses.COLS//2-len(line1)//2, line1)
    stdscr.addstr(curses.LINES//2-2, curses.COLS//2-len(line2)//2, line2)
    stdscr.addstr(curses.LINES//2, curses.COLS//2-len(line3)//2, line3)
    stdscr.getch()
    stdscr.timeout(500) # Set the timeout from now on

    # The core of the program
    scr = Screen(stdscr)
    scr.mainloop()

    # Update the screen and wait for 1 second (curses.napms())
    stdscr.refresh()
    curses.napms(1000)

curses.wrapper(main)