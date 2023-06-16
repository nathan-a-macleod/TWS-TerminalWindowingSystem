# Imports
import curses

def windowManager(char, window):
#	Changing the selected button:
    if char == curses.KEY_DOWN or char == ord("j") or char == ord("J"):
        while True:
            if window.selectedWidget < len(window.widgets)-1:
                window.selectedWidget += 1

            else:
                window.selectedWidget = 0

            try:
                if window.widgets[window.selectedWidget]["type"] != "label" and window.widgets[window.selectedWidget]["type"] != "title":
                    break
            except:
                window.selectedWidget = 1

    elif char == curses.KEY_UP or char == ord("k") or char == ord("K"):
        while True:
            if window.selectedWidget > 0:
                window.selectedWidget -= 1
            else:
                try:
                    window.selectedWidget = len(window.widgets)-1
                except:
                    window.selectedWidget = 0                
            try:
                if window.widgets[window.selectedWidget]["type"] != "label" and window.widgets[window.selectedWidget]["type"] != "title":
                    break
            except:
                window.selectedWidget = 1
    elif char == curses.KEY_ENTER or char == 10 or char == 13:
        clickedWidget = window.widgets[window.selectedWidget]
#	Make the input work (Create a new curses.newwin for the input, and save the getstr to the value of clickedWidget)
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
#	Movement of the windows:
    elif char == ord("A"):
        if window.x > 0:
            window.x -= 1

    elif char == ord("D"):
        if window.x+window.width+2 < curses.COLS:
            window.x += 1

    elif char == ord("W"):
        if window.y-1 > 0:
            window.y -= 1

    elif char == ord("S"):
        if window.y + window.height+1 < curses.LINES:
            window.y += 1
    
#	Resizing of the windows:
    elif char == ord("a"):
        if window.width > 10:
            window.width -= 1

    elif char == ord("d"):
        if window.x+window.width+1 < curses.COLS-1:
            window.width += 1

    elif char == ord("w"):
        if window.height > 3:
            window.height -= 1

    elif char == ord("s"):
        if window.y + window.height+1 < curses.LINES:
            window.height += 1  
      
#	Scrolling windows:
    elif char == ord("E") or char == curses.KEY_PPAGE: # Scrolling up:
        for widget in window.widgets:
            if widget["type"] != "menuButton":
                widget["y"] += 1
            
    elif char == ord("Q") or char == curses.KEY_NPAGE: # Scrolling down:
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
