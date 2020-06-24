import os
import requests
import time

def main():
    os.system("clear")

    url = input("Enter a URL to view or 'q' to quit: ")

    if url != "q" and url != "Q":
        try:
            pageHTML = requests.get(url)
            print(pageHTML.text)

        except:
            print("Error reading request... Did you forget to put 'http://' at the start?")
            time.sleep(0.8)
            main()
        
        time.sleep(1)