from CoreLib.Windows.windowClass import * # Import the library like this

# Import other libraries like this:
global datetime
import datetime
global subprocess
import subprocess
# The main function
def mainWinFunction(window, key, clickedButton):
  
    if clickedButton != 0: # If you have clicked a button
        # If the ID of the button being clicked is "closeButton", close the window. (It's highly recommended to include a button the close the window in each program)
        if clickedButton["widgetID"] == "closeButton":
            window.closeWindow() # Close the window

        elif clickedButton["widgetID"] == "btn_001":
            curses.endwin()
            try:
                os.system("elinks google.com")  
            except:          
                window.getWidgetByID("str_001")["text"] = "Elinks is not installed!"          
                
mainWin = Window("Elinks", mainWinFunction) # Create a window
mainWin.addMenuButton("closeButton", 0, "Close Window") # Create a menu button with the ID of "closeButton"

mainWin.addTitle("", 1, 2, "Web Browser")
mainWin.addTitle("", 3, 2,"Open new tab - t")
mainWin.addTitle("", 4, 2,"Goto URL - g")
mainWin.addTitle("", 5, 2,"Go back - Left")
mainWin.addTitle("", 6, 2,"Go forward - u")
mainWin.addTitle("", 7, 2,"Exit - q")
mainWin.addTitle("", 8, 2,"Toggle images - * (when compatible)")
mainWin.addTitle("", 9, 2,"Toggle link numbering - .")
mainWin.addTitle("", 10, 2,"Toggle document colours - %")
mainWin.addTitle("", 11, 2,"Next tab - >")
mainWin.addTitle("", 12, 2,"Previous tab - <")
mainWin.addTitle("", 13, 2,"Close tab - c")
mainWin.addTitle("", 14, 2,"Open in new tab in background - T")


mainWin.addButton("btn_001", 16, 2, "Go To ELinks Web Browser") # Add a button with an id of "btn_001"

