from TWS.windowClass import *

def helpWinFunction(window, key, selectedButtonID):
    window.addString(2, 2, "'TWS' (short for 'Terminal Windowing System') is a Terminal/Operating environment program with a few other programs (written in Python).")
    window.addString(3, 2, "You can think of it sort of like a terminal-desktop environment - but it's really just a collection of programs you can run inside a terminal.")
    window.addString(5, 2, "The Github page is at https://github.com/nathan-a-macleod/terminalEnv")
    window.addString(7, 2, "Controls: ")
    window.addString(8, 2, "----------")
    window.addString(9, 2, "Up & down Arrow Keys: Highlight a selection.")
    window.addString(10, 2, "Left & right Arrow Keys: Focuses a different window.")
    window.addString(11, 2, "<ENTER>: 'Click' a selection.")
    window.addString(12, 2, "WASD: Moves the selected window.")
    window.addString(14, 2, "Most programs will have at least a few buttons to select. Some of those buttons may be in the toolbar (look at the top of the screen).")
    window.addString(15, 2, "This window has a few buttons at the top - one of them is to close the window, the rest don't do anything.")

    if selectedButtonID == "closeButton":
        window.closeWindow()

helpWin = Window(curses.LINES//9, curses.COLS//9, int(curses.LINES/1.2)-10, int(curses.COLS/1.3), "TWS-Help", helpWinFunction)
helpWin.addMenuButton("closeButton", 0, "Close Window")
helpWin.addMenuButton("", 17, "MenuItem1")
helpWin.addMenuButton("", 31, "MenuItem2")
