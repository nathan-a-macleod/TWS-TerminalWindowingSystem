import curses               # For the core of the main user interface
from curses.textpad import Textbox  # Mainly for the software planner
import datetime             # For printing the time in the terminal shell
import sys                  # For exiting the program (sys.exit)
import os                   # For the terminal (os.system() function is very widely used)

startDir = os.getcwd()

version = "0.1.2"
commandHistory = []

termGlyph = "[\u2550]"
appGlyph = "[\u25a1]"
settingsGlyph = "[\u2592]"
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

    os.chdir(startDir)

# stdscrRoot is the root app launcher window...
def softwarePlanner(stdscrRoot):
    stdscr = curses.newwin(curses.LINES-1, curses.COLS, 1, 0)
    stdscr.bkgd(" ", curses.color_pair(3))
    stdscr.border()
    stdscr.addstr(1, 1, "Welcome to the software planner - why not plan out some software in here? Press Ctrl-G to exit.")
    stdscr.refresh()

    editWin = curses.newwin(curses.LINES-4, curses.COLS-2, 3, 1)
    editWin.bkgd(" ", curses.color_pair(3))

    with open("softwarePlannerText.txt", "r") as file:
        for i, line in enumerate(file):
            editWin.addstr(i+2, 0, line)
    file.close()

    box = Textbox(editWin)
    box.edit()

    editWin.refresh()

    file = open("softwarePlannerText.txt","w")
    file.write(box.gather())
    file.close()

    stdscr.refresh()
    stdscrRoot.refresh()

def gamesLibrary(stdscr):
    pass

def appLauncher(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.clear()

    appLauncherWin = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    appLauncherWin.bkgd(" ", curses.color_pair(3))

    # Header at the top of the screen
    menuTitleStr = " A P P   L A U N C H E R  -  VERSION " + version + " "

    for i in range(0, curses.COLS//2-len(menuTitleStr)//2):
        appLauncherWin.addstr(0, int(i), "\u2592", curses.color_pair(2))

    appLauncherWin.addstr(0, curses.COLS//2-len(menuTitleStr)//2, menuTitleStr, curses.color_pair(1))

    for i in range(curses.COLS//2+len(menuTitleStr)//2+1, curses.COLS):
        appLauncherWin.addstr(0, int(i), "\u2592", curses.color_pair(2))

    # Options for other apps:
    appLauncherWin.addstr(2, 2, termGlyph + " 1. Exit To Shell")
    appLauncherWin.addstr(3, 2, appGlyph + " 2. Software Planner")
    appLauncherWin.addstr(4, 2, appGlyph + " 3. Games Library")
    appLauncherWin.addstr(5, 2, settingsGlyph + " 4. Settings")
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
       softwarePlanner(stdscr)

    elif option == "3":
       curses.wrapper(gamesLibrary)

    elif option == "5":
        sys.exit()

    curses.endwin()
    curses.wrapper(appLauncher)

    appLauncherWin.refresh()
    stdscr.refresh()

# Something containing the version number, and maybe some ascii art (logo or something) - then it says to press any key to continue.
def bootupScreen(stdscr):
    bootupMessage1 = "Version " + version
    bootupMessage2 = "Press any key to continue..."
    
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    stdscr.bkgd(" ", curses.color_pair(1))
    stdscr.addstr(curses.LINES//2-1, curses.COLS//2-len(bootupMessage1)//2, bootupMessage1)
    stdscr.addstr(curses.LINES//2, curses.COLS//2-len(bootupMessage2)//2, bootupMessage2)

    stdscr.getch()
    curses.endwin()

curses.wrapper(bootupScreen)
curses.wrapper(appLauncher)