from CoreLib.Windows.windowClass import * # Import the library like this
global curses
import curses# Import other libraries like this:
global datetime
import datetime
global os
import os
global home
global mainWin
home = os.getcwd()
# The main function

def mainWinFunction(window, key, clickedButton):  
    if clickedButton != 0: # If you have clicked a button
        # If the ID of the button being clicked is "closeButton", close the window. (It's highly recommended to include a button the close the window in each program)
        if clickedButton["widgetID"] == "closeButton":
            os.chdir(home)
            window.closeWindow() # Close the window
        elif clickedButton["widgetID"] == "Back":
            mainWin.widgets = [] # An array of all the widgets
            os.chdir("../")
            idx2 = 1
            for program in os.listdir(os.getcwd()):
                idx2 += 1
                if not os.path.isdir(program):
                    mainWin.addButton(str(program), idx2+1, 2, program)
                else:
                    mainWin.addButton(str(program), idx2+1, 2, program+"/")

            mainWin.addButton("Back", idx2+2, 2, "../")   
            mainWin.addMenuButton("closeButton", 0, "Close Window") # Create a menu button with the ID of "closeButton"
            mainWin.addTitle("", 1, 2, "File Browser") # Add a title with an id of "str_001"    
            curses.setsyx(1, 1)            
        else:
            if not os.path.isdir(str(clickedButton["widgetID"])):
                curses.endwin()
                os.system(f'nano {str(clickedButton["widgetID"])}')
            else:
                mainWin.widgets = [] # An array of all the widgets
                os.chdir(str(clickedButton["widgetID"]))
                idx2 = 1
                for program in os.listdir(os.getcwd()):
                    idx2 += 1
                    if not os.path.isdir(program):
                        mainWin.addButton(str(program), idx2+1, 2, program)
                    else:
                        mainWin.addButton(str(program), idx2+1, 2, program+"/")

                mainWin.addButton("Back", idx2+2, 2, "../")   
                mainWin.addMenuButton("closeButton", 0, "Close Window") # Create a menu button with the ID of "closeButton"
                mainWin.addTitle("", 1, 2, "File Browser") # Add a title with an id of "str_001"    
                curses.setsyx(1, 1)    
                
mainWin = Window("TWS-FileBrowser", mainWinFunction) # Create a window
mainWin.widgets = [] # An array of all the widgets
mainWin.addMenuButton("closeButton", 0, "Close Window") # Create a menu button with the ID of "closeButton"

mainWin.addTitle("", 1, 2, "File Browser") # Add a title with an id of "str_001"
#	Create a button for each file in the 'Programs' directory
idx2 = 1
for program in os.listdir(os.getcwd()):
    idx2 += 1
    if not os.path.isdir(program):
        mainWin.addButton(str(program), idx2+1, 2, program)
    else:
         mainWin.addButton(str(program), idx2+1, 2, program+"/")   
mainWin.addButton("Back", idx2+2, 2, "../")
