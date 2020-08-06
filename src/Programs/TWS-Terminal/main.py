import os
import curses

curses.endwin()

startDir = os.getcwd()

os.system("clear")
print(f"To return to the semi-graphical terminal windowing system, type: 'exit'")

os.system("bash")

os.chdir(startDir)
