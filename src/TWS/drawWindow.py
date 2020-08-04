# Imports:
from TWS.windowClass import *

# Draw the given window:
def drawWindow(stdscr, window):
    stdscr.hline(0, 0, " ", curses.COLS, curses.color_pair(2)) # Draw a horizontal line at the top of the screen

    # SeDrawtup the character array for the window
    for yBg in range(window.height):
        for xBg in range(window.width):
            stdscr.addstr(window.y+yBg, window.x+xBg, " ",  curses.color_pair(2))

    # The window border and corners:
    for xBorder in range(window.width):
        stdscr.addstr(window.y+window.height-1, window.x+xBorder, "\u2550",  curses.color_pair(2))

    for yBorder in range(window.height-2):
        stdscr.addstr(window.y+yBorder+1, window.x, "\u2551",  curses.color_pair(2))
        stdscr.addstr(window.y+yBorder+1, window.x+window.width-1, "\u2551",  curses.color_pair(2))

    stdscr.addstr(window.y+window.height-1, window.x, "\u255a",  curses.color_pair(2))
    stdscr.addstr(window.y+window.height-1, window.x+window.width-1, "\u255d",  curses.color_pair(2))

    # Draw all the widgets:
    for idx, widget in enumerate(window.widgets):
        if widget["type"] == "regularButton":
            if widget["y"] > 0 and widget["y"] < window.height-1: # If it hasn't been scrolled out of view
                if idx == window.selectedWidget: # If it's the selected widget, then draw it with a different color pair
                    stdscr.addstr(window.y+widget["y"], window.x+widget["x"], str(widget["text"]), curses.color_pair(1))

                else:
                    stdscr.addstr(window.y+widget["y"], window.x+widget["x"], str(widget["text"]), curses.color_pair(2))

        # Only draw the menu bar on the selected window
        elif widget["type"] == "menuButton" and window == openWindows[len(openWindows)-1]:
            if idx == window.selectedWidget: # If it's the selected widget, then draw it with a different color pair
                stdscr.addstr(widget["y"], widget["x"], str(widget["text"]), curses.color_pair(1))

            else:
                stdscr.addstr(widget["y"], widget["x"], str(widget["text"]), curses.color_pair(2))

        elif widget["type"] == "label":
            if widget["y"] > 0 and widget["y"] < window.height-1: # If it hasn't been scrolled out of view
                stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x, str(widget["text"]), curses.color_pair(2))

        elif widget["type"] == "title":
            if widget["y"] > 0 and widget["y"] < window.height-1: # If it hasn't been scrolled out of view
                stdscr.addstr(widget["y"]+window.y, widget["x"]+window.x, str(widget["text"]).upper(), curses.color_pair(2) + curses.A_UNDERLINE)

        elif widget["type"] == "input":
            if widget["y"] > 0 and widget["y"] < window.height-1: # If it hasn't been scrolled out of view
                if idx == window.selectedWidget: # If it's the selected widget, then draw it with a different color pair
                    stdscr.addstr(window.y+widget["y"], window.x+widget["x"], str(widget["text"]), curses.color_pair(1))

                else:
                    stdscr.addstr(window.y+widget["y"], window.x+widget["x"], str(widget["text"]), curses.color_pair(2))


    # Draw the shadow (if there is space on the screen, hence the try, except statement):
    try:
        for yShadow in range(window.y+2, window.y+window.height):
            stdscr.addstr(yShadow, window.x+window.width, " ", curses.color_pair(1))
            stdscr.addstr(yShadow, window.x+window.width+1, " ", curses.color_pair(1))

    except:
        pass

    try:
        for xShadow in range(window.x+2, window.x+window.width+2):
            stdscr.addstr(window.y+window.height, xShadow, " ", curses.color_pair(1))

    except:
        pass
    
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