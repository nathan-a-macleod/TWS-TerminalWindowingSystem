# Imports:
from CoreLib.Windows.windowClass import *

# Draw the given window:
def drawWindow(stdscr, window):
    # Draw the character array for the window
    for yBg in range(window.height):
        for xBg in range(window.width+1):
            try:
                stdscr.addstr(window.y+yBg, window.x+xBg, " ",  curses.color_pair(2))

            except:
                pass

    # Draw a horizontal line at the top of the window
    for charIdx in range(window.x, window.x+window.width):
        stdscr.addstr(window.y+1, charIdx, " ", curses.color_pair(2) + curses.A_UNDERLINE)

    # The window border and corners:
    for xBorder in range(window.width):
        try:
            stdscr.addstr(window.y+window.height-1, window.x+xBorder, "\u2550",  curses.color_pair(2))

        except:
            pass

    for yBorder in range(window.height-2):
        try:
            stdscr.addstr(window.y+yBorder+1, window.x, "\u2551",  curses.color_pair(2))
            stdscr.addstr(window.y+yBorder+1, window.x+window.width, "\u2551",  curses.color_pair(2))

        except:
            pass

    # Corners:
    stdscr.addstr(window.y+window.height-1, window.x, "\u255a",  curses.color_pair(2))
    try:
        stdscr.addstr(window.y+window.height-1, window.x+window.width, "\u255d",  curses.color_pair(2))

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

        # Only draw the menu bar on the selected window
        elif widget["type"] == "menuButton":
            if idx == window.selectedWidget: # If it's the selected widget, then draw it with a different color pair
                stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x, str(widget["text"]), curses.color_pair(1) + curses.A_UNDERLINE)

            else:
                stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x, str(widget["text"]), curses.color_pair(2) + curses.A_UNDERLINE)

        elif widget["type"] == "label":
            if widget["y"] > 1 and widget["y"] < window.height-1: # If it hasn't been scrolled out of view
                for charIdx, char in enumerate(widget["text"]):
                    if widget["x"]+charIdx > 1 and widget["x"]+charIdx < window.width-2:
                        stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x+charIdx, str(char), curses.color_pair(2))

        elif widget["type"] == "title":
            if widget["y"] > 1 and widget["y"] < window.height-1: # If it hasn't been scrolled out of view
                for charIdx, char in enumerate(widget["text"]):
                    if widget["x"]+charIdx > 1 and widget["x"]+charIdx < window.width-2:
                        stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x+charIdx, str(char).upper(), curses.color_pair(2) + curses.A_UNDERLINE)

        elif widget["type"] == "input":
            if widget["y"] > 1 and widget["y"] < window.height-1: # If it hasn't been scrolled out of view
                if idx == window.selectedWidget: # If it's the selected widget, then draw it with a different color pair
                    for charIdx, char in enumerate(widget["text"]):
                        if widget["x"]+charIdx > 1 and widget["x"]+charIdx < window.width-2:
                            stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x+charIdx, str(char), curses.color_pair(1))

                else:
                    for charIdx, char in enumerate(widget["text"]):
                        if widget["x"]+charIdx > 1 and widget["x"]+charIdx < window.width-2:
                            stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x+charIdx, str(char), curses.color_pair(2))

    
    # The title background
    if window != openWindows[len(openWindows)-1]: # For the selected window, don't draw '\u2592
        for idx in range(window.width):
            stdscr.addstr(window.y, window.x+idx, "\u2592", curses.color_pair(4))

    else:
        for idx in range(window.width):
            stdscr.addstr(window.y, window.x+idx, " ", curses.color_pair(4))

    # The title text itself
    # if it's the selected window, make the title bold. Otherwise, make it italic:
    if window == openWindows[len(openWindows)-1]:
        stdscr.addstr(window.y, window.x, window.windowTitle, curses.color_pair(1) + curses.A_BOLD)

    else:
        stdscr.addstr(window.y, window.x, window.windowTitle, curses.color_pair(1) + curses.A_DIM)
