import curses                                            # For the core of the main user interface
from applicationFunctions import *                       # applicationFunctions file - functions like getInput, getCtrlG, createNewWindow, etc
import sys                                               # For exiting the program (sys.exit)

# Programs
import applications.terminalShell as terminalShell       # terminalShell.py file
import applications.fileManager as fileManager           # fileManager.py file
import applications.softwarePlanner as softwarePlanner   # softwarePlanner file

version = "0.3.0"

# Window displaying some help - should really move this to another file inside the applications folder
def helpWindow():
    helpWin = createNewWindow("H E L P")

    helpWin.addstr(1, 1, "This is the help page - press Ctrl-G to exit.")

    hlineUnicode(helpWin)

    helpWin.refresh()

    # To inset the text inside it so that it works with the border, create another window which is smaller than the main 'helpWin'
    textWin = curses.newwin(curses.LINES-5, curses.COLS-2, 4, 1)
    textWin.bkgd(" ", curses.color_pair(3))
    
    textWin.addstr(0, 0, "This is a terminal shell environment with support for a couple of other programs written in Python and it should work on any Unix-based Operating System.\nYou can think of it sort of like a terminal-desktop environment for developers - but it is really just a terminal shell with a few other programs.\n\nThe Github page is at https://github.com/nathan-a-macleod/terminalEnv")
    textWin.refresh()

    helpWin.refresh()
    getCtrlG(helpWin)

def appLauncher(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)

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

    '''
    # Options for other apps:
    appLauncherWin.addstr(2, 2, "[>] 1. Exit To Shell")
    appLauncherWin.addstr(3, 2, "[=] 2. Software Planner")
    appLauncherWin.addstr(4, 2, "[\u25a1] 3. File Manager")
    appLauncherWin.addstr(5, 2, "-----------------------")
    appLauncherWin.addstr(6, 2, "[\u2592] 4. Settings")
    appLauncherWin.addstr(7, 2, "[?] 5. Help")
    appLauncherWin.addstr(8, 2, "[x] 6. Exit")
    '''

    appLauncherWin.hline(1, 0, " ", curses.COLS, curses.color_pair(4))
    appLauncherWin.addstr(1, 0, "[>] 1. Shell    [-] 2. Apps    [x] 3. Exit", curses.color_pair(4))
    appLauncherWin.refresh()

    # Get input from the user
    #option = appLauncherWin.getstr(curses.COLS-1, 2)
    setCursor(1)
    option = getInput(appLauncherWin, curses.LINES-2, 2, "Enter an option (1-3): ", curses.color_pair(3))
    setCursor(0)

    if option == "1":
        curses.endwin()
        terminalShell.terminalShellWin()

    # Open up a menu of some more applications
    elif option == "2":
        extraAppWindow1 = curses.newwin(9, 40, 2, 16)
        extraAppWindow1.bkgd(" ", curses.color_pair(3))
        extraAppWindow1.border()
        extraAppWindow1.addstr(1, 2, "[=] 1. Software Planner")
        extraAppWindow1.addstr(2, 2, "[\u25a1] 2. File Manager")
        extraAppWindow1.addstr(3, 2, "-----------------------")
        extraAppWindow1.addstr(4, 2, "[\u2592] 3. Settings")
        extraAppWindow1.addstr(5, 2, "[?] 4. Help")
        setCursor(1)
        appOption = getInput(extraAppWindow1, 7, 2, "Enter an option (1-4): ", curses.color_pair(3))
        setCursor(0)

        if appOption == "1":
            softwarePlanner.softwarePlanner()

        elif appOption == "2":
            fileManager.fileManagerWin()

        elif appOption == "4":
            helpWindow()

    elif option == "3":
        sys.exit()

    '''
    if option == "1":
        curses.endwin()
        terminalShell.terminalShellWin()

    elif option == "2":
        softwarePlanner.softwarePlanner()

    elif option == "3":
        fileManager.fileManagerWin()

    elif option == "5":
        helpWindow()

    elif option == "6":
        sys.exit()
    '''

    appLauncherWin.refresh()


    # When the app is finished (the user presses Ctrl-G in most cases) it closes all windows and runs the app launcher again
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
