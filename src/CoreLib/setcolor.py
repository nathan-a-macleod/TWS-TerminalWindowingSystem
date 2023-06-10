import curses
import os
import random
import re
# ...and some other files
from CoreLib.Windows.windowClass import *
from CoreLib.screenCycle import *
from pathlib import Path
def SetThemeColors():
    bgclr = Path("config.cfg") #Note, the color has to be one of the 7 default colors
    if bgclr.exists():
        f = open("config.cfg", "r")
    else:
        os.system("touch config.cfg")
        f = open("config.cfg", "w")
        f.write("COLOR:blue\nTHEME:light")
        f.close()
    f = open("config.cfg", "r")
    bgnd3 = f.readlines()
    bgnd2 = bgnd3[1]
    bgnd1 = re.sub("COLOR:", '', bgnd2).lower()
    bgnd = re.sub("\n", '', bgnd1).lower()
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
    f2 = open("config.cfg", "r")
    thm3 = f2.readlines()
    thm2 = thm3[2]
    thm1 = re.sub("THEME:", '', thm2).lower()
    mode = re.sub("\n", '', thm1).lower()
    
    if bgnd in BlackFGColors:
        fg = "black"
    else:
        fg = "white"
    
    if bgnd == "yellow":
        curses.init_pair(1, black, red) # For the shadows       
    else:
        curses.init_pair(1, black, yellow) # For the shadows
             
    if mode == "dark":    
        curses.init_pair(2, white, black) # Same, but inverted, Apps Background and Foreground Colors
    else:
        curses.init_pair(2, black, white) # Same, but inverted, Apps Background and Foreground Colors
        
    try:
        curses.init_pair(3, colors[fg], colors[bgnd]) # The background color
    except:
        curses.init_pair(3, white, blue) # The background color  
             
    if mode == "dark":         
        curses.init_pair(4, black, white) # Same, but inverted, Apps Background and Foreground Colors
    else:    
        curses.init_pair(4, white, black) # Same, but inverted, Apps Background and Foreground Colors

