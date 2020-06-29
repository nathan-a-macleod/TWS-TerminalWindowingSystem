import os
import datetime

startDir = os.getcwd()
commandHistory = []

def terminalShell():
    command = ""
    
    os.system("clear")
    print(f"Welcome to the terminal environment.\nTo open the app launcher again, type: 'exit'")

    while command != "exit":
        now = datetime.datetime.now()
        command = input("\033[34;1m" + now.strftime("%H:%M") + "\033[0m~\033[31;1m" + os.popen("whoami").read().split()[0] + "\033[0m~\033[36m" + os.popen("pwd").read().split("\n")[0] + "/\033[0m~$ ")

        os.system(command)

        # To allow the user to press up arrow to go to the last command (not completed yet):
        commandHistory.append(command)

        # To allow changing of directories:
        try:
            os.chdir(command.split()[1])

        except:
            pass

    os.chdir(startDir)