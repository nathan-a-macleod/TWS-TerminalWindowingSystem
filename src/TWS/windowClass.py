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
        self.strings = [] # An array of all the non interactive widgets (right now just strings)

        openWindows.append(self) # Adds the window to the array containing all the open windows

        # Setup the character array for the window
        self.chars = []
        for yBg in range(self.height):
            currentLine = []
            for xBg in range(self.width):
                currentLine.append(" ")

            self.chars.append(currentLine)

        # The window border and corners:
        for xBorder in range(self.width):
            self.addString(self.height-1, xBorder, "\u2550")

        for yBorder in range(self.height-2):
            self.addString(yBorder+1, 0, "\u2551")
            self.addString(yBorder+1, self.width-1, "\u2551")

        self.addString(self.height-1, 0, "\u255a")
        self.addString(self.height-1, self.width-1, "\u255d")

    # Add individual letters from 'string' to the character array
    def addString(self, y, x, string):
        self.strings.append([y, x, string, True])

    def addButton(self, buttonID, y, x, text):
        # The last parameter (regularButton) tells the program that it's specifically a BUTTON widget (not 'menuButton' for example)
        self.widgets.append([buttonID, y, x, text, "regularButton"])

    # a Menu button is just a regular button, but it's drawn at the very top of the screen
    def addMenuButton(self, buttonID, x, text):
        # The last parameter (regularButton) tells the program that it's specifically a BUTTON widget (not 'menuButton' for example)
        self.widgets.append([buttonID, 0, x, text, "menuButton"])

    def closeWindow(self):
        # Remove the window from the array of windows
        # The 'Screen' class inside screenCycle.py will not draw this window anymore since it's not in the array
        openWindows.remove(self)
