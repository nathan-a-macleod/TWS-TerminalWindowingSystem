from canvas import *  # Internal canvas.py file for ascii windows and stuff
import datetime       # For printing the time in the terminal shell
import sys            # For exiting the program (sys.exit)

version = "0.1"
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

def appLauncher():
    canv.addWindow(0, 0, width-1, height-3, "A P P   L A U N C H E R  -  VERSION " + version, False)
    canv.addStr(2, 2, appGlyph + " 1. Terminal Shell")
    canv.addStr(2, 3, appGlyph + " 2. VIM")
    canv.addStr(2, 4, appGlyph + " 3. Games Library")
    canv.addStr(2, 5, appGlyph + " 4. Settings")
    # Development Library Environment. # (Not sure how to do it yet, but maybe a python library (canvas.py or something to link up to automatically) where you can create graphical programs the the program.)
    canv.addStr(2, 7, "5. EXIT")

    # Colors for heading and window content
    canv.addPixel(0, 0, "\033[44m", "l")
    canv.addPixel(0, 1, "\033[47m\033[30m", "l")
    canv.addPixel(width-1, height-3, "\033[0m", "r")
    canv.refresh()
    
    option = input(inputGlyph + "Please enter an option (1-9): ")

    # If it's an invalid option, run the function again
    if option not in ["1", "2", "3", "4", "5"]:
        appLauncher()

    elif option == "1":
        terminalShell()

    elif option == "2":
        os.system("vim")

    elif option == "5":
        sys.exit() # Just ends the whole program

    appLauncher() # Once it has run a program, it goes back to the main home screen (app launcher screen)

def bootupScreen():
    '''for y in range(height):
        for x in range(width):
            print("\u001b[44m ", end="")

    print("\u001b[0m")'''
    pass

bootupScreen()
appLauncher()
