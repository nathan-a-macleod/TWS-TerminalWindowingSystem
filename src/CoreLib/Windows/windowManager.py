# Imports
import curses

def windowManager(char, window):
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
        # Make the input work (Create a new curses.newwin for the input, and save the getstr to the value of clickedWidget)
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
        
    # Scrolling windows:
    elif char == ord("E"): # Scrolling up:
        for widget in window.widgets:
            if widget["type"] != "menuButton":
                widget["y"] += 1
            
    elif char == ord("Q"): # Scrolling down:
        for widget in window.widgets:
            if widget["type"] != "menuButton":
                widget["y"] -= 1

    elif char == ord("e"): # Scrolling right:
        for widget in window.widgets:
            if widget["type"] != "menuButton":
                widget["x"] -= 1
            
    elif char == ord("q"): # Scrolling left:
        for widget in window.widgets:
            if widget["type"] != "menuButton":
                widget["x"] += 1