from TWS.windowClass import *

def clockWinFunction(window, key, selectedButtonID):
    import datetime
    window.addString(1, 2, str(datetime.datetime.now().strftime("%I:%M:%S")))

    if selectedButtonID == "closeButton":
        window.closeWindow()

clockWin = Window(1, 0, 3, 12, "TWS-Clock", clockWinFunction)
clockWin.addMenuButton("closeButton", 0, "Close Window")
