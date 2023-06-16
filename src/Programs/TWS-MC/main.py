import os
import curses
curses.endwin()
startDir = os.getcwd()
os.system("clear")
os.chdir(startDir)
os.system("mc")
