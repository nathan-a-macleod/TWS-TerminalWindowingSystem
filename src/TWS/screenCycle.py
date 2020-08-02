# Imports
import curses
from TWS.windowClass import *

# The main screen class where everything happens:
class Screen:
    def __init__(self, stdscrRoot):
        self.stdscrRoot = stdscrRoot

    # Draw the given window:
    def drawWindow(self, window):
        self.stdscrRoot.hline(0, 0, " ", curses.COLS, curses.color_pair(2)) # Draw a horizontal line at the top of the screen

        # SeDrawtup the character array for the window
        for yBg in range(window.height):
            for xBg in range(window.width):
                self.stdscrRoot.addstr(window.y+yBg, window.x+xBg, " ",  curses.color_pair(2))

        # The window border and corners:
        for xBorder in range(window.width):
            self.stdscrRoot.addstr(window.y+window.height-1, window.x+xBorder, "\u2550",  curses.color_pair(2))

        for yBorder in range(window.height-2):
            self.stdscrRoot.addstr(window.y+yBorder+1, window.x, "\u2551",  curses.color_pair(2))
            self.stdscrRoot.addstr(window.y+yBorder+1, window.x+window.width-1, "\u2551",  curses.color_pair(2))

        self.stdscrRoot.addstr(window.y+window.height-1, window.x, "\u255a",  curses.color_pair(2))
        self.stdscrRoot.addstr(window.y+window.height-1, window.x+window.width-1, "\u255d",  curses.color_pair(2))

        # Draw all the widgets:
        for idx, widget in enumerate(window.widgets):
            if widget["type"] == "regularButton":
                if idx == window.selectedWidget: # If it's the selected widget, then draw it with a different color pair
                    self.stdscrRoot.addstr(window.y+widget["y"], window.x+widget["x"], str(widget["text"]), curses.color_pair(1))

                else:
                    self.stdscrRoot.addstr(window.y+widget["y"], window.x+widget["x"], str(widget["text"]), curses.color_pair(2))

            # Only draw the menu bar on the selected window
            elif widget["type"] == "menuButton" and window == openWindows[len(openWindows)-1]:
                if idx == window.selectedWidget: # If it's the selected widget, then draw it with a different color pair
                    self.stdscrRoot.addstr(widget["y"], widget["x"], str(widget["text"]), curses.color_pair(1))

                else:
                    self.stdscrRoot.addstr(widget["y"], widget["x"], str(widget["text"]), curses.color_pair(2))

            elif widget["type"] == "label":
                self.stdscrRoot.addstr(widget["y"]+window.y, widget["x"]+window.x, str(widget["text"]), curses.color_pair(2))

        # Draw the shadow (if there is space on the screen, hence the try, except statement):
        try:
            for yShadow in range(window.y+2, window.y+window.height):
                self.stdscrRoot.addstr(yShadow, window.x+window.width, " ", curses.color_pair(1))
                self.stdscrRoot.addstr(yShadow, window.x+window.width+1, " ", curses.color_pair(1))

        except:
            pass

        try:
            for xShadow in range(window.x+2, window.x+window.width+2):
                self.stdscrRoot.addstr(window.y+window.height, xShadow, " ", curses.color_pair(1))

        except:
            pass
        
        # The title background
        if window != openWindows[len(openWindows)-1]: # For the selected window, don't draw '\u2592
            for idx in range(window.width):
                self.stdscrRoot.addstr(window.y, window.x+idx, "\u2592", curses.color_pair(4))

        else:
            for idx in range(window.width):
                self.stdscrRoot.addstr(window.y, window.x+idx, " ", curses.color_pair(4))

        # The title text itself
        # if it's the selected window, make the title bold. Otherwise, make it italic:
        if window == openWindows[len(openWindows)-1]:
            self.stdscrRoot.addstr(window.y, window.x, window.windowTitle, curses.color_pair(1) + curses.A_BOLD)

        else:
            self.stdscrRoot.addstr(window.y, window.x, window.windowTitle, curses.color_pair(1) + curses.A_DIM)

    # The main function in the class
    def mainloop(self):
        while True:
            self.stdscrRoot.erase() # Clear the screen

            # Draw all the windows, but don't give the key that's been clicked (only do that for the last window)
            for window in openWindows:
                window.functionName(window, -1, 0)
                self.drawWindow(window)

            char = self.stdscrRoot.getch()

            # Changing the selected button:
            if char == curses.KEY_DOWN:
                while True:
                    if window.selectedWidget < len(window.widgets)-1:
                        window.selectedWidget += 1

                    else:
                        window.selectedWidget = 0

                    if window.widgets[window.selectedWidget]["type"] != "label":
                        break

            elif char == curses.KEY_UP:
                while True:
                    if window.selectedWidget > 0:
                        window.selectedWidget -= 1

                    else:
                        window.selectedWidget = len(window.widgets)-1

                    if window.widgets[window.selectedWidget]["type"] != "label":
                        break

            elif char == curses.KEY_ENTER or char == 10 or char == 13:
                window.functionName(window, char, window.widgets[window.selectedWidget])

            # Changing the focused window:
            elif char == curses.KEY_RIGHT:
                try:
                    lastWindow = openWindows[0]
                    openWindows.remove(lastWindow)
                    openWindows.append(lastWindow)

                except:
                    pass

            elif char == curses.KEY_LEFT:
                try:
                    lastWindow = openWindows[len(openWindows)-1]
                    openWindows.remove(lastWindow)
                    openWindows.insert(0, lastWindow)

                except:
                    pass

            # Movement of the windows:
            if char == ord("a"):
                if window.x-1 > 0:
                    window.x -= 2

            elif char == ord("d"):
                if window.x+window.width+1 < curses.COLS:
                    window.x += 2

            elif char == ord("w"):
                if window.y-1 > 0:
                    window.y -= 1

            elif char == ord("s"):
                if window.y + window.height+1 < curses.LINES:
                    window.y += 1

            else:
                window.functionName(window, char, 0)

            self.drawWindow(window)

            self.stdscrRoot.refresh()