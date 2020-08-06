from CoreLib.Windows.windowClass import *

global psutil
import psutil

def clockWinFunction(window, key, clickedButton):
    window.getWidgetByID("CPUStr")["text"] = str(psutil.cpu_percent()) + " % "

    if clickedButton != 0:
        if clickedButton["widgetID"] == "closeButton":
            window.closeWindow()

clockWin = Window(1, 0, 4, 19, "TWS-CPU_Monitor", clockWinFunction)
clockWin.addMenuButton("closeButton", 0, "Close Window")
clockWin.addLabel("CPUStr", 1, 2, str(psutil.cpu_percent()) + " % ")
