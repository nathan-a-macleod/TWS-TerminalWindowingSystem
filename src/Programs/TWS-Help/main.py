from CoreLib.Windows.windowClass import *

def helpWinFunction(window, key, clickedButton):
    if clickedButton != 0:
        if clickedButton["widgetID"] == "closeButton":
            window.closeWindow()

helpWin = Window("TWS-Help", helpWinFunction)
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
helpWin.addLabel("", 14, 2, "Q, E (UpperCase): Scrolling vertically.")
helpWin.addLabel("", 15, 2, "Q, E (LowerCase): Scrolling horizontally.")
helpWin.addLabel("", 16, 2, "\".\": Toggle between showing & hiding the desktop.")
helpWin.addLabel("", 17, 2, "Most programs will have at least a few buttons to select. Some of those buttons may be in the toolbar (look at the top of the window).")