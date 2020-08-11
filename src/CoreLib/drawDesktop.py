# Imports:
from CoreLib.Windows.windowClass import *

# Draw the given window:
def drawDesktop(stdscr, window):
    # Draw the character array for the window
    for yBg in range(window.height):
        for xBg in range(window.width):
            try:
                if yBg == 0:
                    stdscr.addstr(window.y+yBg, window.x+xBg, " ",  curses.color_pair(2))

                else:
                    stdscr.addstr(window.y+yBg, window.x+xBg, " ",  curses.color_pair(3))

            except:
                pass

    # Draw all the widgets:
    for idx, widget in enumerate(window.widgets):
        if widget["type"] == "regularButton":
            if widget["y"] > 1 and widget["y"] < window.height-1: # If it hasn't been scrolled out of view
                if idx == window.selectedWidget: # If it's the selected widget, then draw it with a different color pair
                    for charIdx, char in enumerate(widget["text"]):
                        if widget["x"]+charIdx > 1 and widget["x"]+charIdx < window.width-2:
                            stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x+charIdx, str(char), curses.color_pair(1))

                else:
                    for charIdx, char in enumerate(widget["text"]):
                        if widget["x"]+charIdx > 1 and widget["x"]+charIdx < window.width-2:
                            stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x+charIdx, str(char), curses.color_pair(2))

        # The menu bar
        elif widget["type"] == "menuButton":
            if idx == window.selectedWidget: # If it's the selected widget, then draw it with a different color pair
                stdscr.addstr(widget["y"]+window.y-1, widget["x"]+window.x, str(widget["text"]), curses.color_pair(1) + curses.A_UNDERLINE)

            else:
                stdscr.addstr(widget["y"]+window.y-1, widget["x"]+window.x, str(widget["text"]), curses.color_pair(2) + curses.A_UNDERLINE)

        elif widget["type"] == "label":
            if widget["y"] > 1 and widget["y"] < window.height-1: # If it hasn't been scrolled out of view
                for charIdx, char in enumerate(widget["text"]):
                    if widget["x"]+charIdx > 1 and widget["x"]+charIdx < window.width-2:
                        stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x+charIdx, str(char), curses.color_pair(3))

        elif widget["type"] == "title":
            if widget["y"] > 1 and widget["y"] < window.height-1: # If it hasn't been scrolled out of view
                for charIdx, char in enumerate(widget["text"]):
                    if widget["x"]+charIdx > 1 and widget["x"]+charIdx < window.width-2:
                        stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x+charIdx, str(char).upper(), curses.color_pair(3) + curses.A_UNDERLINE)

        elif widget["type"] == "input":
            if widget["y"] > 1 and widget["y"] < window.height-1: # If it hasn't been scrolled out of view
                if idx == window.selectedWidget: # If it's the selected widget, then draw it with a different color pair
                    for charIdx, char in enumerate(widget["text"]):
                        if widget["x"]+charIdx > 1 and widget["x"]+charIdx < window.width-2:
                            stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x+charIdx, str(char), curses.color_pair(1))

                else:
                    for charIdx, char in enumerate(widget["text"]):
                        if widget["x"]+charIdx > 1 and widget["x"]+charIdx < window.width-2:
                            stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x+charIdx, str(char), curses.color_pair(3))