#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-

import os

"""
teste quelques propri�t�s pour forensic scientist : expert en criminalistique
ce programme affiche chemins, r�pertoires et fichiers � partir du dossier p�re
"""

rootDir = '..'
for chemin, repertoire, fichiers in os.walk(rootDir):
    print("R�pertoires trouv�s : %s" % chemin)
    for fnom in fichiers:
        print("\t%s" % fnom)
