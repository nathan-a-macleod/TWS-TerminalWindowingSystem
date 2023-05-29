from CoreLib.Windows.windowClass import * # Import the library like this

# Import other libraries like this:
global datetime
import datetime
global re
import re
# The main function
def mainWinFunction(window, key, clickedButton):
  
    if clickedButton != 0: # If you have clicked a button
        # If the ID of the button being clicked is "closeButton", close the window. (It's highly recommended to include a button the close the window in each program)
        if clickedButton["widgetID"] == "closeButton":
            window.closeWindow() # Close the window
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
            if bgnd == "white" or bgnd == "yellow" or bgnd == "cyan" or bgnd == "magenta":
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
            
        elif clickedButton["widgetID"] == "btn_001":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            f = open("bgclr.txt", "w")
            f.write("blue")
            f.close()
        elif clickedButton["widgetID"] == "btn_002":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            f = open("bgclr.txt", "w")
            f.write("black")
            f.close()
        elif clickedButton["widgetID"] == "btn_003":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            f = open("bgclr.txt", "w")
            f.write("cyan")
            f.close()
        elif clickedButton["widgetID"] == "btn_004":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            f = open("bgclr.txt", "w")
            f.write("green")
            f.close()
        elif clickedButton["widgetID"] == "btn_005":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            f = open("bgclr.txt", "w")
            f.write("magenta")
            f.close()
        elif clickedButton["widgetID"] == "btn_006":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            f = open("bgclr.txt", "w")
            f.write("red")
            f.close()
        elif clickedButton["widgetID"] == "btn_007":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            f = open("bgclr.txt", "w")
            f.write("white")
            f.close()
        elif clickedButton["widgetID"] == "btn_008":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            f = open("bgclr.txt", "w")
            f.write("yellow")
            f.close()
                 
mainWin = Window("TWS-BackgroundChanger", mainWinFunction) # Create a window
mainWin.addMenuButton("closeButton", 0, "Close Window") # Create a menu button with the ID of "closeButton"
mainWin.addTitle("", 2, 2, "Change System Background Color") # Add a title with an id of "str_001"

mainWin.addLabel("str_001", 4, 2, "") # Add a label with an id of "str_001"
mainWin.addButton("btn_001", 6, 2, "Blue") # Add a button with an id of "btn_001"
mainWin.addButton("btn_002", 7, 2, "Black") # Add a button with an id of "btn_002"
mainWin.addButton("btn_003", 8, 2, "Cyan") # Add a button with an id of "btn_003"
mainWin.addButton("btn_004", 9, 2, "Green") # Add a button with an id of "btn_004"
mainWin.addButton("btn_005", 10, 2, "Magenta") # Add a button with an id of "btn_005"
mainWin.addButton("btn_006", 11, 2, "Red") # Add a button with an id of "btn_006"
mainWin.addButton("btn_007", 12, 2, "White") # Add a button with an id of "btn_007"
mainWin.addButton("btn_008", 13, 2, "Yellow") # Add a button with an id of "btn_008"
