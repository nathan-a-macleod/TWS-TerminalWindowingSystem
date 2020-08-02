# Imports
import curses

openWindows = [] # An array to store all the open windows

# The main window class:
class Window:
    def __init__(self, y, x, height, width, windowTitle, functionName):
        # Some variable initialisations
        self.y = y
        self.x = x
        self.height = height
        self.width = width
        self.windowTitle = windowTitle
        self.functionName = functionName
        self.widgets = [] # An array of all the widgets
        self.selectedWidget = 0

        openWindows.append(self) # Adds the window to the array containing all the open windows

    # Add individual letters from 'string' to the character array
    def addLabel(self, widgetID, y, x, text):
        self.widgets.append({"widgetID":widgetID, "y":y, "x":x, "text":text, "type":"label"})

        # Make sure you don't start by "selecting" a label:
        try:
            while self.widgets[self.selectedWidget]["type"] == "label":
                self.selectedWidget += 1

        # If it doesn't work it probably means there aren't any button widgets yet
        except:
            pass

    def addButton(self, widgetID, y, x, text):
        self.widgets.append({"widgetID":widgetID, "y":y, "x":x, "text":text, "type":"regularButton"})

    # a Menu button is just a regular button, but it's drawn at the very top of the screen
    def addMenuButton(self, widgetID, x, text):
        self.widgets.append({"widgetID":widgetID, "y":0, "x":x, "text":text, "type":"menuButton"})

    def getWidgetByID(self, ID):
        for widget in self.widgets:
            if widget["widgetID"] == ID:
                return widget

    def closeWindow(self):
        # Remove the window from the array of windows
        # The 'Screen' class inside screenCycle.py will not draw this window anymore since it's not in the array
        openWindows.remove(self)
