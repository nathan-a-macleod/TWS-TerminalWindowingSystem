import curses               # For the core of the main user interface
from curses import textpad  # Mainly for the software planner
import datetime             # For printing the time in the terminal shell
import sys                  # For exiting the program (sys.exit)
import os                   # For the terminal (os.system() function is very widely used)

version = "0.1.2"
commandHistory = []

appGlyph = "[=+=]"
#inputGlyph = "'***'"
inputGlyph = ""

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

def terminalShell():
    command = ""
    
    os.system("clear")
    print(f"Welcome to the terminal environment.\nTo open the app launcher again, type: 'exit'")

    while command != "exit":
        now = datetime.datetime.now()
        command = input("\033[34;1m" + now.strftime("%H:%M") + "\033[0m~\033[31;1m" + os.popen("whoami").read().split()[0] + "\033[0m~\033[36m" + os.popen("pwd").read().split("\n")[0] + "/\033[0m~$ ")

        os.system(command)

        # To allow the user to press up arrow to go to the last command:
        commandHistory.append(command)

        # To allow changing of directories:
        try:
            os.chdir(command.split()[1])

        except:
            pass

def softwarePlanner(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to the software planner.\u2550")
    stdscr.refresh()
    stdscr.getch()

def appLauncher(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    appLauncherWin = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    appLauncherWin.bkgd(" ", curses.color_pair(3))

    # Header at the top of the screen
    menuTitleStr = " A P P   L A U N C H E R  -  VERSION " + version + " "

    for i in range(0, curses.COLS//2-len(menuTitleStr)//2):
        appLauncherWin.addstr(0, int(i), " ", curses.color_pair(2))

    appLauncherWin.addstr(0, curses.COLS//2-len(menuTitleStr)//2, menuTitleStr, curses.color_pair(1))

    for i in range(curses.COLS//2+len(menuTitleStr)//2+1, curses.COLS):
        appLauncherWin.addstr(0, int(i), " ", curses.color_pair(2))

    # Options for other apps:
    appLauncherWin.addstr(2, 2, appGlyph + " 1. Terminal Shell")
    appLauncherWin.addstr(3, 2, appGlyph + " 2. Software Planner")
    appLauncherWin.addstr(4, 2, appGlyph + " 3. Games Library")
    appLauncherWin.addstr(5, 2, appGlyph + " 4. Settings")
    appLauncherWin.addstr(7, 2, "5. EXIT")

    appLauncherWin.refresh()

    # Get input from the user
    #option = appLauncherWin.getstr(curses.COLS-1, 2)
    curses.echo()
    option = getInput(appLauncherWin, curses.LINES-2, 2, "Enter an option (1-5): ", curses.color_pair(3))
    curses.noecho()

    if option == "1":
        curses.endwin()
        terminalShell()

    elif option == "2":
       curses.wrapper(softwarePlanner)

    elif option == "5":
        sys.exit()

    curses.wrapper(appLauncher)

    appLauncherWin.refresh()
    stdscr.refresh()

# Something containing the version number, and maybe some ascii art (logo or something) - then it says to press any key to continue.
def bootupScreen():
    pass

bootupScreen()
curses.wrapper(appLauncher)