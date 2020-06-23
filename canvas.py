import os

width = os.get_terminal_size().columns
height = os.get_terminal_size().lines

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

