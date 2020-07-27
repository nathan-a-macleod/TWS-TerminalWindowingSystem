# Import the curses library...
import curses
import datetime
import psutil
# ...and some other files
import terminalShell
from TWS.windowClass import *
from TWS.screenCycle import *

# The main function
def main(stdscr):
    # Color combinations
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK) # For the shadows
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE) # Same, but inverted
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE) # The background color
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK) # For the titles

    # Stdscr settings
    curses.curs_set(0)
    stdscr.bkgd(" ", curses.color_pair(3))
    stdscr.refresh()
    stdscr.timeout(500)
    
    # The core of the program
    def clockWinFunction(window, key, selectedButtonID):
        window.addString(1, 2, str(datetime.datetime.now().strftime("%I:%M:%S")))

        if selectedButtonID == "closeButton":
            window.closeWindow()

    def CPUMonFunction(window, key, selectedButtonID):
        window.addString(1, 2, str(psutil.cpu_percent()) + " % ")

        if selectedButtonID == "closeButton":
            window.closeWindow()

    def helpWinFunction(window, key, selectedButtonID):
        window.addString(2, 2, "'TWS' (short for 'Terminal Windowing System') is a Terminal/Operating environment program with a few other programs (written in Python).")
        window.addString(3, 2, "You can think of it sort of like a terminal-desktop environment - but it's really just a collection of programs you can run inside a terminal.")
        window.addString(5, 2, "The Github page is at https://github.com/nathan-a-macleod/terminalEnv")
        window.addString(7, 2, "Controls: ")
        window.addString(8, 2, "----------")
        window.addString(9, 2, "<Arrow Keys>: Highlight a selection")
        window.addString(10, 2, "Shift, <Arrow Keys>: Focuses a different window.")
        window.addString(11, 2, "<ENTER>: 'Click' a selection")
        window.addString(12, 2, "WASD: Moves the selected window.")
        window.addString(14, 2, "Most programs will have at least a few buttons to select. Some of those buttons may be in the toolbar (look at the top of the screen).")
        window.addString(15, 2, "This window has a few buttons at the top - one of them is to close the window, the rest don't do anything.")

        if selectedButtonID == "closeButton":
            window.closeWindow()

    def appLauncherFunction(window, key, selectedButtonID):
        if selectedButtonID == "button_001":
            curses.endwin()
            terminalShell.main()

        elif selectedButtonID == "button_002":
            helpWin = Window(stdscr, curses.LINES//9, curses.COLS//9, int(curses.LINES/1.2)-10, int(curses.COLS/1.3), "TWS-Help", helpWinFunction)
            helpWin.addMenuButton("closeButton", 0, "Close Window")
            helpWin.addMenuButton("", 17, "MenuItem1")
            helpWin.addMenuButton("", 31, "MenuItem2")

        elif selectedButtonID == "button_003":
            clockWin = Window(stdscr, 1, 0, 3, 12, "TWS-Clock", clockWinFunction)
            clockWin.addMenuButton("closeButton", 0, "Close Window")

        elif selectedButtonID == "button_004":
            CPUMonWin = Window(stdscr, 1, 0, 3, len("TWS-CPU_Monitor"), "TWS-CPU_Monitor", CPUMonFunction)
            CPUMonWin.addMenuButton("closeButton", 0, "Close Window")

        elif selectedButtonID == "button_005":
            pass

        elif selectedButtonID == "button_006":
            exit()

    scr = Screen(stdscr)
    appLauncher = Window(stdscr, curses.LINES//9, curses.COLS//9, int(curses.LINES/1.2)-10, int(curses.COLS/1.3), "TWS-App_Launcher", appLauncherFunction)
    appLauncher.addString(1, 2, "Use arrow keys to highlight an option and <ENTER> to 'click' an option.")
    appLauncher.addButton("button_001", 3, 2, "[>] Exit To Shell")
    appLauncher.addButton("button_002", 4, 2, "[?] Help")
    appLauncher.addButton("button_003", 5, 2, "[+] Clock")
    appLauncher.addButton("button_004", 6, 2, "[/] CPU Monitor")
    appLauncher.addButton("button_005", 7, 2, "[\u25a1] File Manager")
    appLauncher.addButton("button_006", int(curses.LINES/1.2)-12, 2, "[x] End Session")
    scr.mainloop()

    # Update the screen and wait for 1 second (curses.napms())
    stdscr.refresh()
    curses.napms(1000)

curses.wrapper(main)