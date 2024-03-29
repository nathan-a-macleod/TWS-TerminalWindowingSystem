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
            os.system('clear')
            exit()
        
        elif clickedButton["widgetID"] == "closeWindow":
            window.closeWindow()
        
        else:
            try:
                exec(open("Programs/" + clickedButton["widgetID"] + "/main.py").read())
            except Exception as ex:
                alert("Error Running Program", "There was an error while trying to run the program. Error: " + str(ex))

#	The main screen class where everything happens:
class Screen:
    def __init__(self, stdscrRoot):
        self.stdscrRoot = stdscrRoot  
#	The desktop:
        self.desktop = Window("Desktop", self.desktopFunction)
#	Terminal Icon
        self.desktop.addMenuButton("appLauncher", 0, "[❖] App Launcher")
        self.desktop.add3DLabel(
        1,
        2,
        [
        "███	",
        "  ███	",
        "    ███",
        "  ███	",
        "███    _______"
        ]
        )
        self.desktop.addButton("terminal", 7, 2, "[>] TWS-Terminal")
#	End Session Icon
        self.desktop.add3DLabel(
        11,
        2,
        [
        "███      ███", 
        "  ███  ███",
        "    ████",
        "  ███  ███", 
        "███      ███"
        ]
        )
        self.desktop.addButton("endSession", 17, 2, "[X] End Session")

    def taskbar(self):

#	Define variables for parts of the taskbar to shorten the taskbar string
        user = str(os.popen("whoami").read()).split("\n")[0]
        system = str(os.popen("uname -n").read()).split("\n")[0]
        cpu = str(psutil.cpu_percent())
        time = str(datetime.datetime.now().strftime("%I:%M"))
        windows = str(openWindows[len(openWindows)-1].windowTitle)

#	Actual Taskbar String
        taskBarString = str(f"{time} | {cpu}% | {user}@{system} | {windows}")
        self.stdscrRoot.hline(0, 0, " ", curses.COLS, curses.color_pair(4))

#	Draw a horizontal line at the top of the screen
        self.stdscrRoot.addstr(0, curses.COLS//2-len(taskBarString)//2, taskBarString, curses.color_pair(4))

    def desktopFunction(self, window, key, clickedButton):
        if clickedButton != 0:
            if clickedButton["widgetID"] == "endSession":
                os.system('clear')
                exit()

            elif clickedButton["widgetID"] == "terminal":
                exec(open("Programs/" + "TWS-Terminal" + "/main.py").read())

            elif clickedButton["widgetID"] == "appLauncher":

#	Open a menu with all the installed apps:
                appLauncherWin = Window("App Launcher", appLauncherFunction)
                appLauncherWin.addMenuButton("closeWindow", 0, "Close Window")

#	Create a button for each file in the 'Programs' directory
                idx = 0
                for program in os.listdir("./Programs"):
                    idx += 1

#	If the file has "." as the first letter it's a hidden file.
                    if program[0] != "." and os.path.isfile(os.getcwd() + "/Programs/" + program) == False:

#	Get the programs metadata from the 'TWSProgram.txt' file
                        settingsData = str(open("./Programs/" + program + "/TWSProgram.txt").read())
                        displayname = settingsData.split("\n")[0][13:]
                        displayname = displayname[:-1]
                        displaysymbol = settingsData.split("\n")[1][15:]
                        displaysymbol = displaysymbol[:-1]
                        appLauncherWin.addButton(str(program), idx+1, 2, "[" + displaysymbol + "] " + displayname)

                    else:
                        idx -= 1

                appLauncherWin.addButton("endSession", idx+3, 2, "[X] End Session")
                try:
                   appLauncherWin.width = 30
                   appLauncherWin.height = idx+10
                except:
                   pass
#	The main function in the class
    def mainloop(self):
        while True:
#	Clear the screen
            self.stdscrRoot.erase()

#	Draw the taskbar
            self.taskbar()

#	Draw all the windows, but don't give the key that's been clicked (only do that for the last window)
            for window in openWindows:
                window.functionName(window, -1, 0)
                if window.functionName != self.desktopFunction:
                    drawWindow(self.stdscrRoot, window)

                else:
                    drawDesktop(self.stdscrRoot, window)

            char = self.stdscrRoot.getch()
            windowManager(char, window)

#	Changing the focused window:
#	Test for the Period key to show the desktop
            if char == ord("."):
                try:
                    lastWindow = openWindows[0]
                    openWindows.remove(lastWindow)
                    openWindows.append(lastWindow)

                    # Put the desktop at the first index of openWindows
                    if openWindows[len(openWindows)-1] != self.desktop: # But only if you aren't currently using it
                        openWindows.remove(self.desktop)
                        openWindows.insert(0, self.desktop)

                except:
                    pass

#	Test for the left arrow key to change what window you are focused on
 
            elif char == curses.KEY_LEFT:
                try:
                    lastWindow = openWindows[len(openWindows)-1]
                    openWindows.remove(lastWindow)
                    openWindows.insert(0, lastWindow)

#	Put the desktop at the first index of openWindows
                    openWindows.remove(self.desktop)
                    openWindows.insert(0, self.desktop)

                except:
                    pass

#	Test for the right arrow key to change what window you are focused on
            elif char == curses.KEY_RIGHT:
                try:
                    lastWindow = openWindows[len(openWindows)-1]
                    openWindows.remove(lastWindow)
                    openWindows.insert(1, lastWindow)

#	Put the desktop at the first index of openWindows
                    openWindows.remove(self.desktop)
                    openWindows.insert(0, self.desktop)

                except:
                    pass

#	A Help window that is opened when you press [?]:
            elif char == ord("?") or char == curses.KEY_F1:
                exec(open(os.getcwd() + "/Programs/TWS-Help/main.py").read())

            else:
                window.functionName(window, char, 0)

            if window.functionName != self.desktopFunction:
                drawWindow(self.stdscrRoot, window)

            else:
                drawDesktop(self.stdscrRoot, window)
            self.stdscrRoot.refresh()
