#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-

import os

"""
teste quelques propri�t�s pour forensic scientist : expert en criminalistique
ce programme affiche chemins, r�pertoires et fichiers � partir du dossier p�re
"""

rootDir = '..'
for chemin, repertoire, fichier in os.walk(rootDir,topdown=False):
   # les chemins
   print("R�sultats pour chemins : ")
   print(chemin)
   # les repertoires
   print("---R�sultats pour r�pertoires : ")
   print("---" + str(repertoire))
   # les fichiers
   print("------R�sultats pour fichiers : ")
   print("------" + str(fichier))
