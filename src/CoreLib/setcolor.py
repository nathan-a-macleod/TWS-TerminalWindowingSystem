#	Import Curses and some other modules
import curses
import os
import random
import re
#	Import the screen managing code
from CoreLib.Windows.windowClass import *
from CoreLib.screenCycle import *
from pathlib import Path
def SetThemeColors():
#	Note, the color has to be one of the 7 default colors because of curses
    bgclr = Path("config.cfg")
    if bgclr.exists():
        f = open("config.cfg", "r")
    else:
        os.system("touch config.cfg")
        f = open("config.cfg", "w")
        f.write("COLOR:blue\nTHEME:light")
        f.close()

#	Set The Variable Colors
    f = open("config.cfg", "r")
    config = f.readlines()
    bgnd2 = config[1]
    bgnd1 = re.sub("COLOR:", '', bgnd2).lower()
    bgnd = re.sub("\n", '', bgnd1).lower()
    thm2 = config[2]
    thm1 = re.sub("THEME:", '', thm2).lower()
    mode = re.sub("\n", '', thm1).lower()

#	Dictionary for setting colors since we use the config to get the color and therefore, we can't actually use the text as a variable without this   
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

    blue = colors["blue"]	#	Can have white text
    black = colors["black"]	#	Can have white text
    cyan = colors["cyan"]	#	Can't have white text for the sake of being readable
    green = colors["green"]	#	Can have white text
    magenta = colors["magenta"]	#	Can't have white text for the sake of being readable
    red = colors["red"]		#	Can have white text
    white = colors["white"]	#	Can't have white text for the sake of being readable
    yellow = colors["yellow"]	#	Can't have white text for the sake of being readable

    BlackFGColors = [
"white",
"yellow",
"cyan",
"magenta"
]


    if bgnd in BlackFGColors:	#If we would have a hard time seeing the color white on the background
        fg = "black"
    else:
        fg = "white"

    Foreground = colors[fg]
    Background = colors[bgnd]        
#	For the shadows on the text
    if bgnd == "yellow":
        curses.init_pair(1, black, red)  
    else:
        curses.init_pair(1, black, yellow)

#	Apps Background and Foreground Colors             
    if mode == "dark":    
        curses.init_pair(2, white, black)
    else:
        curses.init_pair(2, black, white) 

#	The Desktop Background and Text Color        
    try:
        curses.init_pair(3, Foreground, Background)
    except:
        curses.init_pair(3, white, blue)

#	Taskbar Alternate Color             
    if mode == "dark":
        if bgnd != "blue": #is the background black
            curses.init_pair(4, white, blue) #otherwise use the lightmode one
        else:
            curses.init_pair(4, black, white) #if not, do the normal dark mode taskbar
    else:  
        if bgnd != "blue": #is the background white
            curses.init_pair(4, white, blue) #otherwise use the darkmode one
        else:
            curses.init_pair(4, white, black) #if not, do the normal dark mode taskbar
