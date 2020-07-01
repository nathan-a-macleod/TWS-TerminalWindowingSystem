import curses

# Function that only finishes if the user presses Ctrl-G (Used in things like the help window)
def getCtrlG(stdscr):
    key = stdscr.getch()
    if key != 7:
        getCtrlG(stdscr)

# Function for curses to get input, then enter, similar to getch() (but lets the user press enter) - need to make backspace and arrow keys work
def getInput(stdscr, y, x, prompt, colorPair):
    stdscr.addstr(y, x, prompt, colorPair)

    string = ""

    while True:
        char = stdscr.getkey()

        try:
            if ord(char) == 10:
                break
            
            else:
                string += char

        except:
            pass

    return string

# Function to create a new window, with the correct size, etc
def createNewWindow(title):
    stdscr = curses.newwin(curses.LINES-1, curses.COLS, 1, 0)
    stdscr.bkgd(" ", curses.color_pair(3))
    stdscr.border()
    stdscr.addstr(0, 0, title)
    stdscr.refresh()
    
    return stdscr