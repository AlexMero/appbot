import pyautogui
from PIL import ImageGrab
import time
import pathlib
import sys
import os
import terminale
import routineConfig

### LISTE DES SERVICES ###
# goToGame()
# changeMap(dir)
# searchItem(item)
# countMax(item)
# printMousePos()
##########################


def countMax(item):
    cpt = 1
    for path in pathlib.Path("assets/"+item).iterdir():
        if path.is_file():
            cpt = cpt+1
    return cpt


def searchItem(item):
    terminale.changeTerminalLine(11, "Recherche de " + item + " en cours ...")
    foundItem = 0
    searching = True
    while searching:
        searching = False
        cpt = 1
        nbFile = countMax(item)
        for path in pathlib.Path("assets/"+item).iterdir():
            terminale.changeTerminalLine(
                11, "Recherche de " + item + " en cours. " + terminale.createProgressBar(cpt, nbFile))
            if path.is_file():
                imgUrl = "assets/"+item+"/"+item+"_"+str(cpt)+".png"
                location = pyautogui.locateCenterOnScreen(
                    imgUrl, confidence=0.7)
                if location:
                    terminale.changeTerminalLine(
                        11, item+" found ! Collecting ...")
                    pyautogui.moveTo(location, duration=0.5)
                    pyautogui.click()
                    time.sleep(8)
                    foundItem = foundItem+1
                    searching = True
                    break
            cpt = cpt+1

    if foundItem == 0:
        terminale.changeTerminalLine(11, item+" not found ! :(")
    else:
        terminale.changeTerminalLine(
            11, str(foundItem)+" "+item+" found here ! :D")
    return foundItem


def printMousePos():
    time.sleep(3)
    print(pyautogui.position())


def getMousePos():
    time.sleep(3)
    x, y = pyautogui.position()
    return [x, y]


def changeMap(dir):
    terminale.changeTerminalLine(12, "Changing map, going " + dir + " ...")
    print(routineConfig.posClickDir)
    time.sleep(10)
    match dir:
        case "rigth":
            pyautogui.moveTo(
                routineConfig.posClickDir[0][0], routineConfig.posClickDir[0][1], duration=1)
            pyautogui.click()
        case "left":
            pyautogui.moveTo(
                routineConfig.posClickDir[1][0], routineConfig.posClickDir[1][1], duration=1)
            pyautogui.click()
        case "down":
            pyautogui.moveTo(
                routineConfig.posClickDir[2][0], routineConfig.posClickDir[2][1], duration=1)
            pyautogui.click()
        case "up":
            pyautogui.moveTo(
                routineConfig.posClickDir[3][0], routineConfig.posClickDir[3][1], duration=1)
            pyautogui.click()
    time.sleep(7)
    terminale.changeTerminalLine(12, " ")


def goToGame():
    terminale.changeTerminalLine(9, "Going to the game ...")
    pyautogui.moveTo(800, 10, duration=1)
    pyautogui.click()
