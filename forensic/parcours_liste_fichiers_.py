#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-

import os

"""
teste quelques propriétés pour forensic scientist : expert en criminalistique
ce programme affiche chemins, répertoires et fichiers à partir du dossier père
"""

rootDir = '..'
for chemin, repertoire, fichiers in os.walk(rootDir):
    print("Répertoires trouvés : %s" % chemin)
    for fnom in fichiers:
        print("\t%s" % fnom)
