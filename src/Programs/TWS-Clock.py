from TWS.windowClass import *

global datetime
import datetime

def clockWinFunction(window, key, clickedButton):
    window.getWidgetByID("timeStr")["text"] = str(datetime.datetime.now().strftime("%I:%M:%S"))

    if clickedButton != 0:
        if clickedButton["text"] == "closeButton":
            window.closeWindow()

clockWin = Window(1, 0, 3, 12, "TWS-Clock", clockWinFunction)
clockWin.addMenuButton("closeButton", 0, "Close Window")
clockWin.addLabel("timeStr", 1, 2, str(datetime.datetime.now().strftime("%I:%M:%S")))
