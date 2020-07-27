# Imports
import curses
from TWS.windowClass import *

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
                window.drawWindow()

            char = self.stdscrRoot.getch()

            # Changing the selected button:
            if char == curses.KEY_DOWN or char == curses.KEY_RIGHT:
                if window.selectedWidget < len(window.widgets)-1:
                    window.selectedWidget += 1

            elif char == curses.KEY_UP or char == curses.KEY_LEFT:
                if window.selectedWidget > 0:
                    window.selectedWidget -= 1

            elif char == curses.KEY_ENTER or char == 10 or char == 13:
                window.functionName(window, char, window.widgets[window.selectedWidget][0])

            # Changing the focused window:
            elif char == curses.KEY_SRIGHT:
                try:
                    lastWindow = openWindows[0]
                    openWindows.remove(lastWindow)
                    openWindows.append(lastWindow)

                except:
                    pass

            elif char == curses.KEY_SLEFT:
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

            window.drawWindow()

            self.stdscrRoot.refresh()