import curses
import os
import random
import re
# ...and some other files
from CoreLib.Windows.windowClass import *
from CoreLib.screenCycle import *
from pathlib import Path
def SetThemeColors():
    bgclr = Path("bgclr.txt") #Note, the color has to be one of the 7 default colors
    if bgclr.exists():
        f = open("bgclr.txt", "r")
    else:
        os.system("touch bgclr.txt")
        f = open("bgclr.txt", "w")
        f.write("blue")
        f.close()
    f = open("bgclr.txt", "r")  
    x = f.read()
    bgnd = re.sub("\n", '', x).lower()
    colors = {
"blue" : curses.COLOR_BLUE,
"black" : curses.COLOR_BLACK,
"cyan" : curses.COLOR_CYAN,
"green" : curses.COLOR_GREEN,
"magenta" : curses.COLOR_MAGENTA,
"red" : curses.COLOR_RED,
"white" : curses.COLOR_WHITE,
"yellow" : curses.COLOR_YELLOW
}

    blue = colors["blue"] #Can have white text
    black = colors["black"] #Can have white text
    cyan = colors["cyan"] #Can't have white text (readability)
    green = colors["green"] #Can have white text
    magenta = colors["magenta"] #Can't have white text (readability)
    red = colors["red"] #Can have white text
    white = colors["white"] #Can't have white text (readability)
    yellow = colors["yellow"] #Can't have white text (readability)

    BlackFGColors = [
"white",
"yellow",
"cyan",
"magenta"
]

    if bgnd in BlackFGColors:
        fg = "black"
    else:
        fg = "white"
    
    if bgnd == "yellow":
        curses.init_pair(1, black, red) # For the shadows
    else:
        curses.init_pair(1, black, yellow) # For the shadows
    curses.init_pair(2, black, white) # Same, but inverted
    try:
        curses.init_pair(3, colors[fg], colors[bgnd]) # The background color
    except:
        curses.init_pair(3, white, blue) # The background color       
         
    curses.init_pair(4, white, black) # For the titles

