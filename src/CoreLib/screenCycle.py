# Imports
import curses
import datetime
import psutil
import os
from CoreLib.Windows.windowClass import *
from CoreLib.Windows.windowManager import *
from CoreLib.drawWindow import *

# The main screen class where everything happens:
class Screen:
    def __init__(self, stdscrRoot):
        self.stdscrRoot = stdscrRoot

    def taskbar(self):
        taskBarString = str(datetime.datetime.now().strftime("%I:%M")) + " | " + str(psutil.cpu_percent()) + " % | " + str(os.popen("whoami").read()).split("\n")[0] + "@" + str(os.popen("uname -n").read()).split("\n")[0] + " | " + str(openWindows[len(openWindows)-1].windowTitle)
        self.stdscrRoot.hline(0, 0, " ", curses.COLS, curses.color_pair(1)) # Draw a horizontal line at the top of the screen
        self.stdscrRoot.addstr(0, curses.COLS//2-len(taskBarString)//2, taskBarString, curses.color_pair(1))

    # The main function in the class
    def mainloop(self):
        while True:
            self.stdscrRoot.erase() # Clear the screen

            # Draw the taskbar
            self.taskbar()

            # Draw all the windows, but don't give the key that's been clicked (only do that for the last window)
            for window in openWindows:
                window.functionName(window, -1, 0)
                drawWindow(self.stdscrRoot, window)

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

            drawWindow(self.stdscrRoot, window)

            self.stdscrRoot.refresh()
