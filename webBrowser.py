import os
import requests
import time

def main():
    os.system("clear")

    url = input("Enter a URL to view or 'q' to quit: ")

    if url != "q" and url != "Q":
        pageHTML = requests.get(url)
        print(pageHTML.text)
        time.sleep(1)