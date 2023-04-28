import terminale
import services
import time

# # recherche d'ortie emplacement de départ -1:10
# listDir = ["down", "down", "down", "down", "rigth",
#            "up", "up", "up", "rigth", "rigth", "down", "down"]
# returnDir = ["up", "up", "up", "left", "left", "left"]
# posStart = [-1, 10]

# recherche d'ortie emplacement de départ 6:8
listDir = ["up", "up", "up", "up", "up", "up", "up", "rigth",
           "down", "down", "down", "down", "down", "down", "down"]
returnDir = ["left"]
posStart = [6, 8]
posClickDir = [
    [950, 365],
    [5, 461],
    [503, 823],
    [581, 49]
]


def setPosClickDir():
    global posClickDir
    terminale.clearTerminal()
    terminale.changeTerminalLine(9, "Setting click position to change map ...")
    terminale.changeTerminalLine(
        10, "Put your mouse where you want to click to change map to the ...")

    terminale.changeTerminalLine(11, "RIGTH")
    newPos = services.getMousePos()
    posClickDir[0] = newPos

    terminale.changeTerminalLine(11, "LEFT")
    newPos = services.getMousePos()
    posClickDir[1] = newPos

    terminale.changeTerminalLine(11, "BOTTOM")
    newPos = services.getMousePos()
    posClickDir[2] = newPos

    terminale.changeTerminalLine(11, "UP")
    newPos = services.getMousePos()
    posClickDir[3] = newPos

    terminale.clearTerminal()
    terminale.changeTerminalLine(9, "Position click set !")
