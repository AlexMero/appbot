import sys
import os
import time

### LISTE DES SERVICES ###
# constructTerminal()
# changeTerminalLine(line_number, new_content)
# createProgressBar(cpt, nbEtapes)
##########################

# ______     ______     ______             ______     ______   ______
# /\  == \   /\  __ \   /\__  _\           /\  __ \   /\  == \ /\  == \
# \ \  __<   \ \ \/\ \  \/_/\ \/   ______  \ \  __ \  \ \  _-/ \ \  _-/
# \ \_____\  \ \_____\    \ \_\  /______/  \ \_\ \_\  \ \_\    \ \_\
#  \/_____/   \/_____/     \/_/             \/_/\/_/   \/_/     \/_/

logo = ["/////////////////////////////////////////////////////////////////////////////",
        "///  ______     ______     ______             ______     ______   ______  ///",
        "/// /\  == \   /\  __ \   /\__  _\           /\  __ \   /\  == \ /\  == \ ///",
        "/// \ \  __<   \ \ \/\ \  \/_/\ \/   ______  \ \  __ \  \ \  _-/ \ \  _-/ ///",
        "///  \ \_____\  \ \_____\    \ \_\  /______/  \ \_\ \_\  \ \_\    \ \_\   ///",
        "///   \/_____/   \/_____/     \/_/             \/_/\/_/   \/_/     \/_/   ///",
        "///    v1.0.0                                                MerozyApp    ///",
        "/////////////////////////////////////////////////////////////////////////////",
        " ",]
defaultContent = logo + [
    # 9
    "Welcome to MerozyApp with BOTAPP !",
    # 10
    "Introducing the BOTAPP ...",
    # 11
    "To start, call main() function !",
    # 12
    "To set up your game call setPosClickDir() function !",
]

# Modifier une ligne spécifique dans le terminal #


# def writeInLine(line_number, new_text):
#     # Trouver la hauteur du terminal
#     height, _ = os.get_terminal_size()

#     # Réécrire le reste du terminal inchangé
#     for i in range(1, height + 1):
#         if i != line_number:
#             # Lire la ligne actuelle à la position i
#             sys.stdout.write("\033[%d;%dH%s" % (i, 1, os.get_terminal_line(i)))
#         else:
#             # Écrire le nouveau texte à la position de la ligne spécifiée
#             sys.stdout.write("\033[%d;%dH%s" % (i, 1, new_text))

#     sys.stdout.flush()


def constructTerminal():
    global defaultContent
    os.system('cls')
    for i in range(len(defaultContent)):
        print(defaultContent[i])


def changeTerminalLine(line_number, new_text):
    global defaultContent
    if line_number < len(defaultContent):
        defaultContent[line_number] = new_text
    else:
        defaultContent.append(new_text)
    constructTerminal()


def createProgressBar(value, max):
    moy = (value * 30 / max) + 1
    res = "["+"#"*int(moy)+">"+"-"*(30-int(moy))+"]"
    return res


def clearTerminal():
    global defaultContent
    global logo
    defaultContent = logo
    constructTerminal()
