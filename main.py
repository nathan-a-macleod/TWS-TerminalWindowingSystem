import curses                        # For the core of the main user interface
from curses.textpad import Textbox   # Mainly for the software planner
import sys                           # For exiting the program (sys.exit)
import terminalShell                 # terminalShell.py file
import random                        # For the number guessing game

version = "0.2.0"

# Function for curses to get input, then enter, similar to getch() (but lets the user press enter) - need to make backspace and arrow keys work
def getInput(stdscr, y, x, prompt, colorPair):
    stdscr.addstr(y, x, prompt, colorPair)

    string = ""

    while True:
        char = stdscr.getkey()

        if ord(char) == 10:
            break

        string += char

    return string

# Function to create a new window, with the correct size, etc
def createNewWindow(stdscrRoot, title):
    stdscr = curses.newwin(curses.LINES-1, curses.COLS, 1, 0)
    stdscr.bkgd(" ", curses.color_pair(3))
    stdscr.border()
    stdscr.addstr(0, 0, title)
    stdscr.refresh()
    
    return stdscr

# stdscrRoot is the root app launcher window...
def softwarePlanner(stdscrRoot):
    stdscr = createNewWindow(stdscrRoot, "S O F T W A R E   P L A N N E R")
    stdscr.addstr(1, 1, "Welcome to the software planner - why not plan out some software in here? Press Ctrl-G to exit.")
    for i in range(0, curses.COLS):
        if i == 0:
            stdscr.addstr(2, 0, "\u251c")

        elif i == curses.COLS-1:
            stdscr.addstr(2, i, "\u2524")

        else:
            stdscr.addstr(2, i, "\u2500")
    stdscr.refresh()

    editWin = curses.newwin(curses.LINES-5, curses.COLS-2, 4, 1)
    editWin.bkgd(" ", curses.color_pair(3))

    with open("softwarePlannerText.txt", "r") as file:
        for i, line in enumerate(file):
            editWin.addstr(i, 0, line)
    file.close()

    box = Textbox(editWin)
    box.edit()

    editWin.refresh()

    file = open("softwarePlannerText.txt","w")
    file.write(box.gather())
    file.close()

    stdscr.refresh()
    stdscrRoot.refresh()

def helpWindow(stdscr):
    helpWin = createNewWindow(stdscr, "H E L P")

    # To inset the text inside it so that it works with the border, create another window which is smaller than the main 'helpWin'
    textWin = curses.newwin(curses.LINES-3, curses.COLS-2, 2, 1)
    textWin.bkgd(" ", curses.color_pair(3))
    textWin.addstr(1, 0, "This is a terminal shell environment with support for a couple of other programs written in Python and it should work on any Unix-based Operating System.\nYou can think of it sort of like a terminal-desktop environment for developers - but it is really just a terminal shell with a few other programs.\n\nIts Github page is at https://github.com/nathan-a-macleod/terminalEnv\n\nPress any key to close this window...")
    textWin.refresh()

    helpWin.refresh()
    helpWin.getch()

def appLauncher(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.clear()
    curses.curs_set(1)

    appLauncherWin = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    appLauncherWin.bkgd(" ", curses.color_pair(3))

    # Header at the top of the screen
    menuTitleStr = " A P P   L A U N C H E R "

    for i in range(0, curses.COLS//2-len(menuTitleStr)//2):
        appLauncherWin.addstr(0, int(i), "\u2592", curses.color_pair(2))

    appLauncherWin.addstr(0, curses.COLS//2-len(menuTitleStr)//2, menuTitleStr, curses.color_pair(1))

    for i in range(curses.COLS//2+len(menuTitleStr)//2+1, curses.COLS):
        appLauncherWin.addstr(0, int(i), "\u2592", curses.color_pair(2))

    # Options for other apps:
    appLauncherWin.addstr(2, 2, "[>] 1. Exit To Shell")
    appLauncherWin.addstr(3, 2, "[=] 2. Software Planner")
    appLauncherWin.addstr(4, 2, "[\u25a1] 3. File Manager")
    appLauncherWin.addstr(5, 2, "[\u2592] 4. Settings")
    appLauncherWin.addstr(6, 2, "--------------------")
    appLauncherWin.addstr(7, 2, "[?] 5. HELP")
    appLauncherWin.addstr(8, 2, "[x] 6. EXIT")

    appLauncherWin.refresh()

    # Get input from the user
    #option = appLauncherWin.getstr(curses.COLS-1, 2)
    curses.echo()
    option = getInput(appLauncherWin, curses.LINES-2, 2, "Enter an option (1-6): ", curses.color_pair(3))
    curses.noecho()

    if option == "1":
        curses.endwin()
        terminalShell.terminalShell()

    elif option == "2":
        softwarePlanner(stdscr)

    elif option == "5":
        helpWindow(stdscr)

    elif option == "6":
        sys.exit()

    curses.endwin()
    curses.wrapper(appLauncher)

# Something containing the version number, and maybe some ascii art (logo or something) - then it says to press any key to continue.
def bootupScreen(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    stdscr.border()

    curses.noecho()
    curses.curs_set(0)

    bootupMessage1 = "Version " + version
    bootupMessage2 = "Press any key to continue..."
    
    stdscr.bkgd(" ", curses.color_pair(1))
    stdscr.addstr(curses.LINES//2-1, curses.COLS//2-len(bootupMessage1)//2, bootupMessage1)
    stdscr.addstr(curses.LINES//2, curses.COLS//2-len(bootupMessage2)//2, bootupMessage2)

    stdscr.getch()
    curses.endwin()

curses.wrapper(bootupScreen)
curses.wrapper(appLauncher)
