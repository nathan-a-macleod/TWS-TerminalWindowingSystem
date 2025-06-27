from CoreLib.Windows.windowClass import * # Import the library like this
from CoreLib.Windows.windowManager import * # Import the library like this
global curses
import curses# Import other libraries like this:
global datetime
import datetime
global os
import os
global pathlib
import pathlib
global home
global mainWin
global row
global lineinc
global winstrs
global wigID
global Inputs
global row2

Inputs = 2
row2 = 3

row = 8
home = os.getcwd()
lineinc = 1
winstrs = [
"Close Window",
"File Browser",
"Make a new file:",
"Make a new directory:",
"Delete a file:",
"Delete a directory:",
"Go to path",
"../"
]

wigID = [
"closeButton",
"",
"Make",
"MKDIR",
"Remove",
"RMDIR",
"Goto",
"Back"
]
#	The main function

def mainWinFunction(window, key, clickedButton):  
    if clickedButton != 0: # If you have clicked a button
        # If the ID of the button being clicked is "closeButton", close the window. (It's highly recommended to include a button the close the window in each program)
        if clickedButton["widgetID"] == "closeButton":
            os.chdir(home)
            window.closeWindow() # Close the window


        elif clickedButton["widgetID"] == "Back":
            os.chdir("../")


        elif clickedButton["widgetID"] == "Make":

            try:
                files = clickedButton["value"].split("/")[1]
                dirs = clickedButton["value"].split("/")[0]
                os.system(f'touch {files} || mkdir {dirs}')
                os.system(f'mv {files} {clickedButton["value"]}')
            except:
                try:
                    files = clickedButton["value"].split("/")[1]
                    dirs = clickedButton["value"].split("/")[0]  
                    os.system(f'mkdir {dirs} && touch {clickedButton["value"]}')
                except:
                    os.system(f'touch {clickedButton["value"]}')
            
        elif clickedButton["widgetID"] == "Remove":
            try:
                os.system(f'rm {clickedButton["value"]}')
            except:
                pass
                                   
        elif clickedButton["widgetID"] == "MKDIR":
            dirs = clickedButton["value"]
            try:
                os.mkdir(dirs)
            except:
                pass

        elif clickedButton["widgetID"] == "RMDIR":
            dirs = clickedButton["value"]
            try:
                os.rmdir(dirs)
            except:
                pass
        elif clickedButton["widgetID"] == "Goto":
            dirs = clickedButton["value"]
            try:
                os.chdir(dirs)
            except:
                try:
                    os.chdir(f"{os.getcwd()}/{dirs}")
                except:
                    pass
        else:
            if not os.path.isdir(str(clickedButton["widgetID"])):
                curses.endwin()
                os.system(f'nano {str(clickedButton["widgetID"])}')
            else:
                os.chdir(str(clickedButton["widgetID"]))

#	Redraw the screen to update for new/removed files and/or directories
#	This is as optimized as I was able to do the code, so I can't really do anything to make it better in terms of not repeating code

        mainWin.widgets = [] # An array of all the widgets, currently empty for redrawing the screen
        mainWin.addMenuButton(wigID[0], 0, winstrs[0])
        mainWin.addTitle(wigID[1], 1, 2, winstrs[1]) 
        Inputs = 2
        row2 = 3
        while Inputs != 7:
            mainWin.addInput(wigID[Inputs], row2, 2, winstrs[Inputs])
            row2 += 1
            Inputs += 1

        mainWin.addButton(wigID[7], 9, 2, winstrs[7])
        idx2 = row
        for program in os.listdir(os.getcwd()):
            idx2 += lineinc
            if not os.path.isdir(program):
                mainWin.addButton(str(program), idx2+1, 2, program)
            else:
                mainWin.addButton(str(program), idx2+1, 2, program+"/")
        curses.setsyx(1, 1)

"""
	Draw the things in the file manager on initilization
	What this does is make a bunch of widgets for some functions
	then when we get to the for loop, we are putting each file and directory as buttons
	I'd like to optimize this further, but I can't since it has been as optimized as I reasonably can
"""
mainWin = Window("TWS-FileBrowser", mainWinFunction) # Create a window
try:
    mainWin.width = int(curses.COLS/1.3)
    mainWin.height = int(curses.LINES/1.2)-10
    mainWin.x = curses.COLS//9
    mainWin.y = curses.LINES//9
except:
    pass
mainWin.widgets = [] # An array of all the widgets

mainWin.addMenuButton(wigID[0], 0, winstrs[0])
mainWin.addTitle(wigID[1], 1, 2, winstrs[1]) 

while Inputs != 7:
    mainWin.addInput(wigID[Inputs], row2, 2, winstrs[Inputs])
    row2 += 1
    Inputs += 1

mainWin.addButton(wigID[7], 9, 2, winstrs[7])

idx2 = row
for program in os.listdir(os.getcwd()):
    idx2 += lineinc
    if not os.path.isdir(program):
        mainWin.addButton(str(program), idx2+1, 2, program)
    else:
         mainWin.addButton(str(program), idx2+1, 2, program+"/")  
curses.setsyx(1, 1) 
