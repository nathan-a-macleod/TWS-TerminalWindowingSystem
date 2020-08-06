# Imports
import curses
import os

openWindows = [] # An array to store all the open windows

# The main window class:
class Window:
    def __init__(self, y, x, height, width, windowTitle, functionName):
        # Some variable initialisations
        self.y = y
        self.x = x
        self.height = height
        self.width = width
        self.windowTitle = "(" + str(len(openWindows)) + ") " + windowTitle
        self.functionName = functionName
        self.widgets = [] # An array of all the widgets
        self.selectedWidget = 0

        if self.y < 3:
            self.y = 3

        openWindows.append(self) # Adds the window to the array containing all the open windows

    # Add individual letters from 'string' to the character array
    def addLabel(self, widgetID, y, x, text):
        self.widgets.append({"widgetID":widgetID, "y":y+1, "x":x, "text":text, "type":"label"})

        # Make sure you don't start by "selecting" a label:
        try:
            while self.widgets[self.selectedWidget]["type"] == "label":
                self.selectedWidget += 1

        # If it doesn't work it probably means there aren't any button widgets yet
        except:
            pass

    # Add individual letters from 'string' to the character array
    def addTitle(self, widgetID, y, x, text):
        self.widgets.append({"widgetID":widgetID, "y":y+1, "x":x, "text":text, "type":"title"})

        # Make sure you don't start by "selecting" a title:
        try:
            while self.widgets[self.selectedWidget]["type"] == "title":
                self.selectedWidget += 1

        # If it doesn't work it probably means there aren't any button widgets yet
        except:
            pass

    def addButton(self, widgetID, y, x, text):
        self.widgets.append({"widgetID":widgetID, "y":y+1, "x":x, "text":text, "type":"regularButton"})

    # a Menu button is just a regular button, but it's drawn at the very top of the screen
    def addMenuButton(self, widgetID, x, text):
        self.widgets.append({"widgetID":widgetID, "y":1, "x":x+2, "text":text, "type":"menuButton"})

    def addInput(self, widgetID, y, x, text):
        self.widgets.append({"widgetID":widgetID, "y":y+1, "x":x, "text":text, "value":"", "type":"input"})

    def getWidgetByID(self, ID):
        for widget in self.widgets:
            if widget["widgetID"] == ID:
                return widget

    # Function to add an alert:
    def alert(self, title, text):
        winWidth = len(text)+3
        alertWin = curses.newwin(6, winWidth, 10, 10)
        alertWin.bkgd(" ", curses.color_pair(2))
        alertWin.border()

        # The window border and corners:
        for xBorder in range(winWidth-1):
            alertWin.addstr(5, xBorder, "\u2550",  curses.color_pair(2))
            
        for yBorder in range(4):
            alertWin.addstr(yBorder+1, 0, "\u2551",  curses.color_pair(2))
            alertWin.addstr(yBorder+1, winWidth-1, "\u2551",  curses.color_pair(2))

        alertWin.addstr(5, 0, "+",  curses.color_pair(2))
        alertWin.insch(5, winWidth-1, "+",  curses.color_pair(2))

        # The title background:
        for idx in range(winWidth):
            alertWin.addstr(0, idx, " ", curses.color_pair(4))
            
        # The title text
        alertWin.addstr(0, 0, "! " + str(title), curses.color_pair(4) + curses.A_BOLD)

        alertWin.addstr(2, 2, str(text))
        alertWin.addstr(4, 2, "Press any key to continue...")
        alertWin.refresh()
        alertWin.getch()

    def closeWindow(self):
        # Remove the window from the array of windows
        # The 'Screen' class inside screenCycle.py will not draw this window anymore since it's not in the array
        openWindows.remove(self)
