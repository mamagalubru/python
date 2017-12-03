#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-

import os

"""
teste quelques propriétés pour forensic scientist : expert en criminalistique
ce programme affiche chemins, répertoires et fichiers à partir du dossier père
"""

rootDir = '..'
for chemin, repertoire, fichier in os.walk(rootDir,topdown=False):
   # les chemins
   print("Résultats pour chemins : ")
   print(chemin)
   # les repertoires
   print("---Résultats pour répertoires : ")
   print("---" + str(repertoire))
   # les fichiers
   print("------Résultats pour fichiers : ")
   print("------" + str(fichier))
