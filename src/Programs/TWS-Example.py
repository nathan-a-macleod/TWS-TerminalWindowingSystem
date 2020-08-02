from TWS.windowClass import * # Import the library like this

# Import other libraries like this:
global datetime
import datetime

# The main function
def mainWinFunction(window, key, clickedButton):
    window.getWidgetByID("timeStr")["text"] = "Time: " + str(datetime.datetime.now().strftime("%I:%M:%S")) # CHanges the text of a widget with an id of "timeStr" with str(datetime.datetime.now().strftime("%I:%M:%S"))
  
    if clickedButton != 0: # If you have clicked a button
        if clickedButton["widgetID"] == "closeButton": # If the ID of the clicked button is "closeButton"
            window.closeWindow() # Close the window
 
mainWin = Window(curses.LINES//8+2, curses.COLS//8, int(curses.LINES/1.3)-10, int(curses.COLS/1.4), "TWS-Example", mainWinFunction) # Create a window
mainWin.addMenuButton("closeButton", 0, "Close Window") # Create a menu button with the ID of "closeButton"
mainWin.addLabel("timeStr", 1, 2, "Time: " + str(datetime.datetime.now().strftime("%I:%M:%S"))) # Add a label with an id of "timeStr"