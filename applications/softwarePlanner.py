import curses
from curses.textpad import Textbox # For the software planner
from applicationFunctions import *

# stdscrRoot is the root app launcher window...
def softwarePlanner():
    curses.curs_set(1)
    stdscr = createNewWindow("S O F T W A R E   P L A N N E R")
    stdscr.addstr(1, 1, "Welcome to the software planner - why not plan out some software in here? Press Ctrl-G to exit.")

    hlineUnicode(stdscr)

    editWin = curses.newwin(curses.LINES-5, curses.COLS-2, 4, 1)
    editWin.bkgd(" ", curses.color_pair(3))

    with open("softwarePlannerText.txt", "r") as file:
        for i, line in enumerate(file):
            editWin.addstr(i, 0, line)
    file.close()

    box = Textbox(editWin)
    box.edit()

    editWin.refresh()

    file = open("softwarePlannerText.txt","w")
    file.write(box.gather())
    file.close()

    stdscr.refresh()