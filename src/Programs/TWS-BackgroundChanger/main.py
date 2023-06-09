from CoreLib.Windows.windowClass import * # Import the library like this
global SetThemeColors
from CoreLib.setcolor import SetThemeColors
# Import other libraries like this:
global datetime
import datetime
global re
import re
from pathlib import Path
global Path
global msg
msg = "Changed Config"

# The main function
def mainWinFunction(window, key, clickedButton):
    SetThemeColors()
    global color
    global lines
    global theme
    global change
    f3 = open("config.cfg", "r")
    temp = f3.readlines()
    theme = temp[1]
    color = temp[0]
    if clickedButton != 0: # If you have clicked a button
        # If the ID of the button being clicked is "closeButton", close the window. (It's highly recommended to include a button the close the window in each program)
        if clickedButton["widgetID"] == "closeButton":
            window.closeWindow() # Close the window
        else:
            if clickedButton["widgetID"] == "btn_001":
                color = "COLOR:blue" 
                change = "colors"
            elif clickedButton["widgetID"] == "btn_002":
                color = "COLOR:black"
                change = "colors"
            elif clickedButton["widgetID"] == "btn_003":
                color = "COLOR:cyan"
                change = "colors"
            elif clickedButton["widgetID"] == "btn_004":
                color = "COLOR:green"
                change = "colors"
            elif clickedButton["widgetID"] == "btn_005":
                color = "COLOR:magenta"
                change = "colors"
            elif clickedButton["widgetID"] == "btn_006":
                color = "COLOR:red"
                change = "colors"
            elif clickedButton["widgetID"] == "btn_007":
                color = "COLOR:white"
                change = "colors"
            elif clickedButton["widgetID"] == "btn_008":
                color = "COLOR:yellow"
                change = "colors"
                
            elif clickedButton["widgetID"] == "btn_009":
                theme = "THEME:light"
                change = "theme"
            elif clickedButton["widgetID"] == "btn_00A":
                theme = "THEME:dark"
                change = "theme"
                
            window.getWidgetByID("str_001")["text"] = msg
            
            with open("config.cfg", "r") as f:
                lines = f.readlines()
            if change == "colors":
                lines[0] = f"{color}\n"
            elif change == "theme":
                lines[1] = f"{theme}\n"
            else:
                lines[0] = f"{color}\n"
            with open("config.cfg", "w") as f:
                f.writelines(lines)   
                f.close()
mainWin = Window("TWS-BackgroundChanger", mainWinFunction) # Create a window
mainWin.addMenuButton("closeButton", 0, "Close Window") # Create a menu button with the ID of "closeButton"
mainWin.addTitle("", 2, 2, "Change System Color Options") # Add a title with an id of "str_001"

mainWin.addLabel("str_001", 4, 2, "") # Add a label with an id of "str_001"
mainWin.addButton("btn_001", 6, 2, "Blue") # Add a button with an id of "btn_001"
mainWin.addButton("btn_002", 7, 2, "Black") # Add a button with an id of "btn_002"
mainWin.addButton("btn_003", 8, 2, "Cyan") # Add a button with an id of "btn_003"
mainWin.addButton("btn_004", 9, 2, "Green") # Add a button with an id of "btn_004"
mainWin.addButton("btn_005", 10, 2, "Magenta") # Add a button with an id of "btn_005"
mainWin.addButton("btn_006", 11, 2, "Red") # Add a button with an id of "btn_006"
mainWin.addButton("btn_007", 12, 2, "White") # Add a button with an id of "btn_007"
mainWin.addButton("btn_008", 13, 2, "Yellow") # Add a button with an id of "btn_008"
mainWin.addLabel("str_002", 15, 2, "Themes") # Add a label with an id of "str_002"
mainWin.addButton("btn_009", 16, 2, "Light") # Add a button with an id of "btn_009"
mainWin.addButton("btn_00A", 17, 2, "Dark") # Add a button with an id of "btn_00A"
