# Imports
import curses
import datetime
import psutil
import os
from CoreLib.Windows.windowClass import *
from CoreLib.Windows.windowManager import *
from CoreLib.drawWindow import *
from CoreLib.drawDesktop import *

# The main screen class where everything happens:
class Screen:
    def __init__(self, stdscrRoot):
        self.stdscrRoot = stdscrRoot

        # The desktop:
        self.desktop = Window(1, 0, curses.LINES-2, curses.COLS, "Desktop", self.desktopFunction)
        self.desktop.addMenuButton("appLauncher", 0, "App Launcher")
        self.desktop.addButton("123", 2, 2, "Button 1")
        self.desktop.addButton("", 3, 2, "Button 2")
        self.desktop.addButton("", 4, 2, "Button 3")

    def taskbar(self):
        taskBarString = str(datetime.datetime.now().strftime("%I:%M")) + " | " + str(psutil.cpu_percent()) + " % | " + str(os.popen("whoami").read()).split("\n")[0] + "@" + str(os.popen("uname -n").read()).split("\n")[0] + " | " + str(openWindows[len(openWindows)-1].windowTitle)
        self.stdscrRoot.hline(0, 0, " ", curses.COLS, curses.color_pair(1)) # Draw a horizontal line at the top of the screen
        self.stdscrRoot.addstr(0, curses.COLS//2-len(taskBarString)//2, taskBarString, curses.color_pair(1))

    def desktopFunction(self, window, key, clickedButton):
        if clickedButton != 0:
            if clickedButton["widgetID"] == "123":
                exit()

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
