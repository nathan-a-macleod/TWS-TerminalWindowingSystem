from CoreLib.Windows.windowClass import *

def helpWinFunction(window, key, clickedButton):
    if clickedButton != 0:
        if clickedButton["widgetID"] == "closeButton":
            window.closeWindow()

helpWin = Window("TWS-Help", helpWinFunction)
helpWin.addMenuButton("closeButton", 0, "Close Window")
helpWin.addMenuButton("", 16, "Menu Item 2")
helpWin.addMenuButton("", 31, "Menu Item 3")
try:
    helpWin.width = int(curses.COLS/1.3)
    helpWin.height = int(curses.LINES/1.2)-10
    helpWin.x = curses.COLS//9
    helpWin.y = curses.LINES//9
except:
    pass
helpWin.addLabel("", 2, 2, "'TWS' (short for 'Terminal Windowing System') is a Terminal/Operating environment program with a few other programs (written in Python).")
helpWin.addLabel("", 3, 2, "You can think of it sort of like a terminal-desktop environment - but it's really just a collection of programs you can run inside a terminal that use some custom windowing modules.")
helpWin.addLabel("", 5, 2, "The Github page is at https://github.com/nathan-a-macleod/TWS-TerminalWindowingSystem")
helpWin.addLabel("", 7, 2, "Controls: ")
helpWin.addLabel("", 8, 2, "----------")
helpWin.addLabel("", 9, 2, "Up & Down Arrow Keys or K(Up) and J(Down): Highlight a selection.")
helpWin.addLabel("", 10, 2, "Left & Right Arrow Keys: Focuses a different window. ")
helpWin.addLabel("", 11, 2, "ENTER: 'Click' a selection.")
helpWin.addLabel("", 14, 2, "Q, E (UpperCase) or PgUp, PgDn: Scrolling vertically.")
helpWin.addLabel("", 15, 2, "Q, E (LowerCase) or Insert(Right) and Delete(Left): Scrolling horizontally.")
helpWin.addLabel("", 16, 2, "W, A, S, D (UpperCase): Move Current Window")
helpWin.addLabel("", 17, 2, "W, A, S, D (LowerCase): Resize Current Window")
helpWin.addLabel("", 18, 2, "\".\": Toggle between showing & hiding the desktop.")
helpWin.addLabel("", 19, 2, "R (UpperCase): Roll Up The Current Window (But Keep It Focused)")
helpWin.addLabel("", 20, 2, "R (LowerCase): Maximize Current Window")
helpWin.addLabel("", 22, 2, "Most programs will have at least a few buttons to select. Some of those buttons may be in the toolbar (look at the top of the window).")
