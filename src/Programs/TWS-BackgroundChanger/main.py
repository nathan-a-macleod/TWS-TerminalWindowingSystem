from CoreLib.Windows.windowClass import * # Import the library like this

# Import other libraries like this:
global datetime
import datetime

# The main function
def mainWinFunction(window, key, clickedButton):
  
    if clickedButton != 0: # If you have clicked a button
        # If the ID of the button being clicked is "closeButton", close the window. (It's highly recommended to include a button the close the window in each program)
        if clickedButton["widgetID"] == "closeButton":
            window.closeWindow() # Close the window

        elif clickedButton["widgetID"] == "btn_001":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            alert("Important", "Color will be changed on restart") # Function to alert the user that they pressed the 'j' key!
            f = open("bgclr.txt", "w")
            f.write("blue")
            f.close()
        elif clickedButton["widgetID"] == "btn_002":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            alert("Important", "Color will be changed on restart") # Function to alert the user that they pressed the 'j' key!
            f = open("bgclr.txt", "w")
            f.write("black")
            f.close()
        elif clickedButton["widgetID"] == "btn_003":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            alert("Important", "Color will be changed on restart") # Function to alert the user that they pressed the 'j' key!
            f = open("bgclr.txt", "w")
            f.write("cyan")
            f.close()
        elif clickedButton["widgetID"] == "btn_004":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            alert("Important", "Color will be changed on restart") # Function to alert the user that they pressed the 'j' key!
            f = open("bgclr.txt", "w")
            f.write("green")
            f.close()
        elif clickedButton["widgetID"] == "btn_005":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            alert("Important", "Color will be changed on restart") # Function to alert the user that they pressed the 'j' key!
            f = open("bgclr.txt", "w")
            f.write("magenta")
            f.close()
        elif clickedButton["widgetID"] == "btn_006":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            alert("Important", "Color will be changed on restart") # Function to alert the user that they pressed the 'j' key!
            f = open("bgclr.txt", "w")
            f.write("red")
            f.close()
        elif clickedButton["widgetID"] == "btn_007":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            alert("Important", "Color will be changed on restart") # Function to alert the user that they pressed the 'j' key!
            f = open("bgclr.txt", "w")
            f.write("white")
            f.close()
        elif clickedButton["widgetID"] == "btn_008":
            window.getWidgetByID("str_001")["text"] = "Set Color"
            alert("Important", "Color will be changed on restart") # Function to alert the user that they pressed the 'j' key!
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
