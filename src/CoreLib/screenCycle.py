# Imports
import curses
import datetime
import psutil
import os
from CoreLib.Windows.windowClass import *
from CoreLib.Windows.windowManager import *
from CoreLib.drawWindow import *
from CoreLib.drawDesktop import *

def appLauncherFunction(window, key, clickedButton):
    if clickedButton != 0:
        if clickedButton["widgetID"] == "endSession":
            exit()
        
        elif clickedButton["widgetID"] == "closeWindow":
            window.closeWindow()
        
        else:
            try:
                exec(open("Programs/" + clickedButton["widgetID"] + "/main.py").read())

            except Exception as ex:
                alert("Error Running Program", "There was an error while trying to run the program. Error: " + str(ex))

# The main screen class where everything happens:
class Screen:
    def __init__(self, stdscrRoot):
        self.stdscrRoot = stdscrRoot

        # The desktop:
        self.desktop = Window(1, 0, curses.LINES-2, curses.COLS, "Desktop", self.desktopFunction)
        self.desktop.addMenuButton("appLauncher", 0, "App Launcher")
        self.desktop.addButton("", 1, 2, "Button 2")
        self.desktop.addButton("terminal", 2, 2, "[#] TWS-Terminal")
        self.desktop.addButton("endSession", 3, 2, "[x] End Session")

    def taskbar(self):
        taskBarString = str(datetime.datetime.now().strftime("%I:%M")) + " | " + str(psutil.cpu_percent()) + " % | " + str(os.popen("whoami").read()).split("\n")[0] + "@" + str(os.popen("uname -n").read()).split("\n")[0] + " | " + str(openWindows[len(openWindows)-1].windowTitle)
        self.stdscrRoot.hline(0, 0, " ", curses.COLS, curses.color_pair(1)) # Draw a horizontal line at the top of the screen
        self.stdscrRoot.addstr(0, curses.COLS//2-len(taskBarString)//2, taskBarString, curses.color_pair(1))

    def desktopFunction(self, window, key, clickedButton):
        if clickedButton != 0:
            if clickedButton["widgetID"] == "endSession":
                exit()

            elif clickedButton["widgetID"] == "terminal":
                exec(open("Programs/" + "TWS-Terminal" + "/main.py").read())


            elif clickedButton["widgetID"] == "appLauncher":
                # Open a menu with all the installed apps:
                appLauncherWin = Window(2, 2, curses.LINES//2, curses.COLS//5, "App Launcher", appLauncherFunction)
                appLauncherWin.addMenuButton("closeWindow", 0, "Close Window")

                # Create a button for each file in the 'Programs' directory
                idx = 0
                for program in os.listdir("./Programs"):
                    idx += 1

                    # If the file has "." as the first letter it's a hidden file.
                    if program[0] != "." and os.path.isfile(os.getcwd() + "/Programs/" + program) == False:
                        # Get the programs metadata from the 'TWSProgram.txt' file
                        settingsData = str(open("./Programs/" + program + "/TWSProgram.txt").read())
                        displayname = settingsData.split("\n")[0][13:]
                        displayname = displayname[:-1]

                        displaysymbol = settingsData.split("\n")[1][15:]
                        displaysymbol = displaysymbol[:-1]

                        appLauncherWin.addButton(str(program), idx+1, 2, "[" + displaysymbol + "] " + displayname)

                    else:
                        idx -= 1

    # The main function in the class
    def mainloop(self):
        while True:
            self.stdscrRoot.erase() # Clear the screen

            # Draw the taskbar
            self.taskbar()

            # Draw all the windows, but don't give the key that's been clicked (only do that for the last window)
            for window in openWindows:
                window.functionName(window, -1, 0)
                if window.functionName != self.desktopFunction:
                    drawWindow(self.stdscrRoot, window)

                else:
                    drawDesktop(self.stdscrRoot, window)

            char = self.stdscrRoot.getch()

            windowManager(char, window)

            # Changing the focused window:
            if char == curses.KEY_RIGHT:
                try:
                    lastWindow = openWindows[0]
                    openWindows.remove(lastWindow)
                    openWindows.append(lastWindow)

                except:
                    pass

            elif char == curses.KEY_LEFT:
                try:
                    lastWindow = openWindows[len(openWindows)-1]
                    openWindows.remove(lastWindow)
                    openWindows.insert(0, lastWindow)

                except:
                    pass

            # A Help window:
            elif char == ord("?"):
                def helpWinFunction(window, key, clickedButton):
                    if clickedButton != 0:
                        if clickedButton["widgetID"] == "closeButton":
                            window.closeWindow()

                helpWin = Window(curses.LINES//9, curses.COLS//9, int(curses.LINES/1.2)-10, int(curses.COLS/1.3), "TWS-Help", helpWinFunction)
                helpWin.addMenuButton("closeButton", 0, "Close Window")
                helpWin.addMenuButton("", 16, "Menu Item 2")
                helpWin.addMenuButton("", 31, "Menu Item 3")

                helpWin.addLabel("", 2, 2, "'TWS' (short for 'Terminal Windowing System') is a Terminal/Operating environment program with a few other programs (written in Python).")
                helpWin.addLabel("", 3, 2, "You can think of it sort of like a terminal-desktop environment - but it's really just a collection of programs you can run inside a terminal.")
                helpWin.addLabel("", 5, 2, "The Github page is at https://github.com/nathan-a-macleod/terminalEnv")
                helpWin.addLabel("", 7, 2, "Controls: ")
                helpWin.addLabel("", 8, 2, "----------")
                helpWin.addLabel("", 9, 2, "Up & down Arrow Keys: Highlight a selection.")
                helpWin.addLabel("", 10, 2, "Left & right Arrow Keys: Focuses a different window. ")
                helpWin.addLabel("", 11, 2, "ENTER: 'Click' a selection.")
                helpWin.addLabel("", 12, 2, "WASD (UpperCase): Moves the selected window.")
                helpWin.addLabel("", 13, 2, "Q, E (UpperCase): Scrolling.")
                helpWin.addLabel("", 15, 2, "Most programs will have at least a few buttons to select. Some of those buttons may be in the toolbar (look at the top of the window).")
                helpWin.addLabel("", 16, 2, "This window has a few buttons at the top - one of them is to close the window, the rest don't do anything.")

            else:
                window.functionName(window, char, 0)

            if window.functionName != self.desktopFunction:
                drawWindow(self.stdscrRoot, window)

            else:
                drawDesktop(self.stdscrRoot, window)

            self.stdscrRoot.refresh()
