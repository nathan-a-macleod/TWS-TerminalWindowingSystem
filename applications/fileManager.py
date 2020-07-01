import curses
from applicationFunctions import *

def fileManagerWin(): # createNewWindow function needs to be passed as an argument
    fileManagerWindow = createNewWindow("F I L E   M A N A G E R")
    fileManagerWindow.addstr(1, 1, "Welcome to the file manager. Press arrow keys to use it and Ctrl-G to exit.")

    hlineUnicode(fileManagerWindow)

    getCtrlG(fileManagerWindow)
