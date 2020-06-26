import os
import sys, tty, termios    # For the getch function

width = os.get_terminal_size().columns
height = os.get_terminal_size().lines

def getch(message):
    print(message)

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno()) # Raw read
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch

class colors:
    reset = "\u001b[0m"

    fgBlack = "\u001b[30m"
    fgRed = "\u001b[31m"
    fgGreen = "\u001b[32m"
    fgYellow = "\u001b[33m"
    fgBlue = "\u001b[34m"
    fgMagenta = "\u001b[35m"
    fgCyan = "\u001b[36m"
    fgWhite = "\u001b[37m"

    bgBlack = "\u001b[40m"
    bgRed = "\u001b[41m"
    bgGreen = "\u001b[42m"
    bgYellow = "\u001b[43m"
    bgBlue = "\u001b[44m"
    bgMagenta = "\u001b[45m"
    bgCyan = "\u001b[46m"
    bgWhite = "\u001b[47m"

class canvas:
    def __init__(self, width, height, bgChar):
        self.width = width
        self.height = height
        self.bgChar = bgChar
        self.screenChars = []

        # Create a list of empty (actually just spaces) chars for all the characters in the screen:
        currentLine = []
        for y in range(height-1):
            for x in range(width):
                currentLine.append(self.bgChar)
            
            currentLine = []
            self.screenChars.append(currentLine)

    # Different to addStr - addStr adds a pixel for each of the strings, but addPixel changes the value of self.screenChars[y][x] to the char, not char by char
    def addPixel(self, xCoord, yCoord, char, side):
        if side == "r":
            self.screenChars[yCoord][xCoord] = self.screenChars[yCoord][xCoord] + char

        elif side == "l":
            self.screenChars[yCoord][xCoord] = char + self.screenChars[yCoord][xCoord]

    def addStr(self, xCoord, yCoord, char):
        #self.screenChars[y][x] = fgColor + bgColor + char + colors.reset
        x = xCoord
        y = yCoord

        for i in range(len(char)):
            self.screenChars[y][x] = char[i]

            if x >= self.width-1:
                y += 1
                x = 0

            else:
                x += 1
    
    def addWindow(self, x, y, width, height, titleStr, border):
        if border == True:
            titleStr = "| " + titleStr + " |"
            topLeftCorner = "+"
            topRightCorner = "+"
            bottomLeftCorner = "+"
            bottomRightCorner = "+"
            verticalEdge = "|"
            horizontalEdge = "_"

        else:
            topLeftCorner = " "
            topRightCorner = " "
            bottomLeftCorner = " "
            bottomRightCorner = " "
            verticalEdge = " "
            horizontalEdge = " "

        # Horizontal Edges:
        for xEdge in range(x, x+width):
            self.addStr(xEdge, y, horizontalEdge)
            self.addStr(xEdge, y+height, horizontalEdge)

        # Vertical Edges:
        for yEdge in range(y, y+height):
            self.addStr(x, yEdge, verticalEdge)
            self.addStr(x+width, yEdge, verticalEdge)

        # Corners
        self.addStr(x, y, topLeftCorner)
        self.addStr(x+width, y, topRightCorner)
        self.addStr(x, y+height, bottomLeftCorner)
        self.addStr(x+width, y+height, bottomRightCorner)

        # Title:
        self.addStr(width//2-(len(titleStr)//2), y, titleStr)

    # Need to give it a way for the user to type yes or no.
    def addConfirm(self, prompt):
        self.addPixel(self.width-len(prompt)-2, self.height-3, colors.bgRed + colors.fgWhite, "l") # Colors (don't need to reset it because it is at the bottom of the canvas)
        self.addStr(self.width-len(prompt)-1, self.height-3, prompt)
 
    def reset(self):
        self.screenChars = []

        currentLine = []
        for y in range(height-1):
            for x in range(width):
                currentLine.append(self.bgChar)
            
            currentLine = []
            self.screenChars.append(currentLine)

    def refresh(self):
        os.system("clear")

        for y in range(len(self.screenChars)):
            for x in range(len(self.screenChars[y])):
                print(self.screenChars[y][x], end="")

            print()

