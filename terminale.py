import sys
import os
#  ______     ______     ______   ______     ______   ______
# /\  == \   /\  __ \   /\__  _\ /\  __ \   /\  == \ /\  == \
# \ \  __<   \ \ \/\ \  \/_/\ \/ \ \  __ \  \ \  _-/ \ \  _-/
#  \ \_____\  \ \_____\    \ \_\  \ \_\ \_\  \ \_\    \ \_\
#   \/_____/   \/_____/     \/_/   \/_/\/_/   \/_/     \/_/
defaultContent = [
    "///////////////////////////////////////////////////////////////////",
    "///  ______     ______     ______   ______     ______   ______  ///",
    "/// /\  == \   /\  __ \   /\__  _\ /\  __ \   /\  == \ /\  == \ ///",
    "/// \ \  __<   \ \ \/\ \  \/_/\ \/ \ \  __ \  \ \  _-/ \ \  _-/ ///",
    "///  \ \_____\  \ \_____\    \ \_\  \ \_\ \_\  \ \_\    \ \_\   ///",
    "///   \/_____/   \/_____/     \/_/   \/_/\/_/   \/_/     \/_/   ///",
    "///                                                             ///",
    "///////////////////////////////////////////////////////////////////",

    "Lancement du programme ...",
    "Etape .../...",
    "Recherche de l'item ...",
    "Changement de map ...",
]

# Modifier une ligne spécifique dans le terminal


def writeInLine(line_number, new_text):
    # Trouver la hauteur du terminal
    height, _ = os.get_terminal_size()

    # Réécrire le reste du terminal inchangé
    for i in range(1, height + 1):
        if i != line_number:
            # Lire la ligne actuelle à la position i
            sys.stdout.write("\033[%d;%dH%s" % (i, 1, os.get_terminal_line(i)))
        else:
            # Écrire le nouveau texte à la position de la ligne spécifiée
            sys.stdout.write("\033[%d;%dH%s" % (i, 1, new_text))

    sys.stdout.flush()
