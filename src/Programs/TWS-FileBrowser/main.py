from CoreLib.Windows.windowClass import * # Import the library like this
from CoreLib.Windows.windowManager import * # Import the library like this
global curses
import curses# Import other libraries like this:
global datetime
import datetime
global os
import os
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

        else:
            if not os.path.isdir(str(clickedButton["widgetID"])):
                curses.endwin()
                os.system(f'nano {str(clickedButton["widgetID"])}')
            else:
                os.chdir(str(clickedButton["widgetID"]))

#	Redraw the screen to update for new files
        mainWin.widgets = [] # An array of all the widgets
        idx2 = row
        for program in os.listdir(os.getcwd()):
            idx2 += lineinc
            if not os.path.isdir(program):
                mainWin.addButton(str(program), idx2+1, 2, program)
            else:
                mainWin.addButton(str(program), idx2+1, 2, program+"/")
        mainWin.addButton("Back", idx2+2, 2, "../")   
        mainWin.addMenuButton("closeButton", 0, "Close Window") # Create a menu button with the ID of "closeButton"
        mainWin.addInput("Make", 3, 2, "Make a new file:") # Add an input line with an id of "input_001"
        mainWin.addTitle("", 1, 2, "File Browser") # Add a title with an id of "str_001"    
        mainWin.addInput("MKDIR", 4, 2, "Make a new directory:") # Add an input line with an id of "input_001"
        mainWin.addInput("Remove", 5, 2, "Delete a file:") # Add an input line with an id of "input_001"
        curses.setsyx(1, 1)

"""
	Draw the things in the file manager on initilization
"""
mainWin = Window("TWS-FileBrowser", mainWinFunction) # Create a window
mainWin.widgets = [] # An array of all the widgets
mainWin.addMenuButton("closeButton", 0, "Close Window") # Create a menu button with the ID of "closeButton"

mainWin.addTitle("", 1, 2, "File Browser") # Add a title with an id of "str_001"

mainWin.addInput("Make", 3, 2, "Make a new file:") # Add an input line with an id of "input_001"
mainWin.addInput("MKDIR", 4, 2, "Make a new directory:") # Add an input line with an id of "input_001"
mainWin.addInput("Remove", 5, 2, "Delete a file:") # Add an input line with an id of "input_001"

#	Create a button for each file in the 'Programs' directory
idx2 = row
for program in os.listdir(os.getcwd()):
    idx2 += lineinc
    if not os.path.isdir(program):
        mainWin.addButton(str(program), idx2+1, 2, program)
    else:
         mainWin.addButton(str(program), idx2+1, 2, program+"/")   
mainWin.addButton("Back", idx2+2, 2, "../")
