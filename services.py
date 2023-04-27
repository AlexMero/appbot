import pyautogui
from PIL import ImageGrab
import time
import pathlib
import sys
import os


def searchItem(item):
    print("Searching some", item)
    foundItem = 0
    searching = True
    while searching:
        searching = False
        cpt = 1
        for path in pathlib.Path("assets/"+item).iterdir():
            print("Nombre d'image vérifié :", cpt)
            if path.is_file():
                imgUrl = "assets/"+item+"/"+item+"_"+str(cpt)+".png"
                location = pyautogui.locateCenterOnScreen(
                    imgUrl, confidence=0.7)
                if location:
                    print(item, "found !")
                    pyautogui.moveTo(location, duration=0.5)
                    pyautogui.click()
                    time.sleep(8)
                    foundItem = foundItem+1
                    print(item, "collected :D")
                    searching = True
                    break
            cpt = cpt+1

    if foundItem == 0:
        print(item, "not found ...")
    else:
        print(foundItem, item, "found here !")
    return foundItem


def printMousePos():
    time.sleep(3)
    print(pyautogui.position())


def changeMap(dir):
    print("Go ", dir)
    match dir:
        case "rigth":
            pyautogui.moveTo(950, 365, duration=1)
            pyautogui.click()
        case "left":
            pyautogui.moveTo(5, 461, duration=1)
            pyautogui.click()
        case "down":
            pyautogui.moveTo(503, 823, duration=1)
            pyautogui.click()
        case "up":
            pyautogui.moveTo(581, 49, duration=1)
            pyautogui.click()
    time.sleep(7)


def goToGame():
    pyautogui.moveTo(800, 10, duration=1)
    pyautogui.click()
