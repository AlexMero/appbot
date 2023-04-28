import pyautogui
from PIL import ImageGrab
import time
import pathlib
import services
import routineConfig
import os
import terminale

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True

listDir = routineConfig.listDir
nbEtapes = len(listDir)
returnDir = routineConfig.returnDir
posStart = routineConfig.posStart

cptItemCollected = 0
cptDir = 0

targetItem = "ortie"


def main(listDir, returnDir, targetItem, nbEtapes=nbEtapes):
    global cptItemCollected
    global cptDir

    ############# INIT TERMINALE #############
    terminale.constructTerminal()

    ############# START / GO TO GAME #############
    services.goToGame()

    ############# ROUTINE #############
    terminale.changeTerminalLine(9, "Harvest in progress ...")
    for dir in listDir:
        terminale.changeTerminalLine(
            10, "Program progress " + terminale.createProgressBar(cptDir, nbEtapes) + " " + str(cptDir) + "/" + str(nbEtapes))
        foundItem = services.searchItem(targetItem)
        cptItemCollected = cptItemCollected+foundItem
        services.changeMap(dir)
        cptDir = cptDir+1

    ############# RETURN TO START #############
    for dir in returnDir:
        terminale.changeTerminalLine(11, "Back to square one ...")
        services.changeMap(dir)
    terminale.changeTerminalLine(
        11, "End ! You collected " + str(cptItemCollected) + " " + targetItem)


# main(listDir, returnDir, targetItem)

def repeatMain(nbRepeat, listDir, returnDir, targetItem):
    global nbEtapes
    nbEtapes = nbEtapes*nbRepeat
    for i in range(nbRepeat):
        main(listDir, returnDir, targetItem, nbEtapes)


# repeatMain(20, listDir, returnDir, targetItem)

# TEST TERMINALE
terminale.constructTerminal()
time.sleep(1)
routineConfig.setPosClickDir()
time.sleep(3)
services.changeMap("down")
# terminale.changeTerminalLine(11, "Test barre de progression ...")
# for i in range(10):
#     terminale.changeTerminalLine(
#         11, "Test barre de progression ... " + terminale.createProgressBar(i, 10))
#     time.sleep(0.3)

# terminale.clearTerminal()
