# Imports
import curses
import os
from PIL import Image # For the image widget

openWindows = [] # An array to store all the open windows

# The main window class:
class Window:
    def __init__(self, y, x, height, width, windowTitle, functionName):
        # Some variable initialisations
        self.y = y
        self.x = x
        self.height = height
        self.width = width
        self.windowTitle = windowTitle
        self.functionName = functionName
        self.widgets = [] # An array of all the widgets
        self.selectedWidget = 0

        openWindows.append(self) # Adds the window to the array containing all the open windows

    # Add individual letters from 'string' to the character array
    def addLabel(self, widgetID, y, x, text):
        self.widgets.append({"widgetID":widgetID, "y":y, "x":x, "text":text, "type":"label"})

        # Make sure you don't start by "selecting" a label:
        try:
            while self.widgets[self.selectedWidget]["type"] == "label":
                self.selectedWidget += 1

        # If it doesn't work it probably means there aren't any button widgets yet
        except:
            pass

    def addButton(self, widgetID, y, x, text):
        self.widgets.append({"widgetID":widgetID, "y":y, "x":x, "text":text, "type":"regularButton"})

    # a Menu button is just a regular button, but it's drawn at the very top of the screen
    def addMenuButton(self, widgetID, x, text):
        self.widgets.append({"widgetID":widgetID, "y":0, "x":x, "text":text, "type":"menuButton"})

    def addInput(self, widgetID, y, x, text):
        self.widgets.append({"widgetID":widgetID, "y":y, "x":x, "text":text, "value":"", "type":"input"})

    def addImage(self, widgetID, y, x, imgWidth, imagePath):
        img = Image.open(os.getcwd() + "/" + imagePath)
        
        # Resize the image:
        width, height = img.size
        aspect_ratio = height/width
        new_width = imgWidth
        new_height = aspect_ratio * new_width * 0.55
        img = img.resize((new_width, int(new_height)))

        # Convert image to greyscale:
        img.convert("L")

        # Get pixels:
        pixels = img.getdata()

        # Convert each pixel to a character from an array
        chars = []
        #for char in "`.!#~+=@qwer#tyui":
        for char in "i`u'~t#rewq@=+~#!.":
            chars.append(char)

        # Get the new pixels:
        new_pixels = [chars[pixel[0]//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)

        # split string of chars into multiple strings of length equal to new width and create a list
        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
        
        
        for idx, line in enumerate(ascii_image.split("\n")):
            self.addLabel("", y+idx, x, str(line))

    def getWidgetByID(self, ID):
        for widget in self.widgets:
            if widget["widgetID"] == ID:
                return widget

    def closeWindow(self):
        # Remove the window from the array of windows
        # The 'Screen' class inside screenCycle.py will not draw this window anymore since it's not in the array
        openWindows.remove(self)
