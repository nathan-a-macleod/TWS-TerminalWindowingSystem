# Imports
import curses

openWindows = [] # An array to store all the open windows

# The main window class:
class Window:
    def __init__(self, stdscrRoot, y, x, height, width, windowTitle, functionName):
        # Some variable initialisations
        self.stdscrRoot = stdscrRoot
        self.y = y
        self.x = x
        self.height = height
        self.width = width
        self.windowTitle = windowTitle
        self.functionName = functionName
        self.widgets = [] # An array of all the widgets
        self.selectedWidget = 0

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
        xNew = x
        for char in string:
            try:
                self.chars[y][xNew] = char

            # For wrapping to the next line inside the window
            except:
                y += 1
                xNew = 0

            self.chars[y][xNew] = char
            xNew += 1

    def addButton(self, buttonID, y, x, text):
        # The last parameter (regularButton) tells the program that it's specifically a BUTTON widget (not 'menuButton' for example)
        self.widgets.append([buttonID, y, x, text, "regularButton"])

    # a Menu button is just a regular button, but it's drawn at the very top of the screen
    def addMenuButton(self, buttonID, x, text):
        # The last parameter (regularButton) tells the program that it's specifically a BUTTON widget (not 'menuButton' for example)
        self.widgets.append([buttonID, 0, x, text, "menuButton"])

    def drawWindow(self):
        self.stdscrRoot.hline(0, 0, " ", curses.COLS, curses.color_pair(2)) # Draw a horizontal line at the top of the screen

        # Draw the character array
        for yIdx, currentLine in enumerate(self.chars):
            for xIdx, currentChar in enumerate(currentLine):
                self.stdscrRoot.addstr(self.y+yIdx, self.x+xIdx, currentChar, curses.color_pair(2))

        # Draw all the widgets (if it's the selected window):
        #if self == openWindows[len(openWindows)-1]:
        for idx, widget in enumerate(self.widgets):
            if widget[4] == "regularButton":
                if idx == self.selectedWidget: # If it's the selected widget, then draw it with a different color pair
                    self.stdscrRoot.addstr(self.y+widget[1], self.x+widget[2], str(widget[3]), curses.color_pair(1))

                else:
                    self.stdscrRoot.addstr(self.y+widget[1], self.x+widget[2], str(widget[3]), curses.color_pair(2))

            elif widget[4] == "menuButton" and self == openWindows[len(openWindows)-1]:
                if idx == self.selectedWidget: # If it's the selected widget, then draw it with a different color pair
                    self.stdscrRoot.addstr(widget[1], widget[2], str(widget[3]), curses.color_pair(1))

                else:
                    self.stdscrRoot.addstr(widget[1], widget[2], str(widget[3]), curses.color_pair(2))
        
        # Draw the shadow (if there is space on the screen, hence the try, except statement):
        try:
            for yShadow in range(self.y+2, self.y+self.height):
                self.stdscrRoot.addstr(yShadow, self.x+self.width, " ", curses.color_pair(1))
                self.stdscrRoot.addstr(yShadow, self.x+self.width+1, " ", curses.color_pair(1))

        except:
            pass

        try:
            for xShadow in range(self.x+2, self.x+self.width+2):
                self.stdscrRoot.addstr(self.y+self.height, xShadow, " ", curses.color_pair(1))

        except:
            pass
        
        # The title background
        if self != openWindows[len(openWindows)-1]: # For the selected window, don't draw '\u2592
            for idx in range(self.width):
                self.stdscrRoot.addstr(self.y, self.x+idx, "\u2592", curses.color_pair(4))

        else:
            for idx in range(self.width):
                self.stdscrRoot.addstr(self.y, self.x+idx, " ", curses.color_pair(4))

        # The title text itself
        # if it's the selected window, make the title bold. Otherwise, make it italic:
        if self == openWindows[len(openWindows)-1]:
            self.stdscrRoot.addstr(self.y, self.x, self.windowTitle, curses.color_pair(1) + curses.A_BOLD)

        else:
            self.stdscrRoot.addstr(self.y, self.x, self.windowTitle, curses.color_pair(1) + curses.A_DIM)

    def closeWindow(self):
        # Remove the window from the array of windows
        # The 'Screen' class inside screenCycle.py will not draw this window anymore since it's not in the array
        openWindows.remove(self)
