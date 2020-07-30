# Import the curses library...
import curses
import os
import random
# ...and some other files
from TWS.windowClass import *
from TWS.screenCycle import *

icons = ["*", "^", "@", "#", "~", "\u2591", "\u039E"]

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
    stdscr.timeout(500)
    
    # The core of the program
    def appLauncherFunction(window, key, selectedButtonID):
        if selectedButtonID == "endSession":
            exit()

        else:
            try:
                if selectedButtonID != 0:
                    exec(open("Programs/" + selectedButtonID).read())

            except:
                pass

    scr = Screen(stdscr)
    appLauncher = Window(curses.LINES//9, curses.COLS//9, int(curses.LINES/1.2)-10, int(curses.COLS/1.3), "TWS-App_Launcher", appLauncherFunction)
    appLauncher.addString(1, 2, "Use arrow keys to highlight an option and <ENTER> to 'click' an option.")

    # Create a button for each file in the 'Programs' directory
    idx = 0
    for program in os.listdir("./Programs"):
        idx += 1

        # If the file has "." as the first letter it's a hidden file. If it's a folder, it can't be run directly
        if program[0] != "." and os.path.isfile(os.getcwd() + "/Programs/" + program):
            icon = random.choice(icons)
            appLauncher.addButton(str(program), idx+2, 2, "[" + icon + "] " + str(program)[:-3])
            icons.remove(icon)

        else:
            idx -= 1

    appLauncher.addButton("endSession", int(curses.LINES/1.2)-12, 2, "[x] End Session")
    scr.mainloop()

    # Update the screen and wait for 1 second (curses.napms())
    stdscr.refresh()
    curses.napms(1000)

curses.wrapper(main)