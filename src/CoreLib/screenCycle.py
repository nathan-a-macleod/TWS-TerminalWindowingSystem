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

            else:
                window.functionName(window, char, 0)

            if window.functionName != self.desktopFunction:
                drawWindow(self.stdscrRoot, window)

            else:
                drawDesktop(self.stdscrRoot, window)

            self.stdscrRoot.refresh()
