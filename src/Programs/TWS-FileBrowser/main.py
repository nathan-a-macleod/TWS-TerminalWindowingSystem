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
row = 6
home = os.getcwd()
lineinc = 1

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
        else:
            if not os.path.isdir(str(clickedButton["widgetID"])):
                curses.endwin()
                os.system(f'nano {str(clickedButton["widgetID"])}')
            else:
                os.chdir(str(clickedButton["widgetID"]))

#	Redraw the screen to update for new/removed files and/or directories
#	This is as optimized as I was able to do the code, so I can't really do anything to make it better in terms of not repeating code

        mainWin.widgets = [] # An array of all the widgets, currently empty for redrawing the screen
        mainWin.addMenuButton("closeButton", 0, "Close Window") # Close Button
        mainWin.addTitle("", 1, 2, "File Browser") # Title
        mainWin.addInput("Make", 3, 2, "Make a new file:") # Touch Input
        mainWin.addInput("MKDIR", 4, 2, "Make a new directory:") # Mkdir Input
        mainWin.addInput("Remove", 5, 2, "Delete a file:") # Rm Input
        mainWin.addInput("RMDIR", 6, 2, "Delete a directory:") # Rmdir Input
        idx2 = row
        for program in os.listdir(os.getcwd()):
            idx2 += lineinc
            if not os.path.isdir(program):
                mainWin.addButton(str(program), idx2+1, 2, program)
            else:
                mainWin.addButton(str(program), idx2+1, 2, program+"/")
        mainWin.addButton("Back", idx2+2, 2, "../")
        curses.setsyx(1, 1)

"""
	Draw the things in the file manager on initilization
	What this does is make a bunch of widgets for some functions
	then when we get to the for loop, we are putting each file and directory as buttons
	I'd like to optimize this further, but I can't since it has been as optimized as I reasonably can
"""
mainWin = Window("TWS-FileBrowser", mainWinFunction) # Create a window
mainWin.widgets = [] # An array of all the widgets
mainWin.addMenuButton("closeButton", 0, "Close Window")
mainWin.addTitle("", 1, 2, "File Browser") 
mainWin.addInput("Make", 3, 2, "Make a new file:")
mainWin.addInput("MKDIR", 4, 2, "Make a new directory:")
mainWin.addInput("Remove", 5, 2, "Delete a file:")
mainWin.addInput("RMDIR", 6, 2, "Delete a directory:")
idx2 = row
for program in os.listdir(os.getcwd()):
    idx2 += lineinc
    if not os.path.isdir(program):
        mainWin.addButton(str(program), idx2+1, 2, program)
    else:
         mainWin.addButton(str(program), idx2+1, 2, program+"/")  
mainWin.addButton("Back", idx2+2, 2, "../")
curses.setsyx(1, 1) 
