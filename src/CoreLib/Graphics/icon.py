def addIcon(window, y, x, iconArr):
    for lineIdx, line in enumerate(iconArr):
        for charIdx, char in enumerate(line):
            if char == 1:
                window.addLabel("", y+lineIdx, x+charIdx+charIdx, "\u2588\u2588")

            else:
                window.addLabel("", y+lineIdx, x+charIdx+charIdx, "  ")