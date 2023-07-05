from CoreLib.Windows.windowClass import *

global psutil
import psutil

def clockWinFunction(window, key, clickedButton):
    window.getWidgetByID("CPUStr")["text"] = str(psutil.cpu_percent()) + " % "

    if clickedButton != 0:
        if clickedButton["widgetID"] == "closeButton":
            window.closeWindow()

clockWin = Window("TWS-CPU_Monitor", clockWinFunction)
try:
    clockWin.width = 16
    clockWin.height = 4
    clockWin.x = curses.COLS//9
    clockWin.y = curses.LINES//9

except:
    pass
clockWin.addMenuButton("closeButton", 0, "Close Window")
clockWin.addLabel("CPUStr", 1, 2, str(psutil.cpu_percent()) + " % ")
