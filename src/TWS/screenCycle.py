# Imports
import curses
from TWS.windowClass import *
from TWS.drawWindow import *

# The main screen class where everything happens:
class Screen:
    def __init__(self, stdscrRoot):
        self.stdscrRoot = stdscrRoot

    # The main function in the class
    def mainloop(self):
        while True:
            self.stdscrRoot.erase() # Clear the screen

            # Draw all the windows, but don't give the key that's been clicked (only do that for the last window)
            for window in openWindows:
                window.functionName(window, -1, 0)
                drawWindow(self.stdscrRoot, window)

            char = self.stdscrRoot.getch()

            # Changing the selected button:
            if char == curses.KEY_DOWN:
                while True:
                    if window.selectedWidget < len(window.widgets)-1:
                        window.selectedWidget += 1

                    else:
                        window.selectedWidget = 0

                    if window.widgets[window.selectedWidget]["type"] != "label" and window.widgets[window.selectedWidget]["type"] != "title":
                        break

            elif char == curses.KEY_UP:
                while True:
                    if window.selectedWidget > 0:
                        window.selectedWidget -= 1

                    else:
                        window.selectedWidget = len(window.widgets)-1

                    if window.widgets[window.selectedWidget]["type"] != "label" and window.widgets[window.selectedWidget]["type"] != "title":
                        break

            elif char == curses.KEY_ENTER or char == 10 or char == 13:
                clickedWidget = window.widgets[window.selectedWidget]
                # Make the input work
                if clickedWidget["type"] == "input":
                    inputWindow = curses.newwin(1, 60, window.y+clickedWidget["y"], window.x+clickedWidget["x"]+len(clickedWidget["text"])+1)
                    inputWindow.bkgd(" ", curses.color_pair(2))
                    curses.curs_set(1)
                    curses.echo()
                    inputWindow.refresh()
                    clickedWidget["value"] = str(inputWindow.getstr())
                    clickedWidget["value"] = clickedWidget["value"][2:]
                    clickedWidget["value"] = clickedWidget["value"][:-1]
                    curses.curs_set(0)
                    curses.noecho()

                window.functionName(window, char, clickedWidget)

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
            elif char == ord("A"):
                if window.x-1 > 0:
                    window.x -= 2

            elif char == ord("D"):
                if window.x+window.width+1 < curses.COLS:
                    window.x += 2

            elif char == ord("W"):
                if window.y-1 > 0:
                    window.y -= 1

            elif char == ord("S"):
                if window.y + window.height+1 < curses.LINES:
                    window.y += 1

            # Scrolling windows:
            elif char == ord("E"): # Scrolling up:
                for widget in window.widgets:
                    if widget["type"] != "menuButton":
                        widget["y"] += 1
                    
            elif char == ord("Q"): # Scrolling down:
                for widget in window.widgets:
                    if widget["type"] != "menuButton":
                        widget["y"] -= 1

            else:
                window.functionName(window, char, 0)

            drawWindow(self.stdscrRoot, window)

            self.stdscrRoot.refresh()
