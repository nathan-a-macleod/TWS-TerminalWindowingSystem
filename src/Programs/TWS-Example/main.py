from TWS.windowClass import * # Import the library like this

# Import other libraries like this:
global datetime
import datetime

# The main function
def mainWinFunction(window, key, clickedButton):
    window.getWidgetByID("timeStr")["text"] = "Time: " + str(datetime.datetime.now().strftime("%I:%M:%S")) # CHanges the text of a widget with an id of "timeStr" with str(datetime.datetime.now().strftime("%I:%M:%S"))
  
    if clickedButton != 0: # If you have clicked a button
        # If the ID of the button being clicked is "closeButton", close the window. (It's highly recommended to include a button the close the window in each program)
        if clickedButton["widgetID"] == "closeButton":
            window.closeWindow() # Close the window

        elif clickedButton["widgetID"] == "btn_001":
            window.getWidgetByID("str_001")["text"] = "You clicked the button!"

        # If you have clicked entered stuff in the input field, and the text entered is "123"
        elif clickedButton["widgetID"] == "input_001" and clickedButton["value"] == "123":
            window.getWidgetByID("str_001")["text"] = "I like the number '123' as well!"

    elif key == ord("j"):
        window.getWidgetByID("str_001")["text"] = "You pressed 'j'!"
        window.alert("You Pressed A Key", "You Pressed the 'j' Key!") # Function to alert the user that they pressed the 'j' key!
 
mainWin = Window(curses.LINES//8, curses.COLS//8-3, int(curses.LINES/1.2)-10, int(curses.COLS/1.3), "TWS-Example", mainWinFunction) # Create a window
mainWin.addMenuButton("closeButton", 0, "Close Window") # Create a menu button with the ID of "closeButton"

mainWin.addTitle("", 2, 2, "This is a title.") # Add a title with an id of "str_001"

mainWin.addLabel("str_001", 4, 2, "Click a button, enter some input in the widget, or press the 'j' key") # Add a label with an id of "str_001"
mainWin.addLabel("timeStr", 5, 2, "Time: " + str(datetime.datetime.now().strftime("%I:%M:%S"))) # Add a label with an id of "timeStr"

mainWin.addButton("btn_001", 6, 2, "Click Me!") # Add a button with an id of "btn_001"
mainWin.addInput("input_001", 7, 2, "Enter a number - try '123':") # Add an input line with an id of "input_001"
