from CoreLib.Windows.windowClass import *

global datetime
import datetime

def clockWinFunction(window, key, clickedButton):
    window.getWidgetByID("timeStr")["text"] = str(datetime.datetime.now().strftime("%I:%M:%S"))

    if clickedButton != 0:
        if clickedButton["widgetID"] == "closeButton":
            window.closeWindow()

clockWin = Window("TWS-Clock", clockWinFunction)
try:
    clockWin.width = 16
    clockWin.height = 4
    clockWin.x = curses.COLS//9
    clockWin.y = curses.LINES//9
except:
    pass
clockWin.addMenuButton("closeButton", 0, "Close Window")
clockWin.addLabel("timeStr", 1, 4, str(datetime.datetime.now().strftime("%I:%M:%S")))
