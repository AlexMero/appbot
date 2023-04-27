import pyautogui
from PIL import ImageGrab
import time
import pathlib
import services
import routineConfig
import os

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True

listDir = routineConfig.listDir
nbEtapes = len(listDir)
returnDir = routineConfig.returnDir
posStart = routineConfig.posStart

cptItemCollected = 0
cptDir = 0

# printMousePos()
targetItem = "ortie"
# services.goToGame()

# for dir in listDir:
#     print("Etape ", cptDir, "/", len(listDir))
#     searching = services.searchItem(targetItem)
#     services.changeMap(dir)
#     cptDir = cptDir+1

# print("Retour au point de départ !")
# for dir in returnDir:
#     services.changeMap(dir)
# print("Fin ! Tu as trouvé", cptItemCollected, targetItem)


def main(listDir, returnDir, targetItem, nbEtapes=nbEtapes):
    global cptItemCollected
    global cptDir

    ############# START / GO TO GAME #############
    services.goToGame()

    ############# ROUTINE #############
    for dir in listDir:
        os.system('cls')
        print("Etape ", cptDir, "/", nbEtapes)
        foundItem = services.searchItem(targetItem)
        cptItemCollected = cptItemCollected+foundItem
        services.changeMap(dir)
        cptDir = cptDir+1

    ############# RETURN TO START #############
    for dir in returnDir:
        os.system('cls')
        print("Retour au point de départ !")
        services.changeMap(dir)
    os.system('cls')
    print("Fin ! Tu as trouvé", cptItemCollected, targetItem)


# main(listDir, returnDir, targetItem)

def repeatMain(nbRepeat, listDir, returnDir, targetItem):
    global nbEtapes
    nbEtapes = nbEtapes*nbRepeat
    for i in range(nbRepeat):
        main(listDir, returnDir, targetItem, nbEtapes)


repeatMain(20, listDir, returnDir, targetItem)


# services.writeInLine(1, "Ligne 1")
