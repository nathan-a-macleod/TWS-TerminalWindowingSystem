from TWS.windowClass import *

def CPUMonFunction(window, key, selectedButtonID):
    import psutil
    window.addString(1, 2, str(psutil.cpu_percent()) + " % ")

    if selectedButtonID == "closeButton":
        window.closeWindow()

CPUMonWin = Window(1, 0, 3, len("TWS-CPU_Monitor"), "TWS-CPU_Monitor", CPUMonFunction)
CPUMonWin.addMenuButton("closeButton", 0, "Close Window")
