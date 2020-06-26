from canvas import *        # Internal canvas.py file for ascii windows and stuff
import datetime             # For printing the time in the terminal shell
import sys                  # For exiting the program (sys.exit)
import curses               # For the software planner
from curses import textpad  # Also for the software planner

version = "0.1.1"
commandHistory = []

canv = canvas(width, height, bgChar=" ")

appGlyph = "[=+=]"
#inputGlyph = "'***'"
inputGlyph = ""

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

def softwarePlanner():
    def main(stdscr):
        stdscr.addstr(0, 0, "Welcome to the software planner.\u2550")
        box = textpad.Textbox(stdscr, True)
        contents = box.edit()
        stdscr.addstr(repr(contents))
        stdscr.refresh()
        stdscr.getch()

    curses.wrapper(main)

def appLauncher():
    canv.addWindow(0, 0, width-1, height-3, "A P P   L A U N C H E R  -  VERSION " + version, False)
    canv.addStr(2, 2, appGlyph + " 1. Terminal Shell")
    canv.addStr(2, 3, appGlyph + " 2. Software Planner")
    canv.addStr(2, 4, appGlyph + " 3. Games Library")
    canv.addStr(2, 5, appGlyph + " 4. Settings")
    # Development Library Environment. # (Not sure how to do it yet, but maybe a python library (canvas.py or something to link up to automatically) where you can create graphical programs the the program.)
    canv.addStr(2, 7, "5. EXIT")

    # Colors for heading and window content
    canv.addPixel(0, 0, colors.bgBlue + colors.fgWhite, "l")
    canv.addPixel(0, 1, colors.bgWhite + colors.fgBlack, "l")
    canv.addPixel(width-1, height-3, colors.reset, "r")

    canv.refresh()
    
    option = input(inputGlyph + "Please enter an option (1-5): ")
    #option = getch(inputGlyph + "Please enter an option (1-5): ")

    # If it's an invalid option, run the function again
    if option not in ["1", "2", "3", "4", "5"]:
        appLauncher()

    elif option == "1":
        terminalShell()

    elif option == "2":
        softwarePlanner()

    elif option == "5":
        sys.exit() # Just ends the whole program

    appLauncher() # Once it has run a program, it goes back to the main home screen (app launcher screen)

# Something containing the version number, and maybe some ascii art (logo or something).
def bootupScreen():
    pass

bootupScreen()
appLauncher()
